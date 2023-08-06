from PIL import Image
from PIL.ImageOps import scale
import os
import sys


class Enhance:
    def __init__(self, walk=False, verbose=False):
        self.walk = walk
        self.verbose = verbose
        pass

    def resize_and_save(self, filename):
        x16 = (16, 16)
        im = Image.open(filename)
        is16x = im.size == x16
        if is16x:
            # double the image in size to 32 by 32
            if self.verbose:
                print(f"Resizing {filename}")
            out = scale(im, 2)
            # save it as the original name
            out.save(f"{filename}", "PNG")

    def get_files(dir=""):
        # allow for a default value of a function call
        if not dir:
            dir = os.getcwd()
        files = os.listdir(dir)
        files = list(file for file in files if file[-4:] == ".png")
        return files

    def do_resize(self):
        if walk:
            data = os.walk(os.getcwd())
            for root, dirs, files in data:
                # separate out the files, dirs, root
                files = [f for f in files if not f[0] == '.']
                files = [f for f in files if f[-4:] == '.png']
                dirs[:] = [d for d in dirs if not d[0] == '.']

                # now we can use them - we'll need to modify the images while
                # we're in the folder
                for file in files:
                    filename = f"{root}\{file}"
                    self.resize_and_save(filename)

        else:
            # get the files in the cwd, resize and save each one
            files = self.get_files()
            for file in files:
                self.resize_and_save(file)


if __name__ == "__main__":
    # All folders/files?
    walk = "-w" in sys.argv
    verbose = "-v" in sys.argv

    enh = Enhance(walk, verbose)
    enh.do_resize()