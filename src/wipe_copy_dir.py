import os
import shutil
import logging

logging.basicConfig(level=logging.DEBUG)

def wipe_copy_dir(src, dst):
    """
    Wipes the destination directory and copies the source directory to it.
    
    :param src: Source directory path
    :param dst: Destination directory path
    """
    logging.debug(f"Wiping destination directory: {dst}")
    
    # Remove the destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
        logging.debug(f"Removed existing directory: {dst}")
    os.makedirs(dst)
    
    # Copy the source directory to the destination
    copy_contents(src, dst)

def copy_contents(src, dst):
    """
    recursively copy all contets from src to dst.

    :param src: Source directory path
    :param dst: Destination directory path
    """
    if not os.path.exists(src):
        logging.error(f"Source directory does not exist: {src}")
        return
    # Get a list of files and subdir in src
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)
        
        # If item is a file, copy it
        if os.path.isfile(src_item):
            shutil.copy2(src_item, dst_item)
            logging.debug(f"Copied file: {src_item} to {dst_item}")
        
        # If item is a directory, copy it recursively
        elif os.path.isdir(src_item):
            os.makedirs(dst_item)
            copy_contents(src_item, dst_item)
            logging.debug(f"Copied {src} to {dst}")