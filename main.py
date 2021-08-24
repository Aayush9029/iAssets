import argparse
import threading
from os import path
from posix import listdir

from Helper import imageset, util

util = util.Utils()


def test():
    # Folder containing the images
    imageFolder = "tests/images"

    storedSets = []

    # Load all images into memory
    for file in listdir(imageFolder):
        if file.endswith(".png") or file.endswith(".jpg"):
            image = file
            imagePath = path.join("tests/images", image)
            storedSets.append(imageset.ImageSet(
                image.split(".")[0], imagePath)
            )
        else:
           util.log_error(file + " is not a valid image")

    # Create a thread for each image
    threads = []
    for image in storedSets:
        thread = threading.Thread(target=image.generateImageset)
        thread.start()
        threads.append(thread)


def main(imageFolder):
    # Folder containing the images
    imageFolder = "tests/images"

    storedSets = []

    # Load all images into memory
    for file in listdir(imageFolder):
        if file.endswith(".png") or file.endswith(".jpg"):
            image = file
            imagePath = path.join("tests/images", image)
            storedSets.append(imageset.ImageSet(
                image.split(".")[0], imagePath)
            )
        else:
           util.log_error(file + " is not a valid image")

    # Create a thread for each image
    threads = []
    for image in storedSets:
        thread = threading.Thread(target=image.generateImageset)
        thread.start()
        threads.append(thread)


# The code is very test centric as it is still in development phase, no releases yet

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate @1x @2x and @3x imagesets for Xcode')
    parser.add_argument('-t', '--test', action='store_true', required=False)
    # if user doesnt pass ass again as input
    parser.add_argument("-i", "--imageFolder", required=False)

    args = parser.parse_args()

    if args.test:

        test()
    else:
        if not args.imageFolder:
            args.imageFolder = input(
                "Folder containing images you want to generate imageset for\n>").strip()

        main(args.imageFolder)
