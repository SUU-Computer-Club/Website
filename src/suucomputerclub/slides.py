import os
from settings import STATIC_ROOT, SLIDESHOW_PATH

EXTENSIONS = ['.jpg', '.jpeg', '.png']

def get_slides():
    try:
        images = []
        dirs = os.listdir(STATIC_ROOT + SLIDESHOW_PATH)
        for dir in dirs:
            files = os.listdir(STATIC_ROOT + SLIDESHOW_PATH + dir)
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in EXTENSIONS:
                    image = {}
                    image['std'] = '%s%s/%s' % (SLIDESHOW_PATH, dir, file)
                    image['thumb'] = '%s%s/%s/%s' % (SLIDESHOW_PATH, dir, 'thumbs', file)
                    images.append(image)
        return images
    except:
        return None