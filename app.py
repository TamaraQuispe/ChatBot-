"""
* @file app.py
* @author Omara Baylón
* @description Servidor HTTP real multi-pantalla usando layouts Tailwind CSS inyectados.
"""
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from config.database import Database
from app.models import inicializar_bd
from app.controllers.auth_controller import AuthController
from app.controllers.reserva_controller import ReservaController
from app.models.espacio import EspacioAcademico
from app.services.ollama_service import OllamaService
from app.views.templates.login_html import HTML_LOGIN
from app.views.templates.chat_html import HTML_CHAT
from app.views.templates.admin_html import HTML_ADMIN
from app.views.templates.salones_html import HTML_SALONES
from app.views.templates.software_html import HTML_SOFTWARE
from app.views.templates.horarios_html import HTML_HORARIOS
from app.views.templates.docentes_html import HTML_DOCENTES
from app.views.templates.reservas_html import HTML_RESERVAS
from app.views.templates.reportes_html import HTML_REPORTES
from app.views.templates.roles_html import HTML_ROLES
from core.logger import get_logger
from core.utils import escapar

logger = get_logger("app")

# Estado global de sesión en memoria para fines de la demo local
SESSION = {"autenticado": False, "usuario": None, "historial": []}

class UTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/login":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_LOGIN.encode("utf-8"))
        elif self.path == "/chat":
            if not SESSION["autenticado"]:
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            
            # Construir el HTML dinámico del chat basándose en el historial
            historial_rendered = ""
            for msg in SESSION["historial"]:
                if msg["tipo"] == "user":
                    texto = escapar(msg["texto"])
                    historial_rendered += f'''
                    <div class="flex flex-col items-end message-in">
                        <div class="max-w-[80%] text-right">
                            <p class="text-text-primary font-body-md text-[17px] leading-relaxed">{texto}</p>
                            <span class="inline-block mt-2 text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Tu • 14:20 PM</span>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "bot":
                    texto = escapar(msg["texto"])
                    historial_rendered += f'''
                    <div class="flex items-start gap-6 message-in">
                        <div class="w-10 h-10 rounded-xl bg-utp-red-institutional flex items-center justify-center flex-shrink-0 shadow-lg shadow-utp-red-institutional/20 mt-1">
                            <span class="material-symbols-outlined text-[22px] text-white" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
                        </div>
                        <div class="flex-1 space-y-4">
                            <div class="glass-dark p-7 rounded-3xl rounded-tl-none shadow-sm">
                                <p class="text-text-primary font-body-md text-[17px] leading-relaxed">{texto}</p>
                            </div>
                            <span class="inline-block text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Asistente • 14:21 PM</span>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "card":
                    d = msg["data"]
                    nombre = escapar(d["nombre"])
                    ubicacion = escapar(d["ubicacion"])
                    capacidad = escapar(d["capacidad"])
                    equipamiento = escapar(d["equipamiento"])
                    software = escapar(d["software"])
                    id_espacio = d["id_espacio"]
                    historial_rendered += f'''
                    <div class="flex items-start gap-6 message-in">
                        <div class="w-10 h-10 rounded-xl bg-utp-red-institutional flex items-center justify-center flex-shrink-0 shadow-lg shadow-utp-red-institutional/20 mt-1">
                            <span class="material-symbols-outlined text-[22px] text-white" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
                        </div>
                        <div class="flex-1 space-y-4">
                            <div class="bg-white rounded-[32px] shadow-[0_12px_40px_rgba(0,0,0,0.04)] border border-black/5 overflow-hidden group hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)] transition-all duration-500">
                                <div class="p-8">
                                    <div class="flex justify-between items-start mb-8">
                                        <div>
                                            <div class="flex items-center gap-2 mb-1">
                                                <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                                                <span class="text-[11px] font-bold text-green-600 uppercase tracking-widest">Disponible Ahora</span>
                                            </div>
                                            <h3 class="font-headline-lg text-[26px] text-text-primary">{nombre}</h3>
                                            <p class="text-text-secondary text-sm flex items-center gap-1.5 mt-1 font-medium">
                                                <span class="material-symbols-outlined text-[18px]">location_on</span>
                                                {ubicacion}
                                            </p>
                                        </div>
                                        <div class="w-14 h-14 rounded-2xl bg-utp-red-institutional/5 flex items-center justify-center text-utp-red-institutional">
                                            <span class="material-symbols-outlined text-[32px]">computer</span>
                                        </div>
                                    </div>
                                    <div class="grid grid-cols-2 gap-y-8 gap-x-12 mb-10">
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center text-text-secondary/80">
                                                <span class="material-symbols-outlined">groups</span>
                                            </div>
                                            <div>
                                                <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider mb-0.5">Capacidad</p>
                                                <p class="text-text-primary font-bold text-[15px]">{capacidad} Alumnos</p>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center text-text-secondary/80">
                                                <span class="material-symbols-outlined">memory</span>
                                            </div>
                                            <div>
                                                <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider mb-0.5">Hardware</p>
                                                <p class="text-text-primary font-bold text-[15px]">{equipamiento}</p>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center text-text-secondary/80">
                                                <span class="material-symbols-outlined">code</span>
                                            </div>
                                            <div>
                                                <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider mb-0.5">Software</p>
                                                <p class="text-text-primary font-bold text-[15px]">{software}</p>
                                            </div>
                                        </div>
                                        <div class="flex items-center gap-4">
                                            <div class="w-12 h-12 rounded-2xl bg-surface flex items-center justify-center text-text-secondary/80">
                                                <span class="material-symbols-outlined">schedule</span>
                                            </div>
                                            <div>
                                                <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider mb-0.5">Horario</p>
                                                <p class="text-text-primary font-bold text-[15px]">Miercoles 15:00 - 17:00</p>
                                            </div>
                                        </div>
                                    </div>
                                    <form method="POST" action="/reservar">
                                        <input type="hidden" name="id_espacio" value="{id_espacio}">
                                        <input type="hidden" name="nombre_aula" value="{nombre}">
                                        <button type="submit" class="w-full py-4.5 bg-utp-red-institutional text-white font-bold rounded-[20px] transition-all hover:bg-primary hover:shadow-xl hover:shadow-utp-red-institutional/20 flex items-center justify-center gap-3 active:scale-[0.98]">
                                            <span class="material-symbols-outlined text-[20px]" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                                            Confirmar Reserva
                                        </button>
                                    </form>
                                </div>
                            </div>
                            <span class="inline-block text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Asistente • 14:21 PM</span>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "success":
                    texto = escapar(msg["texto"])
                    historial_rendered += f'''
                    <div class="flex items-start gap-6 message-in">
                        <div class="w-10 h-10 rounded-xl bg-green-500 flex items-center justify-center flex-shrink-0 shadow-lg shadow-green-500/20 mt-1">
                            <span class="material-symbols-outlined text-[22px] text-white" style="font-variation-settings: 'FILL' 1;">check_circle</span>
                        </div>
                        <div class="flex-1">
                            <div class="bg-green-50 border border-green-200 p-7 rounded-3xl rounded-tl-none shadow-sm">
                                <p class="font-bold text-[17px] text-green-800 mb-1">Reserva Confirmada Exitosamente</p>
                                <p class="text-sm text-green-700">El ambiente <strong>{texto}</strong> ha sido asignado correctamente.</p>
                            </div>
                            <span class="inline-block mt-2 text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Sistema • Confirmado</span>
                        </div>
                    </div>
                    '''

            # Renderizar la vista final
            page_rendered = HTML_CHAT.replace("$NOMBRE_DOCENTE", SESSION["usuario"]["nombre"]).replace("$HISTORIAL_CHAT", historial_rendered)
            
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            page_rendered = HTML_ADMIN.replace("$NOMBRE_ADMIN", SESSION["usuario"]["nombre"])
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/salones":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            db = Database()
            espacio_model = EspacioAcademico(db)
            espacios = espacio_model.listar_todos()

            iconos = {"COMPUTO": "computer", "TEORICA": "meeting_room"}
            filas_html = ""
            for e in espacios:
                icono = iconos.get(e["tipo"], "domain")
                software = e.get("software", "")
                software_tags = ""
                if software and software != "Ninguno":
                    parts = [s.strip() for s in software.split(",")]
                    for s in parts[:3]:
                        software_tags += f'<span class="px-2 py-0.5 bg-surface-container-highest text-[11px] rounded-full text-secondary">{s}</span>'
                    if len(parts) > 3:
                        software_tags += f'<span class="px-2 py-0.5 bg-surface-container-highest text-[11px] rounded-full text-secondary">+{len(parts)-3}</span>'
                else:
                    software_tags = '<span class="text-secondary italic text-label-md">N/A</span>'

                if e["estado"] == "DISPONIBLE":
                    estado_class = "bg-emerald-50 text-emerald-700"
                    estado_dot = "bg-emerald-500"
                    estado_text = "Disponible"
                elif e["estado"] == "OCUPADO":
                    estado_class = "bg-amber-50 text-amber-700"
                    estado_dot = "bg-amber-500"
                    estado_text = "Ocupado"
                else:
                    estado_class = "bg-error-container/20 text-error"
                    estado_dot = "bg-error"
                    estado_text = e["estado"].capitalize()

                filas_html += f'''
                <tr class="hover:bg-surface-container-low/30 transition-colors group">
                <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined">{icono}</span>
                </div>
                <div>
                <p class="font-bold text-on-surface">{e["nombre"]}</p>
                <p class="text-secondary text-[12px]">{e["tipo"].capitalize()}</p>
                </div>
                </div>
                </td>
                <td class="px-6 py-5 text-on-surface">{e["ubicacion"]}</td>
                <td class="px-6 py-5">
                <div class="flex items-center gap-2">
                <span class="material-symbols-outlined text-secondary text-[18px]">groups</span>
                <span class="text-on-surface font-medium">{e["capacidad"]} personas</span>
                </div>
                </td>
                <td class="px-6 py-5">
                <div class="flex flex-wrap gap-1">
                {software_tags}
                </div>
                </td>
                <td class="px-6 py-5">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full {estado_class} text-label-md font-bold">
                <span class="status-dot {estado_dot}"></span>
                {estado_text}
                </span>
                </td>
                <td class="px-6 py-5 text-right">
                <div class="flex justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button class="p-2 hover:bg-surface-container-low rounded-lg text-secondary"><span class="material-symbols-outlined text-[20px]">visibility</span></button>
                <button class="p-2 hover:bg-surface-container-low rounded-lg text-secondary"><span class="material-symbols-outlined text-[20px]">edit</span></button>
                <button class="p-2 hover:bg-surface-container-low rounded-lg text-secondary"><span class="material-symbols-outlined text-[20px]">more_vert</span></button>
                </div>
                </td>
                </tr>
                '''

            page_rendered = HTML_SALONES.replace("$NOMBRE_ADMIN", SESSION["usuario"]["nombre"])
            page_rendered = page_rendered.replace("$TABLA_SALONES", filas_html)
            page_rendered = page_rendered.replace("$TOTAL_SALONES", str(len(espacios)))
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/software":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            # Sample data rows for the Software & Equipment table
            activos = [
                {"id": "PC-LAB-302-01", "categoria": "Hardware", "estado": "Activo", "software": "Windows 11 Pro, Office 2024", "mantenimiento": "2025-06-15", "uso": "92%"},
                {"id": "SW-AUTOCAD-2025", "categoria": "Software", "estado": "Activo", "software": "AutoCAD 2025 - 45 licencias", "mantenimiento": "2025-05-01", "uso": "78%"},
                {"id": "SRV-DB-01", "categoria": "Servidor", "estado": "Mantenimiento", "software": "PostgreSQL 16, Ubuntu Server", "mantenimiento": "2025-07-10", "uso": "64%"},
                {"id": "LIC-SAP-2025", "categoria": "Licencia", "estado": "Por Vencer", "software": "SAP S/4HANA - 12 licencias", "mantenimiento": "2025-08-01", "uso": "45%"},
                {"id": "PC-AUL-105-12", "categoria": "Hardware", "estado": "Inactivo", "software": "Windows 10 Pro", "mantenimiento": "2025-03-20", "uso": "23%"},
                {"id": "SW-MATLAB-2025", "categoria": "Software", "estado": "Activo", "software": "MATLAB R2025a - 30 licencias", "mantenimiento": "2025-06-01", "uso": "81%"},
                {"id": "PROY-01", "categoria": "Equipo", "estado": "Activo", "software": "Firmware v3.2.1", "mantenimiento": "2025-06-28", "uso": "56%"},
                {"id": "LIC-ADOBE-CC", "categoria": "Licencia", "estado": "Vencido", "software": "Adobe Creative Cloud - 8 licencias", "mantenimiento": "2024-12-31", "uso": "12%"},
            ]

            estado_class = {
                "Activo": "bg-emerald-50 text-emerald-700",
                "Inactivo": "bg-surface-container-highest text-secondary",
                "Mantenimiento": "bg-amber-50 text-amber-700",
                "Por Vencer": "bg-orange-50 text-orange-700",
                "Vencido": "bg-error-container/20 text-error",
            }
            estado_dot = {
                "Activo": "bg-emerald-500",
                "Inactivo": "bg-secondary",
                "Mantenimiento": "bg-amber-500",
                "Por Vencer": "bg-orange-500",
                "Vencido": "bg-error",
            }

            iconos = {"Hardware": "computer", "Software": "code", "Servidor": "dns", "Licencia": "key", "Equipo": "videocam"}

            filas_html = ""
            for a in activos:
                icono = iconos.get(a["categoria"], "inventory_2")
                ec = estado_class.get(a["estado"], "bg-surface-container-highest text-secondary")
                ed = estado_dot.get(a["estado"], "bg-secondary")
                filas_html += f'''
                <tr class="hover:bg-surface-container-low/30 transition-colors group">
                <td class="px-6 py-5">
                <div class="flex items-center gap-4">
                <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined">{icono}</span>
                </div>
                <div>
                <p class="font-bold text-on-surface font-mono-sm">{a["id"]}</p>
                <p class="text-secondary text-[12px]">{a["categoria"]}</p>
                </div>
                </div>
                </td>
                <td class="px-6 py-5 text-on-surface">{a["categoria"]}</td>
                <td class="px-6 py-5">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full {ec} text-label-md font-bold">
                <span class="status-dot {ed}"></span>
                {a["estado"]}
                </span>
                </td>
                <td class="px-6 py-5">
                <span class="text-on-surface">{a["software"]}</span>
                </td>
                <td class="px-6 py-5 text-secondary font-mono-sm">{a["mantenimiento"]}</td>
                <td class="px-6 py-5 text-right">
                <div class="flex items-center justify-end gap-2">
                <div class="health-bar w-20">
                <div class="health-bar-fill bg-primary" style="width: {a["uso"].replace("%", "")}%"></div>
                </div>
                <span class="font-mono-sm text-secondary text-label-md w-10 text-right">{a["uso"]}</span>
                </div>
                </td>
                </tr>
                '''

            page_rendered = HTML_SOFTWARE.replace("$NOMBRE_ADMIN", SESSION["usuario"]["nombre"])
            page_rendered = page_rendered.replace("$TABLA_SOFTWARE", filas_html)
            page_rendered = page_rendered.replace("$TOTAL_ACTIVOS", str(len(activos)))
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/horarios":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            page_rendered = HTML_HORARIOS
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/docentes":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            docentes = [
                {"nombre": "Dr. Ricardo Alvares", "id": "2024-DOC-001", "depto": "Ing. Sistemas", "cursos": "Arquitectura de Software, Bases de Datos II", "email": "r.alvares@utp.edu.pe", "telefono": "+51 987 654 321", "estado": "Activo", "estado_color": "bg-emerald-500", "estado_texto": "text-emerald-700"},
                {"nombre": "MSc. Elena Montenegro", "id": "2024-DOC-012", "depto": "Derecho Corporativo", "cursos": "Derecho Civil, Arbitraje Internacional", "email": "e.montenegro@utp.edu.pe", "telefono": "+51 912 345 678", "estado": "En Licencia", "estado_color": "bg-amber-500", "estado_texto": "text-amber-700"},
                {"nombre": "Dr. Jorge Valdivia", "id": "2024-DOC-045", "depto": "Psicologia", "cursos": "Psicologia Social, Etica Profesional", "email": "j.valdivia@utp.edu.pe", "telefono": "+51 933 221 100", "estado": "Activo", "estado_color": "bg-emerald-500", "estado_texto": "text-emerald-700"},
                {"nombre": "Ing. Sofia Castro", "id": "2024-DOC-088", "depto": "Ing. Industrial", "cursos": "Gestion de Operaciones, Logistica", "email": "s.castro@utp.edu.pe", "telefono": "+51 955 887 766", "estado": "Inactivo", "estado_color": "bg-primary", "estado_texto": "text-primary"},
            ]
            filas_html = ""
            for d in docentes:
                filas_html += f'''
                <tr class="hover:bg-surface-container-low/30 transition-colors group">
                <td class="px-6 py-4">
                <div class="flex items-center gap-4">
                <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold">
                {d["nombre"][0]}
                </div>
                <div>
                <p class="font-bold text-on-surface">{d["nombre"]}</p>
                <p class="text-label-md text-secondary">ID: {d["id"]}</p>
                </div>
                </div>
                </td>
                <td class="px-6 py-4">
                <span class="bg-secondary-fixed/50 px-3 py-1 rounded-full text-label-md font-medium text-on-secondary-fixed-variant">{d["depto"]}</span>
                </td>
                <td class="px-6 py-4">
                <span class="text-body-md text-on-surface-variant">{d["cursos"]}</span>
                </td>
                <td class="px-6 py-4">
                <div class="flex flex-col">
                <span class="text-body-md flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">mail</span> {d["email"]}</span>
                <span class="text-label-md text-secondary">{d["telefono"]}</span>
                </div>
                </td>
                <td class="px-6 py-4">
                <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full {d["estado_color"]}"></div>
                <span class="text-label-md font-medium {d["estado_texto"]}">{d["estado"]}</span>
                </div>
                </td>
                <td class="px-6 py-4 text-right">
                <button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">more_vert</button>
                </td>
                </tr>
                '''
            page_rendered = HTML_DOCENTES.replace("$TABLA_DOCENTES", filas_html)
            page_rendered = page_rendered.replace("$TOTAL_DOCENTES", str(len(docentes)))
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/reservas":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            reservas = [
                {"nombre": "Dr. Marcos Arana", "iniciales": "MA", "depto": "Facultad de Ingenieria", "aula": "Laboratorio A-402", "detalle": "Capacidad: 45 personas", "fecha": "Oct 12, 2024", "hora": "08:00 - 10:00 AM", "estado": "Pendiente", "estado_class": "bg-amber-50 text-amber-700 border-amber-100"},
                {"nombre": "Lucia Panta", "iniciales": "LP", "depto": "Dpto. de Investigacion", "aula": "Auditorio Principal", "detalle": "Evento: Simposio I+D", "fecha": "Oct 14, 2024", "hora": "15:00 - 18:00 PM", "estado": "Pendiente", "estado_class": "bg-amber-50 text-amber-700 border-amber-100"},
                {"nombre": "Ricardo Salas", "iniciales": "RS", "depto": "Administracion Central", "aula": "Sala de Grados", "detalle": "Reunion de Consejo", "fecha": "Oct 12, 2024", "hora": "10:30 - 12:00 PM", "estado": "Aprobado", "estado_class": "bg-green-50 text-green-700 border-green-100"},
                {"nombre": "Elena Mendez", "iniciales": "EM", "depto": "Postgrado", "aula": "Aula Magna 1", "detalle": "Examen Final", "fecha": "Oct 15, 2024", "hora": "09:00 - 11:00 AM", "estado": "Rechazado", "estado_class": "bg-red-50 text-red-700 border-red-100"},
            ]
            filas_html = ""
            for r in reservas:
                acciones = ""
                if r["estado"] == "Pendiente":
                    acciones = '''
                    <div class="flex justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                    <button class="w-8 h-8 flex items-center justify-center rounded-full bg-emerald-500 text-white hover:shadow-lg transition-all" title="Aprobar">
                    <span class="material-symbols-outlined text-sm">check</span>
                    </button>
                    <button class="w-8 h-8 flex items-center justify-center rounded-full bg-primary text-white hover:shadow-lg transition-all" title="Rechazar">
                    <span class="material-symbols-outlined text-sm">close</span>
                    </button>
                    </div>
                    '''
                else:
                    acciones = '<span class="text-[11px] text-secondary italic">Procesado</span>'
                filas_html += f'''
                <tr class="group hover:bg-surface-container-low/50 transition-colors">
                <td class="py-4">
                <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded-full bg-secondary-fixed flex items-center justify-center text-on-secondary-fixed font-bold text-xs">{r["iniciales"]}</div>
                <div>
                <div class="font-body-md text-body-md font-semibold">{r["nombre"]}</div>
                <div class="text-[11px] text-secondary">{r["depto"]}</div>
                </div>
                </div>
                </td>
                <td class="py-4">
                <div class="font-body-md text-body-md">{r["aula"]}</div>
                <div class="text-[11px] text-secondary">{r["detalle"]}</div>
                </td>
                <td class="py-4">
                <div class="font-body-md text-body-md">{r["fecha"]}</div>
                <div class="text-[11px] text-secondary">{r["hora"]}</div>
                </td>
                <td class="py-4">
                <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium {r["estado_class"]}">
                {r["estado"]}
                </span>
                </td>
                <td class="py-4 text-right">{acciones}</td>
                </tr>
                '''
            page_rendered = HTML_RESERVAS.replace("$TABLA_RESERVAS", filas_html)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/reportes":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            facultades = [
                {"icono": "precision_manufacturing", "icon_bg": "bg-red-50", "icon_color": "text-primary", "nombre": "Ingenieria y Sistemas", "decano": "Dr. Roberto Gomez", "retencion": "92.4%", "publicaciones": "42", "sparkline": "0,15 10,12 20,18 30,5 40,8 50,2 60,7 70,3 80,6", "sparkline_class": "sparkline-red"},
                {"icono": "business_center", "icon_bg": "bg-gray-50", "icon_color": "text-secondary", "nombre": "Administracion y Negocios", "decano": "Dra. Elena Marin", "retencion": "88.1%", "publicaciones": "28", "sparkline": "0,5 15,10 30,8 45,15 60,12 80,18", "sparkline_class": "sparkline-gray"},
                {"icono": "science", "icon_bg": "bg-red-50", "icon_color": "text-primary", "nombre": "Ciencias de la Salud", "decano": "Dr. Carlos Ruiz", "retencion": "95.8%", "publicaciones": "15", "sparkline": "0,18 20,10 40,12 60,5 80,2", "sparkline_class": "sparkline-red"},
            ]
            filas_html = ""
            for f in facultades:
                filas_html += f'''
                <tr class="hover:bg-surface-container-lowest transition-colors">
                <td class="p-4">
                <div class="flex items-center gap-3">
                <div class="w-8 h-8 rounded {f["icon_bg"]} flex items-center justify-center {f["icon_color"]}">
                <span class="material-symbols-outlined text-[20px]">{f["icono"]}</span>
                </div>
                <div>
                <p class="font-medium text-body-md">{f["nombre"]}</p>
                <p class="text-[12px] text-secondary">Decano: {f["decano"]}</p>
                </div>
                </div>
                </td>
                <td class="p-4 text-body-md">{f["retencion"]}</td>
                <td class="p-4 text-body-md">{f["publicaciones"]}</td>
                <td class="p-4">
                <svg class="{f["sparkline_class"]}" height="20" width="80">
                <polyline points="{f["sparkline"]}"></polyline>
                </svg>
                </td>
                <td class="p-4 text-right">
                <button class="material-symbols-outlined text-secondary hover:text-primary transition-all">more_vert</button>
                </td>
                </tr>
                '''
            page_rendered = HTML_REPORTES.replace("$TABLA_FACULTADES", filas_html)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/admin/roles":
            if not SESSION["autenticado"] or SESSION["usuario"]["rol"] != "Admin":
                self.send_response(303)
                self.send_header("Location", "/login")
                self.end_headers()
                return
            modulos = [
                {"icono": "dashboard", "nombre": "Dashboard General", "desc": "Metricas criticas y salud del sistema", "ver": True, "crear": True, "editar": True, "borrar": False, "accion": "Exportar Data"},
                {"icono": "school", "nombre": "Gestion Academica", "desc": "Cursos, mallas y expedientes docentes", "ver": True, "crear": True, "editar": True, "borrar": True, "accion": "Anular Cierres", "accion_class": "text-primary bg-primary-container/10"},
                {"icono": "domain", "nombre": "Infraestructura", "desc": "Aulas, laboratorios y mantenimiento", "ver": True, "crear": False, "editar": False, "borrar": False, "accion": "Mapas 3D"},
            ]
            filas_permisos = ""
            for m in modulos:
                checked_ver = 'checked' if m['ver'] else ''
                checked_crear = 'checked' if m['crear'] else ''
                checked_editar = 'checked' if m['editar'] else ''
                checked_borrar = 'checked' if m['borrar'] else ''
                accion_class = m.get('accion_class', 'bg-surface-container-high text-secondary')
                filas_permisos += f'''
                <div class="grid grid-cols-12 items-center p-4 border-b border-surface-container-highest hover:bg-surface-container-lowest transition-colors">
                <div class="col-span-5 flex items-center gap-4">
                <div class="w-10 h-10 rounded bg-surface-container flex items-center justify-center text-secondary">
                <span class="material-symbols-outlined">{m["icono"]}</span>
                </div>
                <div>
                <h4 class="font-body-md font-bold">{m["nombre"]}</h4>
                <p class="text-label-md text-secondary">{m["desc"]}</p>
                </div>
                </div>
                <div class="col-span-1 flex justify-center"><input {checked_ver} class="rounded border-surface-container-highest text-primary focus:ring-primary h-5 w-5" type="checkbox"/></div>
                <div class="col-span-1 flex justify-center"><input {checked_crear} class="rounded border-surface-container-highest text-primary focus:ring-primary h-5 w-5" type="checkbox"/></div>
                <div class="col-span-1 flex justify-center"><input {checked_editar} class="rounded border-surface-container-highest text-primary focus:ring-primary h-5 w-5" type="checkbox"/></div>
                <div class="col-span-1 flex justify-center"><input {checked_borrar} class="rounded border-surface-container-highest text-primary focus:ring-primary h-5 w-5" type="checkbox"/></div>
                <div class="col-span-3 flex justify-end gap-3">
                <span class="px-2 py-1 {accion_class} rounded text-[10px] font-bold uppercase">{m["accion"]}</span>
                </div>
                </div>
                '''
            usuarios = [
                {"nombre": "Dr. Ricardo Velasquez", "email": "r.velasquez@utp.edu.pe", "rol": "Docente", "rol_color": "bg-blue-50 text-blue-600", "depto": "Ingenieria de Sistemas", "acceso": "Hoy, 09:42 AM", "estado": "Online", "estado_dot": "bg-emerald-500", "inicial": "RV"},
                {"nombre": "Ing. Maria Castro", "email": "m.castro@utp.edu.pe", "rol": "Administrador", "rol_color": "bg-primary-container/10 text-primary", "depto": "TI Central", "acceso": "Hace 2 horas", "estado": "Online", "estado_dot": "bg-emerald-500", "inicial": "MC"},
                {"nombre": "Lic. Juan Perez", "email": "j.perez@utp.edu.pe", "rol": "Personal", "rol_color": "bg-amber-50 text-amber-600", "depto": "Servicios Estudiantiles", "acceso": "Ayer, 18:15 PM", "estado": "Offline", "estado_dot": "bg-surface-dim", "inicial": "JP"},
            ]
            filas_usuarios = ""
            for u in usuarios:
                filas_usuarios += f'''
                <tr class="hover:bg-surface-container-lowest transition-colors">
                <td class="px-6 py-4">
                <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-full bg-surface-container-highest flex items-center justify-center text-secondary font-bold text-sm">{u["inicial"]}</div>
                <div>
                <p class="font-body-md font-bold text-on-surface">{u["nombre"]}</p>
                <p class="text-label-md text-secondary">{u["email"]}</p>
                </div>
                </div>
                </td>
                <td class="px-6 py-4">
                <span class="px-3 py-1 {u["rol_color"]} rounded-full text-label-md font-bold">{u["rol"]}</span>
                </td>
                <td class="px-6 py-4 text-body-md text-secondary">{u["depto"]}</td>
                <td class="px-6 py-4 text-body-md text-secondary">{u["acceso"]}</td>
                <td class="px-6 py-4">
                <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full {u["estado_dot"]}"></div>
                <span class="text-label-md font-medium text-on-surface">{u["estado"]}</span>
                </div>
                </td>
                <td class="px-6 py-4 text-right">
                <button class="p-2 text-secondary hover:text-primary"><span class="material-symbols-outlined">more_vert</span></button>
                </td>
                </tr>
                '''
            page_rendered = HTML_ROLES.replace("$FILAS_PERMISOS", filas_permisos)
            page_rendered = page_rendered.replace("$TABLA_USUARIOS", filas_usuarios)
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(page_rendered.encode("utf-8"))
        elif self.path == "/logout":
            SESSION["autenticado"] = False
            SESSION["usuario"] = None
            SESSION["historial"] = []
            self.send_response(303)
            self.send_header("Location", "/login")
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)

            db = Database()
            
            if self.path == "/login":
                auth = AuthController(db)
                username = params.get("username", [""])[0]
                password = params.get("password", [""])[0]
                
                usuario = auth.login(username, password)
                if usuario:
                    SESSION["autenticado"] = True
                    SESSION["usuario"] = usuario
                    if usuario["rol"] == "Admin":
                        self.redirect("/admin")
                    else:
                        SESSION["historial"] = [
                            {"tipo": "bot", "texto": f"Hola, {escapar(usuario['nombre'])}. Soy el Asistente Academico UTP. ¿Que aula o reprogramacion deseas gestionar hoy?"}
                        ]
                        self.redirect("/chat")
                else:
                    self.redirect("/login")
                    
            elif self.path == "/query":
                if not SESSION["autenticado"]:
                    self.redirect("/login")
                    return
                
                prompt = params.get("prompt", [""])[0]
                SESSION["historial"].append({"tipo": "user", "texto": prompt})

                reserva_ctrl = ReservaController(db)
                aulas = reserva_ctrl.buscar_disponibilidad(prompt)

                ollama = OllamaService()
                contexto = f"Salones disponibles: {[dict(a) for a in aulas]}" if aulas else "No hay disponibilidad"
                respuesta = ollama.consultar(prompt, contexto)

                if aulas:
                    SESSION["historial"].append({"tipo": "card", "data": aulas[0]})
                else:
                    SESSION["historial"].append({"tipo": "bot", "texto": respuesta})
                    
                self.redirect("/chat")
                
            elif self.path == "/reservar":
                if not SESSION["autenticado"]:
                    self.redirect("/login")
                    return
                
                id_espacio = int(params.get("id_espacio", [0])[0])
                nombre_aula = params.get("nombre_aula", [""])[0]
                
                reserva_ctrl = ReservaController(db)
                exito = reserva_ctrl.procesar_reserva(SESSION["usuario"]["id_usuario"], "Curso Demostracion UTP", id_espacio, "15:00 - 17:00")
                
                if exito:
                    SESSION["historial"].append({"tipo": "success", "texto": nombre_aula})
                
                self.redirect("/chat")
            else:
                self.redirect("/login")
        except Exception as e:
            logger.error(f"Error en POST {self.path}: {str(e)}")
            self.redirect("/login")

    def redirect(self, path):
        self.send_response(303)
        self.send_header("Location", path)
        self.end_headers()

def iniciar_servidor():
    inicializar_bd()
    port = int(os.environ.get("PORT", 8000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, UTPHandler)
    print(f"Servidor UTP activo en: http://localhost:{port}")
    print("Usando PostgreSQL en la nube (Supabase)")
    print("Abre tu navegador e ingresa a esa direccion.")
    httpd.serve_forever()

if __name__ == "__main__":
    iniciar_servidor()