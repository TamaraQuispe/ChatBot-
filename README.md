# ChatBot - Asistente Académico UTP

Sistema de gestión de reservas de espacios académicos con chatbot para la Universidad Tecnológica del Perú (UTP).

## Stack

- **Backend**: Python 3 (http.server, WSGI)
- **Base de datos**: PostgreSQL (Neon)
- **Despliegue**: Vercel (serverless)
- **Autenticación**: bcrypt + cookies con HMAC

## Credenciales

| Usuario   | Contraseña | Rol     |
|-----------|-----------|---------|
| atorres   | admin123  | Admin   |
| C23204737 | utp123    | Docente |
| C23204738 | utp123    | Docente |

## Estructura

```
api/index.py       → WSGI wrapper para Vercel
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

## Desarrollo local

```bash
python3 app.py
# Servidor en http://localhost:8000
```

## Despliegue en Vercel

```bash
https://chatbot-tau-five-21.vercel.app/
```

Requiere variable de entorno `DATABASE_URL` con la conexión a PostgreSQL.
