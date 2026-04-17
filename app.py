import streamlit as st
import pickle
import pandas as pd


# Load saved files
df = pickle.load(open("courses_df.pkl", "rb"))
content_similarity_df = pickle.load(open("content_similarity.pkl", "rb"))
course_similarity_df = pickle.load(open("course_similarity.pkl", "rb"))


# Page title
st.title("Online Course Recommendation System")


# Trending Courses section
st.subheader("Trending Courses")

trending_courses = df.sort_values(
    by="enrollment_numbers",
    ascending=False
).drop_duplicates("course_name")

st.dataframe(
    trending_courses[
        ["course_name", "difficulty_level", "rating"]
    ].head(5)
)


# Filter by difficulty level
st.subheader("Filter Courses by Difficulty")

difficulty_selected = st.selectbox(
    "Select Difficulty Level",
    df["difficulty_level"].unique()
)

filtered_courses = df[
    df["difficulty_level"] == difficulty_selected
]

filtered_courses = filtered_courses.drop_duplicates("course_name")

st.dataframe(
    filtered_courses[
        ["course_name", "rating", "course_price"]
    ].head(5)
)


# Recommend Similar Courses section
st.subheader("Recommend Similar Courses")

selected_course = st.selectbox(
    "Select a course",
    df["course_name"].unique()
)


# Show course details
course_info = df[
    df["course_name"] == selected_course
].iloc[0]

st.subheader("Course Details")

st.write(f"Course Name: {course_info['course_name']}")
st.write(f"Difficulty: {course_info['difficulty_level']}")
st.write(f"Rating: {course_info['rating']}")
st.write(f"Price: {course_info['course_price']}")


# Strategy selector
recommendation_type = st.radio(
    "Choose recommendation strategy",
    [
        "Similar Courses",
        "Top Rated Alternatives",
        "Budget Friendly Alternatives"
    ]
)


if st.button("Recommend Courses"):

    # SIMILAR COURSES
    if recommendation_type == "Similar Courses":

        item_similar = course_similarity_df[selected_course]
        content_similar = content_similarity_df[selected_course]

        hybrid_scores = (item_similar + content_similar) / 2
        hybrid_scores = hybrid_scores.drop(selected_course)

        recommendations = hybrid_scores.sort_values(
            ascending=False
        ).head(5)

        selected_difficulty = course_info["difficulty_level"]

        recommended_courses = df[
            (df["course_name"].isin(recommendations.index)) &
            (df["difficulty_level"] == selected_difficulty)
        ].copy()

        if recommended_courses.empty:
            recommended_courses = df[
                df["course_name"].isin(recommendations.index)
            ].copy()

        recommended_courses["similarity_score"] = \
            recommended_courses["course_name"].map(recommendations)


    # TOP RATED
    elif recommendation_type == "Top Rated Alternatives":

        recommended_courses = df.sort_values(
            "rating",
            ascending=False
        )

        recommended_courses = recommended_courses[
            recommended_courses["course_name"] != selected_course
        ].head(5)


    # BUDGET FRIENDLY
    elif recommendation_type == "Budget Friendly Alternatives":

        recommended_courses = df.sort_values(
            "course_price",
            ascending=True
        )

        recommended_courses = recommended_courses[
            recommended_courses["course_name"] != selected_course
        ].head(5)


    # DISPLAY RESULTS
    st.write("Top Recommended Courses:")

    if recommendation_type == "Similar Courses":

        st.dataframe(
            recommended_courses[
                ["course_name",
                 "difficulty_level",
                 "rating",
                 "course_price",
                 "similarity_score"]
            ]
        )

    else:

        st.dataframe(
            recommended_courses[
                ["course_name",
                 "difficulty_level",
                 "rating",
                 "course_price"]
            ]
        )