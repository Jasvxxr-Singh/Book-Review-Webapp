import abc
from typing import List
from datetime import date

from library.domain.model import *

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_books(self) -> list[Book]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_book(self, book: Book):
        raise NotImplementedError

    @abc.abstractmethod
    def get_authors(self) -> list[Author]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_author(self, author: Author):
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_books(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_users(self) -> list[User]:
        raise NotImplementedError

    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name) -> User or None:
        raise NotImplementedError

    @abc.abstractmethod
    def has_book(self, author: Author) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def get_search_results(self) -> list[Book]:
        raise NotImplementedError

    def set_search_results(self, array):
        raise NotImplementedError

    def clear_search_results(self):
        raise NotImplementedError