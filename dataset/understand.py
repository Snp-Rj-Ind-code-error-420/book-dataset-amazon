import pandas as pd

# global df
df=pd.DataFrame()
df=pd.read_csv(r".\dataset\bestsellers with categories.csv")

df2=df.drop_duplicates()
df2.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"},inplace=True)
# df = df.astype(str)
df2["Price"] = df2["Price"].astype(float)

# cor=pd.DataFrame()
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

cor2['Rating']=(df2['Rating'] - df2['Rating'].min())/(df2['Rating'].max()-df2['Rating'].min())
# cor2['Rating']=df['Rating']
cor2['Reviews']=(df2['Reviews']-df2['Reviews'].min())/(df2['Reviews'].max()-df2['Reviews'].min())
cor2['Price']=(df2['Price']-df2['Price'].min())/(df2['Price'].max()-df2['Price'].min())
rating=df2.sort_values(by='Rating',ascending=False)
reviews=df2.sort_values(by='Reviews',ascending=False)