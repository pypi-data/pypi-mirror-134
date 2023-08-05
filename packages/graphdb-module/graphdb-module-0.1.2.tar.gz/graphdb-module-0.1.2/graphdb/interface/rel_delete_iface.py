from abc import ABC, abstractmethod

from graphdb.schema import Relationship, Node


class RelationshipDeleteInterface(ABC):
    """Base class for basic operation delete relationship node"""

    @abstractmethod
    def delete_relationship(
            self,
            node: Node,
            rel: Relationship
    ) -> bool:
        """ Delete only relationship from specified node
        :param node: object node that you want to remove
        :param rel: relationship name
        :return: boolean
        """
        raise NotImplementedError
