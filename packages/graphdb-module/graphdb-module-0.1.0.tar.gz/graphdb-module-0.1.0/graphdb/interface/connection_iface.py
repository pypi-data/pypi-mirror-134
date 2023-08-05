from abc import ABC, abstractmethod
from typing import ClassVar, Union, List, Dict, Any

from neo4j import Result, GraphDatabase


class GraphDbConnectionInterface(ABC):

    @classmethod
    def from_uri(
            cls,
            connection_uri: str,
            db_name: str = "neo4j",
            username: str = None,
            password: str = None,
            **config
    ) -> ClassVar:
        """Create object connection from connection uri only
        this uri will include username and password for connect
        there's will be 2 option for parse connection uri
            : sample 1
                amqps://admin_rabbit:jFvpmUugMBW42rsPjewk@b-1c35ddb6-f9bd-43fc-b854-015ec01de42e.mq.ap-southeast-1.amazonaws.com:5671
                this connection uri will include username and password then need to take out username and password
                and pass value as separate parameters
            : sample 2
                neo4j://localhost:7687
                this connection uri is not include username and password, so that we need to pass username and password separately
        :param connection_uri: string connection uru
        :param db_name: string database name, leave it empty to use default name
        :param username: string username credential
        :param password: string password credential
        :return: current object class
        """
        raise NotImplementedError

    @abstractmethod
    def get_connection(
            self,
    ) -> GraphDatabase.driver:
        """Get neo4j connection object
        :return: object neo4j driver connection
        """
        raise NotImplementedError

    @abstractmethod
    def execute_query(
            self,
            query: str,
            payload: Union[None, Dict[str, Any], List[Any]] = None,
            inverse: bool = False,
            multi_node: bool = False,
    ) -> bool:
        """Execute query that already prepared and return result
        :param query: string query neo4j
        :param payload: dictionary payload or it can be None
        :param inverse: is vice versa from usually result
            when create or update something it will return result, but when delete it suppose to empty
            so that we only use some flag to inverse when result is empty then operation is successfully
        :param multi_node: boolean to flag that current operation is creating multi node
        :return: boolean
        """
        raise NotImplementedError

    @abstractmethod
    def fetch_query(
            self,
            query: str,
            payload: Union[None, Dict[str, Any], List[Any]] = None
    ) -> Union[Result, None]:
        """Execute query that already prepared and return result
        :param query: string query neo4j
        :param payload: dictionary payload or it can be None
        :return: neo4j result
        """
        raise NotImplementedError
