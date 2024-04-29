import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import tempfile
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from langchain_pinecone import PineconeVectorStore

index_name= os.getenv("index_name")
pinecone_api_key = os.getenv("pinecone_api_key")
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Caching functions
@st.cache_resource
def load_pinecone_index():
    pc = PineconeVectorStore(embedding=embedding, pinecone_api_key=pinecone_api_key, index_name=index_name)
    db_Pinecone = pc.from_existing_index(index_name, embedding)
    return db_Pinecone

@st.cache_resource
def load_llm():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)
    return llm

# Load the data and LLM only once
db_Pinecone = load_pinecone_index()
llm = load_llm()
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db_Pinecone.as_retriever(search_kwargs={'k': 3}), return_source_documents=True)

# Streamlit interface
st.title("Medical Query Assistant")

# Function to recognize speech input
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)
    try:
        st.write("Processing...")
        query = r.recognize_google(audio)
        return query
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand what you said.")
        return None
    except sr.RequestError:
        st.error("Sorry, could not request results.")
        return None

# Text input
query = st.text_input("Enter your medical query:")

# Voice input
if st.button("🎤 Voice Input"):
    query = recognize_speech()

if query:
    result = qa({"query": query})
    st.write("Response:")
    st.write(result["result"])

    # Generate audio file
    temp_dir = tempfile.TemporaryDirectory()
    audio_file = os.path.join(temp_dir.name, "output.mp3")
    tts = gTTS(text=result["result"], lang="en")
    tts.save(audio_file)

    # Play audio file
    st.audio(audio_file)

    # Clean up temporary directory
    temp_dir.cleanup()