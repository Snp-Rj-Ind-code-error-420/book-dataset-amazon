import streamlit as st

pages=[
	st.Page(r".\src\homepage.py",title="Overview",icon=":material/subject:"),
	st.Page(r".\src\insight.py",title="Insights",icon=":material/query_stats:")
]


pg = st.navigation(pages)
# uhouh/sda
#
pg.run()