# 8. Documentação da Análise de Impacto Ético

## 8.1 Introdução

&emsp;&emsp;Esta seção apresenta em detalhes a análise de impacto ético do projeto Data App e as medidas tomadas para garantir a conformidade com as normas de ética e direito, incluindo as políticas da Lei Geral de Proteção de Dados – LGPD. Uma análise é essencial para garantir que o projeto seja conduzido de maneira responsável e transparente, evitando situações indevidas e promovendo a conformidade com a sociedade. Estudos apontam que programas de ética em dados podem oferecer vantagens competitivas, visto que os clientes priorizam privacidade e transparência na escolha de seus fornecedores (Janiszewska-Kiewra, Podlesny e Soller, 2020). Os tópicos a seguir fornecem insights detalhados sobre várias áreas de impacto relevantes; começando pela análise das políticas de privacidade e de proteção de dados, abrangendo impacto a grupos da sociedade, impacto ambiental e o risco de vieses.

## 8.2 Revisão de Políticas de Privacidade e Proteção de Dados

&emsp;&emsp; A proteção de dados é essencial para preservar a privacidade dos indivíduos, evitar abusos com o uso de informações pessoais e construir um ambiente digital seguro e confiável. Com isso, o projeto de Data App torna de suma importância a análise dos conjuntos de dados para que seja assegurado que os mesmos não possuem informações sigilosas.

&emsp;&emsp; Para analisar esses dados, é possível utilizar como base a Lei Geral de Proteção de dados(LGPD). Essa regulamenta o uso, coleta, armazenamento e tratamento de dados pessoais, estabelecendo regras para empresas e organizações sobre como lidar com dados pessoais, visando garantir a privacidade e a proteção das informações dos cidadãos brasileiros.

&emsp;&emsp; Com isso, alguns âmbitos serão análisados acerca dos conjuntos de dados fornecidos pela CPTM:

 - Dados Pessoais: Não há extração de dados pessoais as quais são estabelecidas na LGPD, como nome, endereço, CPF, e-mail, etc. Contudo, no conjunto de dados extraídos e extruturados de catracas de estações, há informações sobre bilhetes validados nas catracas de controle. Contudo, como esses dados não conseguem ser utilizados pelo Data App em conjunto com outros que possibilitem a identificação dos donos dos cartões. Porém, ao observarmos informações sobre ocorrências e falhas, foram encontrados, na coluna de "Descrição da ocorrência", informações de nomes, CPF, CRM e emails. Contudo, a partir de identificação de estruturas comuns, esses dados foram retirados numa limpeza inicial.

 - Dados Sensíveis: Informações que dizem respeito à origem racial ou étnica, convicções religiosas, opinião política, dados sobre saúde ou vida sexual, entre outros não são encontradas nos conjuntos de dados

 &emsp;&emsp;Com base nesses resultados de análise, pode-se dizer que o projeto Data App toma medidas para que a utilização de seus datasets siga a legislação da LGPD. Tendo em vista que não existem dados pessoais, muito menos dados sensíveis, já conforme prevê a lei, temos a certeza de que o projeto preocupa-se com a privacidade e segurança da informação. A mera identificação e exclusão previamente a quaisquer etapas de processamento de dados que poderiam fazer com que a privacidade de alguém fosse colocada em risco, como através de ter seu nome, CPF ou e-mail divulgado, protege os titulares desses direitos e certamente reduz riscos de uso indevido. Ademais, todas as requisições de dados no processo de ETL pelo Flask são asseguradas com usuário e senha, onde a senha é uma hash SHA-256, garantindo que durante o processo de extração até o carregamento, não haverá acesso ao banco de dados sem permissão. Dessa forma, pode-se dizer que o projeto Data App está relacionado com os princípios de proteção de dados, ou seja, construiu-se um ambiente seguro e confiável para a utilização de informações de relevância sem expor os dados pessoais do público em geral. Essas medidas aumentam a confiabilidade do projeto e a sua ética e conformidade, garantindo que a utilização promovida por ele está de acordo com todas as normas e padrões em vigor para proteção de dados.

