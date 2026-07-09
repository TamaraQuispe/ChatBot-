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
from app.controllers.admin_controller import AdminController
from app.models.espacio import EspacioAcademico
from app.models.docente import Docente
from app.models.reserva import Reserva
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
from app.views.templates.header import HEADER_HTML
from core.logger import get_logger
from core.utils import escapar, liberar_espacios_vencidos
from core.session import create_session, get_session, make_set_cookie_header, make_clear_cookie_header

logger = get_logger("app")


class UTPHandler(BaseHTTPRequestHandler):
    def _get_usuario(self):
        return get_session(self.headers.get("Cookie"))

    def _es_admin(self):
        u = self._get_usuario()
        return u and u["rol"] == "Admin"

    def _responder_html(self, html: str, status: int = 200):
        self.send_response(status)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def _redirect(self, path: str, extra_headers: list = None):
        self.send_response(303)
        self.send_header("Location", path)
        if extra_headers:
            for k, v in extra_headers:
                self.send_header(k, v)
        self.end_headers()

    def _liberar_vencidos(self):
        try:
            db_auto = Database()
            liberar_espacios_vencidos(db_auto)
        except Exception:
            pass

    def _render_header(self, placeholder: str = "Buscador global..."):
        usuario = self._get_usuario()
        if not usuario:
            return ""
        return HEADER_HTML.replace("$SEARCH_PLACEHOLDER", placeholder).replace(
            "$AVATAR_LETTER", usuario["nombre"][0].upper()
        )

    def do_GET(self):
        self._liberar_vencidos()
        parsed_path = urllib.parse.urlparse(self.path).path
        usuario = self._get_usuario()

        if parsed_path in ("/", "/login"):
            if usuario:
                if usuario["rol"] == "Admin":
                    self._redirect("/admin")
                else:
                    self._redirect("/chat")
                return
            self._responder_html(HTML_LOGIN)

        elif parsed_path == "/chat":
            if not usuario:
                self._redirect("/login")
                return
            historial_rendered = ""
            historial = self._get_historial()
            for msg in historial:
                texto = escapar(msg.get("texto", ""))
                if msg["tipo"] == "user":
                    historial_rendered += f'''
                    <div class="flex flex-col items-end message-in">
                        <div class="max-w-[80%] text-right">
                            <p class="text-text-primary font-body-md text-[17px] leading-relaxed">{texto}</p>
                            <span class="inline-block mt-2 text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Tu • 14:20 PM</span>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "bot":
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
                    capacidad = escapar(str(d.get("capacidad", "")))
                    equipamiento = escapar(d.get("equipamiento", ""))
                    software = escapar(d.get("software", ""))
                    id_espacio = d.get("id_espacio", 0)
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
            page_rendered = HTML_CHAT.replace("$NOMBRE_DOCENTE", usuario["nombre"]).replace("$HISTORIAL_CHAT", historial_rendered)
            self._responder_html(page_rendered)

        elif parsed_path == "/admin":
            if not self._es_admin():
                self._redirect("/login")
                return
            header = self._render_header()
            page_rendered = HTML_ADMIN.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"])
            self._responder_html(page_rendered)

        elif parsed_path == "/admin/salones":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                espacios = admin.obtener_espacios()
                tipo_nombres_clase = {
                    "AULA": "AulaTeorica", "LABORATORIO": "AulaLaboratorio",
                    "SALA DE COMPUTO": "SalaComputo", "AUDITORIO": "Auditorio",
                    "TALLER": "Taller"
                }
                tipo_iconos = {
                    "AULA": "meeting_room", "LABORATORIO": "biotech",
                    "SALA DE COMPUTO": "computer", "AUDITORIO": "theater_comedy",
                    "TALLER": "handyman"
                }
                estado_map = {
                    "DISPONIBLE": ("bg-emerald-50 text-emerald-700", "bg-emerald-500", "Disponible"),
                    "OCUPADO": ("bg-amber-50 text-amber-700", "bg-amber-500", "Ocupado"),
                    "MANTENIMIENTO": ("bg-red-50 text-red-700", "bg-red-500", "Mantenimiento"),
                }
                filas_html = ""
                for e in espacios:
                    tipo_raw = e.get("tipo", "")
                    icono = tipo_iconos.get(tipo_raw, "domain")
                    tipo_clase = tipo_nombres_clase.get(tipo_raw, tipo_raw)
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
                    estado_str = e.get("estado", "DISPONIBLE")
                    ec, ed, estado_text = estado_map.get(estado_str, ("bg-surface-container-highest text-secondary", "bg-secondary", estado_str))
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group">
                    <td class="px-6 py-5">
                    <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary">
                    <span class="material-symbols-outlined">{icono}</span>
                    </div>
                    <div>
                    <p class="font-bold text-on-surface truncate max-w-[200px]">{e["nombre"]}</p>
                    <p class="text-secondary text-[12px]">{tipo_clase}</p>
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
                    <div class="flex flex-wrap gap-1">{software_tags}</div>
                    </td>
                    <td class="px-6 py-5">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full {ec} text-label-md font-bold">
                    <span class="status-dot {ed}"></span>
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
                header = self._render_header("Buscar recurso...")
                page_rendered = HTML_SALONES.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"])
                page_rendered = page_rendered.replace("$TABLA_SALONES", filas_html)
                page_rendered = page_rendered.replace("$TOTAL_SALONES", str(len(espacios)))
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/salones: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/software":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                estadisticas = admin.obtener_estadisticas()
                activos = admin.obtener_activos()
                tipo_nombres = {
                    "AULA": "AulaTeorica", "LABORATORIO": "AulaLaboratorio",
                    "SALA DE COMPUTO": "SalaComputo", "AUDITORIO": "Auditorio",
                    "TALLER": "Taller"
                }
                estado_class = {
                    "DISPONIBLE": "bg-emerald-50 text-emerald-700",
                    "OCUPADO": "bg-amber-50 text-amber-700",
                    "MANTENIMIENTO": "bg-red-50 text-red-700",
                }
                estado_dot = {
                    "DISPONIBLE": "bg-emerald-500",
                    "OCUPADO": "bg-amber-500",
                    "MANTENIMIENTO": "bg-red-500",
                }
                tipo_iconos = {"AULA": "meeting_room", "LABORATORIO": "biotech", "SALA DE COMPUTO": "computer", "AUDITORIO": "theater_comedy", "TALLER": "handyman"}
                filas_html = ""
                for a in activos:
                    id_activo = f"ACT-{a['id_espacio']:04d}"
                    tipo_raw = a.get("tipo", "")
                    icono = tipo_iconos.get(tipo_raw, "inventory_2")
                    tipo_label = tipo_nombres.get(tipo_raw, tipo_raw)
                    equipamiento = a.get("equipamiento", "") or ""
                    software_list = a.get("software", "") or ""
                    partes = [p for p in [equipamiento, software_list] if p]
                    software_str = ", ".join(partes) if partes else "N/A"
                    estado_str = a.get("estado", "DISPONIBLE")
                    ec = estado_class.get(estado_str, "bg-surface-container-highest text-secondary")
                    ed = estado_dot.get(estado_str, "bg-secondary")
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group">
                    <td class="px-6 py-5">
                    <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary">
                    <span class="material-symbols-outlined">{icono}</span>
                    </div>
                    <div>
                    <p class="font-bold text-on-surface font-mono-sm">{id_activo}</p>
                    <p class="text-secondary text-[12px]">{a["nombre"]}</p>
                    </div>
                    </div>
                    </td>
                    <td class="px-6 py-5 text-on-surface">{tipo_label}</td>
                    <td class="px-6 py-5">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full {ec} text-label-md font-bold">
                    <span class="status-dot {ed}"></span>
                    {estado_str.capitalize()}
                    </span>
                    </td>
                    <td class="px-6 py-5">
                    <span class="text-on-surface">{software_str}</span>
                    </td>
                    <td class="px-6 py-5 text-secondary font-mono-sm">-</td>
                    <td class="px-6 py-5 text-right">
                    <span class="text-secondary text-label-md">-</span>
                    </td>
                    </tr>
                    '''
                header = self._render_header("Buscar recurso...")
                page_rendered = HTML_SOFTWARE.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"])
                page_rendered = page_rendered.replace("$TABLA_SOFTWARE", filas_html)
                total_activos = estadisticas.get("total_activos", len(activos))
                page_rendered = page_rendered.replace("$TOTAL_ACTIVOS", str(total_activos))
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/software: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/horarios":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                bloques = admin.obtener_bloques_horario()
                dias_map = {"LUNES": 0, "MARTES": 1, "MIERCOLES": 2, "JUEVES": 3, "VIERNES": 4, "SABADO": 5, "DOMINGO": 6}
                headers_dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"]
                eventos_por_dia = {i: [] for i in range(7)}
                for b in bloques:
                    dia_str = b.get("dia_semana", "LUNES")
                    dia = dias_map.get(dia_str, 0)
                    if dia > 4:
                        continue
                    hora_ini = b.get("hora_inicio")
                    hora_fin = b.get("hora_fin")
                    h_i = hora_ini.hour if hasattr(hora_ini, 'hour') else 7
                    m_i = hora_ini.minute if hasattr(hora_ini, 'minute') else 0
                    h_f = hora_fin.hour if hasattr(hora_fin, 'hour') else 8
                    m_f = hora_fin.minute if hasattr(hora_fin, 'minute') else 0
                    offset_min = (h_i - 7) * 60 + m_i
                    duration_min = (h_f * 60 + m_f) - (h_i * 60 + m_i)
                    top_px = offset_min * 80 // 60
                    height_px = max(duration_min * 80 // 60, 40)
                    nombre = b.get("espacio_nombre") or b.get("nombre", "Bloque")
                    tipo = b.get("tipo", "")
                    evento = {"top": top_px, "height": height_px, "nombre": nombre, "tipo": tipo}
                    eventos_por_dia[dia].append(evento)
                contenido = ""
                for d in range(5):
                    border_class = "border-r border-surface-container-highest/30" if d < 4 else ""
                    bg_dinamico = " bg-primary-fixed/5" if d in (1, 3) else ""
                    contenido += f'<div class="{border_class}{bg_dinamico} relative" style="min-height: 800px;">'
                    for ev in eventos_por_dia[d]:
                        color_class = "bg-primary-container text-on-primary-container" if d % 2 == 0 else "bg-tertiary-container text-on-tertiary-container"
                        contenido += f'''
                        <div class="absolute left-0 right-0 m-1 p-2 {color_class} rounded-lg shadow-sm border-l-4 border-primary z-10 hover:scale-[1.02] transition-transform cursor-pointer overflow-hidden text-ellipsis whitespace-nowrap"
                             style="top: {ev["top"]}px; height: {ev["height"]}px;">
                            <span class="text-label-md font-bold">{ev["nombre"]}</span>
                            <p class="text-xs opacity-90">{ev["tipo"]}</p>
                        </div>'''
                    contenido += '</div>'
                header = self._render_header("Buscar horario...")
                page_rendered = HTML_HORARIOS.replace("$HEADER", header)
                page_rendered = page_rendered.replace("$CONTENIDO_CALENDARIO", contenido)
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/horarios: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/docentes":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                docentes = admin.obtener_docentes()
                filas_html = ""
                for d in docentes:
                    avatar = d.get("nombre", "?")[0] if d.get("nombre") else "?"
                    estado_texto = "Activo"
                    estado_color = "bg-emerald-500"
                    estado_text_class = "text-emerald-700"
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group">
                    <td class="px-6 py-4">
                    <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold">{avatar}</div>
                    <div>
                    <p class="font-bold text-on-surface">{d.get("nombre", "Sin nombre")}</p>
                    <p class="text-label-md text-secondary">ID: DOC-{d.get("id_docente", "0")}</p>
                    </div>
                    </div>
                    </td>
                    <td class="px-6 py-4">
                    <span class="bg-secondary-fixed/50 px-3 py-1 rounded-full text-label-md font-medium text-on-secondary-fixed-variant">{d.get("departamento", "No asignado")}</span>
                    </td>
                    <td class="px-6 py-4">
                    <span class="text-body-md text-on-surface-variant">{d.get("especialidad", "General")}</span>
                    </td>
                    <td class="px-6 py-4">
                    <div class="flex flex-col">
                    <span class="text-body-md flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">mail</span> {d.get("correo", "N/A")}</span>
                    <span class="text-label-md text-secondary">{d.get("telefono", "N/A")}</span>
                    </div>
                    </td>
                    <td class="px-6 py-4">
                    <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full {estado_color}"></div>
                    <span class="text-label-md font-medium {estado_text_class}">{estado_texto}</span>
                    </div>
                    </td>
                    <td class="px-6 py-4 text-right">
                    <button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">more_vert</button>
                    </td>
                    </tr>
                    '''
                header = self._render_header("Buscar docente, curso o ID...")
                page_rendered = HTML_DOCENTES.replace("$HEADER", header).replace("$TABLA_DOCENTES", filas_html)
                page_rendered = page_rendered.replace("$TOTAL_DOCENTES", str(len(docentes)))
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/docentes: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/reservas":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                reservas = admin.obtener_reservas()
                filas_html = ""
                for r in reservas:
                    iniciales = (r.get("usuario_nombre", "??")[:2]).upper()
                    depto = r.get("username", "")
                    estado_raw = r.get("estado", "PENDIENTE")
                    if estado_raw == "CONFIRMADA":
                        estado_text = "Confirmada"
                        estado_class = "bg-green-50 text-green-700 border-green-100"
                    elif estado_raw == "CANCELADA":
                        estado_text = "Cancelada"
                        estado_class = "bg-red-50 text-red-700 border-red-100"
                    elif estado_raw == "RECHAZADA":
                        estado_text = "Rechazada"
                        estado_class = "bg-red-50 text-red-700 border-red-100"
                    else:
                        estado_text = "Pendiente"
                        estado_class = "bg-amber-50 text-amber-700 border-amber-100"
                    acciones = ""
                    if estado_raw == "CONFIRMADA":
                        acciones = '<span class="text-[11px] text-secondary italic">Confirmada</span>'
                    else:
                        acciones = f'''
                        <div class="flex justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                        <form method="POST" action="/admin/aprobar_reserva" class="inline">
                        <input type="hidden" name="id_reserva" value="{r["id_reserva"]}">
                        <button class="w-8 h-8 flex items-center justify-center rounded-full bg-emerald-500 text-white hover:shadow-lg transition-all" title="Aprobar">
                        <span class="material-symbols-outlined text-sm">check</span>
                        </button>
                        </form>
                        <form method="POST" action="/admin/rechazar_reserva" class="inline">
                        <input type="hidden" name="id_reserva" value="{r["id_reserva"]}">
                        <button class="w-8 h-8 flex items-center justify-center rounded-full bg-primary text-white hover:shadow-lg transition-all" title="Rechazar">
                        <span class="material-symbols-outlined text-sm">close</span>
                        </button>
                        </form>
                        </div>
                        '''
                    filas_html += f'''
                    <tr class="group hover:bg-surface-container-low/50 transition-colors">
                    <td class="py-4">
                    <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded-full bg-secondary-fixed flex items-center justify-center text-on-secondary-fixed font-bold text-xs">{iniciales}</div>
                    <div>
                    <div class="font-body-md text-body-md font-semibold">{r.get("usuario_nombre", "Desconocido")}</div>
                    <div class="text-[11px] text-secondary">{depto}</div>
                    </div>
                    </div>
                    </td>
                    <td class="py-4">
                    <div class="font-body-md text-body-md">{r.get("espacio_nombre", "N/A")}</div>
                    <div class="text-[11px] text-secondary">{r.get("tipo", "")}</div>
                    </td>
                    <td class="py-4">
                    <div class="font-body-md text-body-md">{r.get("fecha", "N/A")}</div>
                    <div class="text-[11px] text-secondary">{r.get("horario", "")}</div>
                    </td>
                    <td class="py-4">
                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium {estado_class}">{estado_text}</span>
                    </td>
                    <td class="py-4 text-right">{acciones}</td>
                    </tr>
                    '''
                header = self._render_header("Buscar reserva...")
                page_rendered = HTML_RESERVAS.replace("$HEADER", header).replace("$TABLA_RESERVAS", filas_html)
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/reservas: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/reportes":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                estadisticas = admin.obtener_estadisticas()
                facultades = admin.obtener_facultades()
                iconos = ["precision_manufacturing", "business_center", "science", "school", "health_and_safety", "account_balance"]
                icon_bgs = ["bg-red-50", "bg-gray-50", "bg-blue-50", "bg-green-50", "bg-purple-50", "bg-amber-50"]
                icon_colors = ["text-primary", "text-secondary", "text-blue-600", "text-green-600", "text-purple-600", "text-amber-600"]
                filas_html = ""
                for i, f in enumerate(facultades):
                    idx = i % len(iconos)
                    ocupados = f["total_espacios"] - f["disponibles"]
                    tasa = round((ocupados / f["total_espacios"] * 100) if f["total_espacios"] > 0 else 0, 1)
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-lowest transition-colors">
                    <td class="p-4">
                    <div class="flex items-center gap-3">
                    <div class="w-8 h-8 rounded {icon_bgs[idx]} flex items-center justify-center {icon_colors[idx]}">
                    <span class="material-symbols-outlined text-[20px]">{iconos[idx]}</span>
                    </div>
                    <div>
                    <p class="font-medium text-body-md">{f["nombre"]}</p>
                    <p class="text-[12px] text-secondary">{f["total_espacios"]} espacios - {f["reservas"]} reservas</p>
                    </div>
                    </div>
                    </td>
                    <td class="p-4 text-body-md">{tasa}%</td>
                    <td class="p-4 text-body-md">{f["reservas"]}</td>
                    <td class="p-4">
                    <svg class="sparkline-red" height="20" width="80">
                    <polyline points="0,{max(5, 20-tasa/5)} 20,{max(5, 20-tasa/5)} 40,{max(5, 20-tasa/5)} 60,{max(5, 20-tasa/5)} 80,{max(5, 20-tasa/5)}"></polyline>
                    </svg>
                    </td>
                    <td class="p-4 text-right">
                    <button class="material-symbols-outlined text-secondary hover:text-primary transition-all">more_vert</button>
                    </td>
                    </tr>
                    '''
                header = self._render_header("Buscar reporte...")
                page_rendered = HTML_REPORTES.replace("$HEADER", header).replace("$TABLA_FACULTADES", filas_html)
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/reportes: {e}")
                self._redirect("/admin")

        elif parsed_path == "/admin/roles":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                admin = AdminController(db)
                estadisticas = admin.obtener_estadisticas()
                usuarios = admin.obtener_usuarios()
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
                filas_usuarios = ""
                roles_iconos = {"Admin": "admin_panel_settings", "Docente": "school", "Estudiante": "person"}
                roles_colores = {"Admin": "bg-purple-50 text-purple-700", "Docente": "bg-blue-50 text-blue-700", "Estudiante": "bg-green-50 text-green-700"}
                for u in usuarios:
                    rol = u.get("rol", "Estudiante")
                    avatar = (u.get("nombre", "?")[:2]).upper() if u.get("nombre") else "??"
                    estado_u = u.get("estado", 1)
                    estado_text = "Activo" if estado_u == 1 else "Inactivo"
                    estado_dot = "bg-emerald-500" if estado_u == 1 else "bg-red-500"
                    filas_usuarios += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group">
                    <td class="px-6 py-4">
                    <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-sm">{avatar}</div>
                    <div>
                    <p class="font-bold text-on-surface">{u["nombre"]}</p>
                    <p class="text-label-md text-secondary">@{u.get("username", "")}</p>
                    </div>
                    </div>
                    </td>
                    <td class="px-6 py-4">
                    <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full {roles_colores.get(rol, 'bg-surface-container-highest text-secondary')} text-label-md font-bold">
                    <span class="material-symbols-outlined text-[14px]">{roles_iconos.get(rol, "person")}</span>
                    {rol}
                    </span>
                    </td>
                    <td class="px-6 py-4">
                    <div class="flex items-center gap-2">
                    <div class="w-2 h-2 rounded-full {estado_dot}"></div>
                    <span class="text-label-md font-medium">{estado_text}</span>
                    </div>
                    </td>
                    <td class="px-6 py-4 text-right">
                    <button class="p-2 hover:bg-surface-container-low rounded-lg text-secondary transition-colors">
                    <span class="material-symbols-outlined text-[20px]">more_vert</span>
                    </button>
                    </td>
                    </tr>
                    '''
                header = self._render_header("Buscar usuario...")
                page_rendered = HTML_ROLES.replace("$HEADER", header).replace("$FILAS_PERMISOS", filas_permisos)
                page_rendered = page_rendered.replace("$TABLA_USUARIOS", filas_usuarios)
                self._responder_html(page_rendered)
            except Exception as e:
                logger.error(f"Error en /admin/roles: {e}")
                self._redirect("/admin")

        elif parsed_path == "/logout":
            self._redirect("/login", [("Set-Cookie", make_clear_cookie_header())])

        else:
            self.send_response(404)
            self.end_headers()

    def _get_historial(self):
        from http.cookies import SimpleCookie
        import json
        cookie = self.headers.get("Cookie", "")
        try:
            c = SimpleCookie()
            c.load(cookie)
            if "utp_historial" in c:
                raw = urllib.parse.unquote(c["utp_historial"].value)
                return json.loads(raw)
        except Exception:
            pass
        return []

    def _set_historial(self, historial: list):
        import json
        raw = json.dumps(historial, default=str)
        encoded = urllib.parse.quote(raw)
        return f"utp_historial={encoded}; Path=/; Max-Age=86400"

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            db = Database()
            parsed_path_post = urllib.parse.urlparse(self.path).path

            if parsed_path_post == "/login":
                auth = AuthController(db)
                username = params.get("username", [""])[0]
                password = params.get("password", [""])[0]
                usuario = auth.login(username, password)
                if usuario:
                    cookie = make_set_cookie_header(usuario)
                    if usuario["rol"] == "Admin":
                        self._redirect("/admin", [("Set-Cookie", cookie)])
                    else:
                        historial = [
                            {"tipo": "bot", "texto": f"Hola, {escapar(usuario['nombre'])}. Soy el Asistente Academico UTP. ¿Que aula o reprogramacion deseas gestionar hoy?"}
                        ]
                        hist_cookie = self._set_historial(historial)
                        self._redirect("/chat", [("Set-Cookie", cookie), ("Set-Cookie", hist_cookie)])
                else:
                    self._redirect("/login?error=1")
                return

            usuario = self._get_usuario()
            if not usuario:
                self._redirect("/login")
                return

            if parsed_path_post == "/query":
                prompt = params.get("prompt", [""])[0]
                if not prompt.strip():
                    self._redirect("/chat")
                    return
                historial = self._get_historial()
                historial.append({"tipo": "user", "texto": prompt})

                reserva_ctrl = ReservaController(db)
                aulas = reserva_ctrl.buscar_disponibilidad(prompt)

                ollama = OllamaService()
                contexto = f"Salones disponibles: {[dict(a) for a in aulas]}" if aulas else "No hay disponibilidad"
                respuesta = ollama.consultar(prompt, contexto)

                if aulas:
                    historial.append({"tipo": "card", "data": dict(aulas[0])})
                else:
                    historial.append({"tipo": "bot", "texto": respuesta})

                self._redirect("/chat", [self._set_historial(historial)])

            elif parsed_path_post == "/reservar":
                id_espacio = int(params.get("id_espacio", [0])[0])
                nombre_aula = params.get("nombre_aula", [""])[0]

                reserva_ctrl = ReservaController(db)
                exito = reserva_ctrl.procesar_reserva(
                    usuario["id_usuario"], "Curso Demostracion UTP", id_espacio, "15:00 - 17:00"
                )

                historial = self._get_historial()
                if exito:
                    historial.append({"tipo": "success", "texto": nombre_aula})
                    logger.info(f"Reserva exitosa: espacio={id_espacio}, usuario={usuario['id_usuario']}")

                self._redirect("/chat", [self._set_historial(historial)])

            elif parsed_path_post == "/admin/aprobar_reserva":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_reserva = int(params.get("id_reserva", [0])[0])
                admin = AdminController(db)
                admin.aprobar_reserva(id_reserva)
                self._redirect("/admin/reservas")

            elif parsed_path_post == "/admin/rechazar_reserva":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_reserva = int(params.get("id_reserva", [0])[0])
                admin = AdminController(db)
                admin.rechazar_reserva(id_reserva)
                self._redirect("/admin/reservas")

            else:
                self._redirect("/chat")

        except Exception as e:
            logger.error(f"Error en POST {self.path}: {e}")
            self._redirect("/login")

    def redirect(self, path):
        self._redirect(path)


def iniciar_servidor():
    try:
        inicializar_bd()
        port = int(os.environ.get("PORT", 8000))
        server_address = ('', port)
        httpd = HTTPServer(server_address, UTPHandler)
        logger.info(f"Servidor UTP iniciado en http://localhost:{port}")
        logger.info("Usando PostgreSQL en la nube (Supabase)")
        httpd.serve_forever()
    except Exception as e:
        logger.error(f"Error iniciando servidor: {e}")
        raise


if __name__ == "__main__":
    import sys, traceback
    try:
        iniciar_servidor()
    except SystemExit:
        raise
    except:
        with open('/tmp/opencode_error.log', 'w') as f:
            traceback.print_exc(file=f)
        raise
