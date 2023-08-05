from typing import Dict, Optional

from jinja2 import Environment, FileSystemLoader

from aws_managers.athena.athena_ser_des import AthenaSerDes
from aws_managers.paths.dirs import DIR_ATHENA_TEMPLATES


class AthenaQueryGenerator(object):

    SER_DES = {
        'parquet': 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe',

    }
    PARQUET_HIVE_SERDE = (
        'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
    )

    def __init__(self):

        self.env = Environment(loader=FileSystemLoader(DIR_ATHENA_TEMPLATES))

    def create_table(
        self,
        db_name: str,
        table_name: str,
        columns: Dict[str, str],
        location: str,
        serialization_format: int = 1,
        row_format: str = AthenaSerDes.Parquet,
        partition_column: Optional[str] = None,
        encrypted: bool = False
    ) -> str:
        """
        Run this query to create a table pointing to parquet data in S3.
        """
        t = self.env.get_template('create_table.jinja2')
        return t.render(
            db_name=db_name,
            table_name=table_name,
            columns=columns,
            location=location,
            serialization_format=serialization_format,
            row_format=row_format,
            encrypted=str(encrypted).lower()
        )

    def repair_table(
            self,
            database: str, table: str
    ) -> str:
        """
        Run this query right after creating the table, if the S3 data is
        partitioned.

        :param database: Name of the database.
        :param table: Name of the table.
        """
        t = self.env.get_template('repair_table.jinja2')
        return t.render(database=database, table=table)

    def distinct(
            self,
            column: str,
            database: str, table: str
    ) -> str:
        """
        Select distinct values from a column.

        :param column: Name of the column to find a histogram of.
        :param database: Name of the database.
        :param table: Name of the table.
        """
        t = self.env.get_template('distinct.jinja2')
        return t.render(database=database, table=table, column=column)

    def histogram(
            self,
            column: str,
            database: str, table: str
    ) -> str:
        """
        Returns a map containing the count of the number of times each input
        value occurs.

        https://prestodb.io/docs/current/functions/aggregate.html#histogram

        :param column: Name of the column to find a histogram of.
        :param database: Name of the database.
        :param table: Name of the table.
        """
        t = self.env.get_template('histogram.jinja2')
        return t.render(database=database, table=table, column=column)

    def numeric_histogram(
            self,
            column: str, buckets: int,
            database: str, table: str
    ):
        """
        Computes an approximate histogram with up to buckets number of buckets
        for all values. This function is equivalent to the variant of
        numeric_histogram() that takes a weight, with a per-item weight of 1.
        In this case, the total weight in the returned map is the count of items
        in the bin.

        https://prestodb.io/docs/current/functions/aggregate.html#numeric_histogram

        :param column: Name of the column to find a histogram of.
        :param buckets: Number of buckets to create.
        :param database: Name of the database.
        :param table: Name of the table.
        """
        t = self.env.get_template('numeric_histogram.jinja2')
        return t.render(database=database, table=table,
                        column=column, buckets=buckets)
