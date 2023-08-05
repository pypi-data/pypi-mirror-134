from abc import ABC, abstractmethod
from typing import List, Dict, Any

from graphdb.schema import Node


class NodeSearchInterface(ABC):
    """Base class for basic operation search or read node"""

    @abstractmethod
    def find_node(
            self,
            node: Node,
            filter_where: Dict[str, Any],
            limit: int
    ) -> List[Dict[str, Any]]:
        """Find node with specified parameters
        :param node: object node
        :param filter_where: dictionary filter
        :param limit: default limit query
        :return: list of dictionary
        """
        raise NotImplementedError