## 8.3 Avaliação de Equidade e Impactos em Grupos Específicos

&emsp;&emsp;Esta seção identifica e registra quaisquer potenciais impactos que a implementação do pipeline de Big Data na CPTM possa ter em grupos específicos, com ênfase nos grupos vulneráveis. Embora o projeto tenha como objetivo otimizar operações e melhorar a eficiência do transporte público, é essencial garantir que essas melhorias não gerem disparidades ou injustiças para quaisquer segmentos da população.

1. **Pessoas com Deficiência (PCD)**:

   - **Dados Relevantes**: Conforme a análise da **Tabela Acompanhamento PCD**, identificou-se que as estações com IDs 64, 9, 13, 94, 16 e 41 apresentam o maior número de ocorrências envolvendo PCD. Além disso, o maior volume de ocorrências ocorre entre as 16h e 19h, horário de pico (Seção 4.2.1).

   - **Impacto Positivo**: A utilização do pipeline permitirá monitorar em tempo real essas ocorrências, possibilitando alocar recursos adicionais e melhorar o suporte oferecido nessas estações e horários.

   - **Impacto Negativo**: Se os dados não forem tratados adequadamente, há o risco de subnotificação ou invisibilidade de necessidades específicas, levando a decisões que não atendam aos PCDs.

2. **Comunidades de Baixa Renda e Áreas Periféricas**:

   - **Dados Relevantes**: A análise da **Tabela de Validações de Bilhetes** mostrou que algumas estações possuem baixa movimentação, possivelmente localizadas em áreas menos atendidas ou com menor acesso ao transporte público (Seção 4.2.2). Essas comunidades frequentemente enfrentam desafios socioeconômicos e podem não estar incluídas adequadamente nos processos de tomada de decisão.

   - **Impacto Positivo**: O pipeline pode identificar essas áreas de baixa demanda, permitindo à CPTM ajustar serviços e melhorar a oferta de transporte nessas comunidades. Além disso, ao incluir dados dessas regiões, é possível desenvolver políticas mais inclusivas que atendam às necessidades específicas desses grupos.

   - **Impacto Negativo**: Se as decisões se basearem apenas em volume de validações, áreas com menor demanda podem ser negligenciadas, aumentando a desigualdade no acesso ao transporte. Há também o risco de segmentação ou exclusão dessas comunidades se não forem consideradas adequadamente nos modelos preditivos. Além disso, a dificuldade em acompanhar os benefícios tecnológicos pode deixar esses grupos em desvantagem.

3. **Usuários Idosos e com Mobilidade Reduzida**:

   - **Dados Relevantes**: A **Tabela de Tipos de Embarque** indicou que gratuidades representam uma parcela significativa dos embarques, incluindo idosos e pessoas com mobilidade reduzida (Seção 4.2.2).

   - **Impacto Positivo**: Compreender o uso do sistema por esses grupos permite à CPTM adequar serviços e políticas tarifárias para melhor atendê-los.

   - **Impacto Negativo**: Caso esses dados não sejam cuidadosamente analisados, pode haver subestimação da importância desses usuários, influenciando negativamente as decisões operacionais.

### Riscos Identificados

- **Viés Algorítmico**:

  - **Detalhe**: Os algoritmos de análise podem priorizar rotas e horários com maior volume de passageiros pagantes, desconsiderando a importância de gratuidades e necessidades especiais.

  - **Parte do Tratamento que Requer Atenção**: Na fase de **Transformação** dos dados, é crucial garantir que todas as categorias de usuários sejam representadas adequadamente.

- **Exclusão de Dados Importantes**:

  - **Detalhe**: Durante o processo de **Limpeza de Dados**, há o risco de exclusão de registros que aparentam ser outliers, mas que representam situações críticas para grupos vulneráveis.

  - **Parte do Tratamento que Requer Atenção**: Na etapa de **Análise de Outliers**, deve-se avaliar cuidadosamente se esses dados refletem eventos relevantes para grupos específicos.

