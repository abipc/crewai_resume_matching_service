#!/usr/bin/env python3
"""
Resume Optimization with CrewAI
Main application file that orchestrates the AI agents for resume optimization.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from src.resume_crew.agents import JobAnalyzer, ResumeAnalyzer
from src.resume_crew.tasks import create_job_analysis_task, create_resume_optimization_task

# Load environment variables
load_dotenv()

def main():
    """
    Main function to run the resume optimization crew.
    """
    # Configuration
    job_url = "https://jobs.weekday.works/google-director%2C-customer-engineering%2C-india%2C-google-cloud?utm_campaign=google_jobs_apply&utm_source=google_jobs_apply&utm_medium=organic"
    company_name = "Google Cloud"
    
    # Resume configuration - using the PDF resume
    resume_path = "knowledge/Abhishek_Sharma_Resume.pdf"
    
    # Create output directory if it doesn't exist
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Validate resume file exists
    if not Path(resume_path).exists():
        print(f"❌ Resume file not found: {resume_path}")
        print("Please place your resume in the knowledge/ directory")
        print("Supported formats: .pdf, .txt, .md")
        return
    
    print(f"📄 Using resume: {resume_path}")
    print(f"🏢 Analyzing job at: {company_name}")
    print(f"🔗 Job URL: {job_url}")
    
    # Initialize agents
    job_analyzer = JobAnalyzer()
    resume_analyzer = ResumeAnalyzer()
    
    # Create tasks
    job_analysis_task = create_job_analysis_task(job_analyzer, job_url, company_name)
    resume_optimization_task = create_resume_optimization_task(resume_analyzer, job_url, company_name, resume_path)
    
    # Create crew (without company researcher)
    crew = Crew(
        agents=[job_analyzer, resume_analyzer],
        tasks=[job_analysis_task, resume_optimization_task],
        process=Process.sequential,
        verbose=True,
        debug=True
    )
    
    # Run the crew
    print("🚀 Starting Resume Optimization Crew...")
    result = crew.kickoff()
    
    # Save results
    save_results(result)
    
    print("✅ Resume optimization completed!")
    print(f"📁 Results saved in: {output_dir.absolute()}")

def save_results(result):
    """
    Save the crew results to JSON and Markdown files.
    """
    output_dir = Path("output")
    try:
        # Try to convert result to dict if possible
        if hasattr(result, 'dict'):
            result_data = result.dict()
        elif hasattr(result, '__dict__'):
            result_data = result.__dict__
        else:
            result_data = str(result)
        
        # Save JSON file
        with open(output_dir / "complete_analysis.json", "w") as f:
            json.dump(result_data, f, indent=2)
        print("✅ Results saved to output/complete_analysis.json")
        
        # Generate and save Markdown report
        generate_markdown_report(result_data, output_dir)
        print("✅ Markdown report saved to output/final_report.md")
        
    except Exception as e:
        print(f"Error saving results: {e}")

def generate_markdown_report(result_data, output_dir):
    """
    Generate a comprehensive markdown report from the analysis results.
    """
    import json
    
    # Extract data from tasks_output
    job_analysis = {}
    resume_optimization = {}
    
    if 'tasks_output' in result_data:
        for task in result_data['tasks_output']:
            agent_name = task.get('agent', '')
            raw_output = task.get('raw', '')
            
            # Parse JSON from raw output
            try:
                if raw_output.startswith('```json'):
                    # Remove markdown code blocks
                    json_str = raw_output.replace('```json', '').replace('```', '').strip()
                    parsed_data = json.loads(json_str)
                elif raw_output.startswith('{'):
                    # Direct JSON
                    parsed_data = json.loads(raw_output)
                else:
                    continue
                
                # Assign data based on agent
                if 'Job Requirements Analyst' in agent_name:
                    job_analysis = parsed_data
                elif 'Resume Optimization Specialist' in agent_name:
                    resume_optimization = parsed_data
                
            except json.JSONDecodeError:
                print(f"Warning: Could not parse JSON for {agent_name}")
                continue
    
    # Get current date
    current_date = datetime.now().strftime("%B %d, %Y")
    
    # Generate markdown content
    markdown_content = f"""# Resume Analysis Report: Abhishek Sharma vs Google Cloud Director Position

## 📊 Executive Summary

**Candidate:** Abhishek Sharma  
**Target Position:** Director, Customer Engineering, Google Cloud  
**Analysis Date:** {current_date}  
**Overall Match Score:** {resume_optimization.get('match_scores', {}).get('overall_fit', 'N/A')}/100

---

## 🎯 Job Analysis

### Position Details
- **Title:** {job_analysis.get('job_title', 'Director, Customer Engineering, Google Cloud')}
- **Location:** Bengaluru, Karnataka, India
- **Experience Required:** {job_analysis.get('required_experience', '10+ years in technology and cloud computing')}

