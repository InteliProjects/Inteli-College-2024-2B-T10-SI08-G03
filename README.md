# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="./assets/logo_inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>

</p>

# Gerenciamento e Análise de Big Data

## Equipe Biggie

### Integrantes:
- <a href="https://www.linkedin.com/in/erik-batista-da-silva-455612215/">Erik Batista</a>
- <a href="https://www.linkedin.com/in/freddy-mester-harari-375860279/">Freddy Harari</a>
- <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox</a>
- <a href="https://www.linkedin.com/in/izadoraluz-rsn/">Izadora Luz</a>
- <a href="https://www.linkedin.com/in/kaylanevasconcelos/">Kaylane Vasconcelos</a>
- <a href="https://www.linkedin.com/in/pedrofariasantos/">Pedro Faria</a>
- <a href="https://www.linkedin.com/in/pedrohenrique-oliveira-lima/">Pedro Henrique Oliveira</a>

## 👩‍🏫 Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/renato-penha/">Renato Penha</a>

### Instrutores
- <a href="https://www.linkedin.com/in/anacristinadossantos/">Ana Cristina dos Santos</a>
- <a href="https://www.linkedin.com/in/cristinagramani/">Cristina Gramani</a>
- <a href="https://www.linkedin.com/in/pedroteberga/">Pedro Teberga</a>
- <a href="https://www.linkedin.com/in/francisco-escobar/">Francisco Escobar</a>
- <a href="https://www.linkedin.com/in/afonsolelis/">Afonso Lelis</a>

## 📝 Descrição

&emsp;&emsp;Este projeto busca desenvolver um pipeline de Big Data voltado para a Companhia Paulista de Trens Metropolitanos (CPTM), com o objetivo de otimizar a análise de grandes volumes de dados. Com a criação de uma infraestrutura de Big Data, será possível agilizar e facilitar o processamento de dados administrativos e operacionais da CPTM. Essa solução visa apoiar a tomada de decisões estratégicas e a gestão eficiente dos recursos operacionais.

## 📁 Estrutura de pastas

|--> .github<br>
  &emsp;| --> PULL_REQUEST_TEMPLATE <br>
|--> assets<br>
|--> document<br>
&emsp;| --> apresentacao<br>
&emsp;| --> docs <br>
&emsp;| --> mkdocs.yml <br>
&emsp;| --> poetry.lock <br>
&emsp;| --> pyproject.toml <br> 
|--> src<br>
&emsp;| --> aead <br>
&emsp;| --> app <br>
&emsp;| --> etlbronze <br>
&emsp;| --> etlprata <br>
&emsp;| --> frontend <br>
&emsp;| --> src <br>
&emsp;| --> tests <br>
| README.md<br>

### Descrição das Pastas e Arquivos:

&emsp;&emsp;Aqui está uma breve descrição de cada arquivo e pasta na estrutura fornecida:

#### **📁 .github**
- **PULL_REQUEST_TEMPLATE**: Um modelo para padronizar e orientar a criação de *pull requests* no repositório, garantindo consistência na comunicação e no rastreamento de alterações.

#### **📁 assets**
- Pasta destinada a armazenar recursos estáticos, como imagens, ícones ou outros arquivos multimídia usados no projeto.

#### **📁 document**
- **📁 apresentacao**: Contém arquivos de apresentação final do projeto.
- **📁 docs**: Armazena a documentação do projeto, como pesquisa de *user experience*, pesquisa de negócios e documentação do código do projeto.
- **mkdocs.yml**: Configuração para o MkDocs, uma ferramenta de geração de documentação estática, que define o conteúdo e o tema do site de documentação.
- **poetry.lock**: Arquivo gerado automaticamente pelo Poetry para travar as versões exatas das dependências do projeto.
- **pyproject.toml**: Arquivo de configuração do Poetry que define as dependências e as configurações do projeto Python.

#### **📁 src**
- **📁 aead**: Contém a análise inicial dos dados oferecidos pela CPTM dentro de notebooks.
- **📁 app**: Diretório principal do aplicativo, possivelmente com a lógica central do projeto.
- **📁 etlbronze**: Contém scripts ou módulos para a camada *bronze* de um pipeline ETL (dados brutos, sem transformação significativa).
- **📁 etlprata**: Contém scripts ou módulos para a camada *prata* de um pipeline ETL (dados transformados ou parcialmente estruturados).
- **📁 frontend**: Armazena arquivos relacionados à interface de usuário do projeto utilizando Streamlit.
- **📁 src**: Subdiretório redundante ou adicional para código-fonte
- **📁 tests**: Contém arquivos de teste para validar a funcionalidade do código do projeto.

