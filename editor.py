import os
from PIL import Image


class Editor:


    def __init__(self, image):
        self.image = Image.open(image)


    def resize_img(self,scale=1):
        """Reduce the size of an image by scale. Defaults to 1.

        Parameters
        -------------
        scale:Integer,
            The scale by which to reduce the width and height of the image.
        """
        reduced = self.image.reduce((scale,scale))
        reduced.save("../edited/{}".format(self.image.filename))

        reduced = Image.open("../edited/{}".format(self.image.filename))
        return reduced

    def _print_img_size(self, img):
        """Print a string representation of the image's width & height.

        Parameters
        -------------
        img:Image,
            Image to be processed
        """
        width, height = img.size
        print('{}, {}'.format(width, height))

    def close(self):
        """Close an open image connection.

        """
        self.image.close()
