from wipe_copy_dir import wipe_copy_dir
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
        print(f"Deleted {dir_path_public} directory.")

    print(f"Copying {dir_path_static} to {dir_path_public} directory...")
    wipe_copy_dir(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()