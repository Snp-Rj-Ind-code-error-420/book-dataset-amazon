import streamlit as st

pages=[
	st.Page("homepage.py",title="Overview",icon=":material/subject:"),
	st.Page("EDA.py",title="EDA(Exploratory Data Analysis)",icon=":material/data_exploration:"),
	st.Page("insights.py",title="Insights",icon=":material/search_insights:"),
]


pg = st.navigation(pages)
# uhouh/sda
pg.run()