import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Mon App Gemini 3", page_icon="⚡")
st.title("⚡ Test de mon application (Gemini 3 Flash)")
st.caption("Application en cours de développement - Vos retours sont précieux !")

# --- CONFIGURATION DE L'IA ---
# Option 1 : Saisie via la barre latérale (pour vos tests)
api_key = st.sidebar.text_input("Clé API Gemini", type="password")

# Option 2 (Plus simple pour vos amis) :
# Décommentez la ligne ci-dessous et mettez votre clé directement
api_key = "AIzaSyBfTF3EbvRU8bjEGGTvrEheaccvVtXuJeY"

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # Le nom technique pour Gemini 3 Flash Preview
        MODEL_NAME = 'gemini-3.0-flash-preview' 
        
        # Chargement du modèle avec vos instructions de "Build"
        # Remplacez le texte ci-dessous par vos "System Instructions" de AI Studio
        model = genai.GenerativeModel(
            model_name=MODEL_NAME,
            system_instruction="Tu es un assistant expert créé dans AI Studio. Réponds de manière concise."
        )

        # Initialisation de l'historique
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Affichage du chat
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Interaction utilisateur
        if prompt := st.chat_input("Posez votre question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # Génération de la réponse
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"Oups ! Une erreur est survenue : {e}")
        st.info("Astuce : Vérifiez que votre clé API est bien valide pour le modèle Gemini 3.")
else:
    st.warning("Veuillez saisir votre clé API dans la barre latérale pour activer l'application.")


