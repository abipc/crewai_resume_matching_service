# Resume Optimization Crew - Documentation

## Overview

This project implements an AI-powered resume optimization system using CrewAI. The system uses three specialized agents to analyze job postings, optimize resumes, and provide company research insights.

## Architecture

### Agents

1. **Job Analyzer Agent**
   - Role: Job Requirements Analyst
   - Purpose: Extract and analyze job requirements from job postings
   - Tools: Web scraping, content analysis

2. **Resume Analyzer Agent**
   - Role: Resume Optimization Specialist
   - Purpose: Analyze resume match and suggest improvements
   - Tools: PDF parsing, match scoring, optimization suggestions

3. **Company Researcher Agent**
   - Role: Company Research Specialist
   - Purpose: Research companies and provide interview insights
   - Tools: Web search, company analysis

### Tasks

Each agent performs specific tasks:

- **Job Analysis Task**: Extract job requirements, skills, and qualifications
- **Resume Optimization Task**: Calculate match scores and suggest improvements
- **Company Research Task**: Gather company insights for interview preparation

### Tools

The system includes specialized tools for:

- Web scraping job postings
- PDF resume parsing
- Content analysis and scoring
- Company research and insights

## Usage

### Prerequisites

- Python 3.10+
- OpenAI API key
- Serper API key (for web search)

### Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables
4. Place your resume in the `knowledge/` directory

### Running the System

```bash
python main.py
```

### Configuration

Edit `main.py` to configure:
- Job posting URL
- Company name
- Resume file path

## Output

The system generates three JSON files:

1. `job_analysis.json` - Detailed job requirements analysis
2. `resume_optimization.json` - Resume optimization suggestions
3. `company_research.json` - Company insights for interviews

## Customization

### Adding New Agents

1. Create a new agent class in `src/resume_crew/agents.py`
2. Define corresponding tools in `src/resume_crew/tools.py`
3. Create tasks in `src/resume_crew/tasks.py`
4. Update `main.py` to include the new agent

### Modifying Tools

Tools can be customized by:
- Adding new API integrations
- Implementing different analysis algorithms
- Extending data processing capabilities

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all required API keys are set in `.env`
2. **PDF Parsing Issues**: Check that resume file exists and is readable
3. **Web Scraping Errors**: Some job sites may block automated access

### Debug Mode

Enable debug mode by setting `CREWAI_DEBUG=true` in your environment variables.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details. 