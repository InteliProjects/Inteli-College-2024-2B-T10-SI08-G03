# 1. Análise do Usuário Final

&emsp;&emsp; Esta seção tem como objetivo fornecer uma visão abrangente sobre o usuário final do data app projetado. Com isso, serão definidas as principais funções do sistema e as estratégias para que a equipe alcance esses objetivos. Para isso, diversas ferramentas serão utilizadas, e a adoção dessas ferramentas de UX é essencial. Elas possibilitam que o processo de design seja guiado por uma compreensão profunda do comportamento, expectativas e desafios enfrentados pelos usuários, resultando em soluções mais eficazes e satisfatórias.

&emsp;&emsp; Três ferramentas principais serão abordadas: Persona, que fornece uma representação semi-fictícia do usuário típico, permitindo à equipe visualizar e antecipar melhor suas necessidades; Mapa de Jornada do Usuário, que mapeia as interações do usuário com a aplicação, ajudando a identificar pontos de atrito e oportunidades de melhoria; e User Stories, que são descrições curtas e objetivas das intenções e necessidades dos usuários, orientando a equipe a priorizar funcionalidades de acordo com o valor percebido pelo usuário. Essas ferramentas, portanto, não só guiam o desenvolvimento da solução, mas também garantem que cada etapa seja fundamentada em um entendimento sólido do usuário, contribuindo para um produto final mais assertivo e alinhado às expectativas dos clientes.

## 1.1 Personas

