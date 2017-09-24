class FileWriter:
    @staticmethod
    def write(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
