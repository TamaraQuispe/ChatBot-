import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from config.database import Database

def seed():
    try:
        db = Database()
        conn = db.obtener_conexion()
        cursor = conn.cursor()
        
        # Bloques de prueba distribuidos en varios días
        bloques = [
            ("Base de Datos (Test)", "08:00", "10:00", "MARTES", "Diurno"),
            ("Ingeniería de Software (Test)", "10:00", "12:00", "MARTES", "Diurno"),
            ("Inteligencia Artificial (Test)", "14:00", "16:00", "MIERCOLES", "Tarde"),
            ("Seguridad Informática (Test)", "16:00", "18:00", "JUEVES", "Tarde"),
            ("Desarrollo Web (Test)", "08:00", "10:00", "VIERNES", "Diurno"),
            ("Taller de Proyectos (Test)", "11:00", "13:00", "VIERNES", "Diurno")
        ]
        
        print("Insertando bloques de horario...")
        for b in bloques:
            cursor.execute(
                "INSERT INTO bloques_horario (nombre, hora_inicio, hora_fin, dia_semana, turno) "
                "VALUES (%s, %s, %s, %s, %s)",
                b
            )
            print(f" -> {b[0]} ({b[3]})")
            
        conn.commit()
        conn.close()
        print("\n¡Datos insertados correctamente")
        
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        raise

if __name__ == '__main__':
    seed()
