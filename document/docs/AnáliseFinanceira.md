# 9. Análise Financeira
## 9.1 Introdução

&emsp;&emsp;Este documento apresenta um planejamento detalhado dos custos necessários para a implementação e manutenção do Data App ao longo de 12 meses. Inicialmente, são descritos os investimentos iniciais para a estruturação do sistema, seguidos de uma análise minuciosa dos gastos relacionados à manutenção contínua, contemplando tanto a arquitetura tecnológica quanto a equipe de suporte. Com este planejamento, busca-se garantir a viabilidade e a eficácia da solução, proporcionando uma experiência robusta e confiável aos seus usuários.

## 9.2 Planejamento de Investimento inicial

&emsp;&emsp;Manter o Data App funcionando de forma eficiente ao longo de 12 meses exige um acompanhamento constante. Para isso, é necessário realizar monitoramento e ajustes regulares, garantindo que a aplicação esteja sempre pronta para atender às novas demandas. Dois aspectos são fundamentais para o sucesso desse processo: a arquitetura tecnológica escolhida e uma equipe dedicada à manutenção e melhoria contínua.

&emsp;&emsp;A arquitetura de Big Data da AWS foi escolhida por sua eficiência e capacidade de escala. Com o Amazon S3 para armazenamento, o AWS Glue para transformar dados e o Amazon EMR para análises avançadas, essa estrutura oferece flexibilidade e economia, permitindo que os custos sejam proporcionais ao uso real. Essa abordagem ajuda a otimizar processos e tomar decisões mais assertivas ao longo do tempo.

- Amazon S3 (Storage):
O Amazon S3 é o serviço de armazenamento na nuvem da AWS que oferece durabilidade, segurança e alta disponibilidade. Ele é projetado para armazenar qualquer tipo de dado, desde arquivos pequenos até volumes massivos em Data Lakes ou Data Warehouses. Além de ser escalável, o S3 permite o acesso rápido aos dados e suporta múltiplas camadas de armazenamento, o que ajuda a otimizar custos ao classificar os dados com base na frequência de acesso. Nesse projeto, o uso estimado é de 500 GB por mês, com um custo mensal de aproximadamente *R$ 36,50*.

- AWS Glue (ETL):
O AWS Glue é uma ferramenta gerenciada de ETL (Extração, Transformação e Carga) que facilita a preparação dos dados para análise. Ele automatiza tarefas repetitivas, como a limpeza e a transformação de dados brutos, reduzindo o tempo necessário para organizar informações. Além disso, o Glue é integrado a outros serviços da AWS, permitindo que os dados sejam carregados diretamente no Amazon S3 ou analisados com ferramentas como o Amazon Athena e o Amazon EMR. Para este projeto, estima-se o uso de 5 DPU/hora durante 40 horas/mês, com um custo mensal de *R$ 836,00*.

- Amazon EMR (Elastic MapReduce):
O Amazon EMR é a solução ideal para processar grandes volumes de dados utilizando frameworks de big data como Apache Spark, Hadoop e Hive. Ele permite que análises complexas sejam realizadas de maneira escalável e eficiente. Uma das vantagens do EMR é a flexibilidade em ajustar o número de nós e o tempo de uso, o que otimiza os custos para diferentes cargas de trabalho. Nesse caso, foram considerados 2 nós m5.large, operando 24 horas por dia durante 30 dias, o que gera um custo mensal de       *R$ 3.441,60*.

&emsp;&emsp;Essa combinação de serviços oferece uma base sólida para armazenar, processar e analisar dados de forma segura e escalável. O custo mensal total da arquitetura é de R$ 4.314,10 e, no acumulado de 12 meses, chega a R$ 51.769,20.

&emsp;&emsp;Após detalhar a arquitetura de Big Data da AWS, é importante entender a equipe responsável por implementar e manter essa solução. A estrutura tecnológica definida pela arquitetura só será eficaz se for operada por uma equipe qualificada, que atuará diretamente nas tarefas de implementação, ajustes e manutenção contínua.

