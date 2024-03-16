
import streamlit as st
from dotenv import load_dotenv
import os
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
import sys
from io import StringIO
from langchain_community.document_loaders import PyPDFLoader
from PyPDF2 import PdfReader

load_dotenv("APIK.env")
api_key = os.getenv('API_K')

st.title('Rhino AI')
