import streamlit as st
import os
import wikipedia as wiki
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-1.5-flash")

prompt_template = """You are a knowledgeable bird encyclopedia chatbot. 
Use {content} (from a PDF encyclopedia) and Wikipedia API to provide accurate information about the bird "{bird}". 
If no reliable information is found, respond with "No information is available about {bird}." 

Include the following details: (if available otherwise skip)
- Scientific name 
- Physical description
- Length
- Wingspan
- Weight
- Lifespan
- Habitat
- Diet
- Behavior
- Distribution
- Conservation status
- Interesting fact

Ensure responses are concise, factual, and sourced from given data. If {bird} is fictional or misspelled, clarify that no data exists.
Note: The response should not write the source or document ID, if some information is not available, just skip it."""

st.set_page_config(
    page_title="Aviary.AI",
    page_icon=":eagle:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply a dark grey theme using CSS
st.markdown("""
    <style>
    /* General app background styling */
    body {
        background-color: #121212;
        color: #e0e0e0;
    }
    .stApp {
        background-color: #121212;
    }
    /* Header and subheader styles */
    header, h1, h2, h3 {
        color: #ffffff;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    h1 {
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 30px;
    }
    h2 {
        font-size: 1.5rem;
        font-weight: normal;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Page header and description
st.write("# Aviary.AI - Your AI-powered bird encyclopedia")
#st.subheader("Powered by Wikipedia, Gemini API, and three encyclopedias")
st.write("##### Enter the name of the bird you want to know more about in the searchbar, and click search")


# Functionality placeholder for user_input (to be replaced with your actual function)
def user_input( bird : str):
    prompt = PromptTemplate(template=prompt_template, input_variables=["content", "bird"])
    database = FAISS.load_local("faiss_index", GoogleGenerativeAIEmbeddings(model="models/embedding-001"), allow_dangerous_deserialization=True)
    encyclopedia_info = database.similarity_search(bird).append(wiki.page(bird).content)
    response = model.generate_content(prompt.format(content = encyclopedia_info, bird = bird))
    return response

bird  = st.text_input("", "")
submit_button = st.button("Search")

if submit_button:
    if bird.strip():
        result = user_input(bird).text
        st.markdown(f"{result}")
    else:
        st.warning("Please enter a bird name before clicking the Search button.")

# Footer or additional information
st.markdown("""    ---
    <div style="text-align: center; color: #9e9e9e; font-size: 0.9rem;">
        Made with ❤️ using Streamlit, powered by Gemini API, Wikipedia & Encyclopedias.
    </div>""", unsafe_allow_html=True)
