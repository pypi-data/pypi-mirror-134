import logging
from typing import ClassVar, List, Dict, Any, Union

from neo4j import GraphDatabase, WRITE_ACCESS, READ_ACCESS, Result
from neo4j.exceptions import ServiceUnavailable

from graphdb.interface.connection_iface import GraphDbConnectionInterface
from graphdb.utils import parse_connection_uri


class GraphDbConnection(GraphDbConnectionInterface):

    def __init__(
            self,
            connection_uri: str,
            db_name: str = "neo4j",
            username: str = None,
            password: str = None,
            **config
    ):
        self.connection_uri = connection_uri
        self.db_name = db_name
        self.username = username
        self.password = password

        if self.username is None and self.password is None:
            # if username and password is empty probably
            # credential is in connection uri
            self.connection_uri, self.username, self.password = parse_connection_uri(connection_uri)

        self.driver = GraphDatabase.driver(
            self.connection_uri,
            auth=(self.username, self.password),
            # The maximum duration in seconds that the driver will
            # keep a connection for before being removed from the pool.
            # unit is in float
            max_connection_lifetime=1_000,
            # maximum pool size
            # unit is in int
            max_connection_pool_size=100,
            # The maximum amount of time in seconds that a managed transaction will retry before failing.
            max_transaction_retry_time=30,
            **config
        )

    def get_connection(
            self,
    ) -> GraphDatabase.driver:
        """Get neo4j connection object
        :return: object neo4j driver connection
        """
        raise self.driver

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
        return cls(connection_uri, db_name, username, password, **config)

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
        try:
            with self.driver.session(database=self.db_name, default_access_mode=WRITE_ACCESS) as session:
                # if any payload is passed then execute with payload
                if payload is not None:
                    # if we want to create multi node then pass
                    # parameters json as keys that already define
                    if multi_node:
                        result = session.run(query, json=payload)
                    else:
                        result = session.run(query, payload)
                    # if we want to see if value is empty then use inverse
                    if inverse:
                        return len(result.data()) == 0

                    return len(result.data()) > 0

                # otherwise let it be
                result = session.run(query)
                # if we want to see if value is empty then use inverse
                if inverse:
                    return len(result.data()) == 0

                return len(result.data()) > 0
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(query=query, exception=exception))
            return False

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
        try:
            with self.driver.session(database=self.db_name, default_access_mode=READ_ACCESS) as session:
                # if any payload is passed then execute with payload
                if payload is not None:
                    result = session.run(query, payload)
                    return result.data()

                # otherwise let it be
                result = session.run(query)
                return result.data()
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(query=query, exception=exception))
            return None
