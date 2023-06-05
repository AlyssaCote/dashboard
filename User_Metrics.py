import streamlit as st
import data

# so it takes up the entire width of the page
st.set_page_config(layout="wide")

# image and header row (built by side by side columns)
iCol, hCol = st.columns([5,10])
with iCol:
    st.image("assets/SmartSim.png", width=200)
with hCol:
    st.header('Example Customer: Experiment Name')

# tabs that render different things. TODO try to put this in sidebar maybe
col1, col2 = st.columns([5, 5])

with col1:
    st.plotly_chart(data.dummy_fig1)

with col2:
    st.plotly_chart(data.dummy_fig2)
