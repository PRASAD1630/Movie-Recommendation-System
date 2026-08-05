import pickle
import pandas as pd

movies_dict = pickle.load(open("models/movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("models/similarity.pkl", "rb"))

print(movies.head())
print(similarity.shape)