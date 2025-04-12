import streamlit as st
import pandas as pd
st.set_page_config(page_title="EDA", 
	page_icon="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\" width=\"24px\" fill=\"#EA33F7\"><path d=\"M70-424q-13-9-15.5-24.5T60-478l122-196q22-35 62.5-37.5T311-683l49 57 95-154q23-38 66.5-38.5T589-782l51 76 112-178q9-15 26.5-18.5T810-895q13 9 15.5 24.5T820-841L708-663q-23 37-66.5 37T574-662l-51-76-95 154q-21 35-61.5 38T300-574l-50-58-122 197q-9 15-26.5 18.5T70-424Zm510 184q42 0 71-29t29-71q0-42-29-71t-71-29q-42 0-71 29t-29 71q0 42 29 71t71 29Zm0 80q-75 0-127.5-52.5T400-340q0-75 52.5-127.5T580-520q75 0 127.5 52.5T760-340q0 26-7 50.5T732-244l80 80q11 11 11 28t-11 28q-11 11-28 11t-28-11l-80-80q-21 14-45.5 21t-50.5 7Z\"/></svg>",
	layout="centered",
	initial_sidebar_state="auto",  
	menu_items=None)
st.title(":violet[:material/query_stats:]   :violet[Exploratory Data Analysis on the dataset]")
st.divider()

st.header("Data Cleaning")
st.text("The dataset will be cleaned to remove any missing or duplicate values.")

df=pd.read_csv(r".\dataset\bestsellers with categories.csv")
with st.container(border=True):
	st.subheader("1.Explore the Data")

	st.text("Once we've loaded the spreadsheet data, we can explore it to get a better understanding of what we're working with. We can use various functions provided by pandas to do this")
st.divider()
st.code("""
	# Get the first 5 rows of the spreadsheet
print(df.head())""")
st.dataframe(df.head())

st.divider()

st.code("""
# Get the shape of the spreadsheet
print(df.shape)
""")
st.dataframe(df.shape,
	column_config={"value":"rows x columns"}
	)

st.divider()

st.code("""
# Get the column names of the spreadsheet
print(df.columns)
""")
st.dataframe(df.columns,
	column_config={"0":"column names"}
	)

st.divider()

st.code("""
# Get summary statistics for each column
print(df.describe())
""")
st.dataframe(df.describe())

st.divider()

st.code(""" 
#Get the number of unique element present in each column 
print(df.nunique())
""")
st.dataframe(df.nunique(),
	column_config={"0":"count of unique elements"})

st.divider()

st.code("""
#Get the data type of each column 
print(df.dtypes)
""")
st.dataframe(df.dtypes,
	column_config={"0":"data types"}
	)
# st.dataframe(df.duplicated().sum())
st.divider()

with st.container(border=True):
	st.markdown("""
# Data Quality Enhancement Steps

### Based on our analysis, we have identified two key steps to enhance data quality:

1. __Data Type Conversion:__ We will convert the data types of relevant columns to ensure consistency and accuracy.
2. __Duplicate Detection and Removal:__ We will check for duplicate records and remove any redundant data to prevent bias and ensure the reliability of our analysis.

By taking these steps, we can ensure that our data is accurate, consistent, and reliable, laying the foundation for meaningful insights and informed decision-making.""")

st.divider()

with st.container(border=True):
	st.subheader("2.Cleaning the data")

	st.text("Once we've explored the data, we may need to clean it before running an analysis.")
	with open(r"./content/clean.md",'r') as clr:

		st.markdown(clr.read())	

st.divider()

df.drop_duplicates(inplace=True)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
df["Price"] = df["Price"].astype(float)
st.subheader("Renamed column")
st.dataframe(df.head(),hide_index=True)
st.subheader("Converted datatype")
st.dataframe(df.dtypes,column_config={"0":"data types"})