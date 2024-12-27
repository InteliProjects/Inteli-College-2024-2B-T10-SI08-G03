import streamlit as st
from frontend.services.auth import AuthService
from all_pages.home import HomePage
from all_pages.login import LoginPage
from all_pages.line import LinePage
from dotenv import load_dotenv
import os
from styles.Global import GlobalStyle
from streamlit_cookies_controller import CookieController

# Carregar as variáveis de ambiente
load_dotenv()

st.set_page_config(page_title="Biggie Dashboard", page_icon="📊")

class BiggieApp:
    def __init__(self):
        # Inicializar o serviço de autenticação
        self.auth_service = AuthService()
        self.controller = CookieController()
        
        self.cookie = self.controller.get("logged_in")
        
        if self.cookie:
            st.session_state["authentication_status"] = True
            st.session_state["user"] = self.cookie["username"]
        # Definir as páginas e passar o authenticator
        self.pages = {
            "Home": lambda: HomePage().render(),
            "Login": lambda: LoginPage().render(self.navigate_to),
            "Line": lambda: LinePage().render(self.navigate_to)
        }
        
        # Inicializar o estilo global
        GlobalStyle()
        
        if "line" not in st.session_state:
            st.session_state["line"] = None 
        if "selected_line_color" not in st.session_state:
            st.session_state["selected_line_color"] = None
        # Executar a navegação
        self.run()

    def navigate_to(self, page_name):
        """
        Navega para a página especificada.
        """
        st.session_state["current_page"] = page_name

    def run(self):
        """
        Controla a lógica de navegação e renderiza a página atual.
        """
        if self.auth_service.is_authenticated():
            st.session_state["current_page"] = "Home"
            if st.session_state["line"] != None:
                st.session_state["current_page"] = "Line"
        else:
            st.session_state["current_page"] = "Login"
        st.write(self.pages[st.session_state["current_page"]]())

if __name__ == "__main__":
    BiggieApp()
