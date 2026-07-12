"""Excepciones personalizadas del sistema."""


class AppError(Exception):
    """Error base del aplicativo."""

    def __init__(self, message: str, status_code: int = 400, code: str = "BAD_REQUEST"):
        self.message = message
        self.status_code = status_code
        self.code = code
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, entity: str = "Recurso"):
        super().__init__(
            message=f"{entity} no encontrado",
            status_code=404,
            code="NOT_FOUND",
        )


class ValidationError(AppError):
    def __init__(self, message: str, errors: list | None = None):
        self.errors = errors or []
        super().__init__(
            message=message,
            status_code=422,
            code="VALIDATION_ERROR",
        )


class UnauthorizedError(AppError):
    def __init__(self, message: str = "No autorizado"):
        super().__init__(
            message=message,
            status_code=401,
            code="UNAUTHORIZED",
        )


class ForbiddenError(AppError):
    def __init__(self, message: str = "Acceso denegado"):
        super().__init__(
            message=message,
            status_code=403,
            code="FORBIDDEN",
        )


class ConflictError(AppError):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            status_code=409,
            code="CONFLICT",
        )


class DatabaseError(AppError):
    def __init__(self, message: str = "Error de base de datos"):
        super().__init__(
            message=message,
            status_code=500,
            code="DATABASE_ERROR",
        )


class ExternalServiceError(AppError):
    def __init__(self, message: str = "Error en servicio externo", service: str = ""):
        self.service = service
        super().__init__(
            message=message,
            status_code=502,
            code="EXTERNAL_SERVICE_ERROR",
        )
