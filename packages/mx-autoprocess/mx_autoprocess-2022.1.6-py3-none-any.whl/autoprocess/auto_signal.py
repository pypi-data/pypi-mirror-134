
import json
import threading
import time
import uuid
from pathlib import Path
from collections import deque
from datetime import timedelta
from multiprocessing import Process, Queue, cpu_count

import zmq
from mxio.formats.eiger import EigerStream
from mxio import read_image

from utils import diffsig

SAVE_DELAY = .05  # Amount of time to wait for file to be written.


def signal_worker(inbox: Queue, outbox: Queue):
    """
    Signal strength worker. Reads data from the inbox queue and puts the results to the outbox
    :param inbox: Inbox queue to fetch tasks
    :param outbox: Outbox queue to place completed results
    """

    while True:
        task = inbox.get()
        name, kind, frame_data = task
        if kind == 'stream':
            dataset = EigerStream()
            dataset.read_header(frame_data[:2])
            dataset.read_image(frame_data[2:])
        else:
            path = Path(frame_data)
            # Avoid reading a file while it's being written
            while time.time() - path.stat().st_mtime < SAVE_DELAY:
                time.sleep(0.001)
            dataset = read_image(frame_data)

        # calculate signal_strength
        results = diffsig.signal(dataset.data, dataset.header)
        results['series_name'] = name
        results['frame_number'] = dataset.header['frame_number']
        outbox.put((name, results))


class SignalManager(threading.Thread):
    def __init__(self, request, outbox):
        super().__init__()
        self.inbox = Queue(maxsize=5000)
        self.outbox = outbox
        self.request = request
        self.num_procs = 4
        self.start_workers()

    def start_workers(self):
        for i in range(self.num_procs):
            p = Process(target=signal_worker, args=(self.inbox, self.outbox))
            p.start()
        print('Workers ready!')

    def run(self):
        request_type = self.request.get('type', 'file')
        if request_type == 'stream':
            self.stream_workload()
        else:
            self.file_workload()

    def file_workload(self):
        name = self.request['request_id']
        directory = Path(self.request['directory'])
        template = self.request['template']
        first_frame = self.request.get('first', 1)
        num_frames = self.request['num_frames']
        timeout = self.request.get('timeout', 360)
        frames = deque(maxlen=num_frames)
        for i in range(num_frames):
            frames.append(directory.joinpath(template.format(i+first_frame)))

        start_time = time.time()
        while len(frames) and time.time() - start_time < timeout:
            frame = frames.popleft()
            if frame.exists():
                self.inbox.put([
                    name, 'file', str(frame)
                ])
            else:
                # Add it back to the front of the queue
                frames.append(frame)
            time.sleep(0.0001)
        print('All tasks submitted.')

    def stream_workload(self):
        name = self.request['request_id']
        address = self.request['address']
        num_frames = self.request['num_frames']
        timeout = self.request.get('timeout', 360)

        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(address)
        socket.setsockopt_string(zmq.SUBSCRIBE, "")

        header_data = []
        count = 0
        start_time = time.time()
        while count <= num_frames and time.time() - start_time < timeout:
            data = socket.recv_multipart()
            info = json.loads(data[0])
            if info['htype'] == 'dheader-1.0':
                header_data = data
                self.start_time = time.time()
            elif info['htype'] == 'dimage-1.0' and header_data:
                self.inbox.put((name, 'stream', header_data + data))
                count += 1
            elif info['htype'] == 'dseries_end-1.0':
                self.end_time = time.time()
                header_data = []
            time.sleep(0.001)


if __name__ == '__main__':
    manager = SignalManager()
    uid = str(uuid.uuid4())
    #manager.stream_workload(uid, {'address': "tcp://10.52.28.23:9995"})
    manager.file_workload(uid, {
        'directory': '/data/Xtal/IDP05511_4noh/data/',
        'template': 'idp05511_1sm-b_{:03d}.img',
        'num_frames': 100,
        'first': 1
    })