class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
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
        elif len(new_name) < 1:
            print('Author name must be longer than 0 characters')
        elif hasattr(self, '_name'):
            print('name is a constant')
        else:
            self._name = new_name


    def articles(self):
        pass

    def magazines(self):
        pass

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
    def category(self)
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
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass