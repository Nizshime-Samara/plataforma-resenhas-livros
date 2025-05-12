# plataforma-resenhas-livros
Este projeto tem como objetivo construir uma plataforma full stack moderna para cadastro e avaliação de livros. Ele utiliza autenticação via Google (OAuth2), comunicação entre microserviços, banco de dados MongoDB e um front-end em React no formato SPA (Single Page Application).

---

## 📂 [Geral] Estrutura do auth-service
```
auth-service/
├── app/
│   ├── api/v1/routes_auth.py
│   ├── adapters/google_oauth.py
│   ├── adapters/jwt_service.py
│   ├── core/config.py
```
---
# [Estrutura] auth-service - <FastAPI + OAuth2 + JWT>
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

## 🧪 Testes
- Back-End: Pytest (FastAPI) + JUnit (Spring)
- Front-End: React Testing Library
- Integração: testes manuais via Postman e automatizados com GitHub Actions

# Instalar as Dependências:
``` pip install fastapi uvicorn[standard] python-dotenv pydantic authlib python-jose[cryptography] motor ``` 

``` pip freeze > requirements.txt ```
# Testar Local :
 ### Inicie seu ambiente : ``` source venv/bin/activate ```
 ### Instale as dependências : ```` pip install fastapi uvicorn[standard] python-dotenv authlib python-jose[cryptography] motor ```
 ### Suba o serviço localmente : ``` uvicorn app.main:app --reload ``` ou se em WSL ```uvicorn app.main:app --host 0.0.0.0 --port 8000```

---
## 📝 Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).
---

## ✍️ Autoria

Projeto desenvolvido por Nizshime Samara para fins de aprendizado e prática de arquitetura de software moderna, integração entre linguagens, autenticação segura, DevOps e CI/CD com ferramentas gratuitas.
