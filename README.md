# plataforma-resenhas-livros
Este projeto tem como objetivo construir uma plataforma full stack moderna para cadastro e avaliação de livros. Ele utiliza autenticação via Google (OAuth2), comunicação entre microserviços, banco de dados MongoDB e um front-end em React no formato SPA (Single Page Application).

# Arquitetura do Projeto:
```
[Frontend - React SPA]
        |
        v
[Auth Service - FastAPI + MongoDB Atlas] → Gera e valida JWT
        |
        +--> [Book Service - Spring Boot + MongoDB Atlas] → Gerencia livros
        |
        +--> [Review Service - FastAPI + MongoDB Atlas] → Gerencia avaliações
```
---

## 🎯 Funcionalidades

- Login com Google (OAuth2)
- Geração e validação de JWT
- Cadastro de livros
- Avaliação de livros (notas e comentários)
- Consulta pública de livros e resenhas
- Interface moderna e responsiva em React SPA

---

## ⚙️ Tecnologias Utilizadas

### Front-End
- React
- React Router DOM
- Axios
- GitHub Pages ou Vercel (para deploy)

### Back-End
- FastAPI (para Auth e Reviews)
- Spring Boot (para Books)
- MongoDB (usando MongoDB Atlas)
- JWT (para autenticação segura)
- OAuth2 (via Google)

### DevOps e CI/CD
- GitHub Actions (build, testes e deploy)
- Docker e Docker Compose (ambiente local)
- Render, Railway ou Fly.io (deploy gratuito dos serviços)

---

## 📂 [Geral] Estrutura do Projeto
```
plataforma-resenhas-livros/
├── auth-service/ # Serviço de autenticação (FastAPI + OAuth2)
├── book-service/ # Serviço de livros (Spring Boot)
├── review-service/ # Serviço de avaliações (FastAPI)
├── frontend/ # Aplicação React SPA
├── .github/workflows/ # CI/CD com GitHub Actions
└── docker-compose.yml # Infraestrutura local (MongoDB, serviços, rede)

```
---
# [Detalhamento] Estrutura de pastas monorepo do projeto
```
plataforma-resenhas-livros/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml             # Orquestração local (MongoDB + serviços)
├── .github/
│   └── workflows/                 # CI/CD GitHub Actions
│       ├── auth-service.yml
│       ├── book-service.yml
│       ├── review-service.yml
│       └── frontend.yml
│
├── services/
│   ├── auth-service/             # FastAPI + OAuth2 + JWT
│   │   └── app/
│   │       ├── api/
│   │       ├── domain/
│   │       ├── usecases/
│   │       ├── adapters/
│   │       └── core/
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── main.py
│   │   └── .env.example
│   │
│   ├── book-service/             # Spring Boot (livros)
│   │   └── src/
│   │       └── main/
│   │           └── java/
│   │               └── com/plataforma/livros/...
│   │   ├── Dockerfile
│   │   ├── pom.xml
│   │   └── .env.example
│   │
│   ├── review-service/           # FastAPI (avaliações)
│   │   └── estrutura similar ao auth-service
│
├── frontend/                     # React SPA
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   ├── .env.example
│   ├── Dockerfile
│   ├── package.json
│   └── README.md
```
---
# auth-service - <FastAPI + OAuth2 + JWT>
```
auth-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py
│   │       └── routes_auth.py
│   ├── domain/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── usecases/
│   │   ├── __init__.py
│   │   └── auth_usecase.py
│   ├── adapters/
│   │   ├── __init__.py
│   │   ├── google_oauth.py
│   │   ├── jwt_service.py
│   │   └── user_repository.py
│   └── core/
│       ├── __init__.py
│       ├── config.py
│       └── security.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── tests/
    └── test_auth.py

```
---

## 🚀 Planejamento por Etapas

### Etapa 1 - Infraestrutura e Setup
- [x] Criar repositório
- [x] Criar README e licença MIT
- [x] Criar cluster MongoDB Atlas
- [x] Criar projeto OAuth2 no Google
- [x] Iniciar o serviço de autenticação (`auth-service`)

### Etapa 2 - Autenticação e JWT
- [x] Implementar login com Google
- [x] Gerar e assinar JWT
- [x] Criar rota protegida para teste (`/me`)

### Etapa 3 - Serviço de Livros (book-service)
- [x] CRUD de livros com autenticação via token
- [x] Validação e modelagem com Spring Data MongoDB

### Etapa 4 - Serviço de Avaliações (review-service)
- [x] Cadastro de avaliações com vínculo a usuário e livro
- [x] Listagem pública de avaliações

### Etapa 5 - Front-End (React SPA)
- [x] Tela de login com Google
- [x] Página de livros
- [x] Página de avaliações
- [x] Formulários de cadastro protegidos

### Etapa 6 - CI/CD e Deploy
- [x] Criar workflows com GitHub Actions
- [x] Deploy do front-end no GitHub Pages ou Vercel
- [x] Deploy dos backends em Render ou Railway

---

## 🧪 Testes
- Back-End: Pytest (FastAPI) + JUnit (Spring)
- Front-End: React Testing Library
- Integração: testes manuais via Postman e automatizados com GitHub Actions

---

## 📝 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## ✍️ Autoria

Projeto desenvolvido por Nizshime Samara para fins de aprendizado e prática de arquitetura de software moderna, integração entre linguagens, autenticação segura, DevOps e CI/CD com ferramentas gratuitas.
