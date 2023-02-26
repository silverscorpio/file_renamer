from file_func import get_file_snakecase
import os


def renamer(curr_dir: str):
    for i in os.listdir(curr_dir):
        if not i.endswith(".DS_Store"):
            # file rename
            if os.path.isfile(os.path.join(curr_dir, i)):
                os.renames(os.path.join(curr_dir, i), os.path.join(curr_dir, get_file_snakecase(i)))

            # folder renaming and recursion
            elif os.path.isdir(os.path.join(curr_dir, i)):
                os.renames(os.path.join(curr_dir, i), os.path.join(curr_dir, get_file_snakecase(i)))
                renamer(os.path.join(curr_dir, get_file_snakecase(i)))


if __name__ == "__main__":
    renamer(curr_dir=os.getcwd())
