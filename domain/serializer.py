# -*- coding: utf-8 -*-
from abc import ABC
from abc import abstractmethod


class BaseSerializer(ABC):
    """Serializer interface"""

    @abstractmethod
    def serialize(self):
        pass