- **Exclusão Digital e Desigualdade Tecnológica**:

  - **Detalhe**: Comunidades de baixa renda podem enfrentar dificuldades em acessar ou utilizar tecnologias avançadas implementadas pela CPTM, resultando em exclusão ou marginalização.

  - **Parte do Tratamento que Requer Atenção**: Durante a fase de **Análise e Implementação**, é importante considerar medidas que facilitem o acesso e o uso das tecnologias por esses grupos, evitando ampliar a desigualdade existente.

- **Privacidade e Segurança de Dados**:

  - **Detalhe**: Dados sensíveis sobre PCDs e outros grupos podem ser expostos se não houver medidas de proteção adequadas.

  - **Parte do Tratamento que Requer Atenção**: Implementar medidas rigorosas na fase de **Carregamento** e **Armazenamento** para garantir a conformidade com a LGPD.

### Plano para Minimizar Disparidades e Assegurar Equidade

1. Coleta e Análise de Dados Inclusivos

- **Ações Específicas**:

  - **Incluir Dados de Gratuidades**: Garantir que os dados de embarques gratuitos sejam considerados nos modelos de demanda.

  - **Monitorar Ocorrências Envolvendo PCDs**: Utilizar os insights da **Tabela Acompanhamento PCD** para identificar necessidades específicas.

- **Parte do Tratamento**: Na fase de **Extração**, assegurar que todas as fontes de dados, incluindo aquelas relacionadas a grupos vulneráveis, sejam integradas.

2. Mitigação de Viés Algorítmico

- **Ações Específicas**:

  - **Auditar Modelos Preditivos**: Verificar se os algoritmos não estão despriorizando áreas ou horários de grupos vulneráveis.

  - **Equilibrar Dados**: Na fase de **Transformação**, aplicar técnicas de balanceamento para evitar que grupos minoritários sejam subrepresentados.

- **Parte do Tratamento**: Durante a **Modelagem dos Dados**, incorporar variáveis que reflitam a importância dos grupos vulneráveis.

3. Engajamento Comunitário

- **Ações Específicas**:

  - **Feedback dos Usuários**: Implementar canais para que PCDs e outros grupos possam reportar problemas.

  - **Consultas Públicas**: Realizar workshops ou pesquisas para entender as necessidades específicas.

- **Parte do Tratamento**: Utilizar os dados coletados como parte do processo de **Transformação** para enriquecer as análises.

4. Melhorias na Acessibilidade

- **Ações Específicas**:

  - **Alocar Recursos em Estações Críticas**: Com base nos dados da **Tabela Acompanhamento PCD**, priorizar melhorias nas estações com maior número de ocorrências.

  - **Treinamento de Equipes**: Capacitar funcionários para melhor atender PCDs.

- **Parte do Tratamento**: Na fase de **Análise**, gerar relatórios que destacam áreas que necessitam de melhorias.

5. Políticas Tarifárias Justas

- **Ações Específicas**:

  - **Analisar Impacto de Gratuidades**: Utilizar os dados da **Tabela de Tipos de Embarque** para avaliar políticas tarifárias.

  - **Transparência**: Comunicar claramente as políticas e benefícios disponíveis.

- **Parte do Tratamento**: Durante a **Análise dos Dados**, considerar o impacto socioeconômico das políticas.

6. Proteção de Dados e Privacidade

- **Ações Específicas**:

  - **Anonimização de Dados**: Implementar técnicas para proteger a identidade dos usuários.

  - **Conformidade Legal**: Assegurar que todas as etapas do ETL estejam em conformidade com a LGPD.

- **Parte do Tratamento**: Na fase de **Carregamento**, aplicar políticas de segurança e privacidade nos sistemas de armazenamento.

7. Monitoramento e Avaliação Contínuos

