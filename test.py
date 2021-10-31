import unittest
from Helper import iconset, imageset, util

util = util.Utils()


class TestImageGeneration(unittest.TestCase):

    def test_generate_imageset_json(self):
        imgset = imageset.ImageSet("ImageSet-Test", "tests/images/Test.png")
        result = imgset.generateJson()

        expected = {'images': [{'idiom': 'universal', 'scale': '1x', 'filename': 'ImageSet-Test@1x.png'}, {'idiom': 'universal', 'scale': '2x',
                                                                                                           'filename': 'ImageSet-Test@2x.png'}, {'idiom': 'universal', 'scale': '3x', 'filename': 'ImageSet-Test@3x.png'}], 'author': 'iAssets', 'version': '90.29'}
        self.assertEqual(expected, result)

    def test_generate_iconset_json(self):
        imgset = iconset.IconSet(
            "AppIcon-Test", "tests/images/Test.png")
        result = imgset.generateJson()

        expected = {'images': [{'size': '60x60', 'idiom': 'car', 'filename': 'AppIcon-Test-120.png', 'scale': '2x'}, {'size': '60x60', 'idiom': 'car', 'filename': 'AppIcon-Test-180.png', 'scale': '3x'}, {'size': '20x20', 'idiom': 'ipad', 'filename': 'AppIcon-Test-20.png', 'scale': '1x'}, {'size': '20x20', 'idiom': 'ipad', 'filename': 'AppIcon-Test-40.png', 'scale': '2x'}, {'size': '29x29', 'idiom': 'ipad', 'filename': 'AppIcon-Test-29.png', 'scale': '1x'}, {'size': '29x29', 'idiom': 'ipad', 'filename': 'AppIcon-Test-58.png', 'scale': '2x'}, {'size': '40x40', 'idiom': 'ipad', 'filename': 'AppIcon-Test-40.png', 'scale': '1x'}, {'size': '40x40', 'idiom': 'ipad', 'filename': 'AppIcon-Test-80.png', 'scale': '2x'}, {'size': '76x76', 'idiom': 'ipad', 'filename': 'AppIcon-Test-76.png', 'scale': '1x'}, {'size': '76x76', 'idiom': 'ipad', 'filename': 'AppIcon-Test-152.png', 'scale': '2x'}, {'size': '83.5x83.5', 'idiom': 'ipad', 'filename': 'AppIcon-Test-167.png', 'scale': '2x'}, {'size': '20x20', 'idiom': 'iphone', 'filename': 'AppIcon-Test-40.png', 'scale': '2x'}, {'size': '20x20', 'idiom': 'iphone', 'filename': 'AppIcon-Test-60.png', 'scale': '3x'}, {'size': '29x29', 'idiom': 'iphone', 'filename': 'AppIcon-Test-58.png', 'scale': '2x'}, {'size': '29x29', 'idiom': 'iphone', 'filename': 'AppIcon-Test-87.png', 'scale': '3x'}, {'size': '40x40', 'idiom': 'iphone', 'filename': 'AppIcon-Test-80.png', 'scale': '2x'}, {'size': '40x40', 'idiom': 'iphone', 'filename': 'AppIcon-Test-120.png', 'scale': '3x'}, {'size': '60x60', 'idiom': 'iphone', 'filename': 'AppIcon-Test-120.png', 'scale': '2x'}, {'size': '60x60', 'idiom': 'iphone', 'filename': 'AppIcon-Test-180.png', 'scale': '3x'}, {'size': '128x128', 'idiom': 'mac', 'filename': 'AppIcon-Test-128.png', 'scale': '1x'}, {'size': '256x256', 'idiom': 'mac', 'filename': 'AppIcon-Test-256.png', 'scale': '1x'}, {'size': '128x128', 'idiom': 'mac', 'filename': 'AppIcon-Test-256.png', 'scale': '2x'}, {'size': '256x256', 'idiom': 'mac', 'filename': 'AppIcon-Test-512.png', 'scale': '2x'}, {
            'size': '32x32', 'idiom': 'mac', 'filename': 'AppIcon-Test-32.png', 'scale': '1x'}, {'size': '512x512', 'idiom': 'mac', 'filename': 'AppIcon-Test-512.png', 'scale': '1x'}, {'size': '16x16', 'idiom': 'mac', 'filename': 'AppIcon-Test-16.png', 'scale': '1x'}, {'size': '16x16', 'idiom': 'mac', 'filename': 'AppIcon-Test-32.png', 'scale': '2x'}, {'size': '32x32', 'idiom': 'mac', 'filename': 'AppIcon-Test-64.png', 'scale': '2x'}, {'size': '512x512', 'idiom': 'mac', 'filename': 'AppIcon-Test-1024.png', 'scale': '2x'}, {'size': '24x24', 'idiom': 'watch', 'filename': 'AppIcon-Test-48.png', 'subtype': '38mm', 'role': 'notificationCenter', 'scale': '2x'}, {'size': '27.5x27.5', 'idiom': 'watch', 'filename': 'AppIcon-Test-55.png', 'subtype': '42mm', 'role': 'notificationCenter', 'scale': '2x'}, {'size': '29x29', 'idiom': 'watch', 'filename': 'AppIcon-Test-58.png', 'role': 'companionSettings', 'scale': '2x'}, {'size': '29x29', 'idiom': 'watch', 'filename': 'AppIcon-Test-87.png', 'role': 'companionSettings', 'scale': '3x'}, {'size': '40x40', 'idiom': 'watch', 'filename': 'AppIcon-Test-80.png', 'subtype': '38mm', 'role': 'appLauncher', 'scale': '2x'}, {'size': '44x44', 'idiom': 'watch', 'filename': 'AppIcon-Test-88.png', 'subtype': '40mm', 'role': 'appLauncher', 'scale': '2x'}, {'size': '50x50', 'idiom': 'watch', 'filename': 'AppIcon-Test-100.png', 'subtype': '44mm', 'role': 'appLauncher', 'scale': '2x'}, {'size': '86x86', 'idiom': 'watch', 'filename': 'AppIcon-Test-172.png', 'subtype': '38mm', 'role': 'quickLook', 'scale': '2x'}, {'size': '98x98', 'idiom': 'watch', 'filename': 'AppIcon-Test-196.png', 'subtype': '42mm', 'role': 'quickLook', 'scale': '2x'}, {'size': '108x108', 'idiom': 'watch', 'filename': 'AppIcon-Test-216.png', 'subtype': '44mm', 'role': 'quickLook', 'scale': '2x'}, {'size': '1024x1024', 'idiom': 'watch-marketing', 'filename': 'AppIcon-Test-1024.png', 'scale': '1x'}, {'size': '1024x1024', 'idiom': 'ios-marketing', 'filename': 'AppIcon-Test-1024.png', 'scale': '1x'}], 'author': 'Iconizer', 'version': '2020.11.0'}

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
