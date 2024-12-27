import streamlit as st
import asyncio
from Components.Header import Header
from Components.Footer import Footer
from Components.SideBar import SideBar
from styles.Global import GlobalStyle
import plotly.express as px
import pandas as pd
from dotenv import load_dotenv
import os
from services.RequestToBackend import BackendService
from datetime import datetime


class HomePage:
    def __init__(self):
        self.header = Header("Biggie Dashboard")
        self.endpoints = {
            "qtd_viagens_por_linha": "/api/qtd_viagens_por_linha",
            "qtd_viagens_semana_linha": "/api/qtd_viagens_semana_linha",
            "taxa_atraso": "/api/taxa_atraso",
            "duracao_media": "/api/duracao_media",
            "duracao_real_programada": "/api/duracao_real_programada",
            "viagens_por_dia_mes": "/api/viagens_por_dia_mes",
            "alertas_pcd_por_linha": "/api/alertas_pcd_por_linha",
            "qtd_pcd_por_dia": "/api/qtd_pcd_por_dia",
            "qtd_pcd_semana_linha": "/api/qtd_pcd_semana_linha"
        }
        
        self.backend = BackendService()
        self.data = asyncio.run(self.backend.fetch_all_data(self.endpoints))


    def render(self):
        SideBar()
        GlobalStyle()
        self.render_content()
        Footer()

    def render_content(self):
        st.markdown('<h1 class="biggie-text">BIGGIE</h1>', unsafe_allow_html=True)
        st.markdown('<div class="content-area">', unsafe_allow_html=True)
        st.markdown("## Dashboards e Métricas Gerais")

        # Fetch data concurrently
        
        data = self.data
        tab1, tab2 = st.tabs(["Gráficos", "Estatísticas"])

        with tab1:
            st.markdown("### Gráficos de Viagens")
            col1, col2 = st.columns(2)

            # Total de Viagens por Linha
            with col1:
                st.markdown("#### Total de viagens por linha")
                # Filtros de data acima do gráfico
                with st.container():
                    filter_col1, filter_col2 = st.columns(2)
                    init_date_viagens = filter_col1.date_input("Data Inicial", key="init_date_viagens", value="2023-01-20")
                    final_date_viagens = filter_col2.date_input("Data Final", key="final_date_viagens", value="2023-12-20")

                # Constrói a URL da API com os parâmetros de filtro
                url_viagens = "/api/qtd_viagens_por_linha"
                params_viagens = []
                if init_date_viagens:
                    params_viagens.append(f"init_date={init_date_viagens}")
                if final_date_viagens:
                    params_viagens.append(f"final_date={final_date_viagens}")

                if params_viagens:
                    url_viagens += "?" + "&".join(params_viagens)

                # Busca os dados com os filtros aplicados
                viagens_data = self.backend.get_data_from_backend(url_viagens)

                if viagens_data:
                    df = pd.DataFrame(viagens_data)
                    df = df.sort_values('total_travels', ascending=False)
                    fig = px.bar(
                        df,
                        x='line',
                        y='total_travels',
                        labels={'line': 'Linha', 'total_travels': 'Total de Viagens'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível para o filtro.")

            # Quantidade de Viagens por Dia da Semana por Linha
            with col2:
                st.markdown("#### Quantidade de viagens por dia da semana")
                if data["qtd_viagens_semana_linha"]["data"]:
                    df = pd.DataFrame(data["qtd_viagens_semana_linha"]["data"])
                    fig = px.bar(df, x='dia_semana_nome', y='quantidade_viagens', color='linha',
                                 labels={'dia_semana_nome': 'Dia da Semana', 'quantidade_viagens': 'Quantidade de Viagens', 'linha': 'Linha'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")

            st.markdown("### Gráficos de Atrasos e Duração")
            col3, col4 = st.columns(2)

            # Taxa de Atraso por Linha
            with col3:
                st.markdown("#### Taxa de atraso por linha")
                if data["taxa_atraso"]["data"]:
                    df = pd.DataFrame(data["taxa_atraso"]["data"])
                    df['taxa_atraso_percentual'] = df['taxa_atraso'] * 100
                    fig = px.bar(df, x='linha', y=['viagens_atrasadas', 'total_viagens'], barmode='group',
                                 labels={'value': 'Quantidade', 'variable': 'Tipo', 'linha': 'Linha'})
                    fig.add_scatter(x=df['linha'], y=df['taxa_atraso_percentual'], mode='lines+markers', name='Taxa de Atraso (%)')
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")

            # Duração Média de Viagem por Linha
            with col4:
                st.markdown("#### Duração Média de Viagem por Linha")
                # Filtros de data acima do gráfico
                with st.container():
                    filter_col1, filter_col2 = st.columns(2)
                    init_date_duracao = filter_col1.date_input("Data Inicial", key="init_date_duracao", value="2023-01-20")
                    final_date_duracao = filter_col2.date_input("Data Final", key="final_date_duracao", value="2023-12-20")

                # Constrói a URL da API com os parâmetros de filtro
                url_duracao = "/api/duracao_media"
                params_duracao = []
                if init_date_duracao:
                    params_duracao.append(f"init_date={init_date_duracao}")
                if final_date_duracao:
                    params_duracao.append(f"final_date={final_date_duracao}")

                if params_duracao:
                    url_duracao += "?" + "&".join(params_duracao)

                # Busca os dados com os filtros aplicados
                duracao_data = self.backend.get_data_from_backend(url_duracao)

                if duracao_data:
                    df = pd.DataFrame(duracao_data)
                    df['duracao_media'] = df['duracao_media'].astype(float)
                    fig = px.bar(
                        df,
                        x='linha',
                        y='duracao_media',
                        labels={'linha': 'Linha', 'duracao_media': 'Duração Média (minutos)'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível para o filtro.")
                    
            # Duração Real x Program
            col5, col6 = st.columns(2)
            with col5:
                st.markdown("#### Duração Real x Programada")
                if data["duracao_real_programada"]["data"]:
                    df = pd.DataFrame(data["duracao_real_programada"]["data"])
                    fig = px.scatter(df, x='duracao_programada', y='duracao_real', color='linha',
                                     labels={'duracao_programada': 'Duração Programada', 'duracao_real': 'Duração Real', 'linha': 'Linha'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")
                    
            # Viagens por Dia do Mês
            with col6:
                st.markdown("#### Viagens por dia do mês")
                if data["viagens_por_dia_mes"]["data"]:
                    df = pd.DataFrame(data["viagens_por_dia_mes"]["data"])
                    fig = px.bar(df, x='dia_mes', y='quantidade_viagens', labels={'dia_mes': 'Dia do Mês', 'quantidade_viagens': 'Quantidade de Viagens'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")
                    
            # Alertas PCD por Linha
            col7, col8 = st.columns(2)
            with col7:
                st.markdown("#### Alertas PCD por linha")
                if data["alertas_pcd_por_linha"]["data"]:
                    df = pd.DataFrame(data["alertas_pcd_por_linha"]["data"])
                    fig = px.bar(df, x='linha', y='total_alertas', labels={'linha': 'Linha', 'total_alertas': 'Quantidade de Alertas'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")
                    
            # Quantidade de PCDs por Dia
            with col8:
                st.markdown("### Quantidade de PCDs por dia")
                if data["qtd_pcd_por_dia"]["data"]:
                    df = pd.DataFrame(data["qtd_pcd_por_dia"]["data"])
                    fig = px.bar(df, x='dia_semana_nome', y='total_pcds', labels={'dia_semana_nome': 'Dia', 'total_pcds': 'Quantidade de PCDs'})
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.write("Nenhum dado disponível.")
                    
            # Quantidade de PCDs por Semana por Linha
            
                

        with tab2:
            st.markdown("### Estatísticas Gerais")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total de Viagens", "X", "Y%")
            with col2:
                st.metric("Média de Atrasos", "X min", "Y%")
            with col3:
                st.metric("Total de PCDs", "X", "Y%")
            with col4:
                st.metric("Receita Mensal", "R$ X", "Y%")

        st.markdown('</div>', unsafe_allow_html=True)
