# LMS-Advance 🎓

> **A sua Evolução Depende de Nós**

O **LMS-Advance** é um Sistema de Gestão de Aprendizagem (*Learning Management System*) desenvolvido para modernizar o processo de avaliação e acompanhamento acadêmico. O projeto visa solucionar limitações de sistemas anteriores, permitindo que professores criem atividades contínuas, apliquem testes online, gerenciem notas e forneçam feedback dinâmico aos alunos.

Este projeto foi reestruturado utilizando uma arquitetura modular em **Django**, separando responsabilidades de negócio em aplicações distintas para garantir maior coesão e baixo acoplamento.

---

## 🚀 Motivação

O desenvolvimento deste sistema foi motivado pela necessidade de:

* Viabilizar um novo sistema de avaliação que incorpore atividades contínuas.


* Facilitar a criação e correção de atividades pelos professores.


* Aumentar a transparência das avaliações e o protagonismo estudantil.


* Reduzir o número de cancelamentos de matrículas através de um melhor acompanhamento do aprendizado.



## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando uma stack robusta e moderna:

* **Backend:** Python 3, Django Framework
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap, django-bootstrap
* 
**Banco de Dados:** SGBD Relacional (modelagem adaptada para o ORM do Django).



## 🏗️ Arquitetura do Projeto

O sistema foi refatorado para seguir uma arquitetura modular, onde cada domínio do negócio reside em sua própria aplicação Django (`app`). A estrutura sugerida é:

* **`usuarios`**: Gerenciamento de Identidade e Acesso.
* Controle de perfis: Coordenador, Professor e Aluno.


* Autenticação e gestão de usuários (Login, Senha, Expiração).




* **`disciplinas`**: Gestão Acadêmica Estrutural.
* Cadastro de Cursos e Grades Curriculares.
* Gestão de Disciplinas (Ementa, Conteúdo Programático, Carga Horária).




* **`turmas`**: Planejamento Semestral.
* Gestão de Disciplinas Ofertadas (Vínculo de Professor, Ano, Semestre, Turma).




* **`matriculas`**: Vida Acadêmica do Aluno.
* Processo de Solicitação e Aprovação de Matrículas.


* Histórico e Boletins.


* **`atividades`**: A parte "Sala de Aula Virtual".
* Criação de Atividades e Testes Online.


* Entrega de trabalhos (Uploads/Links) e Correção pelo professor.


* Quadro de Avisos e Mensagens.





## 📋 Funcionalidades Principais

Conforme o escopo do projeto, o sistema permite:

### Para o Aluno

* 
**Automatrícula:** Solicitar matrícula em disciplinas ofertadas no semestre.


* 
**Dashboard:** Visualização de boletins, resultados de testes e atividades pendentes.


* 
**Atividades:** Envio de respostas para exercícios e trabalhos dentro dos prazos estipulados.



### Para o Professor

* 
**Gestão de Conteúdo:** Disponibilização de materiais (Vídeos e PDFs).


* 
**Avaliação:** Criação de atividades, correção online e lançamento de notas.


* 
**Comunicação:** Envio de mensagens e avisos para as turmas.



### Para o Coordenador

* 
**Gestão:** Aprovação de matrículas e alocação de professores em disciplinas.


* **Relatórios:** Acompanhamento de indicadores de desempenho.

## 📦 Instalação e Execução

Pré-requisitos: Python 3.x e Git instalados.

1. **Clone o repositório:**
```bash
git clone (https://github.com/renatodesouza/LMS-Advance.git)

```
# Mude para a branch de reestruturação e atualize
git checkout refactor/reestruturacao-projeto
git pull origin refactor/reestruturacao-projeto

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

```


3. **Instale as dependências:**
```bash
pip install -r requirements.txt

```


4. **Realize as migrações do banco de dados:**
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Crie um superusuário (Admin):**
```bash
python manage.py createsuperuser

```


6. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver

```



O sistema estará acessível em `http://127.0.0.1:8000/`.

## 🗂️ Modelo de Dados

O banco de dados segue uma modelagem relacional rigorosa, adaptada para as restrições do Django (uso de chaves primárias `id` auto-incrementais). As principais entidades incluem:

* `Usuario` (Centraliza o login)
* 
`Pessoa` (Generalização para Aluno, Professor, Coordenador).


* 
`Disciplina` e `DisciplinaOfertada`.


* 
`Atividade` e `Entrega`.



---

**Status do Projeto:** 🚧 Em Reestruturação / Desenvolvimento

---

