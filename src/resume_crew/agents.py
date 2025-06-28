"""
AI Agents for Resume Optimization
"""

from crewai import Agent
from src.resume_crew.tools import JobAnalysisTools, ResumeAnalysisTools, CompanyResearchTools

class JobAnalyzer(Agent):
    """
    Agent responsible for analyzing job requirements and extracting key information.
    """
    
    def __init__(self):
        super().__init__(
            role="Job Requirements Analyst",
            goal="Extract and analyze job requirements, skills, and qualifications from job postings",
            backstory="""You are an expert HR analyst with 10+ years of experience in 
            job market analysis and recruitment. You specialize in understanding job 
            requirements and matching them with candidate profiles.""",
            verbose=True,
            allow_delegation=False
        )

class ResumeAnalyzer(Agent):
    """
    Agent responsible for analyzing resumes and suggesting optimizations.
    """
    
    def __init__(self):
        super().__init__(
            role="Resume Optimization Specialist",
            goal="Analyze resume match with job requirements and suggest specific improvements",
            backstory="""You are a certified resume writer and career coach with 
            expertise in ATS optimization. You have helped thousands of candidates 
            improve their resumes and land their dream jobs.""",
            verbose=True,
            allow_delegation=False
        )

class CompanyResearcher(Agent):
    """
    Agent responsible for researching companies and providing insights.
    """
    
    def __init__(self):
        super().__init__(
            role="Company Research Specialist",
            goal="Research companies and provide insights for interview preparation",
            backstory="""You are a business analyst and market researcher with 
            deep knowledge of various industries and companies. You help candidates 
            understand company culture, values, and interview preparation strategies.""",
            verbose=True,
            allow_delegation=False
        ) 