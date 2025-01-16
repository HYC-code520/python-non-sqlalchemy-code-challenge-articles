class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self) # mistake
   
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title,str):
            print('Title must be a string')
        elif not len(new_title) > 0:
            print('Title must be > 0 chars')
        elif hasattr(self, '_title'):
            print('Title is constant')
        else:
            self._title = new_title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            print('Author must be a Author object')
        else:
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            print('Magazine must be a Magazine object')
        else:
            self._magazine = new_magazine
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print('Author name must be a string')
        elif not len(new_name) > 1:
            print('Author name must be longer than 0 characters')
        elif hasattr(self, '_name'):
            print('name is a constant')
        else:
            self._name = new_name


    def articles(self):
        author_articles = []
        for article in Article.all:
            if article.author is self:
                author_articles.append(article)
        return author_articles

    def magazines(self): #Need alot of help with this func
        magazines_list = [] # missing list
        for article in self.articles(): # author_articles is from above func
            magazines_list.append(article.magazine)
        return list(set(magazines_list)) # Used to remove duplicates from a list

        

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            print('Magazine name must be a string')
        elif not 2 <= len(new_name) <= 16:
            print('Magazine name must be between 2 to 16 characters')
        else:
            self._name = new_name 

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            print('Categories must be a string')
        elif not len(new_category) > 0:
            print('Categories must be longer than 0 characters')
        else:
            self._category = new_category


    def articles(self):
        magazine_articles = []
        for article in Article.all:
            if article.magazine is self:
                magazine_articles.append(article) # Append the article to the list
        return magazine_articles

    def contributors(self):
        contributors_list = []
        for article in self.articles():
            contributors_list.append(article.author) # Append the author of the article, not contributor
        return list(set(contributors_list))


    def article_titles(self):
        pass

    def contributing_authors(self):
        pass