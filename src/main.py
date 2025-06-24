from wipe_copy_dir import wipe_copy_dir
from content_gen import generate_pages_recursively
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print(f"Deleted {dir_path_public} directory.")

    print(f"Copying {dir_path_static} to {dir_path_public} directory...")
    wipe_copy_dir(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursively(dir_path_content, template_path, dir_path_public)
        

if __name__ == "__main__":
    main()