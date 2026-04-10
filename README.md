# 🎯 Jogo-Do-BichoFull

O **BichoFull** é uma aplicação web **Full Stack** desenvolvida para fins educacionais.  
O sistema permite que usuários:

- Criem contas
- Façam login
- Gerenciem uma carteira virtual
- Realizem apostas simuladas
- Tenham seus resultados processados automaticamente
- Visualizem histórico de apostas e sorteios

⚠️ **Projeto acadêmico – sem fins comerciais.**

---

## 🛠 Tecnologias Utilizadas

### 🎨 FRONTEND
**React Vite Axios React Router DOM CSS**

- **React + Vite:** Biblioteca e ferramenta para construção de interfaces modernas e rápidas.
- **Axios:** Cliente HTTP para consumo da API.
- **React Router DOM:** Gerenciamento de rotas no frontend.
- **CSS:** Estilização da aplicação.

### 🧠 BACKEND
**FastAPI SQLAlchemy Alembic MySQL Python PyMySQL JWT**

- **FastAPI:** Framework para construção da API.
- **SQLAlchemy:** ORM para integração com o banco de dados.
- **Alembic:** Controle de migrations do banco.
- **MySQL:** Banco de dados relacional.
- **Python:** Linguagem principal do backend.
- **PyMySQL:** Driver de conexão com MySQL.
- **Passlib + Python-Jose:** Segurança, hash de senha e autenticação com token.

---

## 🏗 Arquitetura do Sistema

Arquitetura em camadas, dividida em:

### Frontend
- `pages` → telas da aplicação
- `components` → componentes reutilizáveis
- `services` → integração com a API
- `routes` → rotas do sistema
- `utils` → funções auxiliares
- `data` → dados auxiliares

### Backend
- `models` → entidades do banco de dados
- `schemas` → validações e serialização
- `routes` → endpoints da API
- `services` → regras de negócio
- `alembic` → migrations
- `testes` → testes automatizados

---

## 📌 Contrato inicial da API - Endpoints do Sistema

### 🔐 Autenticação
| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/auth/cadastrar` | Cria um novo usuário com carteira inicial |
| POST | `/auth/login` | Autentica o usuário e retorna tokens |
| POST | `/auth/login-form` | Realiza login via formulário OAuth2 |
| GET | `/auth/refresh` | Gera novo token de acesso |
| GET | `/auth/me` | Retorna os dados do usuário autenticado |

### 💰 Carteira
| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/carteira/saldo` | Retorna o saldo atual do usuário |

### 🎲 Apostas
| Método | Endpoint | Descrição |
|---|---|---|
| POST | `/apostas/apostar` | Realiza uma nova aposta e processa a rodada |
| GET | `/apostas/listar` | Lista todas as apostas do usuário autenticado |
| GET | `/apostas/historico` | Lista o histórico de apostas concluídas |

### 🎯 Sorteios
| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/sorteio/listar` | Lista os sorteios realizados |

---

## 📦 Exemplos de Payload

### 🎲 POST /apostas/apostar
Cria uma nova aposta.

### 📥 Request Body
```json
{
  "tipo": "grupo",
  "numero": "5",
  "valor": 10
}
```

### Outro exemplo de aposta
```json
{
  "tipo": "milhar",
  "numero": "1234",
  "valor": 10
}
```

---

## 🚀 Como Executar o Projeto e Configuração do Ambiente 🔧

Siga os passos abaixo para configurar o ambiente localmente.

### 1. Clonando o Repositório
```bash
git clone https://github.com/Rick-Andrade12/Projeto_bichofull.git
```

Entre na pasta:

```bash
cd Projeto_bichofull
```

> Caso o nome do repositório local esteja diferente, entre na pasta correspondente.

---

### 2. Configurando o Banco de Dados (MySQL)
Crie um banco de dados vazio chamado:

```sql
bicho_full2
```
### 2.1 Insira na tabela bichos:

```
INSERT INTO bichos (grupo, nome) VALUES
(1, 'Avestruz'),
(2, 'Águia'),
(3, 'Burro'),
(4, 'Borboleta'),
(5, 'Cachorro'),
(6, 'Cabra'),
(7, 'Carneiro'),
(8, 'Camelo'),
(9, 'Cobra'),
(10, 'Coelho'),
(11, 'Cavalo'),
(12, 'Elefante'),
(13, 'Galo'),
(14, 'Gato'),
(15, 'Jacaré'),
(16, 'Leão'),
(17, 'Macaco'),
(18, 'Porco'),
(19, 'Pavão'),
(20, 'Peru'),
(21, 'Touro'),
(22, 'Tigre'),
(23, 'Urso'),
(24, 'Veado'),
(25, 'Vaca');

```

Certifique-se de que o serviço do **MySQL** está rodando.

No backend, a conexão com o banco está configurada no arquivo:

```bash
backend/database.py
```

Exemplo atual de configuração:

```python
DATABASE_URL = "mysql+pymysql://root@127.0.0.1:3307/bicho_full2"
```

Se necessário, altere para as credenciais do seu ambiente. Exemplo:

```python
DATABASE_URL = "mysql+pymysql://root:sua_senha@127.0.0.1:3306/bicho_full2"
```

---

### 3. Configurando o Backend (FastAPI)
Entre na pasta do Backend:

```bash
cd backend
```

Crie o ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual.

No **PowerShell**:
```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Aplique as migrations:

```bash
alembic upgrade head
```

🚀 Inicie o servidor Backend:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```bash
http://127.0.0.1:8000
```

A documentação Swagger estará em:

```bash
http://127.0.0.1:8000/docs
```

---

### 4. Configurar o Frontend
Abra um novo terminal e navegue até a pasta do cliente:

```bash
cd frontend
```

Instale as dependências:

```bash
npm install
```

🚀 Inicie o servidor Frontend:

```bash
npm run dev
```

Acesse a aplicação em:

```bash
http://localhost:5173
```

---

## 🔗 Integração entre Frontend e Backend

No frontend, a API está configurada no arquivo:

```bash
frontend/src/services/api.js
```

Com a seguinte base URL:

```javascript
baseURL: "http://127.0.0.1:8000"
```

Para o sistema funcionar corretamente:

- O backend deve estar rodando na porta **8000**
- O frontend deve estar rodando na porta **5173**

---

## 📚 Sobre o Projeto

Este projeto foi desenvolvido para fins educacionais na disciplina de:

**Laboratório de Produção de Software**

---

## 👨‍🏫 Professor

**Ronem Lavareda**

---

## 🏫 Instituição

**IFAM – Campus Parintins-AM**

---

## 👤 Autor

**Henrique Beltrão de Andrade**
