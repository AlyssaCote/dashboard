import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import data

# so it takes up the entire width of the page
st.set_page_config(layout="wide")

# image and header row (built by side by side columns)
iCol, hCol = st.columns([5,10])
with iCol:
    st.image("/Users/alyssacote/UIProjects/Dash/assets/SmartSim.png", width=200)
with hCol:
    st.header('Example Customer: Experiment Name')

# @app.callback(
#     Output('graph-with-slider', 'figure'),
#     Input('year-slider', 'value'))
# def update_figure(selected_year):
#     filtered_df = df[df.year == selected_year]

#     fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#     fig.update_layout(transition_duration=500)

#     return fig

# tabs that render different things. TODO try to put this in sidebar maybe
# tab1, tab2, tab3 = st.tabs(["User Metrics", "Workflow Telemetry", "Logs"])
# with tab1:
col1, col2 = st.columns([5, 5])

with col1:
    st.plotly_chart(data.dummy_fig1)

with col2:
    st.plotly_chart(data.dummy_fig2)
