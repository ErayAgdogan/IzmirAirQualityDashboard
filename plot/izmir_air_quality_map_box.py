import plotly.graph_objs as go
import izmir_air_quality_dataframe.col_names as col_names
from izmir_air_quality_dataframe import helper as df_helper
from string_res import string_keys


def create_scatter_mapbox(df, string_dict):
    size = df[col_names.VALUE].fillna(0) / 4 + 10

    fig = go.Figure()

    map_box = go.Scattermapbox(
        lat=df[col_names.LAT],
        lon=df[col_names.LON],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=size,
            color=df[col_names.COLOR]
        ),
        # Show custom text on hover for na data
        customdata=df[[col_names.DISTRICT_NAME, col_names.GAS_NAME, col_names.VALUE]] \
            .fillna(string_dict[string_keys.NO_DATA])
            .assign(status=df_helper.get_levels_status(df[col_names.LEVEL], string_dict)),
        hovertemplate="".join(["<b>%{customdata[0]}</b><br>",
                               "%{customdata[1]} ", string_dict[string_keys.VALUE_IS], ": %{customdata[2]}<br>\n",
                               "%{customdata[3]}"]),
    )

    fig.add_trace(map_box)

    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=10,
        mapbox_center={"lat": 38.4237, "lon": 27.1428},
    )
    return fig
