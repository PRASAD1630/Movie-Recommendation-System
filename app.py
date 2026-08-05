import streamlit as st
import pickle
import pandas as pd
from recommender import recommend

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.main {
    background-color: #0E1117;
}

.title {
    font-size:55px;
    color:#E50914;
    text-align:center;
    font-weight:bold;
    margin-top:10px;
}

.subtitle{
    font-size:22px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.movie-name{
    text-align:center;
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    background:#E50914;
    color:white;
    border-radius:10px;
    height:50px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#ff3030;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #

movies = pickle.load(open("models/movie_dict.pkl","rb"))

if isinstance(movies, dict):
    movies = pd.DataFrame(movies)

movie_list = movies["title"].values

# ---------------- TITLE ---------------- #

st.markdown(
    "<div class='title'>🎬 Movie Recommendation System</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Discover Movies Similar To Your Favourite Movie</div>",
    unsafe_allow_html=True
)

st.markdown("---")

selected_movie = st.selectbox(
    "🎥 Select Movie",
    movie_list
)

recommend_button = st.button("Recommend Movies")
# ---------------- RECOMMENDATION ---------------- #

if recommend_button:

    with st.spinner("Finding similar movies..."):

        try:

            movie_names, movie_posters = recommend(selected_movie)

            st.markdown("## 🍿 Recommended Movies")

            col1, col2, col3, col4, col5 = st.columns(5)

            cols = [col1, col2, col3, col4, col5]

            for i in range(5):

                with cols[i]:

                    if movie_posters[i]:
                        st.image(movie_posters[i], use_container_width=True)

                    st.markdown(
                        f"<div class='movie-name'>{movie_names[i]}</div>",
                        unsafe_allow_html=True
                    )

        except Exception as e:

            st.error("Something went wrong while generating recommendations.")
            st.exception(e)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎬 About")

st.sidebar.info(
    """
This Movie Recommendation System uses **Content-Based Filtering**.

### Technologies Used
- Python
- Pandas
- Scikit-Learn
- Streamlit
- TMDB API

### ML Algorithm
- CountVectorizer
- Cosine Similarity
"""
)

st.sidebar.markdown("---")
st.sidebar.success("Developed by Bhukya Prasad 🚀")

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;font-size:16px'>
Made with ❤️ using Python, Streamlit & Machine Learning
</div>
""",
unsafe_allow_html=True
)