import streamlit as st
import data


iCol, hCol = st.columns([5,10])
with iCol:
    st.image("assets/SmartSim.png", width=200)
with hCol:
    st.header('Example Customer: Experiment Name')

st.subheader("Logs")
tab1, tab2, tab3 = st.tabs(["Experiment", "Applications", "Orchestrator"])
with tab1:
    logs_container =  st.container()
    logs_container.text("Experiment Logs")
    log_data = ""
    for i in data.logs:
        log_data+=(i+'\n')

    logs_container.info(log_data)

with tab2:
    st.selectbox(label="Application Dropdown", options=("Application 1", "Application 2", "Application 3", "Application 4"))
    
    logs_container =  st.container()
    logs_container.text("Application 1 Logs")
    log_data = ""
    for i in data.logs:
        log_data+=(i+'\n')

    logs_container.info(log_data)

with tab3:
    st.selectbox(label="Shard Dropdown", options=("Shard 1", "Shard 2", "Shard 3", "Shard 4"))
    
    logs_container =  st.container()
    logs_container.text("Shard 1 Logs")
    log_data = ""
    for i in data.logs:
        log_data+=(i+'\n')

    logs_container.info(log_data)