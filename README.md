# AI-Powered Resume Analyzer

A web application that analyzes resumes using AI to extract key information, match them to job descriptions, and provide improvement suggestions.

## Features

- **PDF Resume Parsing**: Extracts text from PDF resumes.
- **Information Extraction**: Uses AI to identify skills, experience, and education.
- **Job Matching**: Compares resume content with job descriptions for semantic matching.
- **Improvement Suggestions**: Provides personalized tips to enhance resumes.
- **Interactive UI**: Simple Streamlit-based interface for easy use.

## Technology Stack

- **Backend**: Python
- **AI Model**: Google Gemini API
- **PDF Parsing**: pdfplumber
- **Frontend**: Streamlit
- **Environment**: Conda (recommended)

## Setup Instructions

### Prerequisites

- Python 3.8+
- Conda (for environment management)
- Google Gemini API Key

### Installation

1. **Clone or download the project**:

   ```
   cd /path/to/cv-analyzer
   ```

2. **Create Conda Environment**:

   ```
   conda create -n cv-analyzer python=3.10
   conda activate cv-analyzer
   ```

3. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Set up API Key**:
   - Get your Google Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
   - Edit the `.env` file and replace `your_api_key_here` with your actual API key:
     ```
     GOOGLE_API_KEY=your_actual_api_key
     ```

### Running the Application

1. **Activate the environment**:

   ```
   conda activate cv-analyzer
   ```

2. **Run the Streamlit app**:

   ```
   streamlit run app.py
   ```

3. **Open your browser** to the URL shown (usually `http://localhost:8501`).

## Usage

1. **Upload Resume**: Use the sidebar to upload a PDF resume.
2. **Enter Job Description**: Paste the job description in the text area.
3. **View Results**: The app will display extracted information, match analysis, and suggestions.

## Project Structure

```
cv-analyzer/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (API key)
├── src/
│   ├── __init__.py
│   ├── pdf_parser.py      # PDF text extraction
│   ├── gemini_api.py      # Gemini API integration
│   └── analyzer.py        # Resume analysis logic
└── README.md              # This file
```

## Notes

- Ensure your API key is valid and has sufficient quota.
- The app processes PDFs locally and does not store any data.
- For production use, consider security measures like API key encryption.

## Future Enhancements

- Support for multiple file formats.
- User authentication.
- Resume template generation.
- Batch processing.
