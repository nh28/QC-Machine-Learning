import math
import sys

class Distance:
    @staticmethod
    def find_closest_stations(station_id, query, connection, year, month, day):
        select_clause = 'STN_ID, PROVINCE, ELEVATION, LATITUDE, LONGITUDE'
        from_clause = 'ecodat.station_information'
        where_conditions = 'STN_ID = :id'
        params = {
                    'id': station_id,
                    }
        # Assume station is not going to return an empty dataframe
        station = query.get_value(connection, select_clause, from_clause, where_conditions, params)
        station_lat = station.iloc[0]["LATITUDE"]
        station_long = station.iloc[0]["LONGITUDE"]
        station_elevation = station.iloc[0]["ELEVATION"]
        max_distance = get_max_radius(int(station_lat[:2]))
        closest_station_id = (-1,sys.float_info.max, -1)
        second_closes_station_id = (-1,sys.float_info.max, -1)
    
        all_stations = query.get_value(connection, select_clause, from_clause)
        for index, row in all_stations.iterrows():
            row_id = row["STN_ID"]
            if station_id != row_id:
                row_lat = row["LATITUDE"]
                row_long = row["LONGITUDE"]
                row_elevation = row["ELEVATION"]
                euclid_dist = math.sqrt(((station_lat-row_lat)**2) + ((station_long-row_long)**2) + ((station_elevation-row_elevation)**2))
                
                if euclid_dist <= max_distance and euclid_dist < closest_station_id[1]:
                    value = check_value(row_id, query, connection, year, month, day)
                    if value != None and value[0] == True:
                        closest_station_id = (row_id, euclid_dist, value[1])
                elif euclid_dist <= max_distance and euclid_dist < second_closes_station_id[1]:
                    value = check_value(row_id, query, connection, year, month, day)
                    if value != None and value[0] == True:
                        second_closes_station_id = (row_id, euclid_dist, value[1])
        return [closest_station_id, second_closes_station_id]

def get_max_radius(lat):
    # Southern Canada
    if 41 <= lat < 50:
        return 5
    # Middle Canada
    elif 50 <= lat < 60:
        return 10
    # Northern Canada
    elif lat >= 60:
        return 20
    else:
        return None 

def check_value(station_id, query, connection, year, month, day):
    station_select_clause = '*'
    station_from_clause = 'archive.obs_data'
    station_where_conditions = 'STN_ID = :id AND LOCAL_YEAR = :yr AND LOCAL_MONTH = :mo AND LOCAL_DAY = :day AND MEAS_TYPE_ID IN :meas'
    station_params = {
        'id': station_id,
        'yr': year,
        'mo': month,
        'day': day,
        'meas': -1
        }
    
    station_params['meas'] = 951
    station_info_951 = query.get_value(connection, station_select_clause, station_from_clause, station_where_conditions, station_params)
    station_params['meas'] = 14910
    station_info_14910 = query.get_value(connection, station_select_clause, station_from_clause, station_where_conditions, station_params)
    station_params['meas'] = 15498
    station_info_15498 = query.get_value(connection, station_select_clause, station_from_clause, station_where_conditions, station_params)
    
    if station_info_951 is not None and not station_info_951.empty:
        val = station_info_951.iloc[0]["VALUE"]
        if val != -99999 and val is not None:
            return (True, val)
    elif station_info_14910 is not None and not station_info_14910.empty:
        val = station_info_14910.iloc[0]["VALUE"]
        if val != -99999 and val is not None:
            return (True, val)
    elif station_info_15498 is not None and not station_info_15498.empty:
        val = station_info_15498.iloc[0]["VALUE"]
        if val != -99999 and val is not None:
            return (True, val)
    else:
        return (False, None)
    