import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\hp\Netflix\netflix_titles.csv")
print(df.head())
print(df.shape)      # rows and columns
print(df.columns)    # column names
print(df.info())     # data types
print(df.isnull().sum())
df["director"].fillna("Unknown", inplace=True)
df["cast"].fillna("Unknown", inplace=True)
df["country"].fillna("Unknown", inplace=True)
df["rating"].fillna("Not Rated", inplace=True)
print(df["type"].value_counts())
sns.countplot(x="type", data=df)
plt.title("Movies vs TV Shows on Netflix")
plt.show()
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

df["year_added"].value_counts().sort_index().plot(kind="line")
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.show()
top_country = df["country"].value_counts().head(10)

top_country.plot(kind="bar")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()
rating_count = df["rating"].value_counts().head(10)

rating_count.plot(kind="bar")
plt.title("Most Common Ratings")
plt.show()
genre = df["listed_in"].str.split(",").explode()

genre.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres on Netflix")
plt.show()