#### **README.md**
&emsp;&emsp;Presente documento, arquivo principal de documentação no repositório, geralmente usado para descrever o propósito do projeto, instruções de instalação, uso e outros detalhes importantes.

## 🛠️ Instalação e Configuração do Desenvolvimento

&emsp;&emsp;Este guia irá orientá-lo através dos passos necessários para configurar o ambiente de desenvolvimento do projeto **Biggie** desde o início. Certifique-se de seguir cada etapa cuidadosamente para garantir que tudo funcione corretamente.

### 📋 Pré-requisitos

&emsp;&emsp;Antes de começar, verifique se você tem os seguintes softwares instalados em sua máquina:

- **Git**: Para clonar o repositório. [Download Git](https://git-scm.com/downloads)
- **Python 3.12 ou superior**: Linguagem de programação usada no projeto. [Download Python](https://www.python.org/downloads/)
- **Poetry**: Gerenciador de dependências e ambientes virtuais para Python. [Documentação do Poetry](https://python-poetry.org/docs/)
- **Docker**: Plataforma para criar, gerenciar e executar contêineres de software. [Documentação do Docker](https://docs.docker.com/get-docker/)  
- **Docker Compose**: Ferramenta para orquestrar múltiplos contêineres usando arquivos de configuração. [Documentação do Docker Compose](https://docs.docker.com/compose/install/)

### **Como Rodar a Aplicação**

1. **Pré-requisitos**: Certifique-se de ter o todas as aplicações acima instalados.

2. **Execução**:
   - No diretório principal, rode:
     ```bash
     docker compose up
     ```
   - Isso iniciará todos os serviços configurados e criará quatro novos arquivos docker, são eles:

- **docker-compose.yml**: Define os serviços (API, ETL e Frontend), suas interações, redes e volumes. É usado pelo `docker compose up` para orquestrar os contêineres.

- **Dockerfile.api**: Configura o contêiner da API, instalando dependências e iniciando o servidor.

- **Dockerfile.etl**: Configura o contêiner para os pipelines ETL.

- **Dockerfile.frontend**: Define o contêiner para o frontend, incluindo a construção e o serviço dos arquivos estáticos.

### **Comandos Úteis**

- Parar e remover serviços:
  ```bash
  docker compose down
  ```
- Ver logs:
  ```bash
  docker compose logs
  ```

## 📆 Conteúdo do módulo

1. Sprint 1
    - Visualização de Dados em Big Data
    - Setup de Máquina, Processos para o Módulo, Documentação com MKDocs e Data Model Canvas com Metabase
    - Análise Exploratória Avançada dos Dados com Jupyter - Poetry E criação de Data Lake
    - Inteligência de mercado
    - Arquitetura de Dados com UML de Componentes (Arquitetura Medalhão) E Precificação

2. Sprint 2
    - Análise da concorrência
    - Dataviz, Infográficos e Integração de Dados
    - Centróides e Clusters: Explorando Padrões com Agrupamento de Dados
    - ETL de Transformação Object Storage para Data Warehouse (Raw ou Bronze)
    - Datawarehouses (Working ou Prata)

3. Sprint 3
    - Cubo de Dados e DataMarts (Gold ou Trusted)
    - Inferência Estatística: Teste de Hipóteses
    - Automatização com Prefect
    - Modelos Preditivos - Regressão e Classificação (modelos supervisionados)
    - Pacote DataApp com Arquitetura em Camadas (Views, ETLs e Processadores)
    - Hábitos e usos do consumidor
  
4. Sprint 4
    - Testes Automatizados em Python
    - Gestão do conhecimento como vantagem competitiva nas equipes
    - Tecnologia Persuasiva no Capitalismo de Vigilância: Desafios e Soluções de Design Ético
    - Métricas e Telemetria
    - Economia da inovação (ciclos econômicos, destruição criativa, curva da adoção da inovação)

5. Sprint 5
    - Segurança, Autorizações e Acessos de Dados (LGPD aplicada)
    - Inovação incremental, radical e disruptiva
    - Precificação em Infraestrutura de Nuvem
    - Networking

## Vídeo da aplicação
&emsp;&emsp;O link abaixo está direcionado para o vídeo do DataAPP, postado no Youtube.

- [Vídeo da Aplicação](https://youtu.be/caL4pM0j1pE)

&emsp;&emsp; Demonstra o funcionamento do DataAPP, evidenciando o login, tela de home e telas das diferentes linhas.

## 🗃 Histórico de lançamentos
* 0.1.0 - 27/10/2024
    * TAM, SAM, SOM
    * Canvas Proposta de Valor
    * Matriz de Risco
    * Personas
    * User Storys
    * Mapa de Jornada do Usuário
    * Data Model Canvas
        * Proposta de Valor
        * Estrutura dos Dados
        * Perfil dos Usuários
        * Análise dos Dados
        * Casos de Uso
        * Métricas de Sucesso

* 0.2.0 - 08/11/2024
    * Wireframe
    * Tabela 1 - viagens
    * Tabela 2 - tabela pcd
    * Tabela 3 - intervalos
    * Criação do Metodo de Log
    * Documentação das tabelas 
    * Documentação do ETL.
    * Modelagem UML
    * Criação do README. 

* 0.3.0 - 22/11/2024
    * Optimização do código do ETL
    * API para automatização do ETL
    * Documentação da API
    * Analise de Impacto Ético
    * Cubo de Dados automatizado
    * Documentação do Cubo de Dados

* 0.4.0 - 08/12/2024 
    * Dockerização inicial da solução.
    * Nova etapa de dockerização para ajustes e melhorias.
    * Documentação completa da dockerização, incluindo passos para replicação e manutenção.
    * Desenvolvimento do backend para a página de linhas da aplicação.
    * Implementação geral do backend da aplicação, garantindo integração com os demais componentes.
    * Revisão e correção das views para alinhamento com as funcionalidades do backend.
    * Criação de views, com foco nas seguintes telas:
      * Tela Principal (Desktop).
      * Tela de Linha (Desktop).
    * Atualização das views com novos gráficos definidos no projeto.
    * Definição dos gráficos utilizados no projeto.
    * Validação e escolha final dos gráficos, considerando os requisitos de usabilidade e dados disponíveis.
    * Introdução da documentação do infográfico no **DataAPP**:
      * Documentação da criação dos infográficos.
      * Metodologia detalhada de definição dos gráficos.
      * Documentação da coleta automática de dados.
    * Conclusão da documentação do infográfico no **DataAPP**.
    * Criação de modelos para testes unitários.
    * Projeções de custos.
    * Projeções de investimento.
    * Cálculo do ROI.
    * Desenvolvimento do plano de comunicação:

* 1.0.0: Entrega Final - 17/12/2024
    * Refatoração da integração para otimização.
    * Melhoria da estrutura do frontend.
    * Modularização da API de consulta.
    * Otimização de consultas no sistema.
    * Implementação do infográfico no frontend.
    * Aplicação de filtros em todos os gráficos no frontend.
    * Exportação de dados em CSV.
    * Modularização da API e adição de filtros em gráficos no backend.
    * Conclusão do pipeline completo de dados na AWS.
    * Implementação da arquitetura final da solução.
    * Cobertura de testes ampliada.
    * Documentação dos filtros e do login.
    * Garantia de alinhamento com os padrões do escritório de projetos.

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M6T4-Inteli">Implantação de sistema de gestão empresarial</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/InteliProjects">Inteli</a>, <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/Inteli-College/2024-2A-T10-SI07-G05">Biggie</a>: <a href="https://www.linkedin.com/in/erik-batista-da-silva-455612215/">  Erik Batista</a>, <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox</a>, <a href="https://www.linkedin.com/in/freddy-mester-harari-375860279/">Freddy Harari</a>, <a href="https://www.linkedin.com/in/izadoraluz-rsn/">Izadora Luz</a>, <a href="https://www.linkedin.com/in/kaylanevasconcelos/">Kaylane Vasconcelos</a>, <a href="https://www.linkedin.com/in/pedrofariasantos/">Pedro Faria</a>, <a href="https://www.linkedin.com/in/pedrohenrique-oliveira-lima/">Pedro Henrique Oliveira</a>
is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## Referências

BRASIL. Novo PAC garante recursos para fortalecer transporte ferroviário no Brasil. *Agência Brasil*, 2024. Disponível em: [https://agenciagov.ebc.com.br/noticias/202401/novo-pac-garante-recursos-para-o-transporte-ferroviario-e-acelera-retomada-do-setor-no-brasil](https://agenciagov.ebc.com.br/noticias/202401/novo-pac-garante-recursos-para-o-transporte-ferroviario-e-acelera-retomada-do-setor-no-brasil). Acesso em: 23 out. 2024.
  
ASSOCIAÇÃO NACIONAL DOS TRANSPORTES FERROVIÁRIOS (ANTF). Mapa ferroviário. Disponível em: [https://www.antf.org.br/mapa-ferroviario/](https://www.antf.org.br/mapa-ferroviario/). Acesso em: 23 out. 2024.

RUMO LOGÍSTICA. Nossos negócios: Transporte ferroviário. Disponível em: [https://www.rumolog.com/nossos-negocios/transporte-ferroviario/](https://www.rumolog.com/nossos-negocios/transporte-ferroviario/). Acesso em: 23 out. 2024.

ASSOCIAÇÃO NACIONAL DOS TRANSPORTES FERROVIÁRIOS (ANTF). Associadas. Disponível em: [https://www.antf.org.br/associadas/](https://www.antf.org.br/associadas/). Acesso em: 23 out. 2024.

BRASIL. Novo PAC garante recursos para fortalecer transporte ferroviário no Brasil. Agência Brasil. Disponível em: https://agenciagov.ebc.com.br/noticias/202401/novo-pac-garante-recursos-para-o-transporte-ferroviario-e-acelera-retomada-do-setor-no-brasil. Acesso em: 24 out. 2024.

FGV. O transporte ferroviário no Brasil: desafios e oportunidades. Disponível em: https://repositorio.fgv.br/server/api/core/bitstreams/84b5cead-f541-4e1e-8ac7-982a4228a082/content. Acesso em: 24 out. 2024.

BRASIL ESCOLA. Transporte ferroviário brasileiro. Disponível em: https://brasilescola.uol.com.br/brasil/transporte-ferroviario-brasileiro.htm. Acesso em: 24 out. 2024.

G4 Educação. Significado de Serviceable Obtainable Market (SOM). Disponível em: https://g4educacao.com/glossario/significado-serviceable-obtainable-market-som . Acesso em: 24 out. 2024.

HubSpot. TAM, SAM e SOM: o que são e como calcular. Disponível em: https://blog.hubspot.com/marketing/tam-sam-som?uuid=285466bb-04e0-443f-9848-6e12b58b3831 . Acesso em: 24 out. 2024.

RD Station. Persona: o que é e como criar uma. Disponível em: https://www.rdstation.com/blog/marketing/persona-o-que-e/. Acesso em: 23 out. 2024.

CARVALHO, L. Data Product Canvas — Uma estrutura prática para construir produtos de dados de alto desempenho. 2022. Disponível em: <https://medium.com/@leandroscarvalho/data-product-canvas-a-practical-framework-for-building-high-performance-data-products-7a1717f79f0>. Acesso em: 24 out. 2024.

Wireframes, o que são e por que os utilizamos? Disponível em: <https://www.organicadigital.com/blog/o-que-sao-wireframes-e-por-que-os-utilizamos/>. Acesso em: 31 out. 2024.

MINIO. Documentação do MinIO. Disponível em: https://min.io/docs/minio/linux/index.html. Acesso em: 5 nov. 2024.

JUPYTER. Documentação do Jupyter Notebook. Disponível em: https://jupyter.org/documentation. Acesso em: 5 nov. 2024.

AMAZON WEB SERVICES. AWS Lambda Documentation. Disponível em: https://docs.aws.amazon.com/lambda. Acesso em: 5 nov. 2024.

CLICKHOUSE. Clickhouse Documentation. Disponível em: https://clickhouse.com/docs/en/. Acesso em: 5 nov. 2024.

DOCKER. Docker Documentation. Disponível em: https://docs.docker.com/. Acesso em: 5 nov. 2024.

STREAMLIT. Streamlit Documentation. Disponível em: https://docs.streamlit.io/. Acesso em: 5 nov. 2024.

KHORASANI, M. Streamlit Authenticator. Disponível em: https://github.com/mkhorasani/Streamlit-Authenticator. Acesso em: 5 nov. 2024.

O Que É ETL: Entenda Como Funcionam Os Processos | Blog U. Disponível em: <https://ucommerce.com.br/o-que-e-etl/>. Acesso em: 6 nov. 2024.

‌ETL: o que é, importância e como aplicar na sua estratégia BI. Disponível em: <https://www.fiveacts.com.br/etl>. Acesso em: 6 nov. 2024.

MICROSOFT SUPPORT. Visão geral do OLAP (Processamento Analítico Online). Disponível em: <https://support.microsoft.com/pt-br/office/vis%C3%A3o-geral-do-olap-processamento-anal%C3%ADtico-online-15d2cdde-f70b-4277-b009-ed732b75fdd6>. Acesso em: 12 nov. 2024.


LGPD: Lei Geral de Proteção de Dados. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em 13 nov. 2024.

Nações Unidas Brasil. (2015). Transformando Nosso Mundo: A Agenda 2030 para o Desenvolvimento Sustentável. Disponível em: <https://brasil.un.org/pt-br/sdgs>. Acesso em: 14 nov. 2024.

Programa das Nações Unidas para o Desenvolvimento (PNUD). (2021). ODS 9: Indústria, inovação e infraestrutura. Disponível em: <https://www.undp.org/pt/sustainable-development-goals/goal-9-industry-innovation-and-infrastructure>. Acesso em: 14 nov. 2024.

Ethical data usage in an era of digital technology and regulation. Disponível em: <https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-forward/ethical-data-usage-in-an-era-of-digital-technology-and-regulation>. Acesso em: 14 nov. 2024.

‌BARHAM, B., et al. *Modern Data Workflows with Prefect*. O'Reilly Media, 2021.

Prefect Documentation. Disponível em: [https://docs.prefect.io/](https://docs.prefect.io/). Acesso em: 13 nov. 2024.

UOL. *Cotações: Câmbio*. Disponível em: <https://economia.uol.com.br/cotacoes/cambio/>. Acesso em: 2 dez. 2024.

AMAZON WEB SERVICES. AWS Pricing Calculator. Disponível em: <https://calculator.aws/#/estimate?id=8d7f973f4217c75db48e74a413b106244db3aaca>. Acesso em: 2 dez. 2024.

Lucidchart. *O plano de comunicação de gestão de projetos*. 2024. Disponível em: [https://www.lucidchart.com](https://www.lucidchart.com). Acesso em: 03 dez. 2024.

UOL Economia. Câmbio. Disponível em: https://economia.uol.com.br/cotacoes/cambio/. Acesso em: 2 dez. 2024.

Gupy Blog. Junior, pleno e sênior: entenda as diferenças entre esses níveis hierárquicos. Disponível em: https://www.gupy.io/blog/junior-pleno-senior#:~:text=Júnior%20é%20uma%20pessoa%20recém,liderança%20de%20equipes%20e%20projetos. Acesso em: 2 dez. 2024.

G1 Tecnologia. Cientista e engenheiro de dados estão em alta e têm salário que pode passar de R$ 20 mil; veja como entrar. Disponível em: https://g1.globo.com/tecnologia/noticia/2024/04/07/cientista-e-engenheiro-de-dados-estao-em-alta-e-tem-salario-que-pode-passar-de-r-20-mil-veja-como-entrar.ghtml. Acesso em: 2 dez. 2024.

Ozai. Custo de contratação: quais fatores considerar ao contratar?. Disponível em: https://www.ozai.com.br/custo-de-contratacao/. Acesso em: 2 dez. 2024.

Glassdoor Brasil. Analista de dados pleno: salário. Disponível em: https://www.glassdoor.com.br/Sal%C3%A1rios/analista-de-dados-pleno-sal%C3%A1rio-SRCH_KO0,23.htm. Acesso em: 2 dez. 2024.

Talent.com Brasil. Desenvolvedor back pleno: salário. Disponível em: https://br.talent.com/salary?job=desenvolvedor+back+pleno. Acesso em: 2 dez. 2024.

Glassdoor Brasil. Pleno front-end developer: salário. Disponível em: https://www.glassdoor.com.br/Sal%C3%A1rios/pleno-front-end-developer-sal%C3%A1rio-SRCH_KO0,25.htm. Acesso em: 2 dez. 2024.

Glassdoor Brasil. Salário mensal de Engenheiro da empresa Companhia Paulista de Trens Metropolitanos (CPTM). Disponível em: https://www.glassdoor.com.br/Pagamento-mensal/Companhia-Paulista-de-Trens-Metropolitanos-CPTM-Engenheiro-Pagamento-mensal-E2482741_D_KO48,58.htm. Acesso em: 5 dez. 2024.

Metrô CPTM. CPTM investirá R$ 450 milhões na manutenção da via permanente de suas cinco linhas. Disponível em: https://www.metrocptm.com.br/cptm-investira-r-450-milhoes-na-manutencao-da-via-permanente-de-suas-cinco-linhas/. Acesso em: 5 dez. 2024.
