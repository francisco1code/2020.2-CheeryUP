## Histórico de Versões

| Data       | Versão | Descrição            |         Autor             |
|:----------:|:------:|:--------------------:|:-------------------------:|
| 01/03/2021 | 1.0.0 | Abertura do documento | Davi e Natanel |


## Épicos
| ID | DESCRIÇÃO | 
|----|-----------|
| EP01 | Como um usuário administrador, eu desejo gerenciar o sistema  |
| EP02 | Como um usuário psicologo, eu desejo gerenciar os pacientes, agenda pessoal e ter acesso as informações |
| EP03 | Como um usúario gestor, eu desejo acessar as informações do dashboard|
| EP04 | Como um usúario paciente, eu desejo dar feedbacks e acessar meus dados|


## Funcionalidades (Features)
| ID | DESCRIÇÃO | ID RELACIONADO (ÉPICOS) |
|----|-----------|----------------|
| FT01 | CRUD do usuário administrador | EP01 |
| FT02 | Acesso aos feedbacks  | EP01, EP02 |
| FT03 | CRUD do usuáro psicologo  | EP02 |
| FT04 | Gestão do paciente | EP02 |
| FT05 | Gerenciamento da agenda pessoal | EP02 |
| FT06 | Acesso aos dashboards | EP02, EP03 |
| FT07 | Acesso aos dados pessoais | EP04 |
| FT08 | Dar Feedbacks | EP04 | 


## 3. User Stories
Épico|Feature|US|Descrição|Prioridade
-|-|-|-|-
E1|FT01|US01|Eu, como administrador, gostaria de cadastrar psicologo | ALTO
E1|FT01|US01|Eu, como adminstrador, gostaria de cadastrar gestor| ALTO 
E1|FT01|US03|Eu, como adminstrador, gostaria de deletar psicologo| ALTO 
E1|FT01|US04|Eu, como adminstrador, gostaria de deletar gestor| ALTO
E1|FT02|US05|Eu, como administrador, gostaria de ter accesso aos feedbacks| BAIXO
E2|FT02|US06|Eu, como psicologo, gostaria de ter acesso aos meus feedbacks| BAIXO 
E2|FT03|US07|Eu, como psicologo, gostaria de cadastrar pacientes| ALTO 
E2|FT03|US08|Eu, como psicologo, gostaria de deletar pacientes| ALTO
E2|FT04|US09|Eu, como psicologo ,gostaria de atualizar dados do paciente | ALTO
E2|FT04|US10|Eu, como psicólogo, gostaria ver de quadro de evolução de determinado paciente.|MEDIO
E2|FT05|US11|Eu, como psicologo, gostaria de remarcar/desmarcar consulta| MEDIO
E2|FT05|US12|Eu, como psicologo, gostaria de visualizar as consultas passadas e futuras| MEDIO
E2|FT06|US13|Eu, como psicologo, gostaria de visualizar os dashboards| ALTO
E3|FT06|US14|Eu, como gestor, gostaria de visualizar os dashboards | ALTO
E4|FT07|US15|Eu, como paciente, gostaria de acessar meu historico de consulta| BAIXO
E4|FT08|US16|Eu, como paciente, gostaria de deixar comentarios/feedback para psicologo| BAIXO