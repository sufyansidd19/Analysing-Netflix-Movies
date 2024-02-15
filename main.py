# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt


#part1
netflix_df = pd.read_csv('netflix_data.csv')

#part2
netflix_subset = netflix_df[netflix_df["type"] == 'Movie']  

#part 3
netflix_movies = netflix_subset[['title', 'country', 'genre', 'release_year', 'duration']]

#part 4
short_movies=netflix_movies[netflix_movies["duration"]<60]

#part 5
colors=[]

for i,j in netflix_movies.iterrows():
    if j['genre']=="Children":
        colors.append('Red')
    elif j['genre']=="Documentaries": 
        colors.append('Green')
    elif j['genre']=="Stand-Up":
        colors.append('Blue')
    else:
        colors.append('Yellow')
        
#part 6
fig=plt.figure(figsize=(12,8))
plt.scatter(netflix_movies['release_year'],netflix_movies['duration'],c=colors)

# Create a title and axis labels
plt.title("Movie Duration by Year of Release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()