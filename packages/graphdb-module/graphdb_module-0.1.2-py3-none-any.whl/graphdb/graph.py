from typing import ClassVar, List, Dict, Any

from pandas import DataFrame, read_csv

from graphdb.connection.graph_connection import GraphDbConnection
from graphdb.interface.node_create_constraint_iface import NodeCreateConstraintInterface
from graphdb.interface.node_create_iface import NodeCreateInterface
from graphdb.interface.node_create_index_iface import NodeCreateIndexInterface
from graphdb.interface.node_dataframe_iface import NodeDataframeInterface
from graphdb.interface.node_delete_iface import NodeDeleteInterface
from graphdb.interface.node_search_iface import NodeSearchInterface
from graphdb.interface.node_update_iface import NodeUpdateInterface
from graphdb.interface.rel_create_iface import RelationshipCreateInterface
from graphdb.interface.rel_delete_iface import RelationshipDeleteInterface
from graphdb.schema import Node, Relationship
from graphdb.utils import prepare_identifier, make_identifier, log_execution_time


class GraphDb(NodeCreateInterface, NodeSearchInterface, NodeUpdateInterface, NodeDeleteInterface,
              RelationshipCreateInterface, RelationshipDeleteInterface,
              NodeCreateConstraintInterface,
              NodeCreateIndexInterface,
              NodeDataframeInterface):
    """This will inherit to child class
    and sure you can create another method to support your application"""

    def __init__(
            self,
            connection: GraphDbConnection,
            path_data: str = None
    ):
        self.connection = connection
        self.path_data = path_data
        NodeCreateInterface.__init__(self)
        NodeSearchInterface.__init__(self)
        NodeUpdateInterface.__init__(self)
        NodeDeleteInterface.__init__(self)
        RelationshipCreateInterface.__init__(self)
        RelationshipDeleteInterface.__init__(self)
        NodeCreateConstraintInterface.__init__(self)
        NodeCreateIndexInterface.__init__(self)

    @classmethod
    def from_connection(
            cls,
            connection: GraphDbConnection,
    ) -> ClassVar:
        """Create class object from object connection class
        :param connection: string connection uru
        :return: current object class
        """
        return cls(connection)

    @log_execution_time
    def load_from_csv(
            self,
            path_data: str
    ) -> DataFrame:
        """Load data into dataframe from csv file
        :param path_data: string path data where it is stores
        :return: none
        """
        return read_csv(path_data)

    @log_execution_time
    def create_index(
            self,
            node: Node,
            index_name: str,
    ) -> bool:
        """Create new constraint based on specified properties
        :param node: object node
        :param index_name: string index name
        :return: boolean true or false
        """
        query = """
            CREATE BTREE INDEX {} IF NOT EXISTS
            FOR (n:{})
            ON (n.{});
        """.format(index_name, node.label, node.primary_key)
        return self.connection.execute_query(query, inverse=True)

    @log_execution_time
    def create_constraint(
            self,
            node: Node,
            properties: List[str],
            is_unique: bool = False,
            not_null: bool = False,
    ) -> bool:
        """Create new constraint based on specified properties
        :param node: object node
        :param properties: list of property
        :param is_unique: is constraint is unique
        :param not_null: is constraint is not null
        :return: boolean true or false
        """
        constraint = None
        if is_unique:
            constraint = "IS UNIQUE"

        if not_null:
            constraint = "IS NOT NULL"

        if constraint is None:
            return False

        query = """CREATE CONSTRAINT {} FOR (p: {}) REQUIRE ({}) {};""".format(
            node.primary_key,
            node.label,
            ", ".join(map(lambda x: "p.{}".format(x), properties)),
            constraint,
        )
        return self.connection.execute_query(query)

    @log_execution_time
    def find_node(
            self,
            node: Node,
            filter_where: Dict[str, Any] = None,
            limit: int = 100,
    ) -> List[Dict[str, Any]]:
        """Find node with specified parameters
        :param node: object node
        :param filter_where: dictionary filter
        :param limit: default limit query
        :return: list of dictionary
        """
        query = f"MATCH (n: {node.label}) "
        if node.properties is not None:
            query = f"MATCH (n: {node.label} {make_identifier(node.properties)}) "

        if filter_where is not None:
            tmp = [f"n.{k} = ${k}" for k, v in filter_where.items()]
            query += "WHERE {} ".format(" AND ".join(tmp))

        query += "RETURN n LIMIT {}".format(limit)
        if data := self.connection.fetch_query(query, filter_where):
            return [i.get("n", None) for i in data]

        return []

    @log_execution_time
    def create_node(
            self,
            node: Node
    ) -> bool:
        """Create new node with label and properties if set in node class
        it will search node, if exists then update that node only
        there is 2 types for creating nodes
            1. with property
                https://neo4j.com/docs/cypher-manual/current/clauses/create/#create-create-node-and-add-labels-and-properties
            2. without properties
                https://neo4j.com/docs/cypher-manual/current/clauses/create/#create-create-a-node-with-a-label
        example:
            suppose we have 2 nodes object like this:
            1. n = Node(**{"label": "Person", "primary_key": "name", "properties": {
                    "title": "developer",
                    "name": "andy",
                }})
                this node contains properties and will generate query like this:
                    CREATE (n: Person {"title": "developer", "name": "andy"}) RETURN n.name
            2. n = Node(**{"label": "Person", "primary_key": "name"})
                this node not contains properties and will generate query like this:
                    CREATE (n: Person) RETURN n.name
        :param node: object node
        :return: boolean
        """
        query = """MERGE (n: {}) RETURN n;""".format(node.label)
        if node.properties is not None:
            query = """MERGE (n: {} {}) RETURN n;""".format(
                node.label,
                prepare_identifier(node.properties.keys())
            )
        return self.connection.execute_query(query, node.properties)

    @log_execution_time
    def create_multi_node(
            self,
            nodes: List[Node]
    ) -> List[bool]:
        """Create multiple node with label and properties if set in node class,
        this will doing upsert value
        :param nodes: list of object node
        :return: list of boolean
        """
        return list(map(self.create_node, nodes))

    @log_execution_time
    def update_node_property(
            self,
            node: Node,
            update_query: Dict[str, Any]
    ) -> bool:
        """Update node with specified properties
        :param node: object class node
        :param update_query: dictionary filter query
        :return: boolean
        """
        query = f"""
            MATCH (p {make_identifier(node.properties)})
            SET p += {prepare_identifier(update_query.keys())}
            RETURN p;
        """
        return self.connection.execute_query(query, update_query)

    @log_execution_time
    def replace_node_property(
            self,
            node: Node,
            update_query: Dict[str, Any]
    ) -> bool:
        """Replace node properties with new properties
        :param node: object class node
        :param update_query: dictionary filter query
        :return: boolean
        """
        query = f"""
            MATCH (p {make_identifier(node.properties)})
            SET p = {prepare_identifier(update_query.keys())}
            RETURN p;
        """
        return self.connection.execute_query(query, update_query)

    @log_execution_time
    def remove_node_property(
            self,
            node: Node,
            properties: List[str]
    ) -> bool:
        """Remove specified property from node
        :param node: object node
        :param properties: list of property you want to remove from this node
        :return: boolean
        """
        tmp = []
        for k in properties:
            tmp.append("p.{} = null".format(k))

        query = f"""
            MATCH (p {make_identifier(node.properties)})
            SET {", ".join(tmp)}
            RETURN p;
        """
        return self.connection.execute_query(query)

    @log_execution_time
    def remove_all_node_property(
            self,
            node: Node
    ) -> bool:
        """Remove all property from this node
        :param node: object node
        :return: boolean
        """
        query = f"""
            MATCH (p {make_identifier(node.properties)})
            SET p = {"{}"}
            RETURN p;
        """
        return self.connection.execute_query(query)

    @log_execution_time
    def delete_node_with_relationship(
            self,
            node: Node
    ) -> bool:
        """Delete for specified node object, please note this will remove node with all relationship on it
        :param node: object node that we want to delete
        :return: bool
        """
        query = f"""
            MATCH (p {make_identifier(node.properties)})
            DETACH DELETE p;
        """
        return self.connection.execute_query(query, inverse=True)

    @log_execution_time
    def delete_node(
            self,
            node: Node
    ) -> bool:
        """Delete for specified node object, it will leave relationship as it is
        :param node: object node that we want to delete
        :return: bool
        """
        query = f"""
            MATCH (p {make_identifier(node.properties)})
            DELETE p;
        """
        return self.connection.execute_query(query, inverse=True)

    @log_execution_time
    def create_relationship(
            self,
            node_from: Node,
            node_to: Node,
            rel: Relationship
    ) -> bool:
        """Create new relationship between 2 nodes
        :param node_from: object node from
        :param node_to: object node to
        :param rel: object relationship with name
        :return: boolean
        """
        query = f"""
            MATCH
              (a: {node_from.label} {make_identifier(node_from.properties)}),
              (b: {node_to.label} {make_identifier(node_to.properties)})
            CREATE (a)-[r:{rel.relationship_name}]->(b)
            RETURN a, b;
        """
        return self.connection.execute_query(query)

    @log_execution_time
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
        query = f"""
            MATCH (n: {node.label})-[r:{rel.relationship_name}]->()
            DELETE r;
        """
        if node.properties is not None:
            query = f"""
                MATCH (n: {node.label} {make_identifier(node.properties)})-[r:{rel.relationship_name}]->()
                DELETE r;
            """
        return self.connection.execute_query(query, inverse=True)
