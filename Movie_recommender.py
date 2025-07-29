import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
movies = pd.read_csv('movies.csv')  # Path to movies dataset

# Create a CountVectorizer to convert genres into a matrix
vectorizer = CountVectorizer(stop_words='english')

# Fit and transform the genres column
genre_matrix = vectorizer.fit_transform(movies['genres'])

# Calculate similarity matrix
genre_similarity = cosine_similarity(genre_matrix, genre_matrix)

def get_recommendations(genre_input, top_n=5):
    try:
        genre_idx = movies[movies['genres'].str.contains(genre_input, case=False)].index
        if genre_idx.empty:
            return "No movies found for this genre."
        else:
            # Calculate similarity score for the given genre
            sim_scores = list(enumerate(genre_similarity[genre_idx[0]]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get top N recommendations
            top_movies = [movies['title'][i[0]] for i in sim_scores[1:top_n + 1]]
            return top_movies
    except Exception as e:
        return f"Error: {str(e)}"
        
