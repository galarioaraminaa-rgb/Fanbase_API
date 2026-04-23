# 🐟 FISHTOOL

**FastAPI Interactive Shell Tool** — a developer-friendly CLI tool to quickly scaffold, manage, and inspect FastAPI projects.  
FISHTOOL automates model and router creation, registers routes in `main.py`, and lets you list all endpoints in your project — all from the terminal.

---

## 🚀 Features

- **Project scaffolding**: Create a standard FastAPI project structure with directories for models, routers, dependencies, and internal modules.  
- **Model & router generation**: Generate SQLModel-based models and associated FastAPI routers automatically.  
- **Automatic router registration**: New routers are appended to `main.py` with proper imports and `app.include_router` calls.  
- **Endpoint listing**: List all registered routes with HTTP method and path.  
- **Interactive CLI**: All actions are available through an easy-to-use command-line interface.


Designed for speed, consistency, and zero boilerplate fatigue.
---

## 📦 Installation

```bash
git clone https://github.com/amiel103/fishtool.git
cd fishtool
py fishtool.py init
```



## ⚡ Usage
Create a new FastAPI project
```bash
python fishtool.py new
```


This will generate a project structure like:


app/ <br>
├─ main.py <br>
├─ database.py <br>
├─ dependencies.py <br>
├─ routers/ <br>
├─ models/ <br>
└─ internal/ <br>

## Create a new model and router
```bash
python fishtool.py makemodel users
```


Creates app/models/users.py with a SQLModel class.

Creates app/routers/users.py with CRUD endpoints.

Registers the router in main.py.

##  List all registered endpoints
```bash
python fishtool.py list
```


Example output:

📋 Registered Endpoints:
------------------------------------------------------------
| Router | Method | Path        |
|--------|--------|------------|
| users  | GET    | /          |
| users  | POST   | /          |
| users  | GET    | /{item_id} |
| users  | PUT    | /{item_id} |
| users  | DELETE | /{item_id} |

Total: 5 endpoints

##  🔧 Run Command


```bash
py fishtool.py serve
```


## 📦 Create Database Migrations
```bash
py fishtool.py makemigrations "add user table"
```

Uses Alembic autogeneration

Detects non-nullable columns

Prompts for default values if required

Stores latest migration reference automatically

## 🚀 Apply Migrations
```bash
py fishtool.py migrate 
```

## ⏪ Rollback Last Migration
```bash
py fishtool.py rollback 
```
Downgrades the database by one revision.





## 🐠 Why FISHTOOL?

Saves time by automating boilerplate code.

Keeps your FastAPI project structured and clean.

Ideal for small teams, solo developers, or learning FastAPI.

Easy to extend: add custom router templates, models, or CLI commands.


## 🐟 Final Words
This tool exists to remove friction, not replace understanding.
Use it to move fast — and refactor later.


📜 License

MIT License © 2025 Amiel
