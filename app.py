import streamlit as st
import pandas as pd
import requests
import pickle

with open('movie_data.pkl', 'rb') as file: 
    movies, cosine_sim= pickle.load(file)
    
def get_recommendation(title, cosine_sim=cosine_sim):
    idx = movies[movies['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

def fetch_poster(movie_id):
    api_key= st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"

    response = requests.get(url)
    data = response.json()

    poster_path = data["poster_path"]

    return f"https://image.tmdb.org/t/p/w500{poster_path}"
    
st.title('Movie Recommendation System')

selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendation = get_recommendation(selected_movie)
    st.write('Top 10 recommended movies:')
    
    for i in range( 0, 10, 5):
        cols = st.columns(5)
        for col, j in zip(cols, range(i,i+5)):
            if j < len(recommendation):
                movie_title = recommendation.iloc[j]['title']
                movie_id = recommendation.iloc[j]['movie_id']
                poster_url = fetch_poster (movie_id)
                with col :
                    st.image(poster_url, width = 130)
                    st.write(movie_title)
                    
                    