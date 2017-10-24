import chardet


class FileUtils:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def split_in_two(self, line_limit, file_path_2=None, file_path_3=None):
        file_path_2 = file_path_2 or '/tmp/file_path_2'
        file_path_3 = file_path_3 or '/tmp/file_path_3'

        with open(self.file_path, 'r', encoding=self.file_encoding) as source, \
                open(file_path_2, 'w', encoding=self.file_encoding) as file_2, \
                open(file_path_3, 'w', encoding=self.file_encoding) as file_3:
            for index, line in enumerate(source):
                if index < line_limit:
                    file_2.write(line)
                else:
                    file_3.write(line)

        return file_path_2, file_path_3

    @property
    def file_encoding(self):
        return self.get_file_encoding(self.file_path)

    @staticmethod
    def get_file_encoding(file_path):
        with open(file_path, 'rb') as encoding_file:
            return chardet.detect(encoding_file.read(1024)).get('encoding', 'UTF-8')
