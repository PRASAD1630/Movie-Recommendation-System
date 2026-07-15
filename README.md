# 🎬 Movie Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

A **Content-Based Movie Recommendation System** built using **Machine Learning**, **Natural Language Processing (NLP)**, **Cosine Similarity**, and **Streamlit**. The application recommends movies similar to a user's favorite movie by analyzing movie metadata such as genres, cast, crew, keywords, and overview.

</div>

---

# 📌 Overview

Finding the perfect movie to watch can be challenging with thousands of options available. This project addresses that problem by building a **Content-Based Recommendation Engine** that suggests similar movies based on their content rather than user ratings.

The recommendation model analyzes multiple movie attributes and computes similarity using **Count Vectorization** and **Cosine Similarity**.

---

# 🚀 Features

- 🎬 Content-Based Movie Recommendation
- 🔍 Search and Select Any Movie
- 🖼️ Fetch Movie Posters using TMDB API
- ⚡ Fast Recommendation Generation
- 🎨 Interactive Streamlit User Interface
- 📊 Machine Learning Based Similarity Search
- 📱 Responsive Design
- 🧠 NLP-based Feature Engineering

---

# 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- CountVectorizer
- Cosine Similarity

### Data Processing
- Pandas
- NumPy

### Natural Language Processing
- Porter Stemmer
- Text Preprocessing

### Frontend
- Streamlit

### API
- TMDB API

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/
│   ├── movie_dict.pkl
│   └── similarity.pkl
│
├── notebooks/
│   └── Movie_Recommendation.ipynb
│
├── utils/
│   ├── helper.py
│   └── fetch_poster.py
│
└── assets/
    ├── logo.png
    └── screenshots/
```

---

# 📊 Dataset

The project uses the **TMDB 5000 Movie Dataset**.

The dataset contains information such as:

- Movie Title
- Genres
- Overview
- Cast
- Crew
- Keywords
- Popularity
- Ratings

---

# ⚙️ Machine Learning Workflow

```text
Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Text Vectorization
      │
      ▼
CountVectorizer
      │
      ▼
Cosine Similarity
      │
      ▼
Recommendation Engine
      │
      ▼
Streamlit Web Application
```

---

# 🧠 Recommendation Algorithm

The recommendation engine follows a **Content-Based Filtering** approach.

It combines:

- Movie Overview
- Genres
- Keywords
- Top Cast
- Director

into a single feature called **Tags**.

The text is cleaned, stemmed, vectorized using **CountVectorizer**, and finally compared using **Cosine Similarity**.

Movies with the highest similarity score are recommended.

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/PRASAD1630/Movie-Recommendation-System.git
```

Go inside the folder

```bash
cd Movie-Recommendation-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the preprocessing notebook

```text
notebooks/Movie_Recommendation.ipynb
```

This will generate

```text
models/movie_dict.pkl
models/similarity.pkl
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

## Home Page

<img src="assets/screenshots/home.png" width="100%">

---

## Recommendation Results

<img src="assets/screenshots/result.png" width="100%">

---

# 📈 Future Improvements

- 🎥 Movie Trailer Integration
- ⭐ IMDb Rating Display
- ❤️ Favorite Movies
- 🔥 Trending Movies
- 🎭 Genre Filters
- 🌙 Dark / Light Mode
- 🤖 AI Chatbot for Movie Suggestions
- ☁️ Streamlit Cloud Deployment

---

# 📚 Learning Outcomes

This project demonstrates:

- Machine Learning
- Recommendation Systems
- Natural Language Processing
- Feature Engineering
- Data Preprocessing
- Streamlit Development
- REST API Integration
- Git & GitHub

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Bhukya Prasad**

- 🎓 B.E. Artificial Intelligence & Machine Learning
- 🏫 Chaitanya Bharathi Institute of Technology (CBIT)
- 💼 Aspiring AI/ML Engineer
- 🌐 GitHub: https://github.com/PRASAD1630

---

# ⭐ Support

If you found this project helpful,

⭐ **Star the repository**

and consider following my GitHub profile for more AI & Machine Learning projects.
