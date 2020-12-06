import os
from os.path import isfile, join
from PIL import Image

class WatermarkAutomation:
    def __init__(self):
        self.file_extension = ('.jpg', '.png', '.jpeg')
        self.in_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'pre_photos'}"
        self.out_directory = f"{os.path.dirname(os.path.abspath(__file__))}/{'post_photos'}"
        self.watermark = Image.open('watermark.png')
        self.watermark_width = self.watermark.width
        self.watermark_height = self.watermark.height
    
    def run(self):
        files = self.get_files_from_directory()
        self.watermark_all_files(files)
        self.delete_unedited(files)

    def delete_unedited(self, files):
        for file in files:
            os.remove(f"{self.in_directory}/{file}")

    def get_files_from_directory(self):
        onlyfiles = [f for f in os.listdir(self.in_directory) if isfile(join(self.in_directory, f))]
        return [f for f in onlyfiles if f.endswith(self.file_extension)]

    def watermark_all_files(self, pictures):
        for picture in pictures:
            self.watermark_single_file(picture)

    def watermark_single_file(self, file_name):
        image = Image.open(f"{self.in_directory}/{file_name}")
        image_width = image.width
        image_height = image.height
        image.paste(self.watermark,
                    (int((image_width - self.watermark_width) / 2), int((image_height - self.watermark_height) / 2)),
                    self.watermark)
        image.save(f'{self.out_directory}/marked_{file_name}')

        

def main():
    automation = WatermarkAutomation()
    automation.run()

if __name__ == "__main__":
    main()