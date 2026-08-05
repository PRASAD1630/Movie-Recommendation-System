import pickle
import requests
import pandas as pd

# -----------------------------
# Load Data
# -----------------------------
movies = pickle.load(open("models/movie_dict.pkl", "rb"))
similarity = pickle.load(open("models/similarity.pkl", "rb"))

# If the notebook saved a dictionary instead of a DataFrame
if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

# -----------------------------
# TMDB API
# -----------------------------
API_KEY = "7d179c6424c69c47cc16be5496541e6e"

def fetch_poster(movie_id):
    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        f"?api_key={API_KEY}&language=en-US"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Poster"

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

    except Exception:
        pass

    return "https://via.placeholder.com/500x750?text=No+Poster"


def recommend(movie_name):
    if movie_name not in movies["title"].values:
        return [], []

    movie_index = movies[movies["title"] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for item in movie_list:
        idx = item[0]

        recommended_movies.append(movies.iloc[idx]["title"])
        recommended_posters.append(
            fetch_poster(movies.iloc[idx]["movie_id"])
        )

    return recommended_movies, recommended_posters