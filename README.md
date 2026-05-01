# 🎓 Hybrid Online Course Recommendation System

## 📌 Overview

This project is a **hybrid recommendation system** that suggests relevant online courses using a combination of:

* Content-based filtering
* Collaborative filtering
* Difficulty-level alignment
* Rating-based alternatives
* Budget-based alternatives

The application is deployed using **Streamlit** and allows users to explore trending courses and receive intelligent recommendations interactively.

---

## 🚀 Live Demo

Access the deployed application here:

👉 https://course-recommendation-system-ikkb2znjpn6mkdplu4vhu5.streamlit.app/
---

## ✨ Features

* Hybrid recommendation engine (content + collaborative filtering)
* Trending courses based on enrollment numbers
* Difficulty-level filtering
* Similar course recommendations
* Top-rated alternative suggestions
* Budget-friendly alternative suggestions
* Interactive Streamlit dashboard

---

## 🧠 Recommendation Strategies

### Similar Courses

Uses hybrid similarity scoring:

Hybrid Score = (Content Similarity + Collaborative Similarity) / 2

Returns courses most similar to the selected course.

---

### Top Rated Alternatives

Suggests highest-rated courses excluding the selected course.

---

### Budget Friendly Alternatives

Suggests lowest-price alternatives excluding the selected course.

---

## 📊 Model Evaluation

The recommendation system was evaluated using:

### Precision@5

Measures how many of the top 5 recommendations are relevant.

Result:

Precision@5 ≈ **0.058**

---

### Recall@5

Measures how many relevant courses were retrieved from all possible relevant courses.

Result:

Recall@5 ≈ **0.103**

---

These results validate that the hybrid recommendation approach produces meaningful similarity-based course suggestions.

---

## 🛠️ Technologies Used

* Python
* Pandas
* Streamlit
* Pickle
* Recommendation Systems (Hybrid Filtering)
* Cosine Similarity

---

## 📂 Project Structure

```
course-recommendation-system/
│
├── app.py
├── courses_df.pkl
├── content_similarity.pkl
├── course_similarity.pkl
├── course_recommender.ipynb
└── README.md
```

---

## ▶️ Run Locally

Install dependencies:

```
pip install streamlit pandas
```

Run the app:

```
streamlit run app.py
```

---

## 🔮 Future Improvements

* User-personalized recommendations
* Category-based filtering
* Model performance dashboard
* UI styling enhancements
* Recommendation explainability module

---

## 👩‍💻 Author

Developed by **Meghana**
