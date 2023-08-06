import glob
from PIL import Image


class GIFConverter:

    def __init__(self, 
                 path_in: str = None, 
                 path_out: str = None, 
                 resize: tuple[int, int]=(320, 240)) -> None:
        """
        path_in: images path in format of glob. (ex. images/*.png)
        path_out: GIF image output path. (ex. output/filename.gif)
        resize: the size of resized image. default=(320, 240)
        """
        self._path_in = path_in or "./*.png"
        self._path_out = path_out or "./output.gif"
        self._resize = resize

    def convert_gif(self) -> None:
        """
        convert images to a single gif file.
        """
        img, *images = \
            [Image.open(f).resize(self._resize, Image.ANTIALIAS) for f in sorted(glob.glob(self._path_in))]

        try:
            img.save(self._path_out, 
                     format="GIF", 
                     append_images=images,
                     save_all=True,
                     duration=500,
                     loop=0)
        except IOError as e:
            raise IOError("Cannot convert images to GIF!") from e


# Test
if __name__ == "__main__":
    c = GIFConverter("../project/images/*.png", "../project/image_out/result_test.gif", (320, 240))
    c.convert_gif()
