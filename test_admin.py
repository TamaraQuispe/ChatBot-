from config.database import Database
from app.controllers.admin_controller import AdminController

def test():
    db = Database()
    admin_adm = AdminController(db)
    espacios_adm = admin_adm.obtener_espacios()
    stats = admin_adm.obtener_estadisticas()
    print("Success")

if __name__ == '__main__':
    test()