- **Ações Específicas**:

  - **KPIs Específicos**: Desenvolver indicadores que monitoram o impacto em grupos vulneráveis.

  - **Relatórios Regulares**: Publicar relatórios que avaliam a equidade no uso do sistema.

- **Parte do Tratamento**: Incorporar métricas de equidade na fase de **Análise e Visualização**.

8. Inclusão de Comunidades Marginalizadas na Tomada de Decisões

- **Ações Específicas**:

  - **Participação Comunitária**: Envolver representantes de comunidades de baixa renda e áreas periféricas nos processos de planejamento e decisão.

  - **Educação e Capacitação**: Promover programas que facilitem a compreensão e o uso das novas tecnologias pelas comunidades afetadas.

- **Parte do Tratamento**: Durante a fase de **Análise e Planejamento**, incorporar feedback e insights das comunidades para garantir que as soluções atendam às suas necessidades.

## 8.4 Evidência de Transparência e Consentimento Informado

&emsp;&emsp;Nesta seção, são abordadas as práticas implementadas para garantir a transparência e o consentimento informado no projeto, assegurando que todas as partes interessadas tenham acesso claro ao projeto, e que o consentimento necessário seja documentado. O objetivo é estabelecer documentos e evidências de que todas as comunicações e coletas de consentimento seguem com as melhores práticas de transparência e proteção dos dados.

### Objetivos
- Definir e identificar as partes interessadas no projeto.
- Revisar e assegurar que os requisitos de transparência são aplicáveis e adequados as necessidades dos stakeholders e do projeto.
- Documentar de forma acessível e segura as declarações de consentimento e outros formulários relevantes para o mesmo fim. 

&emsp;&emsp;Esta seção oferece uma visão das práticas adotadas para assegurar que a transparência e o consentimento informado são realizados em todas as fases do projeto.

&emsp;&emsp;As partes interessadas neste projeto incluem:

- CPTM (Companhia Paulista de Trens Metropolitanos): Empresa pública do Estado de São Paulo, responsável pelo fornecimento de dados operacionais e administrativos para o projeto.
- Inteli (Instituto de Tecnologia e Liderança): Instituição acadêmica responsável pelo desenvolvimento do projeto, por meio do TAPI (Termo de Abertura de Projeto Inteli).
- Escritório de Projetos: Responsável pela gestão dos contratos de parceria e acordos de confidencialidade entre as partes envolvidas.
- Biggie: Encarregada de desenvolver o pipeline de Big Data e análises estatísticas.

&emsp;&emsp;Para garantir a transparência com as partes interessadas, os seguintes requisitos foram estabelecidos:

- Comunicação Clara e Constante: Essa comunicação é mantida através de encontros constantes com a CPTM, que ocorrem normalmente a cada duas semanas, no final de cada sprint, além de encontros situacionais durante as sprints.
- Documentação Acessível: Disponibilizar documentos relevantes, relatórios e resultados de análises de forma organizada e acessível, respeitando as restrições de confidencialidade, presente neste documento.
- Respeito à Privacidade e Confidencialidade: Assegurar que todos os dados sensíveis sejam tratados conforme os acordos estabelecidos e as legislações vigentes. Isso é tratado de forma mais aprofundada no tópico "8.2 Revisão de Políticas de Privacidade e Proteção de Dados" desta documentação. 

&emsp;&emsp;Considerando o contexto institucional e a natureza acadêmica do projeto, o Inteli, por meio do Escritório de Projetos, já possui os contratos de parceria necessários com a CPTM. Estes contratos incluem:

- Acordo de Parceria Acadêmica: Estabelece os termos da colaboração entre o Inteli e a CPTM, incluindo objetivos, responsabilidades e direitos de ambas as partes.
- Acordo de Confidencialidade (NDA): Garante que todas as informações e dados compartilhados pela CPTM sejam mantidos em sigilo e utilizados exclusivamente para os fins do projeto.

&emsp;&emsp;Todos os membros da equipe do projeto, e partes interessadas aderem aos acordos estabelecidos, comprometendo-se a seguir as diretrizes de confidencialidade.

