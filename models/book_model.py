from models.BaseObj import BaseObj
import datetime


class Book(BaseObj):
    def __init__(self, isbn: str, title: str, sum_title: str, author: str, publish_date: datetime, publisher: str,
                 pages: int, description: str, website: str):

        self._isbn = isbn
        self._title = title
        self._sum_title = sum_title
        self._author = author
        self._publish_date = publish_date
        self._publisher = publisher
        self._pages = pages
        self._description = description
        self._website = website
