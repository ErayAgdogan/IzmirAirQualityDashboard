from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import requests
import streamlit as st
import extra_streamlit_components as stx
import izmir_air_quality_dataframe.col_names as col_names
from izmir_air_quality_dataframe import helper as df_helper
import utlity
from string_res import string_keys
from string_res import string_res
from plot.izmir_air_quality_map_box import create_scatter_mapbox
from plot.izmir_air_quality_bar import create_bar_plot


@st.cache_data
def fetch_data(url):
    return requests.get(url).json()


@st.cache_data
def get_df(date):
    # Example API URL - replace with your actual API
    date = date.strftime('%Y-%m-%d')

    # Make the API request
    url = 'https://openapi.izmir.bel.tr/api/ibb/cevre/havadegerleri/{date}'

    today_response = fetch_data(url.format(date=date))
    today_df = pd.DataFrame(today_response)
    today_df[col_names.DATE] = pd.to_datetime(today_df[col_names.DATE])

    yesterday_date = today_df.loc[0, col_names.DATE] - timedelta(1)
    yesterday_date = yesterday_date.strftime('%Y-%m-%d')
    yesterday_response = fetch_data(url.format(date=yesterday_date))
    yesterday_df = pd.DataFrame(yesterday_response)

    df = df_helper.transform_df(today_df, yesterday_df)

    return df


def set_language(cookie_manager, language):
    st.session_state.language = language
    cookie_manager.set(
        string_res.LANGUAGE,
        language,
        expires_at=datetime.now() + timedelta(weeks=4)
    )


def get_language(cookie_manager):
    language = cookie_manager.get(string_res.LANGUAGE)
    if language:
        return language
    else:
        return utlity.get_local_language()


st.set_page_config(
    page_title='İzmir Hava Kalitesi',
    page_icon='🌍',
    layout="wide"

)

# To supress 'CachedWidgetWarning'
# See https://github.com/Mohamed-512/Extra-Streamlit-Components/issues/70
with st.empty():
    @st.cache_resource
    def get_cookie_manager():
        return stx.CookieManager(key='izmir_air_quality_cookie_manager')


    cookie_manager = get_cookie_manager()

if "language" not in st.session_state:
    st.session_state.language = get_language(cookie_manager=cookie_manager)

# Language selector in the header
header_col = st.columns((9, 1))
with header_col[1]:
    selected_language = st.selectbox(
        label="Dil / Language",
        options=[string_res.TR, string_res.EN],
        index=0 if st.session_state.language == string_res.TR else 1
    )
    # Save the language choice in cookies
    if st.session_state.language != selected_language:
        set_language(cookie_manager=cookie_manager, language=selected_language)


string_dict = string_res.get_string_dict(language=st.session_state.language)


# Placing selectors into sidebar
with st.sidebar:
    st.title(string_dict[string_keys.IZMIR_AIR_QUALITY])

    # Let the user to select date and fetch data
    today = datetime.today()
    selected_date = st.date_input(
        string_dict[string_keys.SELECT_A_DATE],
        value=today,
        max_value=today
    )
    # fetch data using the selected data
    data = get_df(selected_date)

    # list of all pollutants to use on selector
    pollutants = np.sort(data[col_names.GAS_NAME].unique())
    # User selects pollutant
    selected_item = st.selectbox(
        label=string_dict[string_keys.SELECT_POLLUTANT],
        options=pollutants
    )

    data = data[data[col_names.GAS_NAME] == selected_item]
    returned_date = data.iloc[0][col_names.DATE]

# set title and information text for selected pollutant
st.title(
    string_dict[string_keys.IZMIR_POLLUTANT_DATA].format(pollutant=selected_item),
    help=string_dict[string_keys.PM10_EXPLANATION]
)
# show returned date to users
st.markdown(f'<h4 style="opacity: 0.6;">{returned_date.date()}</h4>', unsafe_allow_html=True)


# columns for showing plots and information.
col = st.columns((4.5, 1.5), gap='large')

# show data on metric with trends on the right side.
with col[1]:
    st.markdown(f'### {string_dict[string_keys.DATA_AND_TRENDS]}')
    for _, row in data.iterrows():

        district_name = row[col_names.DISTRICT_NAME]
        value = row[col_names.VALUE]
        value = string_dict[string_keys.NO_DATA] if np.isnan(value) else int(value)
        delta = None if np.isnan(row[col_names.DELTA]) else int(row[col_names.DELTA])

        st.metric(label=district_name, value=value, delta=delta, delta_color='inverse')

# show plots inside tabs
with col[0]:
    tab_names = [string_dict[string_keys.MAP], string_dict[string_keys.BAR]]
    tab_map, tab_bar = st.tabs(tab_names)
    with tab_map:
        plot_map_box = create_scatter_mapbox(data, string_dict)
        st.plotly_chart(plot_map_box)
    with tab_bar:
        plot_bar = create_bar_plot(data, string_dict)
        st.plotly_chart(plot_bar)

    # show information about danger color codes
    with st.expander(string_dict[string_keys.ABOUT_COLOR_CODES], expanded=True):
        st.markdown(
            string_dict[string_keys.COLOR_CODE_EXPLANATION],
            unsafe_allow_html=True
        )
