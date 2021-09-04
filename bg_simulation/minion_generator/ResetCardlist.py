import os


class ResetCardlist(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def remove_information(self):
        for file in os.listdir(self.file_path):
            os.remove(f"{self.file_path}/{file}")

        open(f"{self.file_path}/__init__.py", 'w')
