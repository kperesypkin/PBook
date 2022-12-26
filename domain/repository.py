from abc import ABC
from abc import abstractmethod


class BaseRepository(ABC):
    """Abstract repository class"""
    @abstractmethod
    def insert(self):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def delete(self):
        raise NotImplementedError

    @abstractmethod
    def get(self):
        raise NotImplementedError


class SqliteRepository(BaseRepository):
    """Sqlite repository implementation"""
    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass
