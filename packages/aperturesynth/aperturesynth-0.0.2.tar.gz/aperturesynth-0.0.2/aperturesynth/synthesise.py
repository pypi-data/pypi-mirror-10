"""aperturesynth - a tool for registering and combining series of photographs.

Usage:
    aperturesynth combine [--no-transform] [--out FILE] [--windows FILE] <images>...
    aperturesynth choose_windows <base_image> <window_file>

Options:

    -h --help           Show this help screen.

    --out FILE          Optional output file. If not specified the output will
                        be written to a tiff file with same name as the
                        baseline image with 'transformed_' prepended. The
                        output format is chosen by the file extension.

    --windows FILE      Optional file to specify the coordinates of the windows
                        to register. This file can be generated using the
                        choose_windows subcommand, or can be written by hand
                        as a comma separated value file. Each row of this file
                        is the integer x,y coordinates of a point in the image.
                        Consecutive rows are interpreted as the top left and
                        bottom right of each window.

    --no-transform      Combine images without transforming first. Useful for
                        visualising the impact of registration.

The combine command is the main interface for synthesising images: it can be
called with just the images as arguments and will present a GUI to select the
focal regions. The first image passed in will be the baseline image to which 
all following images will be matched. 

When selecting focal regions using choose_windows or combine with no windows
file specified, consecutive pairs of points *must* indicate the top left and 
bottom right of the rectangular focal regions.

"""


import multiprocessing as mp
import numpy as np
from skimage import io, img_as_ubyte, img_as_float
from docopt import docopt
import os.path

from .register import Registrator
from .gui import get_windows


def save_image(image, filename):
    """Saves the image to the given filename, ensuring uint8 output. """
    io.imsave(filename, img_as_ubyte(image))


def load_image(image):
    """Loads the given file and converts to float32 format. """
    return img_as_float(io.imread(image))


def register_images(image_list, registrator):
    """A generator to register a series of images.

    The first image is taken as the baseline and is not transformed.

    """
    yield load_image(image_list[0])

    for image_file in image_list[1:]:
        transformed_image, transform = registrator(load_image(image_file))
        # Stub for future operations that examine the transformation
        yield transformed_image


def no_transform(image):
    """Pass through the original image without transformation.

    Returns a tuple with None to maintain compatability with processes that
    evaluate the transform.

    """
    return (image, None)


def process_images(image_list, registrator, fusion=None):
    """Apply the given transformation to each listed image and find the mean.

    Parameters
    ----------

    image_list: list of filepaths
        Image files to be loaded and transformed.
    registrator: callable
        Returns the desired transformation of a given image.
    fusion: callable (optional, default=None)
        Returns the fusion of the given images. If not specified the images are
        combined by averaging.

    Returns
    -------

    image: MxNx[3]
        The combined image as an ndarray.

    """

    registered = register_images(image_list, registrator)

    if fusion is not None: # Stub for future alternative fusion methods
        return fusion(registered)

    else:
        output = sum(registered)
        output /= len(image_list)
        return output


def main():
    """Registers and transforms each input image and saves the result."""
    args = docopt(__doc__)

    if args['choose_windows']:
        reference = load_image(args['<base_image>'])
        windows = get_windows(reference)
        np.savetxt(args['<window_file>'], windows.astype('int'), fmt='%i')

    elif args['combine']:
        images = args['<images>']

        # Is an output filename specified, or do I need to generate my own?
        if args['--out']:
            output_file = args['--out']
        else:
            head, ext = os.path.splitext(images[0])
            head, tail = os.path.split(head)
            output_file = os.path.join(head, 'transformed_' + tail + '.tiff')

        # Are the windows specified, or do I have to provide a gui to choose?
        if args['--no-transform']:
            pass # No windows are needed for the averaging case
        elif args['--windows']:
            windows = np.genfromtxt(args['--windows'])
        else:
            baseline = load_image(images[0])
            windows = get_windows(baseline)

        # What kind of registration am I performing?
        if args['--no-transform']:
            registrator = no_transform
        else:
            try: # Only load the baseline if not loaded earlier.
                baseline.shape
            except NameError:
                baseline = load_image(images[0])
            registrator = Registrator(windows, baseline)

        output = process_images(images, registrator)
        save_image(output, output_file)
