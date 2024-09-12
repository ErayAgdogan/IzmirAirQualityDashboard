import plotly.graph_objs as go
from izmir_air_quality_dataframe import col_names
from string_res import string_keys
from izmir_air_quality_dataframe import helper as df_helper


def create_bar_plot(df, string_dict):
    fig = go.Figure()
    bar = go.Bar(
        x=df[col_names.DISTRICT_NAME],
        y=df[col_names.VALUE],
        marker_color=df[col_names.COLOR],
        opacity=0.88,
        showlegend=False,
        customdata=df[[col_names.DISTRICT_NAME, col_names.GAS_NAME, col_names.VALUE]] \

            .fillna(string_dict[string_keys.NO_DATA])
            .assign(status=df_helper.get_levels_status(df[col_names.LEVEL], string_dict)),
        hovertemplate="".join(["<b>%{customdata[0]}</b><br>",
                               "%{customdata[1]} ", string_dict[string_keys.VALUE_IS], ": %{customdata[2]}<br>\n",
                               "%{customdata[3]}"]),
    )
    bar_yesterday = go.Bar(
        x=df[col_names.DISTRICT_NAME],
        y=df[col_names.YESTERDAYS_VALUE],
        marker_color=df[col_names.YESTERDAY_COLOR],
        opacity=0.6,
        showlegend=False,
        visible=False,
        customdata=df[[col_names.DISTRICT_NAME, col_names.GAS_NAME, col_names.YESTERDAYS_VALUE]] \
            .fillna(string_dict[string_keys.NO_DATA])
            .assign(status=df_helper.get_levels_status(df[col_names.YESTERDAY_LEVEL], string_dict)),
        hovertemplate="".join(["<b>%{customdata[0]}</b><br>",
                               "%{customdata[1]} ", string_dict[string_keys.PREVIOUS_DAYS_VALUE_IS], ": %{customdata[2]}<br>\n",
                               "%{customdata[3]}"]),

    )

    fig.add_trace(bar_yesterday)
    fig.add_trace(bar)

    fig.update_layout(barmode='group')

    fig.update_layout(
        updatemenus=[
            dict(
                buttons=[
                    dict(label=string_dict[string_keys.DEFAULT],
                         method="relayout",
                         args=[{'xaxis': {'categoryorder': 'array',
                                          'categoryarray': df[col_names.DISTRICT_NAME]}}]),
                    dict(
                        label=' - '.join([string_dict[string_keys.VALUE], string_dict[string_keys.INCREASING]]),
                        method='relayout',
                        args=[{'xaxis': {'categoryorder': 'array',
                                         'categoryarray': df.sort_values(by=col_names.VALUE)[col_names.DISTRICT_NAME]
                                         }}]
                    ),
                    dict(
                        label=' - '.join([string_dict[string_keys.VALUE], string_dict[string_keys.DECREASING]]),
                        method='relayout',
                        args=[{'xaxis': {
                            'categoryorder': 'array',
                            'categoryarray': df.sort_values(by=col_names.VALUE, ascending=False)[
                                col_names.DISTRICT_NAME]
                        }}]
                    ),
                    dict(
                        label=' - '.join([string_dict[string_keys.TREND], string_dict[string_keys.INCREASING]]),
                        method='relayout',
                        args=[{'xaxis': {
                            'categoryorder': 'array',
                            'categoryarray': df.sort_values(by=col_names.DELTA)[col_names.DISTRICT_NAME]
                        }}]
                    ),
                    dict(
                        label=' - '.join([string_dict[string_keys.TREND], string_dict[string_keys.DECREASING]]),
                        method='relayout',
                        args=[{'xaxis': {
                            'categoryorder': 'array',
                            'categoryarray': df.sort_values(by=col_names.DELTA, ascending=False)[
                                col_names.DISTRICT_NAME]
                        }}]
                    )
                ],
                direction="down",
                showactive=True,

                x=0.065,
                xanchor="left",
                y=1.2,
                yanchor="top"
            ),

            dict(
                buttons=[
                    dict(label=string_dict[string_keys.HIDE_PREVIOUS_DAYS_VALUE],
                         method="update",
                         args=[{"visible": [False, True]}]),  # Only current values visible
                    dict(label=string_dict[string_keys.SHOW_REVIOUS_DAYS_VALUE],
                         method="update",
                         args=[{"visible": [True, True]}])  # Both bars visible

                ],
                direction="down",
                showactive=True,
                x=0.75,
                xanchor="left",
                y=1.2,
                yanchor="top"
            )
        ]
    )

    # Add annotation
    fig.update_layout(
        annotations=[
            dict(text=f'{string_dict[string_keys.SORT_BY]}: ', showarrow=False,
                 x=-0.5, xanchor="left", y=1.175, yanchor="top", yref="paper", align="left"
                 )
        ]
    )
    return fig
