import json
from os import makedirs, name, path

from PIL import Image, UnidentifiedImageError

from Helper import util

util = util.Utils()


class ImageSet:
    # A class takes a SINGLE image path and carries out operation to the image

    def __init__(self, name, imagePath):
        self.scales = {
            "1x": [342, 342],
            "2x": [683, 683],
            "3x": [1024, 1024]
        }
        self.name = name
        self.imagePath = imagePath

        self.savePath = f"{path.expanduser('~')}/Desktop/iAssetsExports/ImageSets/{self.name}.imageset"

    def saveImage(self, image, scale):
        """Save image to imageset"""
        if not path.exists(self.savePath):
            makedirs(self.savePath)
        else:
            util.log_warning(
                f"{self.savePath} already exists, guess we're overwriting")

        image.save(f"{self.savePath}/{self.name}@{scale}.png")
        util.log_msg(f"Image Saved, name: {self.name}@{scale}.png")

    def resizeImage(self, scale):
        """Resize image to width and height"""

        width = self.scales[scale][0]
        height = self.scales[scale][1]

        img = Image.open(f"{self.imagePath}")
        img = img.resize((width, height), Image.ANTIALIAS)
        util.log_msg(f"Image Resized, name: {self.name}, scale: {scale}")

        self.saveImage(img, scale)

    def printDetails(self):
        print("image name: ", self.name)
        print("image path: ", self.imagePath)
        print("save image path: ", self.savePath)

    def generateJson(self):
        util.log_msg(f"Generating JSON for {self.name}")
        """Generate json file"""

        images = []

        singleImageTemplate = {
            "idiom": "universal",
            "scale": "",
            "filename": ""
        }
        dataTemplate = {
            "images": [],
            "author": "iAssets",
            "version": "90.29"
        }

        for scale in self.scales:
            singleImageCopy = singleImageTemplate.copy()
            singleImageCopy["scale"] = scale
            singleImageCopy["filename"] = f"{self.name}@{scale}.png"
            images.append(singleImageCopy)

        dataTemplate["images"] = images

        with open(f"{self.savePath}/Contents.json", "w") as f:
            json.dump(dataTemplate, f, indent=4)

    def generateImageset(self):
        """Generate imageset"""
        util.log_msg(f"Generating ImageSet for {self.name}")

        try:
            for scale in self.scales:
                self.resizeImage(scale)

            self.generateJson()
            print("Generated imageset: ", self.savePath)
        except UnidentifiedImageError:
            print("Weird Image", name, path)
        except Exception as e:
            print("Unknown error", e)
