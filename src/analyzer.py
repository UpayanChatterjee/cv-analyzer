from .gemini_api import call_gemini

def extract_resume_info(resume_text):
    """
    Extract key information from resume text using Gemini.

    Args:
        resume_text (str): The text extracted from the resume.

    Returns:
        dict: Dictionary containing skills, experience, education.
    """
    prompt = f"""
    Extract the following information from the resume text below:
    - Skills: List of technical and soft skills mentioned.
    - Experience: Summary of work experience, including job titles, companies, and durations.
    - Education: Degrees, institutions, and graduation years.

    Resume Text:
    {resume_text}

    Provide the output in JSON format with keys: 'skills', 'experience', 'education'.
    """
    response = call_gemini(prompt)
    # For simplicity, return the response as is. In production, parse JSON.
    return response

def match_resume_to_job(resume_text, job_description):
    """
    Match resume to job description and provide a score and analysis.

    Args:
        resume_text (str): Resume text.
        job_description (str): Job description text.

    Returns:
        str: Match analysis and score.
    """
    prompt = f"""
    Compare the resume below with the job description and provide:
    - A match score out of 100.
    - Key matching skills and experiences.
    - Gaps or missing qualifications.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Provide a concise analysis.
    """
    response = call_gemini(prompt)
    return response

def generate_resume_suggestions(resume_text):
    """
    Generate improvement suggestions for the resume.

    Args:
        resume_text (str): Resume text.

    Returns:
        str: Suggestions for improvement.
    """
    prompt = f"""
    Analyze the resume below and provide personalized suggestions to improve it:
    - Content enhancements.
    - Formatting tips.
    - Keyword optimization for ATS.

    Resume:
    {resume_text}

    Provide actionable suggestions.
    """
    response = call_gemini(prompt)
    return response