### Key Requirements

#### Required Skills
{format_skills_list(job_analysis.get('required_skills', []))}

#### Preferred Skills
{format_skills_list(job_analysis.get('preferred_skills', []))}

### Key Responsibilities
{format_responsibilities(job_analysis.get('key_responsibilities', []))}

### Company Culture
{job_analysis.get('company_culture', 'Information not available')}

### Benefits
{format_skills_list(job_analysis.get('benefits', []))}

---

## 📈 Resume Match Analysis

### Match Scores
| Category | Score | Status |
|----------|-------|--------|
| **Technical Skills** | {resume_optimization.get('match_scores', {}).get('technical_skills', 'N/A')}/100 | {get_status_emoji(resume_optimization.get('match_scores', {}).get('technical_skills', 0))} |
| **Experience Relevance** | {resume_optimization.get('match_scores', {}).get('experience_relevance', 'N/A')}/100 | {get_status_emoji(resume_optimization.get('match_scores', {}).get('experience_relevance', 0))} |
| **Education Requirements** | {resume_optimization.get('match_scores', {}).get('education_requirements', 'N/A')}/100 | {get_status_emoji(resume_optimization.get('match_scores', {}).get('education_requirements', 0))} |
| **Overall Fit** | {resume_optimization.get('match_scores', {}).get('overall_fit', 'N/A')}/100 | {get_status_emoji(resume_optimization.get('match_scores', {}).get('overall_fit', 0))} |

### Skill Gaps Identified
{format_skill_gaps_simple(resume_optimization.get('skill_gaps', []))}

---

## 🔧 Optimization Recommendations

### Keywords to Add
{format_keywords(resume_optimization.get('skill_gaps', []))}

### Experience Descriptions to Improve
{format_improvements_simple(resume_optimization.get('optimization_suggestions', []))}

### ATS Optimization
{format_ats_tips(resume_optimization.get('ats_optimization', []))}

---

## 🎯 Action Items (Prioritized)

### High Priority
{format_action_items_simple(resume_optimization.get('action_items', []))}

---

## 📋 Next Steps

1. **Immediate (1-2 weeks):**
   - Revise resume with identified keywords and improvements
   - Add Google Cloud Platform experience or certifications
   - Update experience descriptions with quantifiable achievements

2. **Short-term (2-4 weeks):**
   - Research Google Cloud products and services
   - Practice interview questions using STAR method
   - Network with Google Cloud professionals

3. **Long-term (1-3 months):**
   - Consider Google Cloud certifications
   - Build experience with enterprise customers
   - Develop leadership and sales skills

---

*This analysis was generated using AI-powered resume optimization tools. The recommendations are based on the job requirements and industry best practices for ATS optimization and interview preparation.*
"""
    
    # Save markdown file
    with open(output_dir / "final_report.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)

def format_skills_list(skills):
    """Format skills list for markdown."""
    if not skills:
        return "- Information not available"
    return "\n".join([f"- {skill}" for skill in skills])

def format_responsibilities(responsibilities):
    """Format responsibilities for markdown."""
    if not responsibilities:
        return "Information not available"
    return "\n".join([f"{i+1}. {resp}" for i, resp in enumerate(responsibilities)])

def format_skill_gaps_simple(gaps):
    """Format skill gaps for markdown (simple list)."""
    if not gaps:
        return "No specific gaps identified"
    return "\n".join([f"{i+1}. **{gap}**" for i, gap in enumerate(gaps)])

def format_keywords(keywords):
    """Format keywords for markdown."""
    if not keywords:
        return "- Information not available"
    return "\n".join([f"- {keyword}" for keyword in keywords])

def format_improvements_simple(improvements):
    """Format improvements for markdown (simple list)."""
    if not improvements:
        return "Information not available"
    return "\n".join([f"{i+1}. {imp}" for i, imp in enumerate(improvements)])

def format_ats_tips(tips):
    """Format ATS tips for markdown."""
    if not tips:
        return "- Information not available"
    return "\n".join([f"- {tip}" for tip in tips])

def format_action_items_simple(actions):
    """Format action items for markdown (simple list)."""
    if not actions:
        return "No specific actions identified"
    return "\n".join([f"{i+1}. {action}" for i, action in enumerate(actions)])

def get_status_emoji(score):
    """Get status emoji based on score."""
    if isinstance(score, (int, float)):
        if score >= 80:
            return "✅ Excellent"
        elif score >= 70:
            return "✅ Strong"
        elif score >= 60:
            return "⚠️ Good"
        else:
            return "❌ Needs Improvement"
    return "N/A"

if __name__ == "__main__":
    main() 