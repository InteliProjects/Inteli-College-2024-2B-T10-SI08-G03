import streamlit as st
from services.auth import AuthService

class SideBar:
    def __init__(self):
        
        self.auth_service = AuthService()
        st.sidebar.markdown('<p class="sidebar-title">Painel Geral</p>', unsafe_allow_html=True)
        st.sidebar.markdown('<p class="sidebar-menu">Menu</p>', unsafe_allow_html=True)
        
        if st.session_state.current_page == "Home":
            st.sidebar.markdown('<button class="sidebar-selected" style="display:flex;background-color: gray;border-radius:10px; border:1px; align-items:center; justify-content:center;align-content:center;justify-items:center; height:40px">Home</button>', unsafe_allow_html=True)
        
        else:
            if st.sidebar.button("Home"):
                self.home()
            
        
        lines = [
            ("Linha 7 - Rubi", "#a8034f"),
            ("Linha 10 - Turquesa", "#00829b"),
            ("Linha 11 - Coral", "#f55f1a"),
            ("Linha 12 - Safira", "#1c146b"),
            ("Linha 13 - Jade", "#00b052")
        ]
        
        for line, color in lines:
            if line == st.session_state.line:
                st.sidebar.markdown(f'<button class="sidebar-selected" style="display:flex;background-color: {color};border-radius:10px; border:1px; align-items:center; justify-content:center;align-content:center;justify-items:center; height:40px">{line}</button>', unsafe_allow_html=True)
                continue
            if st.sidebar.button(f"{line}", key=f"{line}"):
                st.sidebar.markdown(f'<p class="sidebar-selected" style="background-color: {color};">{line}</p>', unsafe_allow_html=True)
                self.line(line)
                
        if st.sidebar.button("Sair"):
            self.auth_service.logout()
            st.session_state.current_page = "Login"
            st.rerun()
        
        
    def line(self, line):
        st.session_state.line = line
        st.session_state.current_page = "Line"
        st.rerun()
        
    def home(self):
        st.session_state.current_page = "Home"
        st.session_state.line = None
        st.rerun()
        
    