- Engenheiro de Dados:
O engenheiro de dados junior é a base do time quando se trata de suporte técnico e organização dos sistemas. Ele garante que os dados estejam estruturados e prontos para uso, facilitando análises e operações. Com sua dedicação às tarefas do dia a dia, o custo anual desse profissional, incluindo encargos e benefícios, é de R$ 130.657,41.
O engenheiro de dados senior traz experiência e liderança para a equipe, assumindo projetos mais desafiadores. Ele é responsável por desenvolver soluções avançadas que tornam os sistemas mais eficientes, escaláveis e confiáveis. Seu papel estratégico é refletido no custo anual de R$ 634.447,84, um investimento que faz toda a diferença na qualidade dos resultados.

- Analista de Dados
O analista de dados junior é essencial para organizar, preparar e limpar os dados. Ele garante que tudo esteja em ordem para que as análises fluam sem problemas. Suas atividades operacionais têm um impacto direto na eficiência do time, com um custo anual de R$ 109.725,59. Já o analista de dados senior entra em ação quando é necessário realizar análises mais complexas e desenvolver modelos preditivos. Ele transforma dados em insights estratégicos, ajudando na tomada de decisões. Sua expertise justifica o custo anual de R$ 240.383,00.

- Desenvolvedor Backend:
O desenvolvedor backend é o responsável por criar e manter a estrutura técnica que processa e conecta os dados no sistema. Ele garante que as integrações funcionem de maneira eficiente, além de cuidar da segurança e estabilidade da plataforma. Seu papel é essencial para sustentar o funcionamento do projeto, com um custo anual de R$ 151.589,38.

- Desenvolvedor Frontend:
O desenvolvedor frontend cuida da parte visual e interativa do sistema, criando dashboards e gráficos que facilitam a interpretação dos dados pelos usuários. Ele se preocupa em tornar a experiência intuitiva e agradável, garantindo que as informações sejam apresentadas de forma clara. O custo anual desse profissional é de R$ 130.657,41.

&emsp;&emsp;O custo total anual da equipe, somando todos os profissionais, é de R$ 1.397.460,63. Esse valor inclui encargos trabalhistas e benefícios, refletindo o investimento necessário para assegurar uma boa performance do time.

### Investimento Total

&emsp;&emsp;Com a soma dos custos da arquitetura tecnológica com os da equipe de manutenção, o investimento total estimado para 12 meses de operação é de R$ 1.449.229,83. Esse montante engloba todos os recursos tecnológicos e humanos necessários para garantir eficiência, escalabilidade e resultados consistentes ao longo do tempo.

## 9.3 Planejamento de Custo de Manutenção(12 meses)

&emsp;&emsp; Considerando o uso da aplicação por 12 meses(1 ano), será necessário a manutenção e observabilidade constante. Isso pois, com a análise da eficácia da solução Data App aqui proposta, é possível realizar alterações que permitam a melhoria continua da mesma. Com isso, dois fatores são cruciais para a manutenibilidade do projeto: Arquitetura e equipe de manutenção.

### Arquitetura

&emsp;&emsp; Com isso, é possível descorrer sobre ambos os fatores. Inicialmente, mensalmente será necessário consumir de uma arquitetura composta por ferramentas da AWS(Amazon Web Services), isso pois dados precisarão ser armazenados e consumidos. Além disso, a aplicação precisará ser hospedado em algum servidor, isso é, será instalado em uma arquitetura para que seja possível que usuários consultem a solução. Além disso, também será necessário um servidor para banco de dados on premise, isto é, o banco de dados será executado localmente, em um servidor da CPTM. Considerando esses pontos, os custos de arquitetura se darão pelas seguintes ferramentas:

 - Amazon EC2: Amazon Elastic Computing consiste em um computador virtual que permite que usuários acessem virtualmente. Com isso, a máquina pode ser utilizada para hospedagem da aplicação. Com isso, sendo necessário para que o Data App esteja acessível. Isso dado uma configuração de  Locação (Instâncias compartilhadas), Sistema operacional (Linux), Carga de trabalho (Consistent, Número de instâncias: 1), Instância do EC2 avançada (t4g.2xlarge), Pricing strategy (Compute Savings Plans 1yr No Upfront), Habilitar monitoramento (desabilitada), DT Entrada: Not selected (0 TB por mês), DT Saída: Not selected (0 TB por mês), DT Intrarregião: (0 TB por mês)

 - AWS Lambda: Programa orientado a eventos que permite ao usuário definir gatilhos de execução para programas que realizam certas tarefas. No contexto do projeto, será de suma importância para o processo de ETL(Extract, Transform & Loading) dos dados utilizados nos infográficos do data app aqui definido. Com isso, garantindo atualização dos dados em um intervalo pré-definido e com uma configuração de Arquitetura (x86), Arquitetura (x86), Modo de invocação (Em buffer), Quantidade de armazenamento temporário alocada (512 MB), Número de solicitações (200 por dia).

 - AWS S3(Simple, Storage, Service): Será utilizado como um serviço de armazenamento baseado em objetos. Com isso, é possível criar Data Lakes, assim sendo possível armazenar dados ainda não estruturados em um ambiente acessível de diversas formas. Tendo isso, torna-se possível utilizar de uma API, ligada ao lambda, que quando executada, irá extrair dados do Data Lake posicionado em uma instância AWS S3.

