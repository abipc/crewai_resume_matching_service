# Resume Optimization with CrewAI

Resume Optimization System Architecture

An AI-powered tool that optimizes your resume for specific job applications using multiple AI agents. Built with CrewAI.

## What It Does

1. **Job Analysis**: Analyzes job requirements, skills, and qualifications
2. **Resume Scoring**: Calculates match scores for technical skills, experience, and qualifications
3. **Optimization**: Suggests specific improvements to increase your match score
4. **Company Research**: Provides company insights for interview preparation

## Installation

1. Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/resume-optimization-crew.git
cd resume-optimization-crew
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Environment Setup

1. Copy `env.example` to `.env`:
```bash
cp env.example .env
```

2. Add your API keys to `.env`:
   * Required:
     * `OPENAI_API_KEY`: OpenAI API key
     * `SERPER_API_KEY`: Serper API key for web search
   * Optional:
     * See `env.example` for additional optional APIs

## Quick Start

1. Save your resume in the `knowledge/` directory:
   * **Supported formats**: PDF (.pdf)
   * **Sample resume**: `knowledge/<CV_Name>.pdf` is provided as an example
   * **PDF support**: The system can parse PDF resumes using PyPDF2

2. Configure the resume path in `main.py`:
   ```python
   # For text resume
   resume_path = "knowledge/CV_Mohan.txt"
   
   # For PDF resume
   resume_path = "knowledge/CV_Mohan.pdf"
   ```

3. Fill in the input data in `main.py`:
   * `job_url`: URL of the job posting (e.g., 'https://www.mckinsey.com/careers/search-jobs/jobs/associate-15178')
   * `company_name`: Name of the company (e.g., 'Mckinsey & Co.')

4. Run the optimization crew:
```bash
python main.py
```

## Output Files

The tool generates three JSON files in the `output` directory:

* `job_analysis.json`: Detailed job requirements and match scoring
* `resume_optimization.json`: Specific suggestions to improve your resume
* `company_research.json`: Company insights for interview prep

## Architecture

The system uses three specialized AI agents:

1. **Job Analyzer**: Extracts and analyzes job requirements
2. **Resume Analyzer**: Scores resume match and suggests improvements
3. **Company Researcher**: Gathers company information for interviews

## Resume Format Support

The system supports multiple resume formats:

- **PDF (.pdf)**: Full PDF parsing with PyPDF2

The resume parser automatically detects the file format and processes accordingly.

## Requirements

* Python `>= 3.10` and `< 3.13`
* Resume file (PDF)
* Job posting URL
* Company name

## Support

* [CrewAI Documentation](https://docs.crewai.com/)
* [Community Forum](https://community.crewai.com/)
* [Chat with our docs](https://docs.crewai.com/)

## About

Use CrewAI and OpenAI to build Resume Matching 
