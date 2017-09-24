def write_from_file(file, content):
    file.write(content)


def write_from_file_path(file_path, content):
    with open(file_path, 'a') as _file:
        _file.write(content)


def get_content_from_file_path(file_path):
    with open(file_path, 'r') as _file:
        return _file.read()


def return_file_with_extra_text(file_path, extra):
    with open(file_path, 'r') as _file:
        file_content = _file.read()
        return add_extra(file_content, extra)


def add_extra(content, extra):
    return content + extra
