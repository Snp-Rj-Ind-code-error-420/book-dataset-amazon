import streamlit as st

st.set_page_config(page_title="Overview", 
	page_icon="""<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#EA33F7">
	<path d="M280-280h80v-200h-80v200Zm320 0h80v-400h-80v400Zm-160 0h80v-120h-80v120Zm0-200h80v-80h-80v80ZM200-120q-33 0-56.5-23.5T120-200v-560q0-33 
	23.5-56.5T200-840h560q33 0 56.5 23.5T840-760v560q0 33-23.5 56.5T760-120H200Zm0-80h560v-560H200v560Zm0-560v560-560Z"/></svg>""",
	layout="centered",
	initial_sidebar_state="collapsed",  
	menu_items=None)

st.title(":violet[:material/analytics:]   :violet[Amazon Books Dataset Analysis]")
st.divider()

st.header("Project Overview",divider="rainbow")
with open(r".\content\homepage\overview\overview.md",'r') as over:
	st.markdown(over.read())

st.header("Dataset Description",divider=True)
with open(r".\content\homepage\description\description.md",'r') as disc:
	st.markdown(disc.read())

st.header("Research Questions",divider=True)
with open(r".\content\homepage\research\research.md",'r') as res:
	st.markdown(res.read())

st.header("Insights",divider=True)
with open(r".\content\homepage\insight\insight.md",'r') as ins:
	st.markdown(ins.read())

st.header("Conclusion",divider=True)
with open (r".\content\homepage\conclusion\conclusion.txt",'r') as con:
	st.text(con.read())