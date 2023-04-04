import pandas as pd
import streamlit as st

# Read the labeled dataset
df = pd.read_csv('IMDB_Movie_Clean_Label.csv')

# App title and description
st.title("190,000 Movie Recommender (1998-2023)")
st.write("Welcome to the Mood-based Movie Recommendation App! Please enter your current mood, preferred movie genre, and get personalized movie recommendations! *WIP Project*")

# Display tables
st.subheader("Mood Cluster by K-means")
st.write("""
| Cluster   | Mood                                                                                               |
| :-------: | :-------------------------------------------------------------------------------------------------: |
| Cluster 1 | Funny, Western                                                                                    |
| Cluster 2 | Motivating, Educational, Thrilling, Informative, Inspirational, Feel-good, Imaginative, Futuristic, Scary, Intense, Emotional, Exciting, Musical |
| Cluster 3 | Romantic, Mysterious                                                                               |
""")

st.subheader("Genres Cluster by K-Means")
st.write("""
| Cluster |                       Genres                             |
|---------|----------------------------------------------------------|
| 0       | Music, Drama, Romance, Adventure                          |
| 1       | Comedy, Fantasy, Animation, Crime, Action, Thriller       |
| 2       | Sport, Family                                             |
| 3       | Horror, Crime, Mystery                                    |
| 4       | Short, War, Musical, Western, Talk-Show, News, Adult, Sci-Fi |
""")

# User input
user_mood = st.text_input('Enter your current mood (e.g. happy, sad, romantic, action-packed or choose from mood table): ').lower()
user_genre = st.text_input('Enter your preferred movie genre (e.g. action, adventure, comedy, drama or choose from genre table): ').lower()

# Recommendations
if st.button("Get Recommendations"):
    selected_movies = df[(df['Mood'].str.lower().str.contains(user_mood)) & (df['Movie Genres'].str.lower().str.contains(user_genre))]
    selected_movies = selected_movies.sort_values('Number of Votes', ascending=False)
    num_recommendations = min(10, len(selected_movies))
    recommendations = selected_movies.head(num_recommendations)

    st.write(f"Based on your mood '{user_mood}' and preferred genre '{user_genre}', here are {num_recommendations} recommended movies:")
    
    if num_recommendations == 0:
        st.write("Sorry, no movies match your criteria.")
    else:
        for i, movie in enumerate(recommendations.itertuples()):
            st.write(f"{i+1}. {movie._1} ({movie._2}), {movie._5:.1f}/10 Rating")

st.write("Next Progress : Better UI, Better Algorithms, Implementing Deep Learning for recommendation, Add more features")
st.markdown("<p style='text-align: right; font-style: italic;'>Created by: <a href='https://rahmatuelsamuel.com'>Rahmatuel Samuel</a></p>", unsafe_allow_html=True)