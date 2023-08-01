class Book():
    def __init__(self,title,author, pages) :
        self.title=title
        self.author=author
        self.pages=pages

    def __repr__(self):
        return f"Title: {self.title},author:{self.author}"

    def __len__(self):
        return self.pages
mybook=Book("rose", 'jose',250)

length_len=len(mybook)
print(length_len)

        