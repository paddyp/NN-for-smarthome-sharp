###
# Helper file to keep code clean
###


def clean_path(path: str) -> str:
    if not path.endswith("/"):
        path = path + "/"
    return path
