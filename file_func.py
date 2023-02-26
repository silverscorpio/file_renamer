def get_file_snakecase(text: str) -> str:
    return "".join(["_" if i == " " else i for i in text])


if __name__ == "__main__":
    get_file_snakecase("")
