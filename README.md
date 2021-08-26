# iAssets

Generate imageset and appiconsets from png/jpg files.

### Installation:

```bash
git clone Aayush9029/iAssets
cd iAssets
# pipenv shell recommended
pip install -r requirements.txt
```

### Usage:

```bash
usage: main.py [-h] -in IMAGEFOLDER [--appicon] [--imageset] [--out OUT]

Generate AppIcon Set and Imageset for Xcode

optional arguments:
  -h, --help            show this help message and exit
  -in IMAGEFOLDER, --imageFolder IMAGEFOLDER
                        Folder containing image/s
  --appicon             Generate appiconset/s
  --imageset            Generate imageset/s
  --out OUT, --outputFolder OUT
                        Output folder, default: Desktop Folder
```

#### Example Usage:

```bash
# Generate app icon and imageset
python3 main.py -i 'tests/images' --out '/Users/your_user_name/Desktop/ExportTest' --appicon --imageset

# Generate app icon only
python3 main.py -i 'tests/images' --out '/Users/your_user_name/Desktop/ExportTest' --appicon 

# Generate image sets only
python3 main.py -i 'tests/images' --out '/Users/your_user_name/Desktop/ExportTest' --imageset 
```

---

Help info:
IMAGEFOLDER will contain your images you want to use to generate icons and or imagesets eg:

- your_image_folder
  - sunset.png
  - sunrise.png
  - clouds.png
  - trees.jpg

> *Generated imagesets will be saved in the output_folder/ImageSets*
> 
> *Generated appiconsets will be saved in the output_folder/AppIconSets*

---

Some cool facts?

- I am using threading to make everything super duper fast.

- The # of threads spawned = # of images in the folder

- **Logger is used to log the tasks and will be saved as task.log**

---
