import streamlit as st
from Components.Login import LoginContainer
from services.auth import AuthService


class LoginPage:
    def __init__(self):
        self.auth_service = AuthService()

    def render(self, navigate_to):
        """
        Renderiza a página de login.
        """
        LoginContainer()
        
        