&emsp;&emsp;No contexto de projetos que possuem o design centrado no usuário, a Persona [(André Siqueira, 23 out. 2024)](https://www.rdstation.com/blog/marketing/persona-o-que-e/) é uma representação fictícia, mas realista, de um grupo de usuários com características, necessidades e comportamentos semelhantes. Elas são criadas com base em dados reais, como entrevistas, pesquisas e análises, e ajudam a traduzir perfis abstratos em figuras compreensíveis e tangíveis.

&emsp;&emsp;O uso de personas é essencial para garantir que as decisões estratégicas do projeto considerem os interesses e desafios dos usuários finais. Elas orientam a definição de prioridades e escopo, ajudam a identificar pontos de dor e oportunidades de inovação, e garantem que soluções não sejam desenvolvidas com base em suposições. No contexto de um projeto de Big Data, personas são ainda mais úteis para personalizar insights e adaptar as análises às necessidades específicas de cada segmento, maximizando o valor gerado para o cliente e para os usuários.

### 1.1.1 Pesquisa e Coleta de Dados

&emsp;&emsp;A construção da persona foi baseada em um processo que envolveu pesquisa e análise. O objetivo era desenvolver uma personagem fictícia, mas realista, para representar um profissional típico do setor metroferroviário, alinhado aos desafios de gestão operacional e inovação em transporte público. A seguir, está o processo de criação dessa persona:

- **Pesquisa em Perfis Reais do LinkedIn:**
O primeiro passo foi a análise de perfis profissionais autênticos na plataforma [LinkedIn](https://www.linkedin.com/). A escolha de um perfil específico de um profissional com ampla experiência no setor ferroviário, como o da CPTM (Companhia Paulista de Trens Metropolitanos), forneceu uma base de competências, responsabilidades e formações frequentemente encontradas em cargos estratégicos desse setor. A observação das trajetórias profissionais reais garantiu que a persona refletisse características relevantes e coerentes com o mercado atual.

- **Extração de Padrões e Competências Comuns:**
Com base na pesquisa, identificamos informações essenciais, como a formação em Engenharia Elétrica, Gestão de Operações e Planejamento de Manutenção, além do uso de tecnologia para melhorar processos. Isso foi essencial para criar uma narrativa autêntica, que representasse as demandas e desafios enfrentados por profissionais na indústria metroferroviária.

- **Construção da Persona Fictícia:**
A persona foi desenhada para ser uma representação idealizada de um Gerente de Operações, com o nome fictício Ricardo Oliveira. Também foi dada atenção a desejos e frustrações que fazem parte do cotidiano desses profissionais, como a busca por eficiência e falta de uma ferramenta de monitoramento.

&emsp;&emsp;Além desse processo de pesquisa, foram utilizadas informações retiradas a partir da entrevista com o cliente, visando complementar a criação da persona e torná-la ainda mais consistente. Tendo em vista que que muitas pessoas serão beneficiadas, o foco foi criar uma persona que fosse o mais parecida possível com o usuário final da ferramenta, dando atenção a quem de fato vai utilizar a ferramenta em seu dia a dia.


### 1.1.2 Persona - Ricardo Oliveira

<div align="center">
<p><b>Figura 1</b> - Foto de Ricardo Oliveira</p>
  <img src="https://res.cloudinary.com/djeve32p7/image/upload/v1729817600/Documentacao_persona_3_p9xzrc.png" alt="Foto de Ricardo Oliveira">
  <p><b>Fonte:</b> elaborado pela equipe Biggie.</p>
</div>


### 1.1.3 Conclusão

&emsp;&emsp;A definição e uso contínuo de personas é uma prática essencial para manter o foco nas necessidades do usuário ao longo do ciclo de vida do projeto. Em iniciativas de Big Data, o uso de personas não apenas facilita a segmentação e interpretação dos dados, mas também alinha as decisões estratégicas com as expectativas dos stakeholders.

&emsp;&emsp;Neste projeto específico, a aplicação de personas irá contribuir para definir quais tipos de análises são mais relevantes, como os dados devem ser tratados e apresentados, e quais ações podem ser tomadas com base nos insights obtidos. Assim, ao longo de toda a jornada, o uso de personas permitirá um desenvolvimento mais eficiente e orientado a resultados, garantindo que a solução entregue agregue valor real e seja centrada no usuário.

## 1.2 Mapa de Jornada do Usuário

&emsp;&emsp;Uma jornada do usuário é uma representação visual ou descritiva das etapas que um usuário percorre ao interagir com um sistema, serviço ou produto. Ela busca mapear as ações, sentimentos, dificuldades e oportunidades de melhoria ao longo dessa interação. Através da jornada do usuário, é possível entender melhor as necessidades, motivações e pontos de dor do usuário, permitindo que a experiência seja otimizada e o produto final atenda às expectativas do público-alvo. Segundo a definição de Goodman et al., "as jornadas do usuário ajudam a identificar os momentos-chave em que os usuários podem ter dificuldades ou precisam de mais suporte, permitindo às equipes de design ajustar suas soluções para atender melhor essas necessidades" (Goodman, M., Kuniavsky, M., Moed, A. Observing the User Experience: A Practitioner's Guide to User Research, 2012).

&emsp;&emsp;No contexto deste projeto, está sendo desenvolvido um pipeline de Big Data para a CPTM (Companhia Paulista de Trens Metropolitanos), com o objetivo de facilitar a análise de grandes volumes de dados e auxiliar na tomada de decisões operacionais. A jornada aqui descrita se concentra na experiência do Ricardo, um especialista em operações, ao interagir com o sistema proposto.

&emsp;&emsp;
A seguir, apresentamos a jornada do usuário, detalhando os passos, sentimentos (positivos e negativos), pontos de dor e oportunidades em cada uma das fases de interação com o pipeline de Big Data.

<br>
<div align="center">
<sub>Figura 2 - Mapa da Jornada do Usuário</sub>
<img src="./assets/UserJourney.png" width="100%" >
<sup>Fonte: Material produzido pelos autores (2024)</sup>
</div>
<br>

### Fase 1: Recebimento dos dados operacionais e identificação de padrões críticos

**Passos**
- Receber os dados operacionais da CPTM, incluindo métricas de desempenho.
- Avaliar os principais indicadores que precisam de monitoramento e análise.
- Identificar padrões críticos nos dados que podem impactar as operações.

**Sentimentos Positivos**
- **Confiança:** Ricardo se sente confortável analisando dados operacionais devido à sua vasta experiência.
- **Responsabilidade:** Ele sabe que os dados são fundamentais para otimizar as operações da CPTM.

**Sentimentos Negativos**
- **Preocupação:** Ele teme que os dados possam estar incompletos ou desatualizados.

**Pontos de dor**
- Integração limitada entre sistemas operacionais e o pipeline de Big Data.
- Dados fragmentados ou em diferentes formatos dificultam a análise.

**Oportunidades**
- **Automação da coleta de dados:** Implementar processos automatizados para garantir que os dados sejam coletados continuamente e sem falhas.
- **Padronização dos dados operacionais:** Criar uma estrutura que permita a integração de dados de diferentes sistemas em um formato comum.

### Fase 2: Configuração do sistema de ingestão de dados

**Passos**
- Trabalhar com a equipe técnica para configurar o sistema de ingestão de dados em batch e streaming.
- Verificar se os dados operacionais estão corretamente inseridos no Data Lake da AWS.

**Sentimentos Positivos**
- **Satisfação:** Ricardo sente-se satisfeito ao ver que os dados são ingeridos corretamente no sistema.
- **Foco:** Ele entende a importância de configurar tudo corretamente para garantir o sucesso do pipeline.

**Sentimentos Negativos**
- **Cautela:** Preocupação com falhas na ingestão de grandes volumes de dados.

**Pontos de dor**
- Falta de compatibilidade entre os sistemas antigos e o novo pipeline de Big Data.
- Processos manuais para a ingestão de dados de alguns sistemas antigos.

**Oportunidades**
- **Automação de verificações de erros:** Criar alertas automáticos para identificar falhas na ingestão de dados.
- **Padronização e integração contínua:** Garantir que os dados de diferentes fontes sejam padronizados para que a ingestão ocorra sem dificuldades.

### Fase 3: Validação e processamento dos dados

**Passos**
- Validar os dados no pipeline de Big Data, garantindo que estão sendo processados corretamente.
- Executar análises estatísticas preliminares para garantir que os insights esperados estão sendo gerados.

**Sentimentos Positivos**
- **Alívio:** O usuário se sente aliviado ao ver que o pipeline está processando os dados corretamente.
- **Satisfação:** Ele fica satisfeito ao ver os primeiros insights gerados pelos dados operacionais.

**Sentimentos Negativos**
- **Insegurança:** Preocupação se o sistema será capaz de lidar com volumes maiores de dados no futuro.
- **Dúvida:** O usuário questiona se todos os dados estão sendo processados corretamente ou se há perdas no caminho.

**Pontos de dor**
- Lentidão no processamento ao lidar com grandes volumes de dados.
- Ferramentas de análise podem não gerar insights claros ou acionáveis.

**Oportunidades**
- **Escalabilidade:** Implementar soluções que garantam a escalabilidade do pipeline para lidar com o crescimento dos volumes de dados.
- **Otimização do processamento:** Ajustar ferramentas e processos para melhorar o desempenho e velocidade do processamento de grandes volumes de dados.

### Fase 4: Monitoramento e geração de insights operacionais

**Passos**
- Monitorar o desempenho do pipeline de Big Data para garantir que ele esteja gerando insights operacionais úteis.
- Usar ferramentas de visualização, como o AWS QuickSight, para criar dashboards e relatórios visuais dos dados operacionais.

**Sentimentos Positivos**
- **Orgulho:** Satisfação ao ver os dados operacionais visualizados claramente em relatórios.
- **Segurança:** O monitoramento em tempo real oferece a Roberto uma visão clara das operações da CPTM.

**Sentimentos Negativos**
- **Alerta:** Preocupação constante com a precisão dos dados mostrados nos dashboards.

**Pontos de dor**
- Dados desatualizados ou imprecisos podem gerar relatórios equivocados.
- O tempo para atualizar os dashboards pode ser longo, afetando a eficiência.

**Oportunidades**
- **Atualizações automáticas em tempo real:** Configurar dashboards para atualizações automáticas, garantindo que as informações estejam sempre atualizadas.
- **Relatórios customizados:** Criar opções de relatórios customizados que atendam melhor às necessidades operacionais específicas da CPTM.

### Fase 5: Refinamento e ajuste do pipeline

**Passos**
- Revisar o pipeline de Big Data com a equipe técnica, realizando ajustes e refinamentos com base no feedback da equipe operacional.
- Implementar melhorias no pipeline para otimizar o desempenho e gerar resultados mais precisos.

**Sentimentos Positivos**
- **Orgulho:** O usuário se sente orgulhoso ao ver os resultados das melhorias no pipeline.
- **Confiança:** Ele está mais seguro com o desempenho do pipeline, sabendo que ele foi ajustado para atender às necessidades operacionais.

**Sentimentos Negativos**
- **Cansaço:** A necessidade constante de ajustes e refinamentos pode ser cansativa.

**Pontos de dor**
- Ajustes contínuos podem ser demorados e exigir reconfiguração de várias partes do pipeline.
- Falta de coordenação entre equipes pode atrasar os refinamentos necessários.

**Oportunidades**
- **Ciclo contínuo de melhorias:** Estabelecer um processo formal de feedback e refinamento contínuo, baseado em resultados operacionais.
- **Colaboração interdepartamental eficiente:** Melhorar a comunicação entre as equipes técnica e operacional para garantir que os ajustes sejam realizados de maneira mais ágil e coordenada.

&emsp;&emsp;A jornada do usuário do Ricardo, especialista em operações da CPTM, oferece insights valiosos sobre como ele interage com o pipeline de Big Data, desde o recebimento e ingestão dos dados operacionais até o refinamento e ajustes do sistema. Cada fase dessa jornada mapeia as ações e os desafios que Roberto enfrenta, permitindo uma visão clara das suas necessidades técnicas e dos pontos críticos do sistema.

&emsp;&emsp;Essa jornada será extremamente útil para o projeto da CPTM, pois revela os momentos específicos onde o sistema pode ser otimizado para melhorar a eficiência operacional. Por exemplo, na Fase 2, a integração com sistemas legados é um ponto de dor significativo, onde a automação de processos de ingestão de dados poderia economizar tempo e reduzir erros humanos. Implementar verificações automáticas para erros de ingestão e padronizar os formatos de dados de diferentes fontes é uma oportunidade de melhoria que pode impactar diretamente a fluidez do pipeline.

&emsp;&emsp;Portanto, essa jornada detalhada não apenas orienta as melhorias técnicas do sistema, mas também garante que o pipeline de Big Data atenda diretamente aos desafios operacionais, proporcionando uma solução eficaz que impacta positivamente a gestão dos dados e a tomada de decisões da CPTM.

## 1.3 User Stories

&emsp;&emsp; A documentação das User Stories deste projeto visa detalhar as funcionalidades e necessidades específicas para o desenvolvimento de soluções de monitoramento e análise de dados no ambiente operacional da CPTM. O objetivo é assegurar que as demandas da Diretoria de Operação e Manutenção sejam atendidas de forma eficiente e integrada, permitindo acesso em tempo real a dados críticos, realização de análises estatísticas e visualização de insights em formatos acessíveis e intuitivos. Além disso, o projeto contempla a ingestão de grandes volumes de dados não estruturados e a consulta ao Data Lake, garantindo que todas as informações necessárias estejam disponíveis para otimizar processos e tomadas de decisão estratégicas. As User Stories foram priorizadas com base no impacto e na complexidade de implementação, garantindo alinhamento com as expectativas do cliente e com as políticas de segurança e governança de dados da CPTM.

&emsp;&emsp;O framework ágil valoriza entregas frequentes de funcionalidades de forma iterativa e incremental. Dessa maneira, o trabalho é dividido em pequenas entregas que proporcionam valor ao cliente o mais rápido possível. As User Stories desempenham um papel fundamental nesse processo, pois permitem que as equipes priorizem as demandas com base no impacto e na complexidade de implementação.

&emsp;&emsp;Um princípio importante na escrita de User Stories eficazes é o acrônimo INVEST, que serve como guia para garantir a qualidade das histórias. INVEST significa:

- Independent: A história deve ser autossuficiente, sem depender de outras para ser desenvolvida.
- Negotiable: Os detalhes da história devem ser flexíveis e ajustáveis conforme necessário.
- Valuable: A história precisa agregar valor ao cliente ou ao negócio.
- Estimable: A história deve ser clara o suficiente para permitir a estimativa do esforço necessário.
- Small: A história deve ser pequena o suficiente para ser concluída dentro de um sprint ou ciclo de trabalho.
- Testable: A história deve incluir critérios de aceitação claros, para que se possa validar se foi implementada corretamente.

### Escala de Escala de Pontos para Estimativa de Esforço (Tópico 6)

- 1-2 pontos (Baixa Complexidade):
    - Tarefas simples que exigem pouco tempo e recursos para serem implementadas.
- 3-5 pontos (Complexidade Média): 
    - Tarefas que requerem um esforço moderado, possivelmente envolvendo várias etapas ou integração com sistemas existentes.
- 6-8 pontos (Complexidade Média-Alta):
    - Tarefas complexas que exigem planejamento detalhado, desenvolvimento e testes extensivos.
- 9-10 pontos (Alta Complexidade):
    - Tarefas muito complexas que demandam um esforço significativo em termos de tempo, recursos e coordenação.


### User Story 1
**1.** Acesso a Dados Operacionais em Tempo Real

**2.** "Como assessor da Diretoria de Operação e Manutenção, quero acessar dados operacionais em tempo real para monitorar o desempenho dos trens e identificar problemas rapidamente."

**3. Critérios de Aceitação:**
- O sistema deve permitir acesso a dados atualizados com intervalo máximo de 5 minutos.
- Deve exibir métricas-chave de desempenho, incluindo pontualidade, velocidade média e ocorrências de falhas.
- O acesso deve ser realizado através de um painel interativo acessível via navegador web.
- Os dados apresentados devem ser precisos e refletir o estado atual das operações.

**4. Notas ou Comentários:**

Priorizar a visualização de métricas relacionadas à segurança e eficiência operacional.
Garantir conformidade com as políticas de segurança da informação da CPTM.
Considerar a implementação de alertas em tempo real para ocorrências críticas.

**5. Prioridade:**
- Alta

**6. Estimativa de Esforço:**
- 8 pontos (complexidade média-alta devido ao processamento de dados em tempo quase real e desenvolvimento de interface)

**7. Identificação de Relações:**
- Depende da User Story 4 (Implementação do Sistema de Ingestão de Dados Não Estruturados) para garantir que os dados operacionais em tempo real estejam disponíveis para acesso e monitoramento.
- Relaciona-se com a User Story 5 (Consulta e Extração de Dados do Data Lake) caso o acesso aos dados seja feito através do Data Lake.

### User Story 2
**1.** Análise Estatística dos Dados de Manutenção

**2.** "Como assessor da Diretoria de Operação e Manutenção, quero realizar análises estatísticas nos dados de manutenção para otimizar os cronogramas e reduzir o tempo de inatividade dos trens."

**3. Critérios de Aceitação:**
- O sistema deve permitir a execução de análises estatísticas descritivas nos dados históricos de manutenção.
- Deve ser possível identificar padrões de falhas e tendências que impactam a disponibilidade dos trens.
- Os resultados devem ser apresentados de forma clara e visualmente acessível.
- Deve permitir a exportação dos resultados para formatos como CSV e PDF.

**4. Notas ou Comentários:**

Focar na identificação de componentes com maior índice de falhas.
Preparar o sistema para futuras análises preditivas.
Integrar indicadores-chave de desempenho relevantes.

**5. Prioridade:**
- Média-Alta

**6. Estimativa de Esforço:**
- 5 pontos (complexidade média)

**7. Identificação de Relações:**
- Depende da User Story 4 (Implementação do Sistema de Ingestão de Dados Não Estruturados) para obter os dados de manutenção necessários para análise.
- Depende da User Story 5 (Consulta e Extração de Dados do Data Lake) para acessar e extrair os dados históricos de manutenção.
- Fornece resultados para a User Story 3 (Visualização de Insights Através de Infográficos) ao gerar insights que serão visualizados.

### User Story 3
**1.** Visualização de Insights Através de Infográficos

**2.** "Como assessor da Diretoria de Operação e Manutenção, quero visualizar os resultados das análises em infográficos para facilitar a comunicação dos insights durante reuniões e tomadas de decisão."

**3. Critérios de Aceitação:**
- O sistema deve gerar infográficos que apresentem os principais insights de forma clara e atrativa.
- Deve permitir a personalização dos dados e métricas exibidos.
- Os infográficos devem ser acessíveis online e compartilháveis.
- Seguir as diretrizes visuais e de branding da CPTM.

**4. Notas ou Comentários:**
Priorizar usabilidade e clareza nas visualizações.
Considerar diferentes tipos de gráficos conforme adequação aos dados.

**5. Prioridade:**
- Alta

**6. Estimativa de Esforço:**
- 3 pontos (complexidade baixa)

**7. Identificação de Relações:**
- Depende da User Story 2 (Análise Estatística dos Dados de Manutenção) para obter os resultados das análises que serão transformados em infográficos.
- Pode utilizar dados da User Story 1 (Acesso a Dados Operacionais em Tempo Real) para incluir insights em tempo real nas visualizações.

### User Story 4 
**1.** Implementação do Sistema de Ingestão de Dados Não Estruturados

**2.** "Como assessor da Diretoria de Operação e Manutenção, quero que o sistema ingira grandes volumes de dados não estruturados para que todas as informações relevantes estejam disponíveis para análise."

**3.** Critérios de Aceitação:
- O sistema deve ingerir pelo menos 1 GB de dados não estruturados diariamente.
- Deve suportar diferentes formatos de dados (e.g., logs, arquivos de texto).
- A ingestão deve ser confiável, garantindo a integridade dos dados.
- Deve permitir ingestão em batch e em streaming.

**4. Notas ou Comentários:**

Considerar escalabilidade para volumes maiores no futuro.
Garantir conformidade com políticas de segurança e privacidade de dados.

5. Prioridade:
- Média

6. Estimativa de Esforço:
- 6 pontos (complexidade média)

**7. Identificação de Relações:**
- Fundamental para as User Stories 1, 2 e 5, pois fornece a infraestrutura de ingestão de dados necessária para que os dados estejam disponíveis para acesso e análise.
- Habilita a User Story 5 (Consulta e Extração de Dados do Data Lake) ao alimentar o Data Lake com os dados que serão consultados.

### User Story 5
1. Consulta e Extração de Dados do Data Lake

2. "Como assessor da Diretoria de Operação e Manutenção, quero consultar o Data Lake para obter conjuntos de dados específicos e realizar análises detalhadas conforme necessário."

3. Critérios de Aceitação:
- O sistema deve oferecer uma interface intuitiva para consulta ao Data Lake.
- Permitir aplicação de filtros e critérios de busca para localizar dados relevantes.
- Consultas devem retornar resultados em menos de 1 minuto para datasets médios.
- Possibilitar exportação dos dados em formatos padrão (e.g., CSV).

4. Notas ou Comentários:
Implementar controles de acesso adequados.
Interface amigável para usuários sem conhecimento técnico avançado.

5. Prioridade:
- Média-Baixa

6. Estimativa de Esforço:
- 7 pontos (complexidade média-alta)

**7. Identificação de Relações:**
- Depende da User Story 4 (Implementação do Sistema de Ingestão de Dados Não Estruturados) para garantir que os dados estejam disponíveis no Data Lake.
- Suporta as User Stories 1 e 2 ao fornecer os meios para acessar e extrair conjuntos de dados específicos para monitoramento e análises detalhadas.

As User Stories definidas refletem as necessidades essenciais para o aprimoramento das operações da CPTM, focando na integração de dados em tempo real, análises preditivas e visualizações intuitivas. Ao implementar essas funcionalidades, espera-se não só otimizar o desempenho e a manutenção dos trens, como também fornecer uma plataforma robusta e flexível para futuras expansões e melhorias. O sucesso na execução dessas histórias permitirá uma gestão mais eficiente, garantindo agilidade e precisão no acesso e processamento dos dados, fundamentais para a operação segura e eficaz dos serviços da CPTM.

&emsp;&emsp; As ferramentas utilizadas nessa pesquisa inicial foram de suma importância para entender necessidades e dores do cliente(CPTM). Com isso, permitindo uma abordagem mais precisa no desenvolvimento do Data App. Tendo como foco o usuário final, representado pela persona Ricardo Oliveira, será possível identificar aspectos críticos que impactam diretamente a eficiência operacional, como a integração de sistemas legados, a necessidade de visualizações em tempo real e a automação na coleta e padronização de dados.

&emsp;&emsp; A jornada mapeada revela as oportunidades de otimização nas fases de ingestão, processamento e monitoramento dos dados. Entre os principais insights estão a importância de criar alertas automáticos para ingestão contínua de dados, a implementação de dashboards que atualizem em tempo real e o desenvolvimento de processos de refinamento contínuo do pipeline. Esses elementos, se bem executados, vão contribuir para uma gestão de operações mais eficiente e baseada em dados, proporcionando uma solução robusta e alinhada com as demandas da CPTM.
