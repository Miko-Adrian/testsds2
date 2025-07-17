import streamlit as st
import requests
import pandas as pd
from PIL import Image
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Chemical Safety Checker",
    page_icon="⚠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>  
    .stButton>button {  
        background-color: #4CAF50;  
        color: white;  
        padding: 10px 24px;  
        border: none;  
        border-radius: 4px;  
        cursor: pointer;  
    }  
    .stButton>button:hover {  
        background-color: #45a049;  
    }  
    .hazard-icon {  
        font-size: 24px;  
        margin-right: 10px;  
    }  
    .ppe-icon {  
        font-size: 20px;  
        margin-right: 5px;  
    }  
    .warning-box {  
        border-left: 4px solid #FFA500;  
        padding: 10px;  
        background-color: #FFF3CD;  
        margin-bottom: 10px;  
    }  
</style>  
""", unsafe_allow_html=True)

def get_pubchem_data(chemical_name):
    """Fetch chemical data from PubChem API"""
    base_url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"
    cid_url = f"{base_url}/compound/name/{chemical_name}/cids/JSON"

    try:
        response = requests.get(cid_url)
        if response.status_code == 200:
            cid = response.json()['IdentifierList']['CID'][0]
            compound_url = f"{base_url}/compound/cid/{cid}/JSON"
            compound_response = requests.get(compound_url)

            if compound_response.status_code == 200:
                compound_data = compound_response.json()
                return {
                    '}
