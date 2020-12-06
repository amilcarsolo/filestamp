import os
from pathlib import Path
from os.path import isfile, join

class Renaming(object):
    def __init__(self):
        self.folder = f"{os.path.dirname(os.path.abspath(__file__)/{'pre_photos'})}"
        self.file_extensions = ('.jpeg', '.png', '.jpg')

    def run(self):
        files = self.get_files()
        self.rename_multiple_files(files)

    def get_files(self):
        onlyfiles = [f for f in os.listdir(self.folder) if isfile(join(self.folder, f))]
        return [f for f in onlyfiles if f.endswith(self.file_extensions)]

    def rename_multiple_files(self, files):
        start = 1
        os.chdir(self.folder)
        for file in files:
            if file.endswith(self.file_extensions):
                extension = Path(file).suffix
                os.rename(file, str(start) + extension)
            start += 1

def main():
    rename = Renaming()
    rename.run()

if __name__ == '__main__':
    main()