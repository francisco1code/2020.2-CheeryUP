# Plano de Gerenciamento de Riscos

## Histórico de Versões
| Data     | Versão   | Descrição | Autor(es) |
|:----------:|:--------:|:----------------------:|:---------------------------:|
| 13/03/2021 |   0.1    | Criação do Plano de Gerenciamento de Riscos |   Nilvan Peres  |
| 13/03/2021 |   0.2    | Identificação dos riscos |   Nilvan Peres  |

## Sumário
1. [Introdução](#1---introdução)  
1. [Estrutura Analítica dos Riscos (EAR)](#2---estrutura-analítica-dos-Riscos-(EAR))
1. [Análise quantitativa](#3---análise-quantitativa)
    * 3.1. [Probabilidade](#3.1---probabilidade)
    * 3.2. [Impacto](#3.2---impacto)
    * 3.3. [Prioridade](#3.3---prioridade)
        * 3.3.1 [Valor de prioridade](#3.3.1---valor-de-prioridade)
1. [Identificação dos riscos](#4---identificação-dos-riscos)
1. [Riscos levantados](#5---riscos-levantados)
    * 5.1. [Riscos técnicos](#5.1---riscos-técnicos)
    * 5.2. [Riscos externos](#5.2---riscos-externos)
    * 5.3. [Riscos organizacionais](#5.3---riscos-organizacionais)
    * 5.4. [Riscos de gerência](#5.4---riscos-de-gerência)


## 1 - Introdução
<p align="justify"> &emsp;&emsp;
O plano de gerenciamento de riscos possui o intuito de identificar, analisar e planejar contra possíveis riscos associados ao desenvolvimento do projeto. Dessa forma, serão elaboradas ações para previnir, eliminar, mitigar, aceitar esses possíveis riscos. A gerência dos riscos deverá ser realizada pelo scrum master no decorrer das sprints.
</p>

## 2 - Estrutura Analítica dos Riscos (EAR)
<p align="justify"> &emsp;&emsp;
A estrutura analítica dos ricos, é uma ferramenta na qual são agrupados os riscos e classifica-os em categorias. Essas categorias são divididas de forma hieráquica destrinchando as possíveis fontes de risco.
</p>

## 3 - Análise quantitativa


### 3.1 - Probabilidade

|Probabilidade|Intervalo|Peso|
|:----:|:-----:|:------:|
|**Muito Baixa**|0 a 10|1|
|**Baixa**| 11 a 30|2|
|**Média**| 31 a 50|3|
|**Alta**| 51 a 65|4|
|**Muito Alta**| 65 a 100| 5|

### 3.2 - Impacto

|Impacto|Descrição|Peso|
|:----:|:-----:|:------:|
|**Muito Baixo**|Impacto pouco expressivo no desenvolvimento do projeto|1|
|**Baixo**| Pouco impacto no desenvolvimento do projeto|2|
|**Médio**| Possui certo impacto porém é facilmente recuperado|3|
|**Alto**| Há grande impacto no desenvolvimento do projeto|4|
|**Muito Alto**| O impacto inviabiliza o projeto| 5|

### 3.3 - Prioridade

<p align="justify"> &emsp;&emsp; Se baseando com os valores do impacto e de probabilidade calcula-se a prioridade dos riscos. O que determina a urgência com que medidas devem ser tomadas para mitigar ou resolver um risco que pode impedir o projeto.

|Probabilidade/Impacto|Muito Baixa|Baixo|Média|Alta|Muito Alta|
|:----:|:-----:|:------:|:------:|:------:|:------:|
|**Muito Baixa**|1|2|	3|	4|	5|
|**Baixa**| 2|4	|6	|8	|10|
|**Média**| 3|6|	9	|12|	15|
|**Alta**| 4| 8	|12	|16|	20|
|**Muito Alta**| 5| 	10|	15	|20	|25|

#### 3.3.1 - Valor de prioridade

|Prioridade|Intervalo|
|:----:|:-----:|
|Muito Baixo|1 a 5|
|Baixo| 6 a 10|
|Médio| 11  a 15|
|Alto| 16 a 20|
|Muito Alto| 21 a 25 |

## 4 - Identificação dos riscos
<p align="justify"> &emsp;&emsp;
A forma utilizada para a identifação de riscos do projeto foi a análise de premissas e brainstorming - elaborar uma lista de riscos do projeto, promovendo a identificação de ameaças e oportunidades.
</p>

## 5 - Riscos levantados
### 5.1 - Riscos técnicos
|Risco| Descrição|	Ação Preventiva|	Ação Reativa	|Probabilidade	|Impacto|	Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
| R01 | Falta de conhecimento com as tecnologias de desenvolvimento. |  Escolher os alunos que estão dispostos a aprender as ferramentas necessárias. | Procurar cursos e aplicar treinamento sobre as tecnologias. | 4 | 5  | 20 | 
| R02 | Falta de conhecimento sobre DevOps, para configuração do ambiente | Estudo e treinamento do Docker | Reuniões com monitores para sanar problemas do docker | 8 | 5 | 25 | 
| R03 | Alteração de Tecnologias do projeto |  Clareza no escopo do projeto | Planejamento de sprints de modo que possíveis alterações não afetem o desenvolvimento do projeto. | 2 | 2 | 10 |
| R04 | Defeito no equipamento de algum integrante do grupo | Comunicação clara e transparente entre todos os membros do grupo. | Realacação de integrantes em diferentes funções |  1 | 4 | 10 | 

### 5.2 - Riscos externos
|Risco| Descrição|	Ação Preventiva|	Ação Reativa	|Probabilidade	|Impacto|	Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
| R05 | Problemas na comunicação com o cliente | Clareza nas funcionalidades que serão entregues ao cliente | Reuniões para definir de forma concisa escopo e features. | 4 | 3 | 20 | 
| R06 | Falta de cliente real | Levantamento de requisitos  | Elaboração e análise dados para atrair público-alvo | 5 | 2 | 10 | 

### 5.3 - Riscos organizacionais
|Risco| Descrição|	Ação Preventiva|	Ação Reativa	|Probabilidade	|Impacto|	Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
| R07 | Dependência entre as atividades| Planejar de forma paralela | Planejar issues de forma que issues não ocorra o excesso de dependências entre as issues | 3 | 3 | 8 | 

### 5.4 - Riscos de gerência
|Risco| Descrição|	Ação Preventiva|	Ação Reativa	|Probabilidade	|Impacto|	Prioridade|
|:----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
| R08 | Alterar escopo | Reuniões para descrever de forma clara os requisitos do projeto. | Dailys para atualizações de todos os integrantes sobre possíveis mudanças e melhor planejamento. | 3 | 3 | 20 |  
| R09 | Falta de comunicação entre os integrantes do grupo |  Estabelecer ferramentas de comunição entre os membros, realizações de dailys e assuntos pontuais por whatsapp/telegram | Sempre deixar principais pontos das sprints em ambientes que os integrantes acessam constantemente. | 3 | 4 | 12 | 
| R10 | Desistência de algum membro da equipe. | Dividir de forma igualitária as issues do projeto.  | Adequar os horários e realocar as tarefas entre os membros sem sobrecarregar nenhum membro. | 3 | 4 | 15 | 
| R11 | Baixa produtividade dos integrantes do grupo |  Motivação da equipe através de dailys | Realizar checkpoints de saúde mental com os integrantes do grupo, ou elaboração de gamificação | 3 | 4 | 10 |
| R12 | Conflitos de horários disponíveis para os integrantes. |  Montar uma grade com os horários disponíveis de cada membro. | Os pontos das sprints deve ser divido visando a carga horária compatível com o que os integrantes terão na semana, sendo maleável a mudanças(desde que o membro notifique o grupo no planejamento da sprint).| 4 | 3 | 10 | 