# ![YouTube](https://img.icons8.com/color/24/youtube-play.png) YouTube Transcript Summariser (AI Agent)

## Overview
In today’s fast-paced world, consuming long-form video content like podcasts (1–2 hours) is not always feasible. This project solves that problem by building an **AI-powered YouTube Transcript Summarizer** that extracts key learnings from videos in seconds.

The application takes a YouTube video URL, fetches the transcript, and generates:
- Concise summary  
- Key topics discussed  
- Actionable takeaways  

All presented in a clean, readable format.

This project builds an **AI agent pipeline** that:

1. Extracts transcript from a YouTube video  
2. Processes the raw text  
3. Uses an LLM to generate structured insights  
4. Displays results through an interactive UI  

---

## Tech Stack

- Python  
- Streamlit – UI for user interaction  
- OpenAI API – LLM for summarization  
- youtube-transcript-api – Fetch video transcripts  
- dotenv – Manage environment variables  

---

## Project Workflow

### Step 1: Extract Video ID- Parses YouTube URL to retrieve the video ID  

### Step 2: Fetch Transcript- Uses `youtube-transcript-api` to get transcript and combines all snippets into a single text  

### Step 3: Generate Insights by LLM - Sends transcript to OpenAI model and summarizes by highlighiting key topics and key takeaways.

### Step 4: Display Output- Streamlit UI renders insights in a readable format  

---

## 🖥️ Demo UI


### Input:
- YouTube video URL  

### Output:
- Summary  
- Key Topics  
- Key Takeaways  

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <repo-name>
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
```bash
OPENAI_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run main.py
```
