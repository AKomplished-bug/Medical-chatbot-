from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
load_dotenv()
import os

data="medical_data/"
loader=DirectoryLoader(data,glob ="*pdf",loader_cls=PyPDFLoader)
documents=loader.load()
split_txt=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=20)
chunks_txt=split_txt.split_documents(documents)
print(chunks_txt)
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
pinecone_api_key = os.getenv("pinecone_api_key")
index_name= os.getenv("index_name")
pinecone = PineconeVectorStore.from_documents(chunks_txt, embedding, index_name=index_name)
print("vectors upserted")

