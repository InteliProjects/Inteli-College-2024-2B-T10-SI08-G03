import streamlit as st
from services.auth import AuthService
import time

class LoginContainer:
    def __init__(self):
        self.auth_service = AuthService()
        
        st.markdown(
            "<h1 style='text-align: center; color: #4CAF50;'>Biggie Dashboard</h1>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<p style='text-align: center; font-size: 18px;'>Faça login para acessar o sistema</p>",
            unsafe_allow_html=True
        )
        
        self.user_name = st.text_input("username")
        self.password = st.text_input("Senha", type="password")
        # botao para login
        if st.button("Login"):
            self.login(self.user_name, self.password)
        
        
        
    def login(self, user_name, password):
        if self.auth_service.login(user_name, password):
            st.success("Login realizado com sucesso!")
            time.sleep(1)
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
            time.sleep(1)
            st.rerun()
        