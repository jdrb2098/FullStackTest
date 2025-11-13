# 🧠 Asisya API — FullStack Technical Test

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

---

## 📘 Descripción General

**Asisya API** es una aplicación backend construida con **FastAPI** que implementa una arquitectura limpia basada en principios de:

- 🧱 **Clean Architecture**
- 🧩 **Domain-Driven Design (DDD)**
- ⚙️ **CQRS (Command Query Responsibility Segregation)**
- 🧭 **Vertical Slicing**
- 💬 **Mediator Pattern**

El proyecto está diseñado para ser **modular, escalable y fácilmente extensible**, siguiendo una organización por **features** (módulos verticales).

---

## 🧰 Tecnologías Principales

| Componente | Tecnología |
|-------------|-------------|
| **Framework API** | FastAPI |
| **ORM / DB Layer** | SQLAlchemy + Alembic |
| **Base de datos** | PostgreSQL |
| **Mediator Pattern** | [`mediatr`](https://pypi.org/project/mediatr/) |
| **Validación de datos** | Pydantic v2 |
| **Autenticación** | JWT |
| **Infraestructura local** | Docker + Docker Compose |
| **Seeder / Inicialización** | Script Python (`seed_initial_data.py`) |

---

## 🏗️ Arquitectura

### 🧱 Clean Architecture

El proyecto sigue una separación clara de capas:

| Capa | Descripción |
|------|--------------|
| **Domain** | Entidades del dominio y lógica de negocio pura. |
| **Core** | Configuración global, conexión DB, base repository. |
| **Features** | Casos de uso por módulo, agrupando Commands/Queries/Controllers. |
| **Infrastructure** | Implementaciones técnicas: ORM, migraciones, almacenamiento, seeds. |
| **Crosscutting** | Utilidades transversales: logging, autorización, notificaciones. |

---

### 🧩 Vertical Slicing + CQRS

Cada **feature** contiene sus comandos, queries, modelos y controlador propios.  
Esto permite mantener independencia total entre módulos.

Ejemplo: Módulo de Categorías

```bash
features/
├── categories/
│ ├── commands/
│ │ ├── create_category_command.py
│ │ ├── update_category_command.py
│ │ └── delete_category_command.py
│ ├── queries/
│ │ ├── get_all_categories_query.py
│ │ └── get_category_by_id_query.py
│ ├── repository.py
│ ├── models.py
│ └── controller.py

```

**Beneficios:**
- Modularidad completa  
- Separación de responsabilidades (lectura/escritura)  
- Facilidad para testing e incorporación de nuevas features

---

### ⚙️ Mediator Pattern

El patrón **Mediator** (implementado con [`mediatr`](https://pypi.org/project/mediatr/)) desacopla la capa de presentación de los casos de uso:

```python
from mediatr import Mediator

query = GetAllCategoriesQuery()
result = await Mediator.send_async(query)
Cada caso de uso define su Handler con la lógica correspondiente:
@Mediator.handler
class GetAllCategoriesQueryHandler:
    def handle(self, query: GetAllCategoriesQuery):
        return self.category_repository.get_all()
```
🗂️ Estructura del Proyecto
.
```bash
.
├── core/
│   ├── base_repository.py
│   ├── config.py
│   ├── constants.py
│   └── database.py
├── crosscutting/
│   ├── authorization.py
│   ├── logging.py
│   └── notification_service.py
├── domain/
│   ├── category.py
│   ├── product.py
│   ├── role.py
│   └── user.py
├── features/
│   ├── admin/
│   ├── auth/
│   ├── categories/
│   ├── products/
│   └── user/
├── infrastructure/
│   ├── alembic/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions/
│   ├── alembic.ini
│   ├── seeds/
│   │   └── seed_initial_data.py
│   ├── storage_service.py
│   └── email_service.py
├── main.py
└── media/
    └── categories/
```

### Despliegue Local con Docker

#### Construir y levantar contenedores

```bash
docker-compose up --build
```