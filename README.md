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
usage: main.py [-h] [-t] [-i IMAGEFOLDER]

Generate @1x @2x and @3x imagesets for Xcode

optional arguments:
  -h, --help            show this help message and exit
  -t, --test            test using the images from tests/images folder
  -i IMAGEFOLDER, --imageFolder IMAGEFOLDER
 ```

---

Help info: 
  IMAGEFOLDER will contain your images you want to save eg:
  
  - your_image_folder
    -  sunset.png
    -  sunrise.png
    -  clouds.png
    -  trees.jpg
    
  
  The generated images will be saved in the desktop folder, inside the folder iAssetsExports.
 
---

Some cool facts?

- I am using threading to make everything super duper fast.
 
- The # of threads spawned = # of images in the folder

- **Logger is used to log the tasks and will be saved as task.log**

 --- 
 
⚠️ Do not run the code in a remote server with automatic build yet, only use manual inputs. ⚠️

NOTE: *This is a WIP, will add appiconset generator, inputs for type of image compression, outputfolder, threads input etc.*


 

 