&emsp;&emsp;A CPTM forneceu dados operacionais e administrativos necessários para o desenvolvimento do pipeline de Big Data. Estes envios seguem os seguintes padrões e acordos:

- Registro de Transferência de Dados: Cada envio de dados pela CPTM será documentado, indicando a natureza dos dados, a finalidade e quaisquer restrições de uso.
- Mascaramento de Dados Sensíveis: Dados sensíveis deverão ser protegidos e mantidos de acordo com o NDA.
- Uso Exclusivo para Fins Acadêmicos: Os dados recebidos serão utilizados exclusivamente para o desenvolvimento do projeto acadêmico.

&emsp;&emsp;Durante o desenvolvimento do projeto, estamos utilizando os serviços da AWS por fins educacionais. Entretanto, para a entrega final, será feita uma solução on premise, visto que empresas governamentais não podem ter seus dados em serviços de nuvem estrangeiros.  

&emsp;&emsp;Todos os documentos de consentimento, contratos e dados fornecidos pela CPTM são armazenados em repositórios seguros, com acesso restrito.

&emsp;&emsp;Outro fator importante é: diferentes funcionários, com diferentes cargos, terão ou não acesso a dados específicos. Por exemplo, Ricardo (persona) que é gerente de operações, não terá acesso aos mesmos dados que um analista, isso garante a proteção dos dados e a linearidade com cada área específica. A nível MVP do projeto, ainda não forneceremos esse acesso restrito e específico, mas é algo a considerar como próximos passos para o projeto. 

&emsp;&emsp;Através das práticas mencionadas, o projeto assegura que todas as partes interessadas estão informadas e que o consentimento é devidamente seguido e documentado. A colaboração entre o Inteli e a CPTM, formalizada por meio dos contratos estabelecidos pelo EP, permite o desenvolvimento do projeto dentro dos padrões éticos e legais exigidos, promovendo transparência e confiança entre as partes.

## 8.5 Avaliação de Impacto Social e Ambiental

