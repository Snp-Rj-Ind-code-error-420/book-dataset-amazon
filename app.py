import streamlit as st
try :
	# x=1/0
	pages=[
		st.Page("pages/homepage.py",title="Overview",icon=":material/subject:"),
		st.Page("pages/EDA.py",title="EDA(Exploratory Data Analysis)",icon=":material/data_exploration:"),
		st.Page("pages/insights.py",title="Insights",icon=":material/search_insights:"),
	]




	pg = st.navigation(pages)
	# uhouh/sda
	pg.run()
except Exception as e:
	print(f'an exception occure {e} try rebooting')
	st.toast(f'an exception occure {e} try rebooting',icon="🚨")