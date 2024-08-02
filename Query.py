import oracledb
import pandas as pd
import logging

class Query:
    def __init__(self):
        """
        Initialize a new instance of Query.

        Parameters:
        None
        """
        self.driver = 'oracle'
        self.ARKEON_host = 'ARC-CLUSTER.CMC.EC.GC.CA'
        self.ARKEON_port = '1521'
        self.ARKEON_service = 'archive.cmc.ec.gc.ca'

    def connect(self, usern, passw):
        """
        Connect to database.

        Parameters:
        usern: Username that the user entered.
        passw: Password that the user entered.

        Returns:
        src_conn, bool: The connection to the database and True if the connection was successful. Else it returns None, False.
        """
        try:
            src_conn = oracledb.connect(
                user = usern,
                password = passw,
                host = self.ARKEON_host,
                port = self.ARKEON_port,
                service_name = self.ARKEON_service
            )
            return src_conn, True
        except oracledb.DatabaseError as err:
            error, = err.args
            logging.error('Unable to establish connection, due to: %s', error.message)
            return None, False


    def get_value(self, connection, select_clause, from_clause, where_conditions=None, params=None):
        """
        Turn the SQL query into a DataFrame.

        Parameters:
        connection: The arkeon connection.
        select_clause: The SELECT clause of the SQL query.
        from_clause: The FROM clause of the SQL query.
        where_conditions: The WHERE clause of the SQL query. (Optional)
        params: A dictionary of parameters for the SQL query WHERE conditions.

        Returns:
        pd.DataFrame(rows, columns = column_headers): A DataFrame of the normals query, and returns None if it is an empty dataframe.
        """
        if connection is None:
            logging.error('No database connection established.')
            return None
        
        query = f'''
        SELECT
            {select_clause}
        FROM
            {from_clause}
        '''
        if where_conditions:
            query += f' WHERE {where_conditions}'

        cursor = connection.cursor()

        if cursor is not None:
            logging.info('Executing query...')
            logging.info(query)
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
            except Exception as err:
                msg = 'Unable to execute query, due to: %s' % str(err)
                logging.error(msg)
                return None
            logging.info('Query execution complete.')
        else:
            logging.error('Unable to execute query, due to: no cursor.')
            return None
        
        column_headers = [desc[0] for desc in cursor.description]
        rows = []
        for row in cursor:
            rows.append(row)
            
        cursor.close()
        logging.info('Cursor closed.')

        if len(rows) == 0:  
            return None
        else:
            return pd.DataFrame(rows, columns=column_headers)
