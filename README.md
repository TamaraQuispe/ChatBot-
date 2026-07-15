# ChatBot - Asistente Académico UTP

Sistema de gestión de reservas de espacios académicos con chatbot para la Universidad Tecnológica del Perú (UTP).

## Características

- Autenticación segura mediante bcrypt y cookies firmadas con HMAC.
- Gestión de usuarios con roles de administrador y docente.
- Reserva y administración de espacios académicos.
- Chatbot impulsado por inteligencia artificial mediante OpenRouter.
- Base de datos PostgreSQL alojada en Neon.
- Despliegue en AWS EC2 con HTTPS.

## Stack

- **Backend**: Python 3 (http.server)
- **Frontend**: HTML, CSS y JavaScript
- **Base de datos**: PostgreSQL (Neon)
- **Inteligencia Artificial**: OpenRouter (`openrouter/free`)
- **Despliegue**: AWS EC2 (Ubuntu Server, us-east-1)
- **Servidor web**: Nginx
- **Dominio**: DuckDNS
- **HTTPS**: Let's Encrypt
- **Autenticación**: bcrypt + cookies con HMAC

## Credenciales

| Usuario   | Contraseña | Rol     |
|-----------|----------- |---------|
| atorres   | admin123   | Admin   |
| C23204737 | Utp12345@  | Docente |
| C23204738 | Utp12345@  | Docente |

## Arquitectura del proyecto

```
├── app/
│   ├── auth/              # Autenticación y manejo de JWT
│   ├── controllers/       # Controladores y lógica de las rutas
│   ├── database/          # Conexión y configuración de la base de datos
│   ├── docs/              # Especificación OpenAPI
│   ├── dto/               # Objetos de transferencia de datos (DTO)
│   ├── exceptions/        # Manejo de excepciones personalizadas
│   ├── middleware/        # Middleware (CORS, Rate Limit)
│   ├── models/            # Modelos del dominio
│   ├── repositories/      # Acceso y operaciones sobre la base de datos
│   ├── schemas/           # Validación de datos
│   ├── services/          # Lógica de negocio
│   ├── tests/             # Pruebas unitarias
│   ├── utils/             # Utilidades
│   ├── validators/        # Validaciones
│   ├── views/             # Vistas y plantillas HTML
│   ├── response.py
│   ├── settings.py
│   └── logger.py
│
├── api/                   # Punto de entrada para la API
├── config/
│   └── database.py        # Configuración de PostgreSQL
├── core/
│   ├── logger.py          # Sistema de logging
│   ├── session.py         # Gestión de sesiones
│   └── utils.py           # Utilidades compartidas
│
├── public/                # Recursos públicos
├── app.py                 # Punto de entrada principal
├── server.py              # Servidor HTTP
├── seed.py                # Datos iniciales de la base de datos
├── requirements.txt       # Dependencias del proyecto
├── pyproject.toml         # Configuración del proyecto
└── README.md
```

## Seed

Puebla la base de datos con datos iniciales:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
DATABASE_URL="postgresql://..." python3 seed.py
```
## Chatbot con Inteligencia Artificial

El asistente utiliza la API de OpenRouter.

Actualmente se emplea el endpoint gratuito:

```
openrouter/free
```

## Despliegue

La aplicación se encuentra desplegada en una instancia de **AWS EC2 (us-east-1)** y está disponible en:

**https://chatbot-utp.duckdns.org**

La infraestructura de producción utiliza:

- **Servidor**: AWS EC2 (Ubuntu Server)
- **Servidor web**: Nginx como proxy inverso
- **Base de datos**: PostgreSQL (Neon)
- **Dominio**: DuckDNS
- **HTTPS**: Let's Encrypt

Para desplegar una nueva versión:

1. Clonar o actualizar el repositorio en la instancia EC2.
2. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

3. Configurar las variables de entorno requeridas (`DATABASE_URL`, `OPENROUTER_API_KEY`, `SECRET_KEY`, entre otras).
4. Reiniciar el servicio de la aplicación y Nginx si es necesario.

## Desarrollo local

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Configurar las variables de entorno necesarias:

- `DATABASE_URL`
- `OPENROUTER_API_KEY`
- `OPENROUTER_MODEL`
- `SECRET_KEY`

Iniciar la aplicación:

```bash
python app.py
# Servidor en http://localhost:8000
```
