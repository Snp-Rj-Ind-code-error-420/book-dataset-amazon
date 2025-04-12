import streamlit as st

pages=[
	st.Page(r".\src\homepage.py",title="Overview",icon=":material/subject:"),
	st.Page(r".\src\EDA.py",title="EDA(Exploratory Data Analysis)",icon=":material/data_exploration:"),
	st.Page(r".\src\insights.py",title="Insights",icon=":material/search_insights:"),
]


pg = st.navigation(pages)
# uhouh/sda
pg.run()