&emsp;&emsp;Por fim, essa arquitetura AWS possui um custo de USD 141,07 por mês segundo a calculadora da [AWS](https://calculator.aws/#/estimate?id=8d7f973f4217c75db48e74a413b106244db3aaca). Considerando a cotação do dolar do dia 02/12/2024, segundo o [UOL](https://economia.uol.com.br/cotacoes/cambio/), com valor de R$ 6,07, resultando em R$ 858,52 por mês.

### Equipe de manutenção

&emsp;&emsp; Para a manutenção da aplicação, será necessário uma equipe a qual será baseada nas definições de experiências em classes Junior, Pleno e Sênio da [Gupy](https://www.gupy.io/blog/junior-pleno-senior#:~:text=Júnior%20é%20uma%20pessoa%20recém,liderança%20de%20equipes%20e%20projetos.). O profissional Júnior, provavelmente com pouca experiência de mercado, ainda não tem autonômia para tomada de decisão e ,normalmente, necessita de auxilio para executar tarefas, um profissional Pleno tem mais de dois anos de experiência e consegue resolver problemas complexos e simples com autonômia, contudo ainda não participa de tomadas de decisões estratégicas, já o Sênior pode ser o líder de uma equipe, participando da tomada de decisões e ajudando outros profissionais.

<div align="center">
  <p>Figura 38: Descrição Júnior, Pleno e Sênior</p>
  <img src="https://blog.sc.senac.br/wp-content/uploads/2022/09/2508-LinkedIn-J%C3%BAnior-Pleno-S%C3%AAnior-752x393.png" alt="Descrição Júnior, Pleno e Sênior">
  <p><a href="https://blog.sc.senac.br/importancia-da-secretaria/">Senac São Paulo</a></p>
</div>

&emsp;&emsp;Com isso a equipe, antes formada por sete pessoas será reduzida para quatro pessoas na seguinte configuração:

 - 1 Engenheiro de Dados Sênior: Segundo a referênciada citada, o Engenheiro Sênior liderará a equipe de manutenção. Sendo responsável por colher feedbacks dos usuários da aplicação e definir novas funcionalidades do Data App para então levar essas tarefas a equipe. Além disso, ele irá gerir a equipe para que consigam executar suas tarefas. Esse integrante tem como salário em torno de R$ 24.000 segundo o [G1](https://g1.globo.com/tecnologia/noticia/2024/04/07/cientista-e-engenheiro-de-dados-estao-em-alta-e-tem-salario-que-pode-passar-de-r-20-mil-veja-como-entrar.ghtml), contudo, considerando outros custos que envolvem ter um funcionário empregado, segundo a calculadora de custos [Ozai](https://www.ozai.com.br/custo-de-contratacao/), seguindo como uma empresa normal, é chegado a um gasto mensal de R$ 38.642,67, resultando em um gasto anual de R$ 463.712,04. 

 - 1 Analista de Dados Pleno: O analista de dados será responsável por atestar que os infográficos gerados no Data App permanencem gerando insights. Com isso, garantindo a efetividade da aplicação. Esse será de senioridade Plena, isso pois, como visto anteriormente, um profissional Pleno já consegue ter noções sobre o projeto para que entenda suas necessidades, mesmo que não tenha poder de tomar decisões estratégicas no projeto. Com isso, esse profissional, tendo um salário bruto mensal de R$ 6.000 segundo [Glassdoor](https://www.glassdoor.com.br/Sal%C3%A1rios/analista-de-dados-pleno-sal%C3%A1rio-SRCH_KO0,23.htm), contudo, novamente utilizando a calculadora do Ozai, chegamos a R$ 9.660,67 por mês, resultando em R$ 115.928,04 anuais.

 - 1 Desenvolvedor Backend Pleno: Um profissional que atua no desenvolvimento web, planejando, programando, testando e mantendo a estrutura de códigos que interligam o site, o servidor e o banco de dados, contudo, no contexto do Data App, ele será responsável por manter e dar manutenção nas API's que alimentam os dashboards dos infográficos. Sendo Pleno, pois, considerando que haverá apenas um desenvolvedor backend, ele deverá conseguir executar suas tarefar sozinho, o que já pode ser executado por um Pleno.  Com isso, segundo a [Talent](https://br.talent.com/salary?job=desenvolvedor+back+pleno), o salário de um profissional dessa áreagira em torno de R$ 6.000. Seguindo a lógica dos outros profissionais aqui apresentados, o custo mensal para a empresa será de R$ 9.660,67 e R$ 115.928,04 anuais.

 - Desenvolvedor Frontend Pleno: Responsável pela criação, adaptação e manutenção da interface gráfica do Data App. Grantindo UX(User Experience) e UI(User Interface) eficientes. Esse profissional tem um salário mensal de R$ 7.000 segundo o [Glassdoor](https://www.glassdoor.com.br/Sal%C3%A1rios/pleno-front-end-developer-sal%C3%A1rio-SRCH_KO0,25.htm), contudo, novamente seguindo o calculo de custo para o empregador do Ozai, apresentado a anteriormente, resultando em R$ 11.270,78 por mês e R$ 135.249,36.

&emsp;&emsp; Considerando todos os gastos apresentados para montar uma equipe de manutenção para a aplicação, é possível chegar a R$ 803.817,48. Com isso, será possível manter a aplicação por ao menos um ano. Considerando apenas a equipe.

### 9.4 Conclusão Análise Financeira 

&emsp;&emsp; Por fim, os gastos mensais e anuais da aplicaçãose darão pela seguinte tabela:

Segue a tabela com os valores organizados conforme solicitado:

| Nome                         | Categoria             | Valor Mensal (R$) | Valor Anual (R$)   |
|------------------------------|-----------------------|-------------------|-------------------|
| Amazon EC2                   | Arquitetura          | 858,52           | 10.302,24        |
| AWS Lambda                   | Arquitetura          | Incluso no EC2   | Incluso no EC2   |
| AWS S3                       | Arquitetura          | Incluso no EC2   | Incluso no EC2   |
| Engenheiro de Dados Sênior   | Equipe de Manutenção | 38.642,67        | 463.712,04       |
| Analista de Dados Pleno      | Equipe de Manutenção | 9.660,67         | 115.928,04       |
| Desenvolvedor Backend Pleno  | Equipe de Manutenção | 9.660,67         | 115.928,04       |
| Desenvolvedor Frontend Pleno | Equipe de Manutenção | 11.270,78        | 135.249,36       |
| **Total**                    | **-**                | **70.093,31**    | **814.119,72**   |

&emsp;&emsp;Com isso, o investimento total para o primeiro ano de operação do Data App será de R$ 841.119,72. Este valor assegura não apenas o funcionamento da aplicação, mas também sua evolução, possibilitando uma experiência de uso eficiente e resultados efetivos para os usuários. Esse planejamento é fundamental para garantir o sucesso do projeto e o retorno esperado.

## 10. ROI (Retorno sobre o Investimento)

&emsp;&emsp;O cálculo do ROI aqui apresentado leva em consideração benefícios não diretamente ligados a novas receitas, mas sim à economia ligada a otimização dos processos internos. As estimativas abaixo foram pensadas considerando o contexto da CPTM, seu volume de operações e as ineficiências comuns em um ambiente sem muitas análises robustas de dados.

### 10.1 Benefícios Estimados

1. **Redução de Custos Operacionais (R$480.000,00/ano)**  
   **Justificativa da Estimativa:**  
   - **Manutenção Preditiva:** O projeto de Big Data permitirá identificar padrões de falhas e antecipar a manutenção dos trens e equipamentos de infraestrutura, reduzindo a necessidade de reparos emergenciais, que normalmente possuem custo superior (mão-de-obra extra, peças compradas com urgência e interrupções não planejadas). Sabendo que, a média salarial estimada do cargo de Engenheiro na CPTM, é de R$ 7 mil a R$ 9 mil por mês [Glassdoor](https://www.glassdoor.com.br/Pagamento-mensal/Companhia-Paulista-de-Trens-Metropolitanos-CPTM-Engenheiro-Pagamento-mensal-E2482741_D_KO48,58.htm). Podemos mensurar que, com a diminuição de ocorrências emergênciais, considernado o volume das operações da CPTM, poderemos evitar a contratação de pelo menos 5 engenheiros, economizando R$40.000,00 para a CPTM mensalmente, ou R$480.000,00 por ano.
   - **Otimização de Recursos:** Ao analisar dados de consumo energético, uso de materiais e peças de reposição, torna-se possível ajustar políticas de estoque e logística, reduzindo custos com excesso de peças ou com falta de componentes chave.  
   Considerando que a CPTM opera diariamente um alto volume de passageiros e possui uma malha ferroviária complexa, mesmo um pequeno aumento de eficiência (por exemplo, uma redução de 5% a 10% em gastos emergenciais de manutenção ao longo do ano) pode impactar na economia da empresa.

2. **Aumento de Eficiência (R$ 250.000,00/ano)**  
   **Justificativa da Estimativa:**  
   - **Automação de Processos Analíticos:** Sem a ferramenta, a equipe de análise de dados e as áreas operacionais gastariam muitas horas manuais consolidando relatórios de diferentes fontes. Com o pipeline de Big Data, a consolidação e limpeza dos dados passam a ser automatizadas, liberando horas de trabalho qualificadas para tarefas mais estratégicas.  
   Considerando um time de analistas, engenheiros e técnicos que passa a economizar 10% a 15% do seu tempo em tarefas repetitivas, a economia pode chegar a centenas de milhares de reais por ano, conforme a estrutura salarial já apresentada na análise financeira. Assim, R$ 350.000,00 anuais seria uma estimativa frente a toda operação da CPTM.

3. **Melhora na Tomada de Decisão Estratégica (R$ 220.000,00/ano)**  
   **Justificativa da Estimativa:**  
   - **Evitar Investimentos Desnecessários:** Com dados confiáveis, gestores poderão decidir onde investir (por exemplo, quais estações precisam de mais trens ou quais processos operacionais devem ser revisados) com base em nos dados. Evita-se assim despesas mal direcionadas, compras de equipamentos desnecessários ou mudanças que não trazem retorno.  
   - **Alocação Eficiente de Recursos:** Informações acuradas sobre fluxos de passageiros, tempos de deslocamento, períodos de pico e gargalos operacionais possibilitam mudanças que ampliam a capacidade e reduzem custos indiretos (como atrasos ou direcionamentos incorretos da equipe em horários de pico).   
   Um ajuste na alocação de recursos, com base na análises de dados, pode economizar muito tempo de trabalho e gastos desnecessários. A projeção de R$ 200.000,00 é baixa comparado aos custos dos projetos da CPTM, por exemplo, para fazer a manutenção da via permanente de apenas 5 linhas, foi necessário o investimento de R$450.000.000,00 [Metrô CPTM](https://www.metrocptm.com.br/cptm-investira-r-450-milhoes-na-manutencao-da-via-permanente-de-suas-cinco-linhas/).

**Total de Benefícios Estimados (Anual):** 

### Investimento Total Anual

&emsp;&emsp;Conforme a análise financeira apresentada, o investimento total previsto para o primeiro ano de operação é de **R$ 841.119,72**.

### Cálculo do ROI

&emsp;&emsp;ROI = ((Benefícios Estimados - Investimento) / Investimento) x 100

&emsp;&emsp;Portanto:

&emsp;&emsp;ROI = $\frac{R\$950.000,00 - R\$841.119,72}{R\$841.119,72} \times 100$

&emsp;&emsp;ROI = 12,9%


&emsp;&emsp;**ROI Estimado:** aproximadamente **12,9%** ao ano.

&emsp;&emsp;Esse resultado indica que, ao considerar ganhos não diretamente relacionados a receita, mas sim vindos de eficiência, redução de custos e decisões orientadas, o investimento no projeto mostra-se vantajoso, trazendo uma economia significativa para a organização ao longo do primeiro ano.



