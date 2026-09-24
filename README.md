# Movie Recommendation System

A learning project that recommends ten similar movies using TF-IDF and cosine similarity, with a Streamlit interface and TMDB posters.

Built by following [Sujoy Dutta’s tutorial](https://www.youtube.com/watch?v=i-B_I2DGIAI) and [original repository](https://github.com/dutta-sujoy/Movie-Recommendation-System). The initial implementation follows the tutorial; it is not an original algorithm. See the original repository for background and general installation instructions.

## Running this version

1. In a Python 3.11 environment, run `python -m pip install -r requirements.txt`.
2. Place both CSV files from the [TMDB 5000 dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) in the project folder. Run `movie_recommendation_system.ipynb` in that environment to generate `movie_data.pkl`.
3. Create `.streamlit/secrets.toml` with your own key:

```toml
TMDB_API_KEY = "YOUR_TMDB_API_KEY"
```

4. From the project folder, run `python -m streamlit run app.py`.

The secrets file, local environment, and generated model are excluded from Git. Recommendation quality has not yet been formally evaluated.
