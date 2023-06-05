
import pandas as pd
import plotly.express as px

dummy_data = pd.DataFrame({
    "Time": [0,1,2,3,4,5,6,7,8,9],
    "Feed Value": [0,1,1,2,3,3,3,4,4,5]
})

dummy_fig1 = px.line(dummy_data, x="Time", y="Feed Value", title="Simulation 1")
dummy_fig2 = px.line(dummy_data, x="Time", y="Feed Value", title="Simulation 2")
dummy_fig3 = px.line(dummy_data, x="Time", y="Feed Value")

shard_data = pd.DataFrame({
    "Shard": ["Shard 1", "Shard 2", "Shard 3"],
    "IP Address": ["127.0.0.1", "127.0.0.1", "127.0.0.1"],
    "Port": [80,80,80]
})

key_data = pd.DataFrame({
    "Key": ["key_1", "key_2", "key_3"],
    "Key Type": ["Model", "Script", "Tensor"]
})

logs = ['03:24:19 nid00152 SmartSim[2304] INFO Starting Scaling Tests',
'03:24:19 nid00152 SmartSim[2304] DEBUG Configuring model infer-sess-N16-T16-DBN16-DBC1-DBTPQ1 with params {}',
'03:24:29 nid00152 SmartSim[2304] DEBUG Running on allocation 1902231 gleaned from user environment',
'03:24:33 nid00152 SmartSim[2304] DEBUG Launching infer-sess-N16-T16-DBN16-DBC1-DBTPQ1',
'03:24:33 nid00152 SmartSim[2304] DEBUG Starting Job Manager',
'03:24:38 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): New',
'03:24:43 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:24:48 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:24:53 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:24:58 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:25:03 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:25:08 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:25:13 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:25:18 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Running',
'03:25:23 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Completed',
'03:25:23 nid00152 SmartSim[2304] INFO infer-sess-N16-T16-DBN16-DBC1-DBTPQ1(1902231.0): Completed',
'03:25:23 nid00152 SmartSim[2304] DEBUG Sleeping, no jobs to monitor]']
