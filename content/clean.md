### Drop Duplicate

The first thing we can do is check for and remove any duplicate rows in the dataset using the `drop_duplicates()` function.

```python
df.drop_duplicates(inplace=True)
```
By setting the inplace parameter to True, the changes are made directly to the original DataFrame.

### Renaming columns
Next, we can rename the columns of the DataFrame to make them more descriptive and easier to work with. We can use the `rename()` function to do this.
```python
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)
```
This code renames the "Name" column to "Title" and the "Year" column to "Publication Year". Again, by setting the `inplace` parameter to `True`, the changes are made directly to the original DataFrame.

### Converting Data Types 
Finally, we can convert the "Price" column to a float data type to make it easier to work with. We can use the `astype()` function to do this.
```python
df["Price"] = df["Price"].astype(float)
```
This code converts the "Price" column to a float data type. Note that we select the "Price" column of the DataFrame using the square bracket notation, and then apply the astype() function to it. The resulting values are then stored back in the "Price" column of the DataFrame.

After performing these cleaning operations, our DataFrame should be ready for analysis.