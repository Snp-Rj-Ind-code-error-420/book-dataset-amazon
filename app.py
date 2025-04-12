import streamlit as st

pages=[
	st.Page(r".\src\homepage.py",title="Overview",icon=":material/subject:"),
	st.Page(r".\src\EDA.py",title="EDA(Exploratory Data Analysis)",icon=":material/query_stats:")
]


pg = st.navigation(pages)
# uhouh/sda
pg.run()