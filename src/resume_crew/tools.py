"""
Tools for Resume Optimization Agents
"""

import requests
from bs4 import BeautifulSoup
import json
from pathlib import Path
from typing import Dict, List, Any
import PyPDF2
import io

class JobAnalysisTools:
    """Tools for job analysis agent."""
    
    @staticmethod
    def extract_job_details(job_url: str) -> Dict[str, Any]:
        """
        Extract job details from a job posting URL.
        """
        try:
            response = requests.get(job_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract text content
            text_content = soup.get_text()
            
            return {
                "url": job_url,
                "content": text_content,
                "status": "success"
            }
        except Exception as e:
            return {
                "url": job_url,
                "error": str(e),
                "status": "error"
            }
    
    @staticmethod
    def analyze_requirements(job_content: str) -> Dict[str, Any]:
        """
        Analyze job requirements from extracted content.
        """
        # This would typically use NLP/LLM to extract requirements
        # For now, return a structured format
        return {
            "skills": [],
            "experience": "",
            "education": "",
            "responsibilities": [],
            "analysis": "Job requirements analysis completed"
        }

class ResumeAnalysisTools:
    """Tools for resume analysis agent."""
    
    @staticmethod
    def analyze_resume(resume_path: str = "knowledge/CV_Mohan.txt") -> Dict[str, Any]:
        """
        Analyze resume content from PDF or text file.
        Supports both .pdf and .txt files.
        """
        try:
            file_path = Path(resume_path)
            
            if not file_path.exists():
                return {
                    "resume_path": resume_path,
                    "error": f"File not found: {resume_path}",
                    "status": "error"
                }
            
            # Handle PDF files
            if file_path.suffix.lower() == '.pdf':
                return ResumeAnalysisTools._parse_pdf_resume(file_path)
            
            # Handle text files
            elif file_path.suffix.lower() in ['.txt', '.md']:
                return ResumeAnalysisTools._parse_text_resume(file_path)
            
            else:
                return {
                    "resume_path": resume_path,
                    "error": f"Unsupported file format: {file_path.suffix}",
                    "status": "error"
                }
                
        except Exception as e:
            return {
                "resume_path": resume_path,
                "error": str(e),
                "status": "error"
            }
    
    @staticmethod
    def _parse_pdf_resume(file_path: Path) -> Dict[str, Any]:
        """
        Parse PDF resume file.
        """
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text_content = ""
                
                for page in pdf_reader.pages:
                    text_content += page.extract_text()
                
                return {
                    "resume_path": str(file_path),
                    "content": text_content,
                    "file_type": "pdf",
                    "pages": len(pdf_reader.pages),
                    "status": "success"
                }
        except Exception as e:
            return {
                "resume_path": str(file_path),
                "error": f"PDF parsing error: {str(e)}",
                "status": "error"
            }
    
    @staticmethod
    def _parse_text_resume(file_path: Path) -> Dict[str, Any]:
        """
        Parse text resume file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
                
                return {
                    "resume_path": str(file_path),
                    "content": text_content,
                    "file_type": file_path.suffix.lower(),
                    "status": "success"
                }
        except Exception as e:
            return {
                "resume_path": str(file_path),
                "error": f"Text parsing error: {str(e)}",
                "status": "error"
            }
    
    @staticmethod
    def calculate_match_score(resume_content: str, job_requirements: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate match score between resume and job requirements.
        """
        # This would typically use NLP/LLM to calculate scores
        # For now, return a sample structure
        return {
            "technical_skills_score": 75,
            "experience_score": 80,
            "education_score": 90,
            "overall_score": 82,
            "analysis": "Match score calculation completed"
        }

class CompanyResearchTools:
    """Tools for company research agent."""
    
    @staticmethod
    def research_company(company_name: str) -> Dict[str, Any]:
        """
        Research company information.
        """
        # This would typically use web search APIs
        # For now, return a sample structure
        return {
            "company_name": company_name,
            "overview": f"Research results for {company_name}",
            "status": "success"
        }
    
    @staticmethod
    def get_company_insights(company_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract insights from company research data.
        """
        return {
            "culture": "Company culture insights",
            "interview_tips": ["Tip 1", "Tip 2", "Tip 3"],
            "common_questions": ["Question 1", "Question 2"],
            "insights": "Company insights analysis completed"
        } 