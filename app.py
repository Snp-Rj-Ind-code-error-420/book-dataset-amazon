import streamlit as st

pages=[
	st.Page(r".\pages\homepage.py",title="Overview",icon=":material/subject:"),
	st.Page(r".\pages\insight.py",title="Insights",icon=":material/query_stats:")
]


pg = st.navigation(pages)
# uhouh
pg.run()