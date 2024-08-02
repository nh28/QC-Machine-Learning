from datetime import datetime, timedelta

from Distance import Distance

class AddElements:
   
    @staticmethod
    def add(query, row, connection, a, b, c, d, ee, f, g, h, i, j):
        """
        Fill in the input row by fething data from the archive based on the station, year, day, month, and meas type id.

        Parameters:
        query: A Query object used to access ARKEON.
        row: The given row in the excel file.
        connection: The connection to ARKON needed to use query.
        a: Max Temp MEAS_TYPE_ID.
        b: Min Temp MEAS_TYPE_ID.
        c: Mean Temp MEAS_TYPE_ID.
        d: Total Rain MEAS_TYPE_ID.
        e: Total Snow MEAS_TYPE_ID.
        f: Total Precipitation MEAS_TYPE_ID.
        g: 	Snow on Grnd MEAS_TYPE_ID.
        h: DLY04 Snow MEAS_TYPE_ID.
        i: DLY02 Snow MEAS_TYPE_ID.
        j: DLY44 Snow MEAS_TYPE_ID.


        Returns:
        row: The filled in row with all the information from ARKEON.
        """
        select_clause = '*'
        from_clause = 'archive.obs_data'
        where_conditions = 'STN_ID = :id AND LOCAL_YEAR = :yr AND LOCAL_MONTH = :mo AND LOCAL_DAY = :day AND MEAS_TYPE_ID = :meas'
        try:
            station = row['STN_ID']
            year = row['LOCAL_YEAR']
            day = row['LOCAL_DAY']
            month = row['LOCAL_MONTH']
            date = datetime.strptime(row['LOCAL_DATE_VALUE'].strftime('%m/%d/%Y'), '%m/%d/%Y')
            day_1_before = date - timedelta(days=1)
            day_2_before = date - timedelta(days=2)
            day_3_before = date - timedelta(days=3)
            day_1_after = date + timedelta(days=1)
            day_2_after = date + timedelta(days=2)
            day_3_after = date + timedelta(days=3)
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': a
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Max Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Max Temp: {e}")
                row['Max Temp'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': b
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Min Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Min Temp: {e}")
                row['Min Temp'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': c
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Mean Temp'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Mean Temp: {e}")
                row['Mean Temp'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': d
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Total Rain'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Rain: {e}")
                row['Total Rain'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': ee
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Total Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Snow: {e}")
                row['Total Snow'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': f
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Total Precipitation'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Total Precipitation: {e}")
                row['Total Precipitation'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_1_before.year,
                'mo': day_1_before.month,
                'day': day_1_before.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd -1'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -1: {e}")
                row['Snow on Grnd -1'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_2_before.year,
                'mo': day_2_before.month,
                'day': day_2_before.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd -2'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -2: {e}")
                row['Snow on Grnd -2'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_3_before.year,
                'mo': day_3_before.month,
                'day': day_3_before.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd -3'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd -3: {e}")
                row['Snow on Grnd -3'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_1_after.year,
                'mo': day_1_after.month,
                'day': day_1_after.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd +1'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +1: {e}")
                row['Snow on Grnd +1'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_2_after.year,
                'mo': day_2_after.month,
                'day': day_2_after.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd +2'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +2: {e}")
                row['Snow on Grnd +2'] = None
            
            try:
                params = {
                'id': station,
                'yr': day_3_after.year,
                'mo': day_3_after.month,
                'day': day_3_after.day,
                'meas': g
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow on Grnd +3'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching Snow on Grnd +3: {e}")
                row['Snow on Grnd +3'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1982
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Drizzle'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Drizzle: {e}")
                row['Drizzle'] = None
            
            """ No Data
            try:
                value = query.get_value(connection, station, year, month, day, 1984)
                row['Freezing Drizzle'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Freezing Drizzle: {e}")
                row['Freezing Drizzle'] = None
            """

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1980
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Rain'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Rain: {e}")
                row['Rain'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1983
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Freezing Rain'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Freezing Rain: {e}")
                row['Freezing Rain'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1985
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow: {e}")
                row['Snow'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1986
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow Grains'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Grains: {e}")
                row['Snow Grains'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1988
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Ice Pellets'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Ice Pellets: {e}")
                row['Ice Pellets'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1981
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Rain Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Rain Showers: {e}")
                row['Rain Showers'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1990
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Showers: {e}")
                row['Snow Showers'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1992
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Hail'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Hail: {e}")
                row['Hail'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1997
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Blowing Snow'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Blowing Snow: {e}")
                row['Blowing Snow'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1979
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Thunderstorm'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Thunderstorm: {e}")
                row['Thunderstorm'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1991
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Snow Pellet'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Snow Pellet: {e}")
                row['Snow Pellet'] = None

            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': 1989
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['Ice Pellet Showers'] = value.shape[0] if value is not None else 0
            except Exception as e:
                print(f"Error fetching Ice Pellet Showers: {e}")
                row['Ice Pellet Showers'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': h
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['DLY04 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY04 Snow: {e}")
                row['DLY04 Snow'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': i
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['DLY02 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY02 Snow: {e}")
                row['DLY02 Snow'] = None
            
            try:
                params = {
                'id': station,
                'yr': year,
                'mo': month,
                'day': day,
                'meas': j
                }
                value = query.get_value(connection, select_clause, from_clause, where_conditions, params)
                row['DLY44 Snow'] = value['VALUE'] if value is not None else None
            except Exception as e:
                print(f"Error fetching DLY44 Snow: {e}")
                row['DLY44 Snow'] = None
            
            try:
                stations = Distance.find_closest_stations(station, query, connection, year, month, day)
                closest = stations[0]
                second_closest = stations[1]

                if closest[0] != -1:
                    row['Closest_Station'] = (closest[2]/closest[1])
                if second_closest[0] != -1:
                    row['Second_Closest_Station'] = (second_closest[2]/second_closest[1])
            except Exception as e:
                print(f"Error fetching Nearby Station's Snow: {e}")
                row['Closest_Station'] = None
                row['Second_Closest_Station'] = None

        except Exception as e:
            print(f"Error processing row: {e}")
            # Handle any other errors that may occur during row processing
        return row
