import streamlit as st

pages=[
	st.Page("pages/homepage.py",title="Overview",icon=":material/subject:"),
	st.Page("pages/EDA.py",title="EDA(Exploratory Data Analysis)",icon=":material/data_exploration:"),
	st.Page("pages/insights.py",title="Insights",icon=":material/search_insights:"),
]


pg = st.navigation(pages)
# uhouh/sda
pg.run()