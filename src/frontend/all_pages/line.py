import streamlit as st
from Components.Header import Header
from Components.Footer import Footer
from Components.SideBar import SideBar
import plotly.express as px
import pandas as pd
import asyncio
from urllib.parse import quote
from services.RequestToBackend import BackendService


class LinePage:
    def __init__(self):
        self.backend = BackendService()
        self.curr_line = st.session_state.line
        self.param = quote(self.curr_line.upper())
        self.endpoints = {
            "duracao_viagens":f"/api/duracao_viagens/{self.param}",
            "viagens_dia_semana":f"/api/viagens_dia_semana/{self.param}",
            "quantidade_viagens_origem":f"/api/quantidade_viagens_origem/{self.param}",
            "pcd_origem":f"/api/pcd_origem/{self.param}",
            "pcd_destino":f"/api/pcd_destino/{self.param}",
            "quantidade_viagens_destino":f"/api/quantidade_viagens_destino/{self.param}",
            "quantidade_viagens_dia_mes":f"/api/quantidade_viagens_dia_mes/{self.param}",
            "alerta_estacao":f"/api/alerta_estacao/{self.param}",
            "quantidade_viagens_origem_destino":f"/api/quantidade_viagens_origem_destino/{self.param}",
            "viagens_dia_semana":f"/api/viagens_dia_semana/{self.param}",
            "duracao_viagens":f"/api/duracao_viagens/{self.param}",
            "pcd_origem":f"/api/pcd_origem/{self.param}"
        }
        
        self.data = asyncio.run(self.backend.fetch_all_data(self.endpoints))
        
    def render(self, navigate_to):
        
        SideBar()
        st.markdown("<h1>Line Page</h1>", unsafe_allow_html=True)
        st.write(f"Current Line: {self.curr_line}")
        self.render_content()
        Footer()
        
        
    def render_content(self):
        data = self.data
        tab1, tab2 = st.tabs(["Gráficos", "Estatísticas"])
        with tab1:
            st.markdown("### Gráficos da Linha")
            st.markdown("#### Duração das Viagens")
            with st.container():
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                if data:
                    df = pd.DataFrame(data["duracao_viagens"]["data"])
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
                if data:
                    df = pd.DataFrame(data["viagens_dia_semana"]["data"])
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
                if data:
                    df = pd.DataFrame(data["quantidade_viagens_origem"]["data"])
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
                if data:
                    df = pd.DataFrame(data["pcd_origem"]["data"])
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
                if data:
                    df = pd.DataFrame(data["pcd_destino"]["data"])
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
                if data:
                    df = pd.DataFrame(data["quantidade_viagens_destino"]["data"])
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
                if data:
                    df = pd.DataFrame(data["quantidade_viagens_dia_mes"]["data"])
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
                if data:
                    df = pd.DataFrame(data["alerta_estacao"]["data"])
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
                if data:
                    df = pd.DataFrame(data["quantidade_viagens_origem_destino"]["data"])
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
            total_viagens = sum([item['quantidade_viagens'] for item in data["viagens_dia_semana"]["data"]]) if data["viagens_dia_semana"]["data"] else 0
            with col1:
                st.metric("Total de Viagens", f"{total_viagens}", "2%")
            duracao_media = (pd.DataFrame(data["duracao_viagens"]["data"])['duracao_real'].mean()) if data["duracao_viagens"]["data"] else 0
            with col2:
                st.metric("Duração Média das Viagens", f"{duracao_media:.2f} minutos", "-1%")
            total_pcds = sum([item['total_pcds'] for item in data["pcd_origem"]["data"]]) if data["pcd_origem"]["data"] else 0
            with col3:
                st.metric("Total de PCDs", f"{total_pcds}", "5%")
        st.markdown('</div>', unsafe_allow_html=True)
