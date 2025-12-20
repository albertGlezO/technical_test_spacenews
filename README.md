# 🚀 Space News API – Technical Test

API REST desarrollada con **Django + Django REST Framework** que consume artículos desde *Spaceflight News API*, los procesa bajo reglas de negocio y expone endpoints para reportes y favoritos autenticados.

---

## 🧱 Stack Tecnológico

- Python 3.10
- Django 5.x
- Django REST Framework
- SQLite (por simplicidad en el test)
- JWT Authentication

---

## 📁 Estructura del Proyecto

```bash
apps/
├── favorites/
│   ├── migrations/
│   ├── tests/
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── news/
│   ├── management/commands/sync_news.py
│   ├── migrations/
│   ├── tests/
│   ├── apps.py
│   ├── models.py
│   ├── rerializers.py
│   ├── services.py
│   ├── urls.py
│   └── views.py
│
config/
├── asgi.py
├── settings.py
├── urls.py
├── wsgi.py
.gitignore
manage.py
README.md
requirements.txt
```
---

## ⚙️ Instalación y Ejecución

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🗄️ Migraciones de Base de Datos

#### Aplicar migraciones
```bash
python manage.py migrate
```

---

## 👤 Usuarios

#### Usuario para pruebas
```bash
- username: admin
- email: admin@example.com
- password: admin123!:
```

#### Crear usuarios adicionales
```bash
python manage.py createsuperuser
```

Durante el proceso se solicitarán los siguientes datos:
- Nombre de usuario
- Correo electrónico
- Contraseña
---

## 🧪 Ejecución de Tests Unitarios

#### Ejecución de todos
```bash
python manage.py test
```

#### Ejecución de solo news
```bash
python manage.py test apps.news
```

#### Ejecución de favorities
```bash
python manage.py test apps.favorites
```

#### Notas
```bash
• Las pruebas utilizan APITestCase de Django REST Framework
• Los endpoints de favoritos requieren autenticación
• La base de datos de pruebas se crea y elimina automáticamente
• No se realizan llamadas a APIs externas durante las pruebas
```

---

## ▶️ Ejecución del Servidor de Desarrollo

#### Levantar el servidor local
```bash
python manage.py runserver
```

---

## 📰 Ejecución de Sincronización de Noticias
```bash
python manage.py sync_news --limit 500
```

#### Reglas aplicadas
- Solo artículos relacionados con NASA
- Se descartan artículos cuyo título contenga SpaceX o Musk
- sentiment_score = 1 si el título contiene Mars o Moon
- Uso de external_id para evitar duplicados

---

## 📊 Reporte Mensual
```bash
GET /api/reports/monthly/

Respuesta:

[
  {
    "month": "2025-12",
    "total": 2,
    "top_site": "NASA"
  }
]
```

---

## ⭐ Favoritos
```bash
POST /api/articles/{id}/favorite/
GET /api/favorites/
```

---


✔️ Proyecto completo según requerimientos del technical test.