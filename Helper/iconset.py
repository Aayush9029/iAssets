import json
from os import makedirs, name, path

from PIL import Image, UnidentifiedImageError

from Helper import util

util = util.Utils()


class IconSet:
    # A class takes a SINGLE image path and carries out operation to the image

    def __init__(self, name, imagePath, savePath=None):
        self.name = name
        self.imagePath = imagePath

        if savePath is None:
            # Default output path is Desktop
            self.savePath = f"{path.expanduser('~')}/Desktop/iAssetsExports/IconSets/{self.name}.appiconset"
        else:
            self.savePath = savePath

        self.dataTemplate = {
            "images": [
                {
                    "size": "60x60",
                    "idiom": "car",
                    "filename": self.title_to_icon_name(120),
                    "scale": "2x"
                },
                {
                    "size": "60x60",
                    "idiom": "car",
                    "filename": self.title_to_icon_name(180),
                    "scale": "3x"
                },
                {
                    "size": "20x20",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(20),
                    "scale": "1x"
                },
                {
                    "size": "20x20",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(40),
                    "scale": "2x"
                },
                {
                    "size": "29x29",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(29),
                    "scale": "1x"
                },
                {
                    "size": "29x29",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(58),
                    "scale": "2x"
                },
                {
                    "size": "40x40",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(40),
                    "scale": "1x"
                },
                {
                    "size": "40x40",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(80),
                    "scale": "2x"
                },
                {
                    "size": "76x76",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(76),
                    "scale": "1x"
                },
                {
                    "size": "76x76",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(152),
                    "scale": "2x"
                },
                {
                    "size": "83.5x83.5",
                    "idiom": "ipad",
                    "filename": self.title_to_icon_name(167),
                    "scale": "2x"
                },
                {
                    "size": "20x20",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(40),
                    "scale": "2x"
                },
                {
                    "size": "20x20",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(60),
                    "scale": "3x"
                },
                {
                    "size": "29x29",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(58),
                    "scale": "2x"
                },
                {
                    "size": "29x29",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(87),
                    "scale": "3x"
                },
                {
                    "size": "40x40",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(80),
                    "scale": "2x"
                },
                {
                    "size": "40x40",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(120),
                    "scale": "3x"
                },
                {
                    "size": "60x60",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(120),
                    "scale": "2x"
                },
                {
                    "size": "60x60",
                    "idiom": "iphone",
                    "filename": self.title_to_icon_name(180),
                    "scale": "3x"
                },
                {
                    "size": "128x128",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(128),
                    "scale": "1x"
                },
                {
                    "size": "256x256",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(256),
                    "scale": "1x"
                },
                {
                    "size": "128x128",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(256),
                    "scale": "2x"
                },
                {
                    "size": "256x256",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(512),
                    "scale": "2x"
                },
                {
                    "size": "32x32",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(32),
                    "scale": "1x"
                },
                {
                    "size": "512x512",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(512),
                    "scale": "1x"
                },
                {
                    "size": "16x16",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(16),
                    "scale": "1x"
                },
                {
                    "size": "16x16",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(32),
                    "scale": "2x"
                },
                {
                    "size": "32x32",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(64),
                    "scale": "2x"
                },
                {
                    "size": "512x512",
                    "idiom": "mac",
                    "filename": self.title_to_icon_name(1024),
                    "scale": "2x"
                },


                {
                    "size": "24x24",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(48),
                    "subtype": "38mm",
                    "role": "notificationCenter",
                    "scale": "2x"
                },
                {
                    "size": "27.5x27.5",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(55),
                    "subtype": "42mm",
                    "role": "notificationCenter",
                    "scale": "2x"
                },
                {
                    "size": "29x29",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(58),
                    "role": "companionSettings",
                    "scale": "2x"
                },
                {
                    "size": "33x33",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(66),
                    "role": "notificationCenter",
                    "scale": "2x"
                },
                
                {
                    "size": "46x46",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(92),
                    "role": "appLauncher",
                    "scale": "2x"
                },

                {
                    "size": "51x51",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(102),
                    "role": "appLauncher",
                    "scale": "2x"
                },
                {
                    "size": "117x117",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(234),
                    "role": "quickLook",
                    "scale": "2x"
                },
                {
                    "size": "29x29",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(87),
                    "role": "companionSettings",
                    "scale": "3x"
                },
                {
                    "size": "40x40",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(80),
                    "subtype": "38mm",
                    "role": "appLauncher",
                    "scale": "2x"
                },
                {
                    "size": "44x44",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(88),
                    "subtype": "40mm",
                    "role": "appLauncher",
                    "scale": "2x"
                },
                {
                    "size": "50x50",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(100),
                    "subtype": "44mm",
                    "role": "appLauncher",
                    "scale": "2x"
                },
                {
                    "size": "86x86",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(172),
                    "subtype": "38mm",
                    "role": "quickLook",
                    "scale": "2x"
                },
                {
                    "size": "98x98",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(196),
                    "subtype": "42mm",
                    "role": "quickLook",
                    "scale": "2x"
                },
                {
                    "size": "108x108",
                    "idiom": "watch",
                    "filename": self.title_to_icon_name(216),
                    "subtype": "44mm",
                    "role": "quickLook",
                    "scale": "2x"
                },
                {
                    "size": "1024x1024",
                    "idiom": "watch-marketing",
                    "filename": self.title_to_icon_name(1024),
                    "scale": "1x"
                },
                {
                    "size": "1024x1024",
                    "idiom": "ios-marketing",
                    "filename": self.title_to_icon_name(1024),
                    "scale": "1x"
                }
            ],
            "author": "iAssets",
            "version": "2020.11.0"
        }

    def save_image(self, image):
        """Save image to iconsets"""
        if not path.exists(self.savePath):
            util.log_warning(f"Creating directory {self.savePath}")
            makedirs(self.savePath)

        image.save(f"{self.savePath}/{self.name}-{image.width}.png")
        util.log_msg(f"Image Saved, name: {self.name}-{image.width}.png")

    def resize_image(self, size=(1024, 1024)):
        """Resize image to width and height"""

        img = Image.open(f"{self.imagePath}")
        img = img.resize(size, Image.ANTIALIAS)
        util.log_msg(f"Image Resized, name: {self.name}, scale: {size}")

        self.save_image(img)

    def printDetails(self):
        print("image name: ", self.name)
        print("image path: ", self.imagePath)
        print("save image path: ", self.savePath)

    def title_to_icon_name(self, size=120):
        """Convert title to icon name"""
        return f"{self.name}-{str(size)}.png"

    def get_appropriate_size(self, size, scale):
        """Get appropriate size for image"""

        width = float(size.split("x")[0])
        height = float(size.split("x")[1])
        scale = int(scale.split("x")[0])
        width = width * scale
        height = height * scale
        return (int(width), int(height))

    def generate_json(self):
        util.log_msg(f"Generating JSON for {self.name}")
        """Generate json file"""

        with open(f"{self.savePath}/Contents.json", "w") as f:
            json.dump(self.dataTemplate, f, indent=4)

        # For testing purposes
        return self.dataTemplate

    def generate_icon_set(self):
        """Generate App IconSet"""
        util.log_msg(f"Generating App IconSet for {self.name}")

        try:

            for image in self.dataTemplate["images"]:
                self.resize_image(
                    self.get_appropriate_size(image["size"], image["scale"])
                )

                self.generate_json()
                print("Generated iconset: ", self.savePath)

        except UnidentifiedImageError:
            print("Weird Image", name, path)
        except Exception as e:
            print("Unknown error", e)

