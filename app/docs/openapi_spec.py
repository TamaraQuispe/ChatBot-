"""OpenAPI 3.0 specification for the ChatBot API."""
# ruff: noqa: E501

OPENAPI_SPEC = {
    "openapi": "3.0.3",
    "info": {
        "title": "ChatBot UTP API",
        "description": "API del sistema de gestión de espacios académicos y chatbot de la UTP",
        "version": "1.0.0",
        "contact": {"name": "UTP - ChatBot Team"},
    },
    "servers": [{"url": "/", "description": "Servidor local"}],
    "paths": {
        "/login": {
            "get": {
                "summary": "Página de login",
                "tags": ["Auth"],
                "responses": {"200": {"description": "HTML del formulario de login"}},
            },
            "post": {
                "summary": "Iniciar sesión",
                "tags": ["Auth"],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/x-www-form-urlencoded": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "username": {"type": "string"},
                                    "password": {"type": "string", "format": "password"},
                                },
                                "required": ["username", "password"],
                            }
                        }
                    },
                },
                "responses": {
                    "302": {"description": "Redirección a /chat o /admin según rol"},
                    "401": {"description": "Credenciales inválidas"},
                },
            },
        },
        "/logout": {
            "get": {
                "summary": "Cerrar sesión",
                "tags": ["Auth"],
                "responses": {"302": {"description": "Redirección a /login"}},
            }
        },
        "/chat": {
            "get": {
                "summary": "Página principal del chat",
                "tags": ["Chat"],
                "responses": {"200": {"description": "HTML del chat"}},
            }
        },
        "/": {
            "get": {
                "summary": "Redirección según autenticación",
                "tags": ["General"],
                "responses": {
                    "302": {"description": "Redirección a /chat o /admin o /login"}
                },
            }
        },
        "/api/sesion/nueva": {
            "get": {
                "summary": "Crear nueva sesión de chat",
                "tags": ["Chat API"],
                "responses": {"200": {"description": "JSON con id_sesion"}},
            }
        },
        "/api/sesion/cargar": {
            "get": {
                "summary": "Cargar sesiones del usuario",
                "tags": ["Chat API"],
                "responses": {"200": {"description": "JSON con lista de sesiones"}},
            }
        },
        "/api/sesion/eliminar": {
            "get": {
                "summary": "Eliminar una sesión",
                "tags": ["Chat API"],
                "parameters": [
                    {
                        "name": "id",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {"200": {"description": "JSON con resultado"}},
            }
        },
        "/api/chat": {
            "post": {
                "summary": "Enviar mensaje al chatbot",
                "tags": ["Chat API"],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/x-www-form-urlencoded": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "mensaje": {"type": "string"},
                                    "sesion_id": {"type": "integer"},
                                    "id_espacio": {"type": "integer"},
                                },
                                "required": ["mensaje"],
                            }
                        }
                    },
                },
                "responses": {
                    "200": {"description": "Respuesta del chatbot en HTML/JSON"},
                    "400": {"description": "Mensaje vacío o inválido"},
                },
            }
        },
        "/api/notificaciones": {
            "get": {
                "summary": "Obtener notificaciones del usuario",
                "tags": ["Chat API"],
                "responses": {
                    "200": {"description": "JSON con lista de notificaciones"},
                    "401": {"description": "No autenticado"},
                },
            }
        },
        "/admin": {
            "get": {
                "summary": "Dashboard de administración",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML del dashboard"}},
            }
        },
        "/admin/salones": {
            "get": {
                "summary": "Gestión de espacios académicos",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de salones"}},
            }
        },
        "/admin/salones/editar": {
            "get": {
                "summary": "Editar un espacio académico",
                "tags": ["Admin"],
                "parameters": [
                    {
                        "name": "id",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {"200": {"description": "HTML del formulario de edición"}},
            }
        },
        "/admin/salones/historial": {
            "get": {
                "summary": "Historial de reservas de un espacio",
                "tags": ["Admin"],
                "parameters": [
                    {
                        "name": "id",
                        "in": "query",
                        "required": True,
                        "schema": {"type": "integer"},
                    }
                ],
                "responses": {"200": {"description": "HTML del historial"}},
            }
        },
        "/admin/software": {
            "get": {
                "summary": "Gestión de software",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de software"}},
            }
        },
        "/admin/horarios": {
            "get": {
                "summary": "Gestión de horarios",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de horarios"}},
            }
        },
        "/admin/docentes": {
            "get": {
                "summary": "Gestión de docentes",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de docentes"}},
            }
        },
        "/admin/reservas": {
            "get": {
                "summary": "Gestión de reservas",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de reservas"}},
            }
        },
        "/admin/reportes": {
            "get": {
                "summary": "Reportes y estadísticas",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de reportes"}},
            }
        },
        "/admin/roles": {
            "get": {
                "summary": "Gestión de roles",
                "tags": ["Admin"],
                "responses": {"200": {"description": "HTML de roles"}},
            }
        },
    },
}

COMPONENTS = {
    "components": {
        "schemas": {
            "LoginRequest": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string", "format": "password"},
                },
                "required": ["username", "password"],
            },
            "ChatRequest": {
                "type": "object",
                "properties": {
                    "mensaje": {"type": "string"},
                    "sesion_id": {"type": "integer"},
                },
                "required": ["mensaje"],
            },
            "UserResponse": {
                "type": "object",
                "properties": {
                    "id_usuario": {"type": "integer"},
                    "username": {"type": "string"},
                    "nombre": {"type": "string"},
                    "rol": {"type": "string"},
                    "correo": {"type": "string"},
                },
            },
            "EspacioResponse": {
                "type": "object",
                "properties": {
                    "id_espacio": {"type": "integer"},
                    "nombre": {"type": "string"},
                    "tipo": {"type": "string"},
                    "ubicacion": {"type": "string"},
                    "capacidad": {"type": "integer"},
                    "estado": {"type": "string"},
                },
            },
            "ReservaResponse": {
                "type": "object",
                "properties": {
                    "id_reserva": {"type": "integer"},
                    "id_usuario": {"type": "integer"},
                    "id_espacio": {"type": "integer"},
                    "curso_nombre": {"type": "string"},
                    "horario": {"type": "string"},
                    "fecha": {"type": "string"},
                    "estado": {"type": "string"},
                },
            },
        }
    }
}

OPENAPI_SPEC.update(COMPONENTS)
