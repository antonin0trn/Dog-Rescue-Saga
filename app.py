import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="Mon App Dog Rescue Saga", page_icon="🤖")
st.title("🤖 Testez mon application !")
st.caption("Donnez-moi vos retours pour m'aider à l'améliorer.")

# --- CONFIGURATION DE L'IA ---
# Remplacez par votre clé API ou utilisez les secrets Streamlit en production
api_key = st.sidebar.text_input("AIzaSyBfTF3EbvRU8bjEGGTvrEheaccvVtXuJeY", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash') # Ou votre modèle spécifique

    # Initialisation de l'historique du chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Affichage des messages précédents
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Zone de saisie utilisateur
    if prompt := st.chat_input("Dites quelque chose..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Génération de la réponse
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.info("Veuillez entrer une clé API dans la barre latérale pour commencer.", icon="🔑")
