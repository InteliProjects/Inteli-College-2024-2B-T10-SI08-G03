import streamlit as st
import plotly.express as px
import pandas as pd
import requests
import os
from urllib.parse import quote
from dotenv import load_dotenv

load_dotenv()

class LinhaPage:
    def _init_(self):
        st.set_page_config(
            page_title="Biggie - Página de Linhas",
            layout="wide",
            initial_sidebar_state="expanded",
        )
        self.backend_url = "http://localhost:5000"
        params = st.experimental_get_query_params()
        self.api_token = params.get('token', [None])[0]
        self.line_mapping = {
            "Linha 7 Rubi": "LINHA 7 - RUBI",
            "Linha 10 Turquesa": "LINHA 10 - TURQUESA",
            "Linha 11 Coral": "LINHA 11 - CORAL",
            "Linha 12 Safira": "LINHA 12 - SAFIRA",
            "Linha 13 Jade": "LINHA 13 - JADE"
        }
        self.configure_page()
        self.render_sidebar()
        self.render_content()
        self.render_footer()
    
    def configure_page(self):
        st.markdown(
            """
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Chewy&family=Roboto:wght@400;700&display=swap');
                :root {
                    --background-color: #404040;
                    --text-color: white;
                    --header-color: #E6BD50;
                    --button-hover-color: #E6BD50;
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
                    font-size: 64px;
                    color: var(--header-color);
                    text-align: center;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    transition: transform 0.3s ease;
                    margin-bottom: 30px;
                }
                .biggie-text:hover {
                    transform: scale(1.05);
                }
                .content-area {
                    background-color: #333333;
                    border-radius: 10px;
                    padding: 20px;
                    margin-top: 20px;
                }
                .chart-container {
                    background-color: #2A2A2A;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 20px;
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
    
    def render_sidebar(self):
        st.sidebar.title("Seleção de Linha")
        st.sidebar.markdown("Escolha a linha abaixo para visualizar os dados.")
        lines = [
            ("Linha 7 Rubi", "#A8034F", "linha_7_rubi"),
            ("Linha 10 Turquesa", "#00829B", "linha_10_turquesa"),
            ("Linha 11 Coral", "#F55F1A", "linha_11_coral"),
            ("Linha 12 Safira", "#1C146B", "linha_12_safira"),
            ("Linha 13 Jade", "#00B052", "linha_13_jade")
        ]
        if 'selected_line' not in st.session_state:
            st.session_state['selected_line'] = lines[0][0]
        for line_name, color, line_id in lines:
            if st.sidebar.button(line_name, key=line_id):
                st.session_state['selected_line'] = line_name
        self.selected_line = st.session_state['selected_line']
    
    def render_content(self):
        st.markdown(f'<h1 class="biggie-text">{self.selected_line} - BIGGIE</h1>', unsafe_allow_html=True)
        st.markdown('<div class="content-area">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["Gráficos", "Estatísticas"])
        linha_param = self.line_mapping.get(self.selected_line, self.selected_line)
        linha_param_encoded = quote(linha_param)

        with tab1:
            st.markdown("### Gráficos da Linha")
            st.markdown("#### Duração das Viagens")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/duracao_viagens/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'duracao_real' in df.columns and 'duracao_programada' in df.columns:
                        df = df.sort_values('id_viagem')
                        fig = px.line(df, x='id_viagem', y=['duracao_real', 'duracao_programada'],
                                      labels={'id_viagem': 'ID da Viagem', 'value': 'Duração (min)', 'variable': 'Tipo de Duração'},
                                      title='Duração Real vs Programada')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Viagens por Dia da Semana")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/viagens_dia_semana/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'dia_semana' in df.columns:
                        dias_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
                        df['dia_semana'] = pd.Categorical(df['dia_semana'], categories=dias_semana, ordered=True)
                        df = df.sort_values('dia_semana')
                        fig = px.bar(df, x='dia_semana', y='quantidade_viagens',
                                     labels={'dia_semana': 'Dia da Semana', 'quantidade_viagens': 'Quantidade de Viagens'},
                                     title='Quantidade de Viagens por Dia da Semana')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Quantidade de Viagens por Estação de Origem")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/quantidade_viagens_origem/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_alerta' in df.columns:
                        fig = px.bar(df, x='total_flags', y='estacao_alerta', orientation='h',
                                     labels={'estacao_alerta': 'Estação de Origem', 'total_flags': 'Quantidade de Viagens'},
                                     title='Quantidade de Viagens por Estação de Origem')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### PCDs por Estação de Origem")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/pcd_origem/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_origem' in df.columns:
                        fig = px.bar(df, x='total_pcds', y='estacao_origem', orientation='h',
                                     labels={'estacao_origem': 'Estação de Origem', 'total_pcds': 'Quantidade de PCDs'},
                                     title='Quantidade de PCDs por Estação de Origem')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### PCDs por Estação de Destino")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/pcd_destino/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_destino' in df.columns:
                        fig = px.bar(df, x='total_pcds', y='estacao_destino', orientation='h',
                                     labels={'estacao_destino': 'Estação de Destino', 'total_pcds': 'Quantidade de PCDs'},
                                     title='Quantidade de PCDs por Estação de Destino')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Quantidade de Viagens por Estação de Destino")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/quantidade_viagens_destino/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_destino' in df.columns:
                        fig = px.bar(df, x='quantidade_viagens', y='estacao_destino', orientation='h',
                                     labels={'estacao_destino': 'Estação de Destino', 'quantidade_viagens': 'Quantidade de Viagens'},
                                     title='Quantidade de Viagens por Estação de Destino')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Quantidade de Viagens por Dia do Mês")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/quantidade_viagens_dia_mes/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'dia_mes' in df.columns:
                        df = df.sort_values('dia_mes')
                        fig = px.line(df, x='dia_mes', y='quantidade_viagens',
                                      labels={'dia_mes': 'Dia do Mês', 'quantidade_viagens': 'Quantidade de Viagens'},
                                      title='Quantidade de Viagens por Dia do Mês')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Alerta por Estação")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/alerta_estacao/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_alerta' in df.columns:
                        fig = px.bar(df, x='estacao_alerta', y='total_flags',
                                     labels={'estacao_alerta': 'Estação', 'total_flags': 'Total de Alertas'},
                                     title='Total de Alertas por Estação')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

            st.markdown("#### Quantidade de Viagens por Estação de Origem e Destino")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                data = self.get_data_from_backend(f"/api/quantidade_viagens_origem_destino/{linha_param_encoded}")
                if data:
                    df = pd.DataFrame(data)
                    if not df.empty and 'estacao_origem' in df.columns and 'estacao_destino' in df.columns:
                        fig = px.bar(df, x='estacao_destino', y='quantidade_viagens', color='estacao_origem',
                                     labels={'estacao_destino': 'Estação de Destino', 'quantidade_viagens': 'Quantidade de Viagens', 'estacao_origem': 'Estação de Origem'},
                                     title='Quantidade de Viagens por Estação de Origem e Destino')
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.write("Dados insuficientes para gerar o gráfico.")
                else:
                    st.write("Nenhum dado disponível.")
                st.markdown('</div>', unsafe_allow_html=True)

        with tab2:
            st.markdown("### Estatísticas da Linha")
            col1, col2, col3 = st.columns(3)
            data = self.get_data_from_backend(f"/api/viagens_dia_semana/{linha_param_encoded}")
            total_viagens = sum([item['quantidade_viagens'] for item in data]) if data else 0
            with col1:
                st.metric("Total de Viagens", f"{total_viagens}", "2%")
            data = self.get_data_from_backend(f"/api/duracao_viagens/{linha_param_encoded}")
            duracao_media = (pd.DataFrame(data)['duracao_real'].mean()) if data else 0
            with col2:
                st.metric("Duração Média das Viagens", f"{duracao_media:.2f} minutos", "-1%")
            data = self.get_data_from_backend(f"/api/pcd_origem/{linha_param_encoded}")
            total_pcds = sum([item['total_pcds'] for item in data]) if data else 0
            with col3:
                st.metric("Total de PCDs", f"{total_pcds}", "5%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def render_footer(self):
        st.markdown("<p class='footer'>Equipe Biggie © 2024 | Todos os direitos reservados</p>", unsafe_allow_html=True)
    
    def get_data_from_backend(self, endpoint):
        try:
            if not self.api_token:
                st.error("Erro: API Token não está definido. Por favor, inclua o token na URL como parâmetro 'token'.")
                return []
            headers = {
                "Authorization": f"Bearer {self.api_token}"
            }
            response = requests.get(f"{self.backend_url}{endpoint}", headers=headers)
            if response.status_code == 200:
                return response.json().get("data", [])
            elif response.status_code == 401:
                st.error("Erro ao obter dados do backend: 401 - Não autorizado. Verifique o token de autenticação.")
            else:
                st.error(f"Erro ao obter dados do backend: {response.status_code}")
        except requests.exceptions.RequestException as e:
            st.error(f"Erro de conexão com o backend: {e}")
        return []

if _name_ == "_main_":
    LinhaPage()