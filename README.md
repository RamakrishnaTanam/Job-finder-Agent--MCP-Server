
# 🧠 Job-finder-Agent--MCP-Server  
**Job Search Agent with Bright Data & Nebius AI Studio**

![Demo](assets/demo.gif)

A powerful AI-powered job search agent that analyzes LinkedIn profiles and finds relevant job opportunities using **Bright Data** for web scraping and **Nebius AI Studio** for intelligent analysis.

---

## 🚀 Features

### 🔍 LinkedIn Profile Analysis
- Professional experience and career progression  
- Education and certifications  
- Core skills and expertise  
- Industry reputation  

### 🧠 Intelligent Job Matching
- Domain classification (Software Engineering, Design, Product Management, etc.)  
- Y Combinator job board integration  
- Personalized job recommendations  
- Direct application links  

### 💻 Modern Web Interface
- Real-time analysis  
- Interactive results display  
- Progress tracking  
- Error handling  

---

## 📽️ How It Works (GIF Demo)
![Demo](assets/job-search.gif)


---

## ⚙️ Prerequisites

Before running this project, ensure you have:

- Python 3.10 or higher  
- A **Bright Data** account and API credentials  
- A **Nebius AI Studio** account and API key  

---

## 📁 Project Structure

```
job_finder_agent/
├── app.py               # Streamlit web interface
├── job_agents.py        # AI agent definitions and analysis logic
├── mcp_server.py        # Bright Data MCP server management
├── requirements.txt     # Python dependencies
├── assets/              # Static assets (images, GIFs)
└── .env                 # Environment variables (create this)
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Job-finder-Agent--MCP-Server.git
cd Job-finder-Agent--MCP-Server

# Create a virtual environment
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Configuration

Create a `.env` file in the root directory:

```
NEBIUS_API_KEY=your_nebius_api_key
BRIGHT_DATA_API_KEY=your_bright_data_api_key
BROWSER_AUTH=your_browser_auth
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

Then open your browser at [http://localhost:8501](http://localhost:8501) and:

1. Enter your Nebius API key in the sidebar  
2. Input a LinkedIn profile URL  
3. Click **"Analyze Profile"**  
4. Wait for the results to be displayed

---

## 🧬 How It Works (Logic Flow)

1. **Profile Analysis**: Extracts experience, skills, education from LinkedIn  
2. **Domain Classification**: Uses AI to classify the user's field  
3. **Job Matching**: Searches YC startup job board  
4. **URL Processing**: Cleans & prepares job application links  
5. **Summary Generation**: Presents a detailed final report

---

## 🧪 Technical Highlights

- Built with **Streamlit** for the UI  
- Async processing with `asyncio`  
- Scraping powered by **Bright Data MCP**  
- AI models served via **Nebius AI Studio (Llama 3.3 70B)**  
- Error handling and logging built-in  

---

## 🤝 Contributing

Contributions are welcome!  
Please feel free to submit a pull request or open an issue.

---

## 🙏 Acknowledgments

- [Bright Data](https://brightdata.com) – Web scraping & data pipeline  
- [Nebius AI Studio](https://nebius.ai/) – Generative AI inference  
- [Streamlit](https://streamlit.io) – Rapid app development framework  
