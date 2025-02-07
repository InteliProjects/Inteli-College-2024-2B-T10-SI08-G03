import streamlit as st
from dotenv import load_dotenv
import os
from streamlit_cookies_controller import CookieController

class AuthService:
    def __init__(self):
        
        load_dotenv()
        # Carregar credenciais do .env
        usernames = os.getenv("USERNAMES", "").split(',')
        passwords = os.getenv("PASSWORDS", "").split(',')
        names = os.getenv("NAMES", "").split(',')
        emails = os.getenv("EMAILS", "").split(',')
        
        if not all([usernames, passwords, names, emails]):
            raise ValueError("One or more environment variables are missing or empty.")

        # Configurar autenticação com um `key` único
        self.credentials = {
            "usernames": {
                usernames[i]: {"email": emails[i], "name": names[i], "password": passwords[i]}
                for i in range(len(usernames))
            }
        }

    def login(self, username, password):
        """
        Realiza o login do usuário e retorna status e informações.
        """
        self.controller = CookieController()
        if username in self.credentials["usernames"] and self.credentials["usernames"][username]["password"] == password:
            st.session_state["authentication_status"] = True
            st.session_state["user"] = self.credentials["usernames"][username]
            self.controller.set("logged_in", {"username": username})
            return True
        else:
            st.session_state["authentication_status"] = False
            st.session_state["user"] = None
            return False

    def logout(self):
        """
        Realiza o logout do usuário.
        """
        self.controller = CookieController()
        st.session_state["authentication_status"] = False
        st.session_state["user"] = None
        self.controller.remove("logged_in")
        
    def is_authenticated(self):
        """
        Verifica se o usuário está autenticado.
        """
        return st.session_state.get("authentication_status")
