import os
class Paper():
    def __init__(self, author: str, title: str, date: str, branch: str, twig: str,
                 subset: str, path=None) -> None:
        self._author = author
        self._title = title
        self._date = date   #Date must be in DD/MM/YYYY format example 03/02/2025
        self._content = " "
        self.branch = branch
        self.twig = twig
        self.subset = subset
        self.path = path
        if path is not None:
            self.extract(path)


    def __str__(self):
        return f"{self.branch} paper: {self._title} by {self._author}"
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content: str):
        self._content = content

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author: str):
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date: str):
        self._date = date

    def extract(self, file_path) -> bool:
        """Extracts text from a .txt file. Returns True if successful"""
        if os.path.exists(file_path):
            if file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as file:
                    self._content = file.read()
                    print("Successfully extracted file!")
                    self.path = file_path
                    return True
            else:
                print("File type not supported!")
                return False
        else:
            print("File does not exist!")
            return False


if __name__ == "__main__":
    relativity = Paper(author="Albert Einstein", title="theory of Relativity", date="02/03/2025",
                       branch="math", subset="math", twig="math")
    print(str(relativity))
