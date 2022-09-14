import os
import sys
import glob
import shutil

def merge(folder_path_to_merge: str):
    merged_file_name = os.path.split(folder_path_to_merge)[-1]
    with open(merged_file_name, 'wb') as wfd:
        for part in sorted(glob.glob(os.path.join([folder_path_to_merge, '*.part*']))):
            with open(part, 'fb') as fd:
                shutil.copyfileobj(fd, wfd)

    pass

if __name__ == '__main__':
    args = sys.argv
    folder_path = sys.argv[1]
    merge(folder_path)
    pass
