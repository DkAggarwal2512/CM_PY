import graphviz
import streamlit as st


# object
a = graphviz.Graph(engine='neato')
a.node('DataSet')
a.edge('Input', 'Process')
a.edge('Process', 'Input', 'Input Unit')
a.edge('Output', 'Process', 'Output Process')
a.edge('Process', 'Output')

a.node('Client')

st.graphviz_chart(a)