&emsp;&emsp;A implementação desse projeto oferece uma série de impactos sociais, tanto positivos como negativos, e são esses impactos que serão analisados nessa seção. A análise dos impactos sociais é crucial para assegurar que o projeto não só atinja seus objetivos operacionais, mas também gere benefícios reais e equilibrados para a comunidade. Avaliar esses efeitos permite à CPTM adaptar suas estratégias para aumentar a acessibilidade, promover a equidade e melhorar a qualidade de vida urbana. Dessa forma, a análise social e ambiental se torna uma ferramenta fundamental, alinhando o desenvolvimento do projeto com os interesses coletivos e reforçando seu compromisso com o bem-estar social e a inclusão. ([PNUD, 2024](https://www.undp.org/pt/sustainable-development-goals/goal-9-industry-innovation-and-infrastructure))

### 8.5.1 Impacto Social

&emsp;&emsp;Iniciando com os impactos positivos, a melhoria na qualidade do serviço de transporte público, com aumento na eficiência das viagens, permite à CPTM fornecer um serviço mais confiável e pontual para a população. Isso se traduz em menos atrasos e maior previsibilidade, resultando em uma experiência de deslocamento melhorada e menos estresse para os usuários. Com os dados fornecidos pela CPTM sobre o perfil de passageiros PCD e os fluxos de movimento nas estações, o projeto permite que nossa equipe identifique as necessidades de infraestrutura inclusiva de maneira mais precisa. A análise desses dados possibilita direcionar melhorias para promover acessibilidade em todas as estações. Dessa forma, o projeto amplia o acesso de Pessoas com Deficiência (PCD) ao transporte público, promovendo a independência e a inclusão social, e reforçando o compromisso da CPTM com a igualdade de acesso para todos os cidadãos. 

&emsp;&emsp;A melhoria na pontualidade e na eficiência do sistema de transporte pode ter um impacto significativo também na saúde mental dos usuários. Com a redução de atrasos e maior previsibilidade nas viagens, as pessoas podem experimentar menos ansiedade e estresse relacionados ao deslocamento diário de suas rotinas. A confiabilidade no transporte também facilita o planejamento de rotinas e compromissos, o que contribui para uma sensação de controle e tranquilidade. Esse impacto é especialmente relevante em uma cidade grande, como São Paulo, onde o deslocamento é parte integral da rotina.

&emsp;&emsp;Entretanto, os possíveis impactos negativos também devem ser considerados. Projetos como esse, podem privilegiar regiões de alta demanda, marginalizando áreas com menor movimento, o que limita o acesso equitativo ao transporte público. Esse tipo de desigualdade já ocorre no acesso à infraestrutura digital em setores como telecomunicações e redes de quinta geração (5G), por exemplo, onde áreas periféricas frequentemente ficam desfavorecidas em relação às centrais. Esse fato, levanta um ponto de atenção em relação aos possíveis impactos sociais negativos que a solução pode acarretar.

### 8.5.2 Impacto Ambiental

&emsp;&emsp;Em relação aos impactos ambientais, o projeto também oferece benefícios consideráveis. A otimização das viagens e a redução de atrasos diminuem o tempo de operação dos trens e, consequentemente, o consumo de energia, o que reduz as emissões de gases de efeito estufa (GEE) e a pegada de carbono, promovendo um transporte mais sustentável. Adicionalmente, um serviço de transporte público mais eficiente e atrativo pode reduzir o uso do transporte rodoviário individual, ajudando a diminuir a poluição atmosférica e sonora, o que contribui para melhorar a qualidade do ar e reduzir o impacto sonoro nas cidades.

&emsp;&emsp;No entanto, os impactos negativos precisam de atenção. A expansão da oferta de trens para atender a maior demanda pode resultar em um aumento no consumo de energia, o que gera maior pressão sobre os recursos energéticos. Além disso, a infraestrutura e o processamento intensivo de dados requerem altos níveis de energia. Em setores como o público, o Big Data auxilia no gerenciamento de recursos hídricos e práticas agrícolas mais eficientes, mas o consumo de energia é um desafio recorrente. Para mitigar esses riscos, a análise deve considerar a importância social de cada estação e linha, e não apenas o volume de passageiros, de modo a garantir um transporte inclusivo e sustentável que atenda todas as áreas de maneira justa. Para mitigar este efeito, recomenda-se o investimento em tecnologias de energia renovável, como painéis solares nas estações, e a avaliação da viabilidade de adotar trens movidos a energia limpa, para reduzir a dependência de fontes de energia não renováveis. ([Nações Unidas Brasil, 2024](https://brasil.un.org/pt-br/sdgs)) 

### 8.5.3 Plano de mitigação e potencialização de efeitos

&emsp;&emsp;Para garantir o sucesso do projeto e maximizar os impactos positivos enquanto minimiza os negativos, propõe-se o seguinte plano de ação:

- Monitoramento contínuo dos indicadores sociais e ambientais, acompanhando regularmente os indicadores de satisfação do usuário, acessibilidade, emissões de carbono e consumo energético, para garantir que as metas de sustentabilidade e inclusão social sejam cumpridas.

- Aprimoramento de acessibilidade e inclusão, utilizando dados sobre PCD para planejar adaptações específicas em estações e trens, aumentando o conforto e segurança dos passageiros.

- Redução de consumo de energia e emissões, com a implementação de tecnologias de baixo consumo energético e exploração da viabilidade de energias renováveis, como energia solar nas estações.

### 8.5.4 Conclusão da Avaliação de Impacto Social e Ambiental

&emsp;&emsp;A análise de impacto social e ambiental do projeto mostra que o projeto tem um grande potencial de contribuir para a melhoria da mobilidade urbana, ao mesmo tempo que minimiza os efeitos adversos. Ao focar em uma operação de transporte ferroviário mais eficiente, inclusiva e sustentável, o projeto pode aumentar a atratividade do transporte público e, assim, contribuir para a redução do impacto ambiental das viagens diárias. O plano de mitigação foi elaborado para assegurar que a CPTM não só ofereça um serviço de alta qualidade, mas também se comprometa com a responsabilidade social e ambiental em todas as suas operações.

## 8.6 Revisão de Riscos de Viés e Discriminação

 &emsp;&emsp;Nesta seção, iremos **examinar o projeto para identificar riscos de viés algorítmico ou discriminação** decorrentes da implementação do pipeline de **Big Data** na CPTM. Embora o projeto não inclua modelagem preditiva, a análise de grandes volumes de dados pode inadvertidamente introduzir vieses ou discriminações caso não seja conduzida com cautela.

 &emsp;&emsp;Nosso objetivo é **propor formas de mitigação para esses problemas**, assegurando que a solução desenvolvida seja justa, ética e beneficie todos os usuários, sem discriminação ou exclusão de grupos. Para isso, iremos:

- **Identificar potenciais fontes de viés** no projeto, referenciando dados e análises realizadas.
- **Avaliar os riscos de discriminação ou exclusão** de grupos vulneráveis decorrentes dessas fontes de viés.
- **Propor medidas de mitigação** para minimizar esses riscos, garantindo a equidade no uso do sistema.

#### Potenciais Fontes de Viés no Projeto de Big Data:

1. **Representação Desigual nos Dados Coletados**

   - **Observação**: A análise da **Tabela de Movimentação de Validações** (Seção 4.2.2) indica que certas estações apresentam baixo volume de validações, possivelmente em áreas periféricas ou com menor acesso ao transporte público.

   - **Risco**: A sub-representação dessas áreas nos dados pode levar a análises que não refletem adequadamente as necessidades dessas comunidades, resultando em decisões que perpetuam a exclusão ou falta de investimentos.

   - **Parte do Tratamento que Requer Atenção**: Durante a **Extração e Transformação** dos dados, é crucial garantir que todas as áreas e grupos de usuários sejam representados de forma equilibrada.

2. **Desconsideração de Grupos Vulneráveis nos Relatórios e Visualizações**

   - **Observação**: A **Tabela Acompanhamento PCD** (Seção 4.2.1) mostra que há horários e estações com maior incidência de ocorrências envolvendo PCDs, mas esses detalhes podem ser diluídos em análises agregadas.

   - **Risco**: Relatórios que não destacam grupos vulneráveis podem resultar na ausência de ações direcionadas.

   - **Parte do Tratamento que Requer Atenção**: Na fase de **Análise e Visualização**, é importante segmentar os dados para evidenciar as necessidades de diferentes grupos.

3. **Viés na Interpretação dos Dados**

   - **Observação**: A predominância de dados de passageiros pagantes, conforme visto na **Tabela de Tipos de Embarque** (Seção 4.2.2), pode levar à interpretação de que esses usuários são os principais stakeholders, negligenciando aqueles que utilizam gratuidades.

   - **Risco**: Decisões baseadas em tais interpretações podem resultar em alocação desigual de recursos, favorecendo grupos já privilegiados.

   - **Parte do Tratamento que Requer Atenção**: Na **Análise de Dados**, é necessário considerar o contexto socioeconômico e a importância dos diferentes tipos de usuários.

#### Riscos de Discriminação ou Exclusão de Grupos

- **Negligência das Necessidades de PCDs e Idosos**

  - **Detalhe**: Sem destaque adequado nos relatórios, as necessidades de PCDs e idosos podem ser subestimadas, levando a decisões que não contemplam melhorias de acessibilidade ou suporte adequado.

- **Desigualdade na Alocação de Recursos**

  - **Detalhe**: Áreas com menor volume de dados podem ser interpretadas como de baixa prioridade, resultando em menos investimentos e perpetuando a falta de infraestrutura nessas regiões.

- **Invisibilidade de Grupos Minoritários**

  - **Detalhe**: Sem segmentação apropriada, padrões de uso e desafios enfrentados por grupos minoritários podem passar despercebidos, excluindo-os das considerações estratégicas.

### Medidas de Mitigação Propostas

#### 1. Garantir Representatividade nos Dados

- **Ação**: Verificar e ajustar os conjuntos de dados para assegurar que todas as áreas geográficas e grupos de usuários estejam adequadamente representados.

- **Implementação**: Durante a **Extração e Transformação**, aplicar técnicas de amostragem ou coleta adicional de dados onde houver lacunas.

#### 2. Segmentação e Análise Detalhada dos Dados

- **Ação**: Realizar análises segmentadas por grupo demográfico, tipo de usuário, região e outros critérios relevantes para identificar necessidades específicas.

- **Implementação**: Na fase de **Análise e Visualização**, desenvolver dashboards que permitam filtrar e visualizar dados de grupos vulneráveis.

#### 3. Envolvimento de Stakeholders Diversos

- **Ação**: Incluir representantes de grupos vulneráveis no processo de interpretação dos dados e tomada de decisões.

- **Implementação**: Organizar workshops e sessões de feedback com PCDs, idosos e comunidades periféricas para validar as conclusões das análises.

#### 4. Contextualização dos Dados

- **Ação**: Complementar os dados operacionais com informações socioeconômicas e demográficas para uma compreensão mais ampla das necessidades.

- **Implementação**: Integrar dados externos, como índices de desenvolvimento humano ou mapas de vulnerabilidade social, às análises existentes.

#### 5. Transparência na Comunicação

- **Ação**: Divulgar metodologias e critérios utilizados nas análises para que possam ser compreendidos e auditados por terceiros.

- **Implementação**: Documentar os processos de tratamento de dados e disponibilizar relatórios acessíveis ao público e partes interessadas.

#### 6. Formação e Sensibilização da Equipe

- **Ação**: Capacitar a equipe de análise de dados sobre vieses inconscientes, discriminação e a importância da equidade nas decisões baseadas em dados.

- **Implementação**: Promover treinamentos e workshops sobre ética em Big Data e impactos sociais.

#### 7. Monitoramento Contínuo e Revisão

- **Ação**: Estabelecer processos para monitorar continuamente os resultados das análises e identificar possíveis vieses ou exclusões.

- **Implementação**: Implementar indicadores de desempenho que avaliem a equidade das decisões tomadas com base nos dados.

 &emsp;&emsp;Embora o projeto não envolva modelagem preditiva, o uso de Big Data na CPTM possui riscos inerentes de viés e discriminação se não forem tomadas medidas proativas. Ao identificar potenciais fontes de viés e propor ações concretas de mitigação, buscamos assegurar que as análises e decisões resultantes do projeto promovam a equidade e atendam às necessidades de todos os usuários. A revisão e validação por especialistas em ética e fairness reforçam nosso compromisso com a responsabilidade social e a justiça no uso de dados.


## 8.7 Conclusão da Documentação da Análise de Impacto Ético

&emsp;&emsp;Para que fosse possível fazer a análise de impacto ético, foram ponderadas as responsabilidades e cuidados necessários no desenvolvimento do pipeline de Big Data para a CPTM. Ao mesmo tempo, foi priorizada a proteção de dados e a privacidade, através de práticas que asseguram o uso responsável das informações coletadas.

&emsp;&emsp;Um dos principais objetivos foi padronizar o tratamento das informações, garantindo a identificação e a redução de possíveis vieses que poderiam prejudicar determinados grupos. Também foi dada atenção especial à transparência, buscando manter as partes interessadas bem informadas e obtendo consentimentos de forma simples e acessível.

&emsp;&emsp;Além disso, foram considerados os impactos sociais e a sustentabilidade do projeto, contribuindo para a otimização dos serviços da CPTM e para a experiência dos passageiros. Ao adotar essas medidas éticas, o projeto não apenas atende aos objetivos técnicos, mas também aos valores fundamentais de responsabilidade e respeito à ética.

