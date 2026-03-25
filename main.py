import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
import json 

load_dotenv()

def get_videoid_from_url(url):
    video_id = ""
    splitted_url = url.split("?")
    query_params = splitted_url[1]
    query_paramssplitted = query_params.split("&")
    for item in query_paramssplitted:
        if item.startswith("v="):
            video_id = item[2:]
    return video_id

def get_transcript(video_id):
    api =YouTubeTranscriptApi()
    transcript = api.fetch(video_id)
    #print(transcript.snippets[0].text)

    full_transcript = ""
    for item in transcript.snippets:
        full_transcript = full_transcript + item.text + " "

    return full_transcript

def get_insights(transcript):
    insights = ""

    client = OpenAI()
    prompt = f"""
    You are an expert podcast summarizer. Read the transcript below and return a concise summary in JSON with:
    - Summary: 2-3 sentences capturing the episode's core ideas

    - Key_Topics: 3-5 main topics discussed
    
    - Key_Takeaways: 3 actionable or memorable insights for the listener

    Make the output easy to read, like a normal article, not JSON.

    Transcript:
    {transcript}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        max_output_tokens=1500

    )
    # raw_output = response.output[0].content[0].text
    # clean_output = raw_output.replace("```json", "").replace("```", "").strip()
    # insights = json.loads(clean_output)
    # # insights = response.output[0].content[0].text
    # return json.dumps(insights, indent=4)
    return response.output[0].content[0].text.strip()

# def main():

#     # Step 0: Get video_id from url
#     url = input("Enter url: ")
#     video_id = get_videoid_from_url(url)
   
#     #Step 1: Get transcript from video_id 
#     transcript = get_transcript(video_id)
    
#     # Step 2: Get insights from LLM
#     insights = get_insights(transcript)
#     print(insights)

# main()    



st.title("YouTube Transcript Summariser")

url = st.text_input("Enter YouTube URL:")

if st.button("Generate Summary"):
    if url:
        with st.spinner("Fetching transcript and generating insights..."):
            try:
                video_id = get_videoid_from_url(url)
                transcript = get_transcript(video_id)
                insights = get_insights(transcript)
                # st.json(json.loads(insights))
                st.subheader("Podcast Summary")
                st.markdown(insights)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a valid YouTube URL")
