import numpy as np
import pandas as pd

import izmir_air_quality_dataframe.col_names as col_names
from string_res import string_keys

__izmir_district_locations = {
    "CIGLI": (38.490519, 27.083688),
    "BAYRAKLI": (38.4500, 27.1667),
    "GUZELYALI": (38.396700, 27.083242),
    "KARSIYAKA": (38.4550, 27.1090),
    "BORNOVA": (38.4622, 27.2165),
    "SIRINYER": (38.390696, 27.154486),
    "ALSANCAK": (38.4382, 27.1424),
}

# danger levels of gases
__PM10_cut_points = [0, 50, 100, 260, 400, 520, float('inf')]
__SO2_cut_points = [0, 100, 250, 500, 850, 1100, float('inf')]

# colors for each danger level from green to brown
__colors = ['#00E400', '#FFFF00', '#FF7E00', '#FF0000', '#99004C', '#7E0023']

__levels = [0, 1, 2, 3, 4, 5]


def __get_lat_and_lon(df):
    # set latitudes and longitudes to corresponding districts
    lat_lon = df[col_names.DISTRICT_NAME] \
        .map(__izmir_district_locations) \
        .apply(pd.Series)
    return lat_lon


def __apply_levels_and_colors(df):
    PM10_mask = df[col_names.GAS_NAME] == 'PM10'
    SO2_mask = df[col_names.GAS_NAME] == 'SO2'

    for mask, bins in (PM10_mask, __PM10_cut_points), (SO2_mask, __SO2_cut_points):
        # add colors for today's and yesterday's values
        df.loc[mask, col_names.COLOR] = pd.cut(df[col_names.VALUE], bins=bins, labels=__colors)
        df.loc[mask, col_names.YESTERDAY_COLOR] = pd.cut(df[col_names.YESTERDAYS_VALUE], bins=bins, labels=__colors)

        # add levels for today's and yesterday's values
        df.loc[mask, col_names.LEVEL] = pd.cut(df[col_names.VALUE], bins=bins, labels=__levels)
        df.loc[mask, col_names.YESTERDAY_LEVEL] = pd.cut(df[col_names.YESTERDAYS_VALUE], bins=bins, labels=__levels)

    return df

def get_levels_status(level_series, string_dict):
    levels = [
        string_dict[string_keys.GOOD],
        string_dict[string_keys.MODERATE],
        string_dict[string_keys.SENSITIVE],
        string_dict[string_keys.UNHEALTHY],
        string_dict[string_keys.VERY_UNHEALTHY],
        string_dict[string_keys.HAZARDOUS]
    ]
    map_function = lambda x: '' if np.isnan(x) \
        else ''.join([string_dict[string_keys.AIR_QUALITY_IS],' <b>', levels[int(x)], '</b>'])
    return level_series.map(map_function)



def transform_df(today_df, yesterday_df):
    today_df[col_names.DATE] = pd.to_datetime(today_df[col_names.DATE])
    today_df[col_names.VALUE] = pd.to_numeric(today_df[col_names.VALUE], errors='coerce')

    # we only need yesterday's values however we also need district and gas id for merging data
    yesterday_df = yesterday_df[[col_names.DISTRICT_ID, col_names.GAS_ID, col_names.VALUE]]
    yesterday_df = yesterday_df.rename(columns={col_names.VALUE: col_names.YESTERDAYS_VALUE})

    # merge yesterday's values with the dataframe
    today_df = today_df.merge(yesterday_df, on=(col_names.DISTRICT_ID, col_names.GAS_ID), how='left')
    today_df[col_names.YESTERDAYS_VALUE] = pd.to_numeric(today_df[col_names.YESTERDAYS_VALUE], errors='coerce')
    # difference between today's and yesterday's values for trend
    today_df[col_names.DELTA] = today_df[col_names.VALUE] - today_df[col_names.YESTERDAYS_VALUE]

    ## add levels and colors for today's and yesterday's values
    __apply_levels_and_colors(today_df)

    # add coordinates of districts
    today_df[[col_names.LAT, col_names.LON]] = __get_lat_and_lon(today_df)

    return today_df

