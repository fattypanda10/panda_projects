def get_html(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()