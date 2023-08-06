import time

import numpy
from scipy.ndimage.filters import maximum_filter, uniform_filter
from scipy.ndimage.interpolation import zoom
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
from skimage import filters

SCALE = 2
FACTOR = numpy.sqrt(SCALE ** 2 + SCALE ** 2)
ICE_RINGS = [
    (3.93, 3.87),
    (3.70, 3.64),
    (3.47, 3.41),
    (2.70, 2.64),
    (2.28, 2.22),
    (2.102, 2.042),
    (1.948, 1.888),
    (1.524, 1.519),
    (1.473, 1.470),
    (1.444, 1.440),
    (1.372, 1.368),
    (1.367, 1.363),
    (1.299, 1.296),
    (1.275, 1.274),
    (1.261, 1.259),
    (1.224, 1.222),
    (1.171, 1.168),
    (1.124, 1.122),
]

numpy.errstate(invalid='ignore', divide='ignore')

def window_stdev(X, window_size):
    c1 = uniform_filter(X, window_size, mode='reflect')
    c2 = uniform_filter(X * X, window_size, mode='reflect')
    return numpy.sqrt(numpy.abs(c2 - c1 * c1))


def detect_peaks(image):
    """
    Takes an image and detect the peaks using the local maximum filter.
    Returns a boolean mask of the peaks (i.e. 1 when
    the pixel's value is the neighborhood maximum, 0 otherwise)
    """

    # define an 8-connected neighborhood
    # apply the local maximum filter; all pixel of maximal value
    # in their neighborhood are set to 1
    # local_max is a mask that contains the peaks we are
    # looking for, but also the background.
    # In order to isolate the peaks we must remove the background from the mask.
    # we create the mask of the background
    # a little technicality: we must erode the background in order to
    # successfully subtract it form local_max, otherwise a line will
    # appear along the background border (artifact of the local maximum filter)
    # we obtain the final mask, containing only peaks,
    # by removing the background from the local_max mask (xor operation)

    neighborhood = generate_binary_structure(2, 2)
    local_max = maximum_filter(image, footprint=neighborhood) == image
    background = (image == 0)
    eroded_background = binary_erosion(background, structure=neighborhood, border_value=1)
    detected_peaks = local_max ^ eroded_background
    peaks = numpy.argwhere(detected_peaks)
    return peaks


def signal(image, metadata):
    # represent image as z-scores of the standard deviation
    # zero everything less than MIN_SIGMA
    # find peaks in the resulting image
    # calculate the resolution of found peaks
    # mask peaks that are within ice rings
    t = time.time()
    if SCALE > 1:
        image = zoom(image, 1 / SCALE)
    cy, cx = numpy.array(metadata['beam_center']) / SCALE

    std_img = window_stdev(image, 2)
    data = filters.gaussian(std_img, sigma=2)
    thresh = numpy.percentile(std_img, 99.)
    data[data < thresh] = 0.0
    peaks = detect_peaks(data)

    peak_l = SCALE * metadata['pixel_size'] * ((peaks - (cx, cy)) ** 2).sum(axis=1) ** 0.5
    peak_a = 0.5 * numpy.arctan(peak_l / metadata['distance'])
    peak_d = metadata['wavelength'] / (2 * numpy.sin(peak_a))

    spots = numpy.array([
        (SCALE * pk[1], SCALE * pk[0], metadata['frame_number'], image[pk[0], pk[1]], 0, 0, 0)
        for i, pk in enumerate(peaks)
    ])
    num_peaks = len(peaks)
    if num_peaks > 5:
        mask_refl = peak_d > 20
        bins = numpy.array(ICE_RINGS).ravel()[::-1]
        counts, edges = numpy.histogram(peak_d, bins=bins)
        edges = numpy.column_stack((edges[:-1], edges[1:]))
        fracs = counts /counts.sum()
        ice_rings = []
        for i, frac in enumerate(fracs):
            if i % 2 == 0 and frac >= .005:  # 0.5% threshold for detecting rings
                region = edges[i]
                mask_refl |= (peak_d > region[0]) & (peak_d < region[1])
                ice_rings.append((region.mean(), frac))
        num_rings = len(ice_rings)
        flt_spots = spots[~mask_refl]
        good_spots = flt_spots[flt_spots[:, 3].argsort()[::-1]]
        num_good = len(good_spots)
        signal_avg = good_spots[:50, 3].mean()
        signal_min = good_spots[:50, 3].min()
        signal_max = good_spots[0, 3]
        resolution = numpy.percentile(peak_d, 1)
    else:
        num_rings = 0
        num_good = 0
        resolution = 50.
        signal_min = 0
        signal_max = 0
        signal_avg = 0

    #numpy.savetxt('SPOT.XDS', good_spots, fmt='%10g')

    return {
        'ice_rings': num_rings,
        'resolution': resolution,
        'total_spots': num_peaks,
        'bragg_spots': num_good,
        'signal_avg': signal_avg,
        'signal_min': signal_min,
        'signal_max': signal_max,
    }
