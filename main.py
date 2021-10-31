import argparse
import threading
from os import path
from posix import listdir

from Helper import iconset, imageset, util

util = util.Utils()


def main(imageFolder, iconSet=False, imageSet=False, outputFolder=None):
    if imageSet:

        storedSets = []

        # Load all images into memory
        for file in listdir(imageFolder):
            if file.endswith(".png") or file.endswith(".jpg"):
                image = file
                name = image.split(".")[0]
                imagePath = path.join(imageFolder, image)
                storedSets.append(
                    imageset.ImageSet(
                        name=name,
                        imagePath=imagePath,
                        savePath=f"{outputFolder}/ImageSets/{name}.imageset"
                    )
                )
            else:
                util.log_error(
                    file + " is not a valid image -> Can't generate ImageSet")

        # Create a thread for each image
        threads = []
        for image in storedSets:
            thread = threading.Thread(target=image.generate_imageset)
            thread.start()
            threads.append(thread)

    if iconSet:

        storedSets = []

        # Load all images into memory
        for file in listdir(imageFolder):
            if file.endswith(".png") or file.endswith(".jpg"):
                image = file
                name = image.split(".")[0]
                imagePath = path.join(imageFolder, image)
                storedSets.append(
                    iconset.IconSet(
                        name=name,
                        imagePath=imagePath,
                        savePath=f"{outputFolder}/AppIconSets/{name}.appiconset"
                    )
                )

            else:
                util.log_error(
                    file + " is not a valid image -> Can't generate App Icon")

        # Create a thread for each image
        threads = []
        for image in storedSets:
            thread = threading.Thread(target=image.generate_icon_set)
            thread.start()
            threads.append(thread)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Generate AppIcon Set and Imageset for Xcode')

    # if user doesnt pass ass again as input
    parser.add_argument("-in", "--imageFolder",
                        help="Folder containing image/s", required=True)

    parser.add_argument("--appicon",
                        help="Generate appiconset/s", action="store_true")
    parser.add_argument("--imageset",
                        help="Generate imageset/s", action="store_true")
    parser.add_argument(
        "--out", "--outputFolder", help="Output folder, default: Desktop Folder")

    args = parser.parse_args()

    main(imageFolder=args.imageFolder,
         iconSet=args.appicon,
         imageSet=args.imageset,
         outputFolder=args.out
         )
