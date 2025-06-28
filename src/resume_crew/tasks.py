"""
Tasks for Resume Optimization Crew
"""

from crewai import Task

def create_job_analysis_task(agent, job_url, company_name):
    """
    Create a task for job analysis.
    """
    return Task(
        description=f"""
        Analyze the job posting at {job_url} for {company_name} and extract:
        
        1. Job title and level
        2. Required skills (technical and soft skills)
        3. Required qualifications and experience
        4. Preferred qualifications
        5. Key responsibilities
        6. Company culture indicators
        7. Salary range (if mentioned)
        8. Benefits and perks
        
        Provide a comprehensive analysis that can be used for resume optimization.
        """,
        agent=agent,
        expected_output="""
        A detailed JSON analysis containing:
        - job_title: string
        - required_skills: list of strings
        - preferred_skills: list of strings
        - required_experience: string
        - key_responsibilities: list of strings
        - company_culture: string
        - salary_range: string (if available)
        - benefits: list of strings
        """
    )

def create_resume_optimization_task(agent, job_url, company_name, resume_path):
    """
    Create a task for resume optimization.
    """
    return Task(
        description=f"""
        Based on the job analysis for {company_name}, analyze the candidate's resume from {resume_path} and:
        
        1. Calculate a match score (0-100) for:
           - Technical skills match
           - Experience relevance
           - Education requirements
           - Overall fit
        
        2. Identify gaps between resume and job requirements
        
        3. Provide specific optimization suggestions:
           - Keywords to add
           - Experience descriptions to improve
           - Skills to highlight
           - Format improvements for ATS
        
        4. Suggest specific action items to improve the resume
        
        Use the job analysis results from the previous task.
        """,
        agent=agent,
        expected_output="""
        A comprehensive optimization report containing:
        - match_scores: dict with technical, experience, education, overall scores
        - skill_gaps: list of missing skills
        - optimization_suggestions: list of specific improvements
        - action_items: prioritized list of changes to make
        - ats_optimization: specific ATS improvements
        """
    )

def create_company_research_task(agent, company_name):
    """
    Create a task for company research.
    """
    return Task(
        description=f"""
        Research {company_name} and provide comprehensive insights for interview preparation:
        
        1. Company overview and mission
        2. Company culture and values
        3. Recent news and developments
        4. Interview process and tips
        5. Common interview questions
        6. Company challenges and opportunities
        7. Industry position and competitors
        8. Growth and career opportunities
        
        Focus on information that would be useful for interview preparation.
        """,
        agent=agent,
        expected_output="""
        A detailed company research report containing:
        - company_overview: string
        - culture_values: list of strings
        - recent_news: list of strings
        - interview_tips: list of strings
        - common_questions: list of strings
        - challenges_opportunities: list of strings
        - industry_position: string
        - career_growth: string
        """
    ) 