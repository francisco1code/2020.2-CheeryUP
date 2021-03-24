# Documento de visão

## Histórico de revisão
| Data   | Versão | Modificação  | Autor  |
| :- | :- | :- | :- |
| 15/02/2021 | 1.0.0 | Abertura do Documento |  Nilvan Júnior |
| 15/02/2021 | 1.0.1 | Adição da introdução e Construção do escopo | Nilvan Júnior  |
| 16/02/2021 | 1.0.2 | Adição de Descrições da Parte interessada e do usuário (tópico 3) |  Davi Matheus |
| 16/02/2021 | 1.0.3 | Adição dos Recursos de Produto (tópico 5) | Antônio Neto |
| 17/02/2021 | 1.0.4 | Adição da Visão Geral do Produto (tópico 4)| Abraao Alves|
| 17/02/2021 | 1.0.5 | Adição das Restrições (tópico 6) | Arthur Talles |
| 17/02/2021 | 1.0.6| Adição do Posicionamento(tópico 2) |  Natanael Fernandes |
| 09/02/2021 | 1.0.7| Atualização sumário |  Nilvan Peres |

## Sumário 
[1 - Introdução](#1---Introdução)
* [1.1 - Propósito](#1.1---propósito)
* [1.2 - Escopo](#1.2---escopo)
* [1.3 - Definições, acrônomos e Abreviações](#1.3---Definições,-acrônomos-e-Abreviações)
* [1.4 - Referências](#1.4---Referências)
* [1.5 - Visão Geral](#1.5---Visão-Geral)

[2 - Posicionamento](#2---Posicionamento)
* [2.1 - Oportunidade de negócios](#2.1---Oportunidade-de-negócios)
* [2.2 - Descrição do problema](#2.2---Descrição-do-problema)
* [2.3 - Descrição de posição de produto](#2.3---Descrição-de-posição-de-produto)

[3 - Descrições da parte interessada e do usuário](#3---Descrições-da-parte-interessada-e-do-usuário)
* [3.1 - Resumo dos envolvidos](#3.1---Resumo-dos-envolvidos)
* [3.2 - Resumo dos usuários](#3.2---Resumo-dos-usuários)
* [3.3 - Perfis dos envolvidos](#3.3---Perfis-dos-envolvidos)
    * [3.3.1 - Equipe de desenvolvimento de software](#3.3.1---Equipe-de-desenvolvimento-de-software )
    * [3.3.2 - Avaliadores](#3.3.2---Avaliadores)
* [3.4 - Perfis dos usuários](#3.4---Perfis-dos-usuários)
    * [3.4.1 - Paciente](#3.4.1---Paciente)
    * [3.4.2 - Psicólogo](#3.4.2---Psicólogo)
    * [3.4.3 - Gerente](#3.4.3---Gerente)
* [3.5 - Ambiente dos usuários](#3.5---Ambiente-dos-usuários)
* [3.6 - Alternativas e concorrências](#3.6---Alternativas-e-concorrências)

[4 - Visão geral do produto](#4---Visão-geral-do-produto)
  
[5 - Recursos do produto](#5---Recursos-do-produto)

[6 - Restrições](#6---Restrições)
* [6.1 - Restrições de design](#6.1---Restrições-de-design)
* [6.2 - Restrições de implementação](#6.2---Restrições-de-implementação)
* [6.3 - Restrições de segurança](#6.3---Restrições-de-segurança)
* [6.4 - Restrições de uso](#6.4---Restrições-de-uso)

## 1 - Introdução 

### 1.1 - Propósito
O atual documento possui o intuito de apresentar o CheeryUP e destrinchar as características, requisitos e funcionalidades do produto, além entender o contexto que ele está inserido, de forma que a proposta e o escopo do projeto estejam claros.


### 1.2 - Escopo
Esse projeto tem como principal objetivo a elaboração de um prontuário eletrônico destinado ao profissional da psicologia. Possibilitando o psicólogo monitorar e analisar o estado de saúde mental da comunidade inserida no contexto da pandemia do Covid-19. Tudo isso com apoio de Dashboards e quadros de evolução.

O produto será desenvolvido em uma aplicação web, com a finalidade de acompanhar e fiscalizar a saúde mental dos pacientes. O projeto se torna viável pois oferece seus serviços respeitando as regras do distacimento social.


### 1.3 - Definições, acrônomos e Abreviações
* FGA - Faculdade do Gama (UnB)
* UnB - Universidade de Brasília
* MDS - Método de Desenvolvimento de Software 
* Prescrição - Lista de medicamentos e recomendações de saúde para um paciente


### 1.4 - Referências
IBM Knowlege Center - Documento de visão. Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSYMRC_6.0.5/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html. Acesso em: 15 fev. 2021;

### 1.5 - Visão Geral
Este documento é dividido em seis tópicos que detalham as características e planejamento de construção do produto. 
* Introdução: no qual é introduzido os detalhes gerais sobre a visão do projeto;
* Posicionamento: descrevendo o problema e a oportunidade de negócio;
* Perfis dos Envolvidos e dos Usuários:  esta seção descreve o perfil das partes interessadas no projeto;
* Recursos do Produto:  breve descrição dos recursos do produto;
* Restrições: as restrições de *design*, restrições externas, como requisitos operacionais ou regulamentares;

## 2 - Posicionamento

### 2.1 - Oportunidade de negócios 
No contexto da pandemia é notável que, após o período de isolamento e a perda de entes queridos, a parcela da população que necessita de acompanhamento psicológico aumentará de modo considerável.
Neste caso, nosso projeto tem como foco auxiliar os profissionais da psicologia a otimizarem o acesso a informações dos pacientes e, dessa forma, monitorar melhor a saúde mental de seus pacientes.
Além disso, nosso projeto gerará um dashboard que apresenta informações em tempo real sobre a saúde mental da comunidade afetada pela situação da pandemia.

### 2.2 - Descrição do problema

| O problema é  | quem afeta | cujo impacta  | possível solução  |
| :- | :- | :- | :- |
| Aumento significativo de doenças psicológicas | A sociedade e psicólogos  | a qualidade do monitoramento da saúde psicológica da sociedade | Formulários eletrônicos capazes de otimizar a vigilância da saúde mental de uma comunidade |

### 2.3 - Descrição de posição de produto

O produto finalizado é uma aplicação web e se posicionará no mercado como uma plataforma onde o profissional da psicologia terá acesso a ferramentas que o ajudará na supervisão da saúde psicológica de seus pacientes ao longo do tempo. Ferramentas como os Dashboards e quadros de evolução, que utilizarão dados dos laudos de cada paciente cadastrado pelo psicólogo.

## 3 - Descrições da parte interessada e do usuário

### 3.1 - Resumo dos envolvidos
| Nome  | Descrição | Responsabilidades |
| :- | :- | :-  |
| Equipe de desenvolvimento de Software | Estudantes da disciplina Métodos de Desenvolvimento de Software (MDS). | Desenvolvimento, Testes, Documentação e Implementações do Software. |
| Cliente | Profissionais da psicologia interessados na otimização de monitoramento da saúde mental | - |
| Coach | Estudante da UnB, monitora da disciplina Métodos de Desenvolvimento de Software (MDS). | Auxiliar a equipe durante o desenvolvimento do projeto. | 
| Professora  | Professora na Universidade de Brasília, atual professora da disciplina de MDS. | Avaliar e Auxiliar os estudantes. |

### 3.2 - Resumo dos usuários
| Nome  | Descrição |
| :- | :- |
| Psicólogos  | Todos os profissionais de psicologia que utilizam a plataforma. |

### 3.3 - Perfis dos envolvidos  

#### 3.3.1 - Equipe de desenvolvimento de software 
|  | |
| :--- | :-------- |  
| Representantes | Abraao Alves, Antônio Ferreira, Arthur Talles, Davi Matheus, Nilvan Peres, Natanael Fernandes, Lucas Ferraz. |
| Descrição | Desenvolvedores da matéria MDS. |
| Responsabilidades | Desenvolver e documentar o projeto, criar e manter documentos, desenvolver e testar softwares.
| Critérios de Sucesso | Finalizar o aplicativo no prazo determinado atendendo todos os requisitos.|
| Envolvimento | Alto. |
| Problemas/Comentários | A equipe é inexperiente em relação ao frameworks que serão utilizados ao decorrer do projeto. O grupo precisará de orientação de algum profissional da área, para estabelecer métricas e critérios.|
| - | - |

#### 3.3.2 - Avaliadores
|  | |
| :--- | :-------- |  
| Representantes | Professora Carla Silva Rocha Aguiar e monitora Gabriela Pivetta. | 
| Descrição | Professora da disciplina Métodos de Desenvolvimento de Software(MDS). |  
| Responsabilidades | Orientar e avaliar a equipe de desenvolvimento. |
| Critérios de Sucesso | Transmitir e observar o sucesso da equipe no desenvolvimento do projeto . |
| Envolvimento | Médio. |
| Problemas/Comentários | - |

### 3.4 - Perfis dos usuários  

#### 3.4.1 - Psicólogo
|  | |
| :--- | :-------- |  
| Representante | Psicólogo. |
| Descrição | Formado em psicologia e pronto para auxiliar. |
| Tipo | Formado em psicologia/afins. |
| Responsabilidade  | Monitorar e analisar o estado e evolução da saúde mental dos seus pacientes e da comunidade no geral. |
| Critérios de sucesso | Gerenciar a fim de melhorar do estado psicológico da comunidade, no contexto da pandemia. |
| Envolvimento | Alto. |
| Problemas/Comentários | - |

### 3.5 - Ambiente dos usuários
Os usuários poderão utilizar a plataforma a partir de computador ou celular por meio de uma página web.

### 3.6 - Alternativas e concorrências
Não foi encontrada nenhum aplicação para esse contexto específico do projeto.

### 4 - Visão geral do produto

O projeto irá fornecer uma plataforma web para o monitoramento e acompanhamento, por parte do psicólogo, da saúde mental de uma comunidade no contexto da pandemia. O profissional irá contar com a possibilidade de analisar laudos de consultas passadas, verificando o quadro de saúde mental de pacientes e a gravidade, além de poder adicionar novos laudos. Ademais, Dashboards e quadros de evolução irão ajudar o psicólogo na supervisão da saúde psicológica da comunidade.

### 5 - Recursos do produto
O sistema oferece as seguintes funcionalidades ao usuário:
* Cadastro de psicólogo.
* Login do psicólogo.
* Cadastro e gerenciamento de perfis de pacientes, por parte do psicólogo.
* Registro e gerenciamento de laudos.
* Inserção de informações referentes à novos laudos.
* Disponibilizar Dashboard com indicadores e métricas da saúde mental da comunidade.
* Disponibilizar aos psicólogos informações de cada paciente cadastrado. 
* Disponibilizar aos psicólogos a listagem de todos seus pacientes cadastrados.
* Avaliação e monitoramento dos resultados para fins de atenção à saúde mental no cenário epidêmico.

### 6 - Restrições

### 6.1 - Restrições de design
O design será elegante e simples, proporcional ao tempo de trabalho estimado (15 semanas), buscando atender, prioritariamente, as essencialidades do projeto.

### 6.2 - Restrições de implementação
O sistema será desenvolvido fazendo-se uso das linguagens Python, utilizando o Django para o back-end. E JavaScript, utilizando o React para o front-end.

### 6.3 - Restrições de segurança
É assegurado ao psicólogo total sigilo de suas informações pessoais, e também de seus pacientes cadastrados.

### 6.4 - Restrições de uso
Faz-se necessário o acesso à internet pelo usuário e que este possua um navegador web compatível ao sistema. Caso contrário, a página fornecerá mensagem de erro e impossibilitando seus serviços.