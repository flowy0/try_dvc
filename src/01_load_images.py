# 01_load_images.py
# ref https://pypi.org/project/bing-image-downloader/

from utility import create_folders
from bing_image_downloader import downloader

DIR_IMG = 'data/images'
search_string ='superman'
search_limit=15


if __name__ == "__main__": 
    #create some folders to store
    create_folders([DIR_IMG])
    #get a csv
    downloader.download(search_string, limit=search_limit, \
    output_dir=DIR_IMG, adult_filter_off=True, force_replace=False, timeout=60)
