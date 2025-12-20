## 📝 Propósito

Este documento registra las decisiones técnicas clave durante el desarrollo del **Space News API Technical Test**.

---

## 🛠️ Stack Tecnológico

* **Python 3.10**: estabilidad, compatibilidad con Django 5.
* **Django 5.x + Django REST Framework**: rápido desarrollo de APIs REST, soporte de serialización y autenticación.
* **SQLite**: base de datos ligera para pruebas y desarrollo, fácil de configurar.
* **JWT Authentication**: manejo de usuarios autenticados y favoritos de forma segura.
* **Entorno virtual (venv)**: aislamiento de dependencias.

**Decisión:** Se eligió SQLite por simplicidad y para no requerir instalación de un servidor externo en el technical test. En producción se recomendaría PostgreSQL.

---

## 📦 Estructura del Proyecto

* Se creó un esquema modular con **apps/news** y **apps/favorites** para mantener separadas la lógica de noticias y favoritos.
* Cada app incluye `models.py`, `serializers.py`, `views.py`, `urls.py` y `tests/` para facilitar pruebas unitarias.

**Decisión:** Mantener las apps independientes permite escalar el proyecto y agregar nuevas funcionalidades sin afectar otras áreas.

---

## 🌐 Consumo de API Externa

* API externa: [Spaceflight News API](https://api.spaceflightnewsapi.net/v4/articles)
* La sincronización de artículos se hace con un comando custom (`sync_news`) que filtra por reglas de negocio:

  * Solo artículos de NASA
  * Se descartan artículos con títulos que contengan SpaceX o Musk
  * Sentiment score basado en presencia de palabras clave (Mars, Moon)
  * Uso de `external_id` para evitar duplicados

**Decisión:** Implementar un comando de management permite sincronizar artículos sin depender de llamadas automáticas en tiempo real.

---

## 🧪 Pruebas Unitarias

* Se utilizan `APITestCase` de DRF.
* Se crean bases de datos temporales para tests.
* Los tests cubren:

  * Sincronización de noticias
  * Reportes mensuales
  * CRUD de favoritos (requiere autenticación JWT)

**Decisión:** Mantener los tests dentro de cada app permite ejecución independiente y asegura cobertura mínima de cada módulo.

---

## 🔒 Autenticación y Seguridad

* JWT con DRF SimpleJWT
* Endpoints públicos: `/api/reports/monthly/`
* Endpoints privados (requieren JWT): `/api/favorites/`, `/api/articles/{id}/favorite/`

**Decisión:** Separar endpoints públicos y privados permite exponer información agregada sin comprometer datos sensibles.

---

## 🖥️ Endpoints

* `/api/reports/monthly/`: reporte mensual de artículos, agregando total y sitio más frecuente.
* `/api/articles/{id}/favorite/`: marcar/desmarcar artículo como favorito.
* `/api/favorites/`: listar artículos favoritos del usuario autenticado.

**Decisión:** Mantener endpoints RESTful, claros y consistentes con la convención `resource/action`.

---

## ⚖️ Trade-offs

* SQLite para desarrollo, PostgreSQL recomendado en producción.
* Sin tareas programadas (Celery, cron) para sincronización: se hace manual con `sync_news`.
* Validación mínima de `sentiment_score` y reglas de negocio, para el cumpliiento de la prueba tecnica.
