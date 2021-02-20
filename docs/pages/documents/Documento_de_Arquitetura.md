## Histórico de Versões

| Versão  |  Data  | Autor  |  Descrição  |
| ------------------- | ------------------- | ------------------- | ------------------- |
| 1.0.0 | 17/02/2021  | Davi Matheus  | Estrutura inicial  |
| 1.0.1 | 17/02/2021  | Nilvan Peres  | Adição dos tópicos 1,2 e 3 |


## Sumário
[1 - Introdução](#1---introdução)
* [1.1 - Objetivo](#1.1---objetivo)
* [1.2 - Escopo](#1.2---escopo)
* [1.3 - Visão Geral](#1.3---Visão-Geral)
* [1.4 - Definições, acrônimos e abreviações](#1.4---Definições,-acrônimos-e-abreviações)

[2 - Represetanção de Arquitetura](#2---Represetanção-de-Arquitetura)

* [2.1 - Padrão Arquitetural](###2.1---Padrão-Arquitetural)
* [2.2 - Tecnologias](#2.2---Tecnologias)

[3 - Metas e Restrições da Arquitetura](#3---Metas-e-Restrições-da-Arquitetura)

* [ 3.1 - Metas](#3.1--Metas)
* [3.2 - Restrições da Arquitetura](#3.2--Restrições-da-Arquitetura)


## 1 - Introdução

### 1.1 - Objetivo 
O objetivo deste documento é dissecar a arquitetura do projeto ***mindXcovid***, de modo que, todo a visão arquitetural do sistema que será desenvolvido esteja clara.  
Outro ponto que será abordado, são as principais características do software permitindo que desenvolvedores/gestores entendam os processos que levaram na escolha das tecnologias e decisões a respeito dessa arquitetura.

### 1.2 - Escopo
A plataforma web ***mindXcovid*** será desenvolvida para ser um prontuário de atendimento psicológico a pacientes em fase de recuperação de covid-19, facilitando a acompanhamento, exames e orientações dos pacientes, o profissional da saúde vai poder agendar, gerenciar e registrar atendimentos. Além de business inteligence a partir dos dados inseridos pelos psicológos. 
Os componenete de software, frameworks, plataformas de desenvolvimento utilizados serão descritos neste documento.

### 1.3 - Visão Geral
Este documento é dividio nas seguintes seções:
* Introdução: Explica o propósito e organização do documento.
* Representação Arquitetural: Apresenta a arquitetura adotada para desenvolver o projeto.
* Metas e Requisitos de Software: Destrincha os requisistos de usabilidade do software, e as metas mais relevantes para o sistema que será desenvolvido.
* Visão de dados: Apresentação de todos os dados e métricas da aplicação.
* Visão de Casos de uso: Apresentação de todos os casos de uso da aplicação.
* Referências bibliográficas: Material de apoio na elaboração desse documento

### 1.4 - Definições, acrônimos e abreviações

| **Sigla/Termo/Acrônimo** | **Definição** |
| ------------------------ | ------------- |
| API | Application Programming Interface | 
| OMR | Mapeamento de objeto Relacional | 
| MDS | Métodos de Desenvolvimento de Software | 
| EPS | Engenharia de Produto de Software| 
| FGA | Faculdade do Gama | 
| UnB | Universidade de Brasília | 
| DRF | Django Rest Framework |
| MTV | Model Template View |
| MVC | Model View Controller |

## 2 - Represetanção de Arquitetura
< Imagine uma imagem da arquitetura >

### 2.1 - Padrão Arquitetural
O padrão de aquitetura adotado será o MVC (Modelo Visão e Controle). Ele é um modelo que contribui na otimização da velocidade entre as requisições feitas pelo comando do usuário. Cada componente da arquitetura é construído para lidar com alguma parte específica do desenvolvimento da aplicação. Os três componentes que serão utilizados nesse projeto serão destrinchados abaixo: 
* Model : Esse componente armazena dados, e está relacionado com a parte lógica. Essa parte será desempenhada pelos framework Django e com o mySQL para a manipulação de dados.
* View: É parte da aplicação que será visível ao usuário, a apresentação dos dados. A ferramenta que fará isso no nosso projeto é o react.js.
* Controller: É parte que lida com a interação do usuário com a aplicação, ele interpreta as inputs do usuário, comunica a model e a view muda de acordo as mudanças feitas.

### 2.2 - Tecnologias
|tecnologias | descrição |
| ------------------- | ------------------- |
| Python | Linguagem para o desenvolvimento do backend |
| Django | Framework que segue a arquitetura MVC, fará comunicação do back com o banco de dados |
| MkDocs | Gerador de site estático, voltado a criação de documentações markdown
|Bootstrap |  Framework para desenvolvimento em HTML e JS. |
| React |  Biblioteca em javascript com foco em criar inteface de usuário em páginas web. |
|Docker | Criação e administração de ambientes de desenvolvimento |
|Docker-compose |  Para a comunicação dos containers criados pelo docker |
|Git | Git é um sistema de controle de versão distruibuído, com estímulos a projetos open source |
|HTML |  Será utiliza para implementação do frontend junto ao jss |
|JavaScript |  Alia-se no desenvolvimento do frontend junto com HTML e |
|mySQL | Banco de dados relacional, será usado para gerir a base de dados|

  

### 3 - Metas e Restrições da Arquitetura

#### 3.1 - Metas
* Facilitar o acompanhamento psicológico;
* Automatizar processos de agendamento, e registros de atendimentos;
* Acompanhamento no quadro de evolução dos pacientes;
* Dashboards com métricas e indicadores da saúde mental de determinada comunidade; 

#### 3.2 - Restrições da Arquitetura
* Ter acesso a internet;
* Possuir um navegador de internet (Google Chrome 60, Safari, Mozilla Firefox 55, Opera 47 e Microsoft Edge);
* Cadastro no site;

