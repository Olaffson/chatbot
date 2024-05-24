import streamlit as st
import openai
from openai.error import RateLimitError, InvalidRequestError, AuthenticationError
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Configurez votre clé API OpenAI à partir de la variable d'environnement
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("Chatbot avec GPT-3.5 Turbo")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

def generate_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except RateLimitError:
        return "Vous avez dépassé votre quota d'utilisation de l'API OpenAI. Veuillez vérifier votre forfait et vos détails de facturation."
    except InvalidRequestError as e:
        return f"Erreur dans la requête : {str(e)}"
    except AuthenticationError:
        return "Erreur d'authentification. Veuillez vérifier votre clé API."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"

# Affichage des messages
for message in st.session_state['messages']:
    st.write(message)

# Champ de saisie de l'utilisateur
user_input = st.text_input("You: ", "")

if st.button("Envoyer"):
    if user_input:
        st.session_state['messages'].append(f"You: {user_input}")
        response = generate_response(user_input)
        st.session_state['messages'].append(f"Bot: {response}")

    # Rafraîchir la page pour afficher les nouveaux messages
    st.rerun()
