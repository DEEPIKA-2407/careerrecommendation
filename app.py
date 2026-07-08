import streamlit as st
import pickle


# Load trained model
with open("resume_job_model.pkl", "rb") as file:
    model = pickle.load(file)


# Page configuration
st.set_page_config(
    page_title="Smart Career Recommendation System",
    page_icon="💼"
)


# Title
st.title("💼 Smart Career Recommendation System")

st.write(
    "Enter your resume details and get the recommended job role."
)


# Resume input
resume_text = st.text_area(
    "Paste Your Resume Text Here",
    height=250
)


# Prediction button
if st.button("Recommend Job Role"):

    if resume_text.strip() == "":
        st.warning("Please enter resume text")

    else:

        prediction = model.predict(
            [resume_text]
        )

        st.success(
            f"Recommended Job Role: {prediction[0]}"
        )
        
