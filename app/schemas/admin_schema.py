"""Schemas de administración."""

from dataclasses import dataclass


@dataclass
class CrearEspacioSchema:
    nombre: str
    id_tipo: int
    ubicacion: str
    capacidad: int
    estado: str = "DISPONIBLE"

    def validate(self) -> list[str]:
        errors = []
        if not self.nombre or not self.nombre.strip():
            errors.append("El nombre del espacio es requerido")
        elif len(self.nombre) > 100:
            errors.append("El nombre no debe exceder 100 caracteres")
        if not isinstance(self.id_tipo, int) or self.id_tipo <= 0:
            errors.append("El tipo de espacio debe ser un número positivo")
        if not self.ubicacion or not self.ubicacion.strip():
            errors.append("La ubicación es requerida")
        elif len(self.ubicacion) > 200:
            errors.append("La ubicación no debe exceder 200 caracteres")
        if not isinstance(self.capacidad, int) or self.capacidad <= 0:
            errors.append("La capacidad debe ser un número positivo")
        estados_validos = ("DISPONIBLE", "OCUPADO", "MANTENIMIENTO")
        if self.estado and self.estado not in estados_validos:
            errors.append(f"Estado inválido. Debe ser: {', '.join(estados_validos)}")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "CrearEspacioSchema":
        try:
            id_tipo = int(data.get("id_tipo", 0))
        except (ValueError, TypeError):
            id_tipo = 0
        try:
            capacidad = int(data.get("capacidad", 0))
        except (ValueError, TypeError):
            capacidad = 0
        return cls(
            nombre=data.get("nombre", "").strip(),
            id_tipo=id_tipo,
            ubicacion=data.get("ubicacion", "").strip(),
            capacidad=capacidad,
            estado=data.get("estado", "DISPONIBLE").upper(),
        )


@dataclass
class CambiarEstadoSchema:
    id_espacio: int
    estado: str

    def validate(self) -> list[str]:
        errors = []
        if not isinstance(self.id_espacio, int) or self.id_espacio <= 0:
            errors.append("El ID del espacio debe ser un número positivo")
        estados_validos = ("DISPONIBLE", "OCUPADO", "MANTENIMIENTO")
        if not self.estado or self.estado not in estados_validos:
            errors.append(f"Estado inválido. Debe ser: {', '.join(estados_validos)}")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "CambiarEstadoSchema":
        try:
            id_espacio = int(data.get("id_espacio", 0))
        except (ValueError, TypeError):
            id_espacio = 0
        return cls(
            id_espacio=id_espacio,
            estado=data.get("estado", "").upper(),
        )


@dataclass
class ActualizarEspacioSchema:
    id_espacio: int
    nombre: str
    id_tipo: int
    estado: str
    ubicacion: str
    capacidad: int
    equipamiento: list[int] | None = None
    software: list[int] | None = None

    def validate(self) -> list[str]:
        errors = []
        if not isinstance(self.id_espacio, int) or self.id_espacio <= 0:
            errors.append("El ID del espacio debe ser un número positivo")
        if not self.nombre or not self.nombre.strip():
            errors.append("El nombre del espacio es requerido")
        if not isinstance(self.id_tipo, int) or self.id_tipo <= 0:
            errors.append("El tipo de espacio debe ser un número positivo")
        estados_validos = ("DISPONIBLE", "OCUPADO", "MANTENIMIENTO")
        if self.estado not in estados_validos:
            errors.append(f"Estado inválido")
        if not self.ubicacion or not self.ubicacion.strip():
            errors.append("La ubicación es requerida")
        if not isinstance(self.capacidad, int) or self.capacidad <= 0:
            errors.append("La capacidad debe ser un número positivo")
        return errors

    @classmethod
    def from_dict(cls, data: dict) -> "ActualizarEspacioSchema":
        try:
            id_espacio = int(data.get("id_espacio", 0))
        except (ValueError, TypeError):
            id_espacio = 0
        try:
            id_tipo = int(data.get("id_tipo", 0))
        except (ValueError, TypeError):
            id_tipo = 0
        try:
            capacidad = int(data.get("capacidad", 0))
        except (ValueError, TypeError):
            capacidad = 0
        equip = data.get("equipamiento", [])
        if isinstance(equip, str):
            equip = [int(x) for x in equip.split(",") if x.strip()]
        soft = data.get("software", [])
        if isinstance(soft, str):
            soft = [int(x) for x in soft.split(",") if x.strip()]
        return cls(
            id_espacio=id_espacio,
            nombre=data.get("nombre", "").strip(),
            id_tipo=id_tipo,
            estado=data.get("estado", "DISPONIBLE").upper(),
            ubicacion=data.get("ubicacion", "").strip(),
            capacidad=capacidad,
            equipamiento=equip,
            software=soft,
        )
