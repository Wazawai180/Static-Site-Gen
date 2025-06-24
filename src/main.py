from wipe_copy_dir import wipe_copy_dir
from content_gen import generate_pages_recursively
import os
import shutil
import sys

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        if not basepath.startswith("/"):
            print("Basepath should start with a '/' character. Using default basepath '/' instead.")
            basepath = default_basepath
    """
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print(f"Deleted {dir_path_public} directory.")
        """

    print(f"Copying {dir_path_static} to {dir_path_public} directory...")
    wipe_copy_dir(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursively(dir_path_content, template_path, dir_path_public, basepath)
        

if __name__ == "__main__":
    main()