import streamlit as st
from pages import understand 

st.set_page_config(page_title="Analysis", 
	page_icon="""<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#EA33F7">
	<path d="M400-320q100 0 170-70t70-170q0-100-70-170t-170-70q-100 0-170 70t-70 170q0 100 70 170t170 70Zm0-120q-17 0-28.5-11.5T360-480v-200q0-17 
	11.5-28.5T400-720q17 0 28.5 11.5T440-680v200q0 17-11.5 28.5T400-440Zm-140 0q-17 0-28.5-11.5T220-480v-120q0-17 11.5-28.5T260-640q17 0 28.5 11.5T300-600v120q0 
	17-11.5 28.5T260-440Zm280 0q-17 0-28.5-11.5T500-480v-80q0-17 11.5-28.5T540-600q17 0 28.5 11.5T580-560v80q0 17-11.5 28.5T540-440ZM400-240q-134 0-227-93T80-560q0-134 
	93-227t227-93q134 0 227 93t93 227q0 56-17.5 106T653-363l199 199q11 11 11 28t-11 28q-11 11-28 11t-28-11L597-307q-41 32-91 49.5T400-240Z"/></svg>""",
	layout="wide",
	initial_sidebar_state="auto",  
	menu_items=None)

st.title(":violet[:material/search_insights:]   :violet[Insights]")
st.divider()
with st.container(border=True):

	# st.subheader("What are the most popular books on amazon?")
	st.header("Top 20 most popular book by rating are",divider=True)
	with open("md/insight.md") as ins:

		st.markdown(ins.read())

	
	st.dataframe(understand.rating.head(20),
		hide_index=True
		)

	st.header("Top 20 most popular book by most reviews are ",divider=True)
	with open("md/insight2.md") as ins2:

		st.markdown(ins2.read())

	st.dataframe(understand.reviews.head(20),
		hide_index=True
		)
	st.header("Top 10 most popular Author ",divider=True)
	with open("md/insight3.md") as ins3:

		st.markdown(ins3.read())

	st.dataframe(understand.author_counts.head(10)
		)
	col=[]
	col=st.columns(5,border=True)
	x,y=0,0
	# print(col)
	for i in col:
		if x>0:

			i.metric(understand.auth3.iloc[x,0],
				understand.auth3.iloc[x,1],
				int(understand.auth3.iloc[x,1]-understand.auth3.iloc[x-1,1]))
		else:
			i.metric(understand.auth3.iloc[x,0],understand.auth3.iloc[x,1],0)

		x+=1
		
	

	col=[]
	# dasd
	col=st.columns(5,border=True)
	for i in col:

		i.metric(understand.auth3.iloc[x,0],
			understand.auth3.iloc[x,1],
			int(understand.auth3.iloc[x,1]-understand.auth3.iloc[x-1,1]))
		x+=1


	st.header("How do ratings and reviews correlate with book popularity?",divider=True)
	with open("md/insight4.md") as ins4:

		st.markdown(ins4.read())

	st.subheader("Correlation calculation",divider=True)
	st.dataframe(understand.cor2.corr())
	
	st.subheader("Correlation scatter graph",divider=True)
	with st.container(border=True):

		st.scatter_chart(understand.cor2,
			x="Rating",
			y="Reviews",
			size=100,
			)


	st.subheader("Genre Analysis",divider=True)
	with open("md/insight5.md") as ins5:

		st.markdown(ins5.read())
	# st.dataframe(understand.genre)
	st.subheader("Genre count",divider=True)
	st.bar_chart(understand.genre,horizontal=True,height=250)

