import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import data


iCol, hCol = st.columns([5,10])
with iCol:
    st.image("/Users/alyssacote/Streamlit/dashboard/assets/SmartSim.png", width=200)
with hCol:
    st.header('Example Customer: Experiment Name')

with st.container():
    st.subheader("DB at a glance")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
            st.write(':large_green_circle: Health Status: Good')
    with col2:
            st.write('DB Name: Redis')
    with col3:
            st.write('Deployment Type: Colocated') 

with st.container():
        st.subheader("Shard Info")
        col1, col2 = st.columns([6, 6])
        with col1:
            st.write("Shard Table: 3 Shards")
            st.table(data.shard_data)
        with col2:
            st.write("Shard 2 Memory Usage")
            st.plotly_chart(data.dummy_fig3)

with st.container():
        st.subheader("Client Info")
        col1, col2 = st.columns([6, 6])
        with col1:
            st.write("Client Table? Maybe just more info tbd")
            st.table(data.shard_data)
        with col2:
            st.write("Total Client Count")
            st.plotly_chart(data.dummy_fig3)

with st.container():
        st.subheader("Key Info")
        col1, col2 = st.columns([6, 6])
        with col1:
            st.selectbox(label="Key Dropdown", options=("All", "Model", "Script", "Tensor"))
            st.write("Key Tables: 3 Keys")
            st.table(data.key_data)
        with col2:
            st.write("Total Key Count")
            st.plotly_chart(data.dummy_fig3)