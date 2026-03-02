import streamlit as st
import google.generativeai as genai
from google.generativeai import types

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Mon App Gemini 3", page_icon="⚡")
st.title("⚡ Test de mon application (Gemini 3 Flash)")

# --- CONFIGURATION DE L'IA (OPTION 2) ---
# 1. REMPLACEZ PAR VOTRE CLÉ API
API_KEY = "AIzaSyBfTF3EbvRU8bjEGGTvrEheaccvVtXuJeY" 

try:
    # On configure l'API
    genai.configure(api_key=API_KEY)
    
    # FORCER LA VERSION BETA pour Gemini 3
    # Le nom exact est souvent 'models/gemini-3.0-flash-preview'
    MODEL_NAME = 'gemini-3.0-flash-preview' 

    # Initialisation du modèle
    model = genai.GenerativeModel(
        model_name=MODEL_NAME
    )

    # --- LOGIQUE DU CHAT ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Posez votre question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # On précise ici qu'on veut utiliser la version beta si nécessaire
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})

except Exception as e:
    # Si le 404 persiste, on affiche une aide au diagnostic
    st.error(f"Erreur : {e}")
    if "404" in str(e):
        st.info("Le modèle Gemini 3 est peut-être restreint. Essayez de remplacer 'gemini-3.0-flash-preview' par 'gemini-1.5-flash' dans le code pour vérifier si votre clé fonctionne.")
