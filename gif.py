import imageio
from pygifsicle import gifsicle
import os
from editor import Editor
import random

class GIFFactory:

    def make_gif(src=None, set=None, resize=1, fps=30):
        """Make gif from sequence of images. Saves to media folder.

        Parameters
        -------------
        src:String,
            The path or file location of the image sequence
        resize=1:Integer,
            Calls on Editor.resize_img to Scale down image by resize.
            Defaults to 1 which is no change.
        set=None:List,
            A list of two integer indices for a set of
            images to make the GIF.
        fps=30:Integer,
            Source's frames per second.
        """
        images = []
        os.chdir('./media/img/' + str(src))

        image_dir = os.listdir('.') if set is None else os.listdir('.')[slice(set[0], set[1])]
        print('{:s} files to be processed in {:s}:'.format(str(len(image_dir)), src))
        for image in image_dir:
            # Load image into Editor.
            new_image = Editor(image)
            reduced = new_image.resize_img(resize)
            images.append(imageio.imread(reduced.filename))
            reduced.close()
        new_gif_name = str(random.randint(1,10000))
        print('Saving new GIF: {}.gif'.format(new_gif_name))

        imageio.mimwrite('../../{}.gif'.format(new_gif_name), images, fps=fps)

    def scale_width_down(src, dest=None, size=None):
        """Reduce size of gif using gifsicle's scale method.

        Parameters
        -------------
        src:String,
            File or location of gif to be resized.
        dest:String,
            Path/filename for new gif.
        size:Integer,
            The amount of reduction to be applied.
        """
        reduction_size = '{}x_'.format(size)
        gifsicle(
            sources=[src],
            destination=dest,
            optimize=False,
            #colors=256,
            options=['--resize', reduction_size]
        )
