import streamlit as st

class GlobalStyle:
    def __init__(self):
        st.markdown(
            """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Chewy&family=Roboto:wght@400;700&display=swap');
                :root {
                    --background-color: #404040;
                    --text-color: white;
                    --header-color: #e6bd50;
                    --button-hover-color: #e6bd50;
                }
                body {
                    font-family: 'Roboto', sans-serif;
                    background-color: var(--background-color);
                    color: var(--text-color);
                    transition: background-color 0.3s ease, color 0.3s ease;
                }
                .stApp {
                    background-color: var(--background-color);
                }
                .biggie-text {
                    font-family: 'Chewy', cursive;
                    font-size: 72px;
                    color: var(--header-color);
                    text-align: center;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    transition: transform 0.3s ease;
                    margin-bottom: 30px;
                }
                .biggie-text:hover {
                    transform: scale(1.05);
                }
                .stSidebar {
                    background-color: #2a2a2a;
                    padding: 2rem 1rem;
                }
                .sidebar-title {
                    color: var(--header-color);
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }
                .sidebar-menu {
                    color: var(--header-color);
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 15px;
                }
                .sidebar-button {
                    width: 100%;
                    padding: 10px;
                    margin-bottom: 10px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    font-weight: bold;
                    cursor: pointer;
                    transition: all 0.3s ease;
                    display: flex;
                    align-items: center;
                }
                .sidebar-button:hover {
                    transform: translateX(5px);
                    box-shadow: -2px 0 5px rgba(255,255,255,0.2);
                }
                .sidebar-button-icon {
                    width: 20px;
                    height: 20px;
                    margin-right: 10px;
                    border-radius: 50%;
                }
                .content-area {
                    background-color: #333333;
                    border-radius: 10px;
                    padding: 20px;
                    margin-top: 20px;
                }
                .chart-container {
                    background-color: #2a2a2a;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 20px;
                }
                .metric-container {
                    background-color: #2a2a2a;
                    border-radius: 8px;
                    padding: 15px;
                    text-align: center;
                }
                .footer {
                    text-align: center;
                    color: var(--header-color);
                    margin-top: 50px;
                    font-size: 14px;
                    opacity: 0.8;
                }
            </style>
            """,
            unsafe_allow_html=True
        )
