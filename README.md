# Sistema de Gestão Acadêmica (LMS Advance) - Reestruturação v2.0 🚀

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)

## 📋 Sobre o Projeto

Este projeto consiste em uma API robusta para o gerenciamento de uma instituição de ensino, controlando o fluxo entre **Alunos, Professores, Cursos e Disciplinas**.

### 🔄 Motivo da Reestruturação
A versão anterior deste projeto funcionava como um monolito acoplado. Esta nova versão (v2.0) foi totalmente refatorada para atender a requisitos de escalabilidade, manutenção e segurança.

**Principais mudanças:**
* **Desacoplamento:** Separação clara de responsabilidades entre as entidades.
* **Otimização de Consultas:** Melhoria nas queries do ORM para evitar o problema de N+1.
* **Documentação:** Adição de Swagger/Redoc automática.

---

## 🏗️ Arquitetura e Tecnologias

O projeto foi reestruturado seguindo princípios de [inserir padrão, ex: Clean Architecture / MVT com Services / Microsserviços].

* **Linguagem:** Python 3.x
* **Framework:** Django 
* **Banco de Dados:** SQLite

---

## 🗂️ Estrutura de Diretórios (Nova)

A organização das pastas foi alterada para refletir a separação de contextos:

```text
/
├── apps/
│   ├── core/           # Configurações base e mixins
│   ├── academicos/     # Gestão de Alunos e Professores
│   ├── pedagogico/     # Gestão de Cursos e Disciplinas  
├── config/             # Settings do projeto
├── requirements/       # Dependências separadas (dev.txt, prod.txt)
└── manage.py
