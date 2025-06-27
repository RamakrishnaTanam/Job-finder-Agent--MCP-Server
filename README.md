# Job-finder-Agent--MCP-Server


**Job Search Agent with Bright Data and Nebius AI Studio**


(assets/demo.gif)


A powerful AI-powered job search agent that analyzes LinkedIn profiles and finds relevant job opportunities using Bright Data for web scraping and Nebius AI Studio for intelligent analysis.

Features
LinkedIn Profile Analysis

Professional experience and career progression
Education and certifications
Core skills and expertise
Industry reputation
Intelligent Job Matching

Domain classification (Software Engineering, Design, Product Management, etc.)
Y Combinator job board integration
Personalized job recommendations
Direct application links
Modern Web Interface

Real-time analysis
Interactive results display
Progress tracking
Error handling
How it Works
Gif

Prerequisites
Before running this project, make sure you have:

Python 3.10 or higher
A Bright Data account and API credentials
Nebius AI Studio account and API key
Project Structure
job_finder_agent/
├── app.py              # Streamlit web interface
├── job_agents.py       # AI agent definitions and analysis logic
├── mcp_server.py       # Bright Data MCP server management
├── requirements.txt    # Python dependencies
├── assets/            # Static assets (images, GIFs)
└── .env              # Environment variables (create this)
Installation
Clone the repository:
git clone https://github.com/Arindam200/awesome-ai-apps.git
cd advance_ai_agents/job_finder_agent
Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Configuration
Create a .env file in the project root with:

NEBIUS_API_KEY="Your Nebius API Key"
BRIGHT_DATA_API_KEY="Your Bright Data API Key"
BROWSER_AUTH="Your Bright Data Browser Auth"
Usage
Start the application:
streamlit run app.py
Open your browser at http://localhost:8501

Enter your Nebius API key in the sidebar

Input a LinkedIn profile URL to analyze

Click "Analyze Profile" and wait for results

How It Works
Profile Analysis: The LinkedIn Profile Analyzer agent extracts key information from the provided LinkedIn profile.

Domain Classification: The Job Suggestions agent identifies the primary professional domain and confidence score.

Job Matching: The system searches Y Combinator's job board for relevant positions based on the identified domain.

URL Processing: Job application URLs are processed to provide direct application links.

Summary Generation: A comprehensive report is generated with profile analysis, skill assessment, and job recommendations.

Technical Details
Uses Streamlit for the web interface
Implements asynchronous processing with asyncio
Leverages Bright Data's MCP server for web scraping
Utilizes Nebius AI Studio's Llama-3.3-70B-Instruct model for analysis
Implements proper error handling and logging
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Acknowledgments
Bright Data for web scraping capabilities
Nebius AI Studio for AI model access
Streamlit for the web interface framework
