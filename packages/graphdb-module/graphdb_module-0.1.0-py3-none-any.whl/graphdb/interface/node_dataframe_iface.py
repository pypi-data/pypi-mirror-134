from abc import ABC, abstractmethod

from pandas import DataFrame

from graphdb.connection.graph_connection import GraphDbConnection


class NodeDataframeInterface(ABC):
    """Base class for basic operation load data from csv to dataframe"""

    @abstractmethod
    def load_from_csv(
            self,
            connection: GraphDbConnection,
            path_data: str
    ) -> DataFrame:
        """Load data into dataframe from csv file
        :param connection: string connection uru
        :param path_data: string path data where it is stores
        :return: none
        """
        raise NotImplementedError
