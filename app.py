import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c34d6d363a28c52f11171152430286b1&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def fetch_ratings(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c34d6d363a28c52f11171152430286b1&language=en-US'.format(movie_id))
    data = response.json()
    return data['vote_average']




def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_ratings = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_ratings.append(fetch_ratings(movie_id))

    return recommended_movies,recommended_movies_posters,recommended_movies_ratings

movies_list_dict  = pickle.load(open('movie_list_dict.pkl','rb'))
movies = pd.DataFrame(movies_list_dict)


similarity = pickle.load(open('similarity.pkl','rb')) 

st.title('Movie Recommender System')


selected_movie = st.selectbox('Search for movies',movies['title'].values)


if st.button('Recommend'):
    names,poster,ratings = recommend(selected_movie)

    col1, col2, col3,col4,col5 = st.beta_columns(5)
    with col1:
        st.subheader(names[0])
        st.image(poster[0])
        st.text("Ratings:")
        st.text(ratings[0])
    with col2:
        st.subheader(names[1])
        st.image(poster[1])
        st.text("Ratings:")
        st.text(ratings[1])
    with col3:
        st.subheader(names[2])
        st.image(poster[2])
        st.text("Ratings:")
        st.text(ratings[2])
    with col4:
        st.subheader(names[3])
        st.image(poster[3])
        st.text("Ratings:")
        st.text(ratings[3])
    with col5:
        st.subheader(names[4])
        st.image(poster[4])
        st.text("Ratings:")
        st.text(ratings[4])


