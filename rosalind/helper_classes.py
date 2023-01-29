import pathlib
import shutil


class Solution:

    def __init__(self, filename: str = None):
        if filename is not None:
            self.filename = filename

    def get_dataset(self):
        src_dir = '/Users/hello/Downloads/' + self.filename
        tgt_dir = pathlib.Path().absolute()
        shutil.move(src_dir, tgt_dir)

    def read_dataset(self) -> str:
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print("File non-existent")
        else:
            return data[:-1]
