import streamlit as st
import tempfile
import os
from src.pdf_parser import extract_text_from_pdf
from src.analyzer import extract_resume_info, match_resume_to_job, generate_resume_suggestions

st.title("AI-Powered Resume Analyzer")

st.sidebar.header("Upload Resume")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

st.sidebar.header("Job Description")
job_desc = st.sidebar.text_area("Paste the job description here", height=200)

if uploaded_file is not None:
    # Save uploaded file to temp
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Extract text
    resume_text = extract_text_from_pdf(tmp_path)

    st.header("Resume Analysis")

    # Extract info
    info = extract_resume_info(resume_text)
    st.subheader("Extracted Information")
    st.write(info)

    if job_desc:
        # Match to job
        match = match_resume_to_job(resume_text, job_desc)
        st.subheader("Job Match Analysis")
        st.write(match)

    # Suggestions
    suggestions = generate_resume_suggestions(resume_text)
    st.subheader("Improvement Suggestions")
    st.write(suggestions)

    # Clean up temp file
    os.unlink(tmp_path)
else:
    st.write("Please upload a resume PDF to get started.")