## Histórico de Versões

| Data       | Versão | Descrição            |         Autor             |
|:----------:|:------:|:--------------------:|:-------------------------:|
| 01/03/2021 | 1.0.0 | Abertura do documento | Davi e Natanel |
| 04/03/2021 | 1.1.0 | Atualização completa | Davi Matheus |
## Épicos
| ID | DESCRIÇÃO | 
|----|-----------|
| EP01 | Autenticação e Conta  |
| EP02 | Gerenciação das informações|
| EP03 | Implementação e exposição do Dashboards|


## Funcionalidades (Features)
| ID | DESCRIÇÃO | ID RELACIONADO (ÉPICOS) |
|----|-----------|----------------|
| FT01 | CRUD do psicologo | EP01 |
| FT02 | Cadastro do paciente por parte do psicologo  | EP01 |
| FT03 | Gerenciamento dos pacientes | EP02 |
| FT04 | Gerencimento dos laudos | EP02 |
| FT05 | Implementação dos graficos dos pacientes| EP02 |
| FT06 | Gerenciamento da agenda pessoal | EP02 |
| FT07 | Implementação das infomações em dashboards|EP03 |
| FT08 | Acesso aos dashboards | EP04 
## 3. User Stories
Épico|Feature|US|Descrição|Prioridade
-|-|-|-|-
E1|FT01|US06|Eu, como psicologo, gostaria de relizar o meu cadastro| ALTO 
E1|FT01|US06|Eu, como psicologo, gostaria de apagar minha conta| ALTO
E1|FT01|US06|Eu, como psicologo, gostaria de atualizar minha conta| ALTO 
E1|FT01|US05|Eu, como psicologo, gostaria de receber um email para recuperar a senha|MEDIO
E1|FT02|US07|Eu, como psicologo, gostaria de cadastrar pacientes| ALTO 
E1|FT02|US08|Eu, como psicologo, gostaria de deletar pacientes| ALTO
E1|FT03|US09|Eu, como psicologo ,gostaria de atualizar dados do paciente | ALTO
E1|FT03|US09|Eu, como psicologo ,gostaria de listar meus pacientes | BAIXO
E1|FT04|US09|Eu, como psicologo ,gostaria de inserir laudo a um paciente | MEDIO
E2|FT05|US10|Eu, como psicólogo, gostaria ver de quadro de evolução de determinado paciente.|ALTO
E2|FT06|US11|Eu, como psicologo, gostaria de ter acesso a minha agenda pessoal| ALTO
E2|FT06|US11|Eu, como psicologo, gostaria de ter acesso a um calenderio no proprio aplicativo| BAIXO
E2|FT06|US11|Eu, como psicologo, gostaria de remarcar/desmarcar consulta| MEDIO
E2|FT06|US11|Eu, como psicologo, gostaria de receber notificações das consultas| MEDIO
E2|FT06|US12|Eu, como psicologo, gostaria de visualizar as consultas passadas e futuras| MEDIO
E3|FT07|US13|Eu, como psicologo, gostaria de visualizar os dashboards| ALTO
