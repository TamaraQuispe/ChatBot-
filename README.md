# ChatBot - Asistente Académico UTP

Sistema de gestión de reservas de espacios académicos con chatbot para la Universidad Tecnológica del Perú (UTP).

## Stack

- **Backend**: Python 3 (http.server)
- **Base de datos**: PostgreSQL (Neon)
- **Despliegue**: Render
- **Autenticación**: bcrypt + cookies con HMAC

## Credenciales

| Usuario   | Contraseña | Rol     |
|-----------|-----------|---------|
| atorres   | admin123  | Admin   |
| C23204737 | utp123    | Docente |
| C23204738 | utp123    | Docente |

## Estructura

```
server.py          → Servidor HTTP principal
app/
├── controllers/   → Lógica de negocio
├── models/        → Modelos de datos (usuario, reserva)
└── views/         → Templates HTML
config/database.py → Conexión PostgreSQL
core/
├── logger.py      → Logging con fallback a /tmp
└── utils.py       → Utilidades varias
```

## Seed

Puebla la base de datos con datos iniciales:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
DATABASE_URL="postgresql://..." python3 seed.py
```

## Despliegue en Render

[https://chatbot-x0vp.onrender.com](https://chatbot-x0vp.onrender.com)

1. Conecta el repo en https://dashboard.render.com
2. Crea un **Web Service** con:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
3. Agrega `DATABASE_URL` en Environment Variables
4. La app escucha el puerto `$PORT` automáticamente

## Desarrollo local

```bash
python3 app.py
# Servidor en http://localhost:8000
```

```bash
python3 app.py
# Servidor en http://localhost:8000
```

Requiere variable de entorno `DATABASE_URL` con la conexión a PostgreSQL.
