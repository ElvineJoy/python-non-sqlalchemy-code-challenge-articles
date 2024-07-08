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
    def title(self, value):
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
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        articles = self.articles()
        if not articles:
            return None
        unique_topic_areas = {article.magazine.category for article in self.articles()}
        return list(unique_topic_areas)

class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <=16):
            raise ValueError("The name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or not category:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("The name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("The name length must be between 2 and 16 characters.")
        self._name = name
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category): 
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        if not category:
            raise ValueError("The category cannot be empty.")
        self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        contributing_authors = [author for author in set(authors) if authors.count(author) >2]
        if not contributing_authors:
            return None
        return contributing_authors