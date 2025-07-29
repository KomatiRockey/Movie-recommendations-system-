# app.py
import streamlit as st
from movie_recommender import get_recommendations

# Title of the web app
st.title("Movie Genre-Based Recommender")

# User input for genre
genre_input = st.text_input("Enter a Genre (e.g., Comedy, Horror, Action)")

# Display recommendations
if genre_input:
    recommendations = get_recommendations(genre_input)
    st.write(f"Top 5 {genre_input} Movies:")
    for movie in recommendations:
        st.write(movie)

# This section ensures the app binds to the correct address when running in a production environment (like Render)
if __name__ == "__main__":
    st.run(host="0.0.0.0", port=8000)
    
