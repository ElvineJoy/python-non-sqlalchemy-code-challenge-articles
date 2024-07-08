class Article:
    # an empty list to store all instances of class Article
    all = [] 


    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <=50):
            raise ValueError("Title must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        print("Title is immutable")
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("The Author's name should be a string")
        if not name:
            raise ValueError("The name cannot be empty")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("The author's name is immutable")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        return Article(magazine, title)

    def topic_areas(self):
        pass

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        if not (2 <=len(name) <= 16):
            raise ValueError("The name length must be between 2 and 16 characters.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        if not category:
            raise ValueError("The category cannot be empty.")
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass