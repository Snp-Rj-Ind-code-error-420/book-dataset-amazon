import streamlit as st
import pandas as pd
st.set_page_config(page_title="EDA", 
	page_icon="<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\" width=\"24px\" fill=\"#EA33F7\"><path d=\"M480-80q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480v320q0 33-23.5 56.5T800-80H480Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 23 3 45t9 43l122-122q11-11 26.5-11.5T348-516l104 87 131-131h-23q-17 0-28.5-11.5T520-600q0-17 11.5-28.5T560-640h120q17 0 28.5 11.5T720-600v120q0 17-11.5 28.5T680-440q-17 0-28.5-11.5T640-480v-23L482-346q-11 11-26.5 12T428-344l-103-88-118 118q42 69 113.5 111.5T480-160Zm300 20q17 0 28.5-11.5T820-180q0-17-11.5-28.5T780-220q-17 0-28.5 11.5T740-180q0 17 11.5 28.5T780-140ZM455-480Z\"/></svg>",
	layout="centered",
	initial_sidebar_state="auto",  
	menu_items=None)
st.title(":violet[:material/data_exploration:]   :violet[Exploratory Data Analysis on the dataset]")
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
	with open(r".\content\eda\clean.md",'r') as clr:

		st.markdown(clr.read())	

st.divider()

df.drop_duplicates(inplace=True
	)
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
# df = df.astype(str)
df["Price"] = df["Price"].astype(float)

st.subheader("Renamed column")
st.dataframe(df.head(),hide_index=True)
st.subheader("Converted datatype")
st.dataframe(df.dtypes,column_config={"0":"data types"})
cor=pd.DataFrame()
cor2=pd.DataFrame()
# standardization
# """
# 1.
# Code

# X_scaled = (X - mean(X)) / std(X)
# Where:
# X is the original value.
# mean(X) is the mean of the feature.
# std(X) is the standard deviation of the feature.
# X_scaled is the scaled value.
# """
# cor['Rating']=(df['Rating'] - df['Rating'].mean())/df['Rating'].std()
# cor['Reviews']=((df['Reviews']-df['Reviews'].mean())/df['Reviews'].std())
# cor['Price']=(df['Price']-df['Price'].mean())/df['Price'].std()
# st.dataframe(cor.corr())
# st.scatter_chart(cor,
# 	x="Rating",
# 	y="Reviews",
# 	size="Price"
# 	)

# 1. Min-Max Scaling (Normalization)
# This method scales data to a specific range, typically between 0 and 1. 
# Code

# X_scaled = (X - X_min) / (X_max - X_min)
# Where:
# X is the original value.
# X_min is the minimum value of the feature.
# X_max is the maximum value of the feature.
# X_scaled is the scaled value.

cor2['Rating']=(df['Rating'] - df['Rating'].min())/(df['Rating'].max()-df['Rating'].min())
# cor2['Rating']=df['Rating']
cor2['Reviews']=(df['Reviews']-df['Reviews'].min())/(df['Reviews'].max()-df['Reviews'].min())
cor2['Price']=(df['Price']-df['Price'].min())/(df['Price'].max()-df['Price'].min())
st.dataframe(cor2.corr())
st.scatter_chart(cor2,
	x="Rating",
	y="Reviews"
	)