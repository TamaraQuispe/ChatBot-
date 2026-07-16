import os, json
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
from app.repositories.usuario_repository import UsuarioRepository
from app.controllers.reserva_controller import ReservaController
from app.controllers.admin_controller import AdminController
from app.models.docente import Docente
from app.models.sesion_chat import SesionChat
from app.models.notificacion import Notificacion
from app.services.openrouter_service import OpenRouterService
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
from app.docs.swagger_html import HTML_DOCS
from core.logger import get_logger
from core.utils import escapar, liberar_espacios_vencidos
from core.session import create_session, get_session, make_set_cookie_header, make_clear_cookie_header
from app.response import send_json

logger = get_logger("app")


class UTPHandler(BaseHTTPRequestHandler):
    _usuario_actual: dict | None = None
    _skip_refresh: bool = False

    def end_headers(self):
        if self._usuario_actual and not self._skip_refresh:
            self.send_header("Set-Cookie", make_set_cookie_header(self._usuario_actual))
        super().end_headers()

    def _get_usuario(self):
        u = get_session(self.headers.get("Cookie"))
        self._usuario_actual = u
        return u

    def _get_sesion_id(self) -> int:
        from http.cookies import SimpleCookie
        cookie = self.headers.get("Cookie", "")
        try:
            c = SimpleCookie()
            c.load(cookie)
            if "utp_sesion" in c:
                return int(c["utp_sesion"].value)
        except Exception:
            pass
        return 0

    def _es_admin(self):
        u = self._get_usuario()
        return u and u["rol"] == "Admin"

    def _responder_html(self, html: str, status: int = 200):
        self.send_response(status)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def _responder_json(self, data, status: int = 200):
        send_json(self, data, status)

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
            return

        elif parsed_path == "/docs":
            self._responder_html(HTML_DOCS)
            return
        elif parsed_path == "/openapi.json":
            from app.docs.openapi_spec import OPENAPI_SPEC
            raw = json.dumps(OPENAPI_SPEC, ensure_ascii=False, indent=2)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(raw.encode("utf-8"))
            return

        elif parsed_path == "/chat":
            if not usuario:
                self._redirect("/login")
                return
            historial_rendered = ""
            sesion_id = self._get_sesion_id()
            if sesion_id:
                try:
                    sc_carga = SesionChat(Database())
                    mensajes_bd = sc_carga.obtener_mensajes(sesion_id)
                    if mensajes_bd:
                        historial = []
                        for m in mensajes_bd:
                            try:
                                contenido = json.loads(m["contenido"])
                            except Exception:
                                contenido = {"texto": m["contenido"]}
                            if m["tipo"] == "card":
                                if isinstance(contenido, list):
                                    historial.append({"tipo": "aulas", "data": contenido})
                                else:
                                    historial.append({"tipo": "card", "data": contenido})
                            elif m["tipo"] == "user":
                                historial.append({"tipo": "user", "texto": contenido.get("texto", "")})
                            elif m["tipo"] == "bot":
                                historial.append({"tipo": "bot", "texto": contenido.get("texto", "")})
                            elif m["tipo"] == "success":
                                historial.append({"tipo": "success", "texto": contenido.get("texto", "")})
                    else:
                        historial = self._get_historial()
                except Exception:
                    historial = self._get_historial()
            else:
                historial = self._get_historial()
            for msg in historial:
                texto = escapar(msg.get("texto", ""))
                if msg["tipo"] == "user":
                    historial_rendered += f'''
                    <div class="flex flex-col items-end message-in">
                        <div class="max-w-[80%] text-right">
                            <p class="text-text-primary font-body-md text-[17px] leading-relaxed">{texto}</p>
                            <span class="inline-block mt-2 text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Tu</span>
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
                            <span class="inline-block text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Asistente</span>
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
                            <span class="inline-block text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Asistente</span>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "aulas":
                    historial_rendered += '''
                    <div class="flex items-start gap-6 message-in">
                        <div class="w-10 h-10 rounded-xl bg-utp-red-institutional flex items-center justify-center flex-shrink-0 shadow-lg shadow-utp-red-institutional/20 mt-1">
                            <span class="material-symbols-outlined text-[22px] text-white" style="font-variation-settings: 'FILL' 1;">auto_awesome</span>
                        </div>
                        <div class="flex-1 space-y-4">
                    '''
                    for d in msg["data"]:
                        nombre = escapar(d["nombre"])
                        ubicacion = escapar(d["ubicacion"])
                        capacidad = escapar(str(d.get("capacidad", "")))
                        equipamiento = escapar(d.get("equipamiento", ""))
                        software = escapar(d.get("software", ""))
                        id_espacio = d.get("id_espacio", 0)
                        historial_rendered += f'''
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
                        '''
                    historial_rendered += '''
                            <span class="inline-block text-[10px] text-text-secondary/50 font-bold uppercase tracking-widest">Asistente</span>
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
            try:
                db_reservas = Database()
                reserva_ctrl = ReservaController(db_reservas)
                reservas = reserva_ctrl.reserva_service.listar_por_usuario(usuario["id_usuario"])
            except Exception:
                reservas = []
            reservas_rendered = ""
            for r in reservas:
                rid = r.get("id_reserva", 0)
                ename = escapar(r.get("espacio_nombre", ""))
                tipo = escapar(r.get("tipo_nombre", ""))
                ubicacion = escapar(r.get("ubicacion", ""))
                fecha = escapar(str(r.get("fecha", "")))
                curso = escapar(r.get("curso_nombre", ""))
                estado_raw = r.get("estado", "PENDIENTE")
                if estado_raw == "CONFIRMADA":
                    estado_class = "bg-emerald-100 text-emerald-800"
                    estado_text = "Confirmada"
                elif estado_raw == "CANCELADA":
                    estado_class = "bg-red-100 text-red-800"
                    estado_text = "Cancelada"
                else:
                    estado_class = "bg-amber-100 text-amber-800"
                    estado_text = "Pendiente"
                reservas_rendered += f'''
                <tr class="hover:bg-black/[0.02] transition-colors" data-estado="{estado_raw}">
                    <td class="py-4 px-4 text-text-primary font-medium">#RES-{rid}</td>
                    <td class="py-4 px-4 text-text-primary">{ename}</td>
                    <td class="py-4 px-4 text-text-secondary">{tipo}</td>
                    <td class="py-4 px-4 text-text-primary">{fecha}</td>
                    <td class="py-4 px-4 text-text-primary">-</td>
                    <td class="py-4 px-4"><span class="inline-flex items-center px-2 py-0.5 rounded text-[12px] font-semibold {estado_class}">{estado_text}</span></td>
                    <td class="py-4 px-4 text-right whitespace-nowrap relative">
                        <button onclick="toggleAcciones(this)" class="p-1 rounded hover:bg-black/5 text-text-secondary/60 hover:text-text-primary transition-colors">
                            <span class="material-symbols-outlined text-[20px]">more_vert</span>
                        </button>
                        <div class="acciones-menu hidden absolute right-0 top-10 mt-0.5 w-44 bg-white rounded-lg shadow-xl border border-black/5 py-1.5 z-50">
                            <button onclick="abrirModal({rid},'{ename}','{tipo}','{ubicacion}','{fecha}','{estado_text}','{estado_class}','{curso}'); cerrarTodosAcciones()" class="w-full text-left px-4 py-2.5 text-sm text-text-secondary hover:bg-black/5 flex items-center gap-3">
                                <span class="material-symbols-outlined text-[18px] text-text-secondary/50">visibility</span> Ver Detalles
                            </button>
                            <button onclick="if(confirm('Cancelar esta reserva?'))window.location.href='/api/reserva/cancelar?id={rid}'" class="w-full text-left px-4 py-2.5 text-sm text-text-secondary hover:bg-red-50 hover:text-red-600 flex items-center gap-3">
                                <span class="material-symbols-outlined text-[18px] text-text-secondary/50">cancel</span> Cancelar
                            </button>
                        </div>
                    </td>
                </tr>'''
            if not reservas_rendered:
                reservas_rendered = '<tr data-estado=""><td class="py-4 px-4 text-text-secondary text-center" colspan="7">No tienes reservas.</td></tr>'
            sesiones_rendered = ""
            try:
                sc = SesionChat(db_reservas)
                sesiones = sc.listar_por_usuario(usuario["id_usuario"])
                for s in sesiones:
                    sid = s["id_sesion"]
                    titulo = escapar(s["titulo"])
                    sesiones_rendered += f'''
                    <div class="flex items-center gap-1 px-4 py-2.5 rounded-xl text-sm group relative hover:bg-black/5 transition-all duration-200">
                        <a href="/api/sesion/cargar?id={sid}" class="flex items-center gap-3 flex-1 min-w-0 text-text-secondary hover:text-text-primary transition-all duration-200">
                            <span class="material-symbols-outlined text-[18px] text-text-secondary/60">chat</span>
                            <span class="truncate">{titulo}</span>
                        </a>
                        <a href="/api/sesion/eliminar?id={sid}" onclick="return confirm('Eliminar esta conversación?')" class="opacity-0 group-hover:opacity-100 p-1.5 hover:bg-red-50 rounded-lg text-text-secondary/40 hover:text-red-600 transition-all shrink-0">
                            <span class="material-symbols-outlined text-[16px]">delete</span>
                        </a>
                    </div>'''
            except Exception as e:
                logger.error(f"Error al listar sesiones: {e}")
            page_rendered = HTML_CHAT.replace("$NOMBRE_DOCENTE", usuario["nombre"]).replace("$HISTORIAL_CHAT", historial_rendered).replace("$TABLA_RESERVAS", reservas_rendered).replace("$LISTA_SESIONES", sesiones_rendered)
            self._responder_html(page_rendered)

        elif parsed_path == "/api/sesion/nueva":
            if not usuario:
                self._redirect("/login")
                return
            db_sc = Database()
            sc = SesionChat(db_sc)
            historial = [
                {"tipo": "bot", "texto": f"Hola, {escapar(usuario['nombre'])}. Soy el Asistente Academico UTP. ¿Que aula o reprogramacion deseas gestionar hoy?"}
            ]
            titulo = "Nueva conversacion"
            sesion = sc.crear(usuario["id_usuario"], titulo)
            id_sesion = sesion["id_sesion"]
            sc.guardar_mensaje(id_sesion, "bot", json.dumps({"texto": historial[0]["texto"]}))
            self._redirect("/chat#fin", [("Set-Cookie", self._set_historial(historial)), ("Set-Cookie", f"utp_sesion={id_sesion}; Path=/; Max-Age=86400")])

        elif parsed_path == "/api/sesion/cargar":
            if not usuario:
                self._redirect("/login")
                return
            params_get = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            id_sesion = int(params_get.get("id", [0])[0])
            if not id_sesion:
                self._redirect("/chat")
                return
            db_sc = Database()
            sc = SesionChat(db_sc)
            if not sc.verificar_propiedad(id_sesion, usuario["id_usuario"]):
                self._redirect("/chat")
                return
            mensajes = sc.obtener_mensajes(id_sesion)
            historial = []
            for m in mensajes:
                try:
                    contenido = json.loads(m["contenido"])
                except Exception:
                    contenido = {"texto": m["contenido"]}
                if m["tipo"] == "card":
                    historial.append({"tipo": "card", "data": contenido})
                elif m["tipo"] == "user":
                    historial.append({"tipo": "user", "texto": contenido.get("texto", "")})
                elif m["tipo"] == "bot":
                    historial.append({"tipo": "bot", "texto": contenido.get("texto", "")})
                elif m["tipo"] == "success":
                    historial.append({"tipo": "success", "texto": contenido.get("texto", "")})
            self._redirect("/chat#fin", [("Set-Cookie", self._set_historial(historial)), ("Set-Cookie", f"utp_sesion={id_sesion}; Path=/; Max-Age=86400")])

        elif parsed_path == "/api/sesion/eliminar":
            if not usuario:
                self._redirect("/login")
                return
            params_get = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            id_sesion = int(params_get.get("id", [0])[0])
            if id_sesion:
                db_sc = Database()
                sc = SesionChat(db_sc)
                try:
                    ok = sc.eliminar(id_sesion, usuario["id_usuario"])
                    if ok:
                        logger.info(f"Sesión {id_sesion} eliminada por usuario {usuario['id_usuario']}")
                    else:
                        logger.warning(f"No se eliminó sesión {id_sesion} (no existe o no pertenece al usuario)")
                except Exception as e:
                    logger.error(f"Error eliminando sesión {id_sesion}: {e}")
            self._redirect("/chat")

        elif parsed_path == "/api/reserva/cancelar":
            if not usuario:
                self._redirect("/login")
                return
            params_get = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            id_reserva = int(params_get.get("id", [0])[0])
            if id_reserva:
                db_cancel = Database()
                rc = ReservaController(db_cancel)
                try:
                    rc.reserva_service.cancelar(id_reserva, usuario["id_usuario"])
                except Exception as e:
                    logger.error(f"Error al cancelar reserva: {e}")
            self._redirect("/chat#reservas")

        elif parsed_path == "/admin/salones/editar":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                params_get = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                id_espacio = int(params_get.get("id", [0])[0])
                db_edit = Database()
                conn_edit = db_edit.obtener_conexion()
                cur_edit = conn_edit.cursor()
                cur_edit.execute("SELECT e.*, t.nombre AS tipo_nombre FROM espacios_academicos e JOIN tipos_espacio t ON e.id_tipo = t.id_tipo WHERE e.id_espacio = %s", (id_espacio,))
                espacio = dict(cur_edit.fetchone())
                cur_edit.execute("SELECT id_tipo, nombre FROM tipos_espacio ORDER BY nombre")
                tipos = [dict(r) for r in cur_edit.fetchall()]
                cur_edit.execute("SELECT id_equipamiento, nombre FROM equipamientos ORDER BY nombre")
                equipos_todos = [dict(r) for r in cur_edit.fetchall()]
                cur_edit.execute("SELECT ee.id_equipamiento FROM espacio_equipamiento ee WHERE ee.id_espacio = %s", (id_espacio,))
                equipos_seleccionados = {r["id_equipamiento"] for r in cur_edit.fetchall()}
                cur_edit.execute("SELECT id_software, nombre FROM software ORDER BY nombre")
                soft_todos = [dict(r) for r in cur_edit.fetchall()]
                softwares_seleccionados = set()
                cur_edit.execute("SELECT es.id_software FROM espacio_software es WHERE es.id_espacio = %s", (id_espacio,))
                softwares_seleccionados = {r["id_software"] for r in cur_edit.fetchall()}
                conn_edit.close()
                opts_tipo = "".join(f'<option value="{t["id_tipo"]}" {"selected" if t["id_tipo"]==espacio["id_tipo"] else ""}>{t["nombre"]}</option>' for t in tipos)
                opts_estado = "".join(f'<option value="{e}" {"selected" if e==espacio["estado"] else ""}>{e.capitalize()}</option>' for e in ["DISPONIBLE","OCUPADO","MANTENIMIENTO"])
                chk_equipos = "".join(f'<label class="flex items-center gap-2"><input type="checkbox" name="equipamiento" value="{eq["id_equipamiento"]}" {"checked" if eq["id_equipamiento"] in equipos_seleccionados else ""} class="rounded border-surface-container-highest text-primary focus:ring-primary"> <span class="text-sm">{eq["nombre"]}</span></label>' for eq in equipos_todos)
                chk_software = "".join(f'<label class="flex items-center gap-2"><input type="checkbox" name="software" value="{sw["id_software"]}" {"checked" if sw["id_software"] in softwares_seleccionados else ""} class="rounded border-surface-container-highest text-primary focus:ring-primary"> <span class="text-sm">{sw["nombre"]}</span></label>' for sw in soft_todos)
                html = f'''<!DOCTYPE html><html class="light" lang="es"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><title>Editar Salon | UTP Admin</title><script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script><link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100;300;400;500;600;700;800;900&family=Courier+Prime&display=swap" rel="stylesheet"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/><style>body{{background:#F8F9FA;color:#191C1D;font-family:'Libre Franklin',sans-serif}}.material-symbols-outlined{{font-variation-settings:'FILL'0,'wght'400,'GRAD'0,'opsz'24;vertical-align:middle}}.glass-panel{{background:rgba(255,255,255,0.7);backdrop-filter:blur(12px);border:1px solid #e6e8eb}}</style></head><body class="p-8">
                <div class="max-w-3xl mx-auto">
                <div class="flex items-center gap-4 mb-8">
                <a href="/admin/salones" class="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-500 hover:bg-gray-200 transition-colors"><span class="material-symbols-outlined">arrow_back</span></a>
                <div><h1 class="text-2xl font-bold text-gray-900">Editar Salón</h1><p class="text-sm text-gray-500">{espacio["nombre"]}</p></div>
                </div>
                <form method="POST" action="/admin/salones/actualizar" class="glass-panel rounded-2xl p-8 space-y-6">
                <input type="hidden" name="id_espacio" value="{id_espacio}">
                <div><label class="block text-sm font-bold text-gray-500 mb-1">Nombre</label><input name="nombre" value="{escapar(espacio['nombre'])}" class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-1 focus:ring-red-700 focus:border-red-700" required></div>
                <div class="grid grid-cols-2 gap-4">
                <div><label class="block text-sm font-bold text-gray-500 mb-1">Tipo</label><select name="id_tipo" class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-1 focus:ring-red-700 focus:border-red-700">{opts_tipo}</select></div>
                <div><label class="block text-sm font-bold text-gray-500 mb-1">Estado</label><select name="estado" class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-1 focus:ring-red-700 focus:border-red-700">{opts_estado}</select></div>
                </div>
                <div class="grid grid-cols-2 gap-4">
                <div><label class="block text-sm font-bold text-gray-500 mb-1">Ubicación</label><input name="ubicacion" value="{escapar(espacio.get('ubicacion',''))}" class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-1 focus:ring-red-700 focus:border-red-700" required></div>
                <div><label class="block text-sm font-bold text-gray-500 mb-1">Capacidad</label><input type="number" name="capacidad" value="{espacio.get('capacidad',0)}" class="w-full px-4 py-3 border border-gray-200 rounded-xl focus:ring-1 focus:ring-red-700 focus:border-red-700" required></div>
                </div>
                <div><label class="block text-sm font-bold text-gray-500 mb-2">Equipamiento</label><div class="grid grid-cols-2 gap-2">{chk_equipos}</div></div>
                <div><label class="block text-sm font-bold text-gray-500 mb-2">Software</label><div class="grid grid-cols-2 gap-2">{chk_software}</div></div>
                <div class="flex gap-3 pt-4 border-t border-gray-200">
                <a href="/admin/salones" class="px-6 py-3 border border-gray-200 rounded-xl text-gray-500 font-bold hover:bg-gray-50 transition-all">Cancelar</a>
                <button type="submit" class="px-6 py-3 bg-red-700 text-white font-bold rounded-xl hover:bg-red-800 transition-all">Guardar Cambios</button>
                </div>
                </form>
                </div></body></html>'''
                self._responder_html(html)
            except Exception as e:
                logger.error(f"Error en editar salon: {e}")
                self._redirect("/admin/salones")

        elif parsed_path == "/admin/salones/historial":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                params_get = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
                id_espacio = int(params_get.get("id", [0])[0])
                db_hist = Database()
                conn_hist = db_hist.obtener_conexion()
                cur_hist = conn_hist.cursor()
                cur_hist.execute("SELECT e.*, t.nombre AS tipo_nombre FROM espacios_academicos e JOIN tipos_espacio t ON e.id_tipo = t.id_tipo WHERE e.id_espacio = %s", (id_espacio,))
                espacio = dict(cur_hist.fetchone())
                cur_hist.execute("SELECT r.id_reserva, r.fecha, r.estado, u.nombre AS usuario_nombre, u.username FROM reservas r JOIN usuarios u ON r.id_usuario = u.id_usuario WHERE r.id_espacio = %s ORDER BY r.fecha DESC", (id_espacio,))
                reservas = [dict(r) for r in cur_hist.fetchall()]
                conn_hist.close()
                filas_hist = ""
                if reservas:
                    for r in reservas:
                        estado_r = r.get("estado","PENDIENTE")
                        ec = {"CONFIRMADA":"text-emerald-700 bg-emerald-50","RECHAZADA":"text-red-700 bg-red-50","CANCELADA":"text-red-700 bg-red-50"}.get(estado_r,"text-amber-700 bg-amber-50")
                        filas_hist += f'<tr class="hover:bg-surface-container-low/30"><td class="px-4 py-3">RES-{r["id_reserva"]:04d}</td><td class="px-4 py-3">{r.get("usuario_nombre","-")}</td><td class="px-4 py-3">@{r.get("username","")}</td><td class="px-4 py-3">{r["fecha"]}</td><td class="px-4 py-3"><span class="px-2 py-1 rounded-full text-xs font-bold {ec}">{estado_r.capitalize()}</span></td></tr>'
                else:
                    filas_hist = '<tr><td colspan="5" class="px-4 py-8 text-center text-secondary">No hay reservas registradas para este espacio</td></tr>'
                html = f'''<!DOCTYPE html><html class="light" lang="es"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/><title>Historial | UTP Admin</title><script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script><link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100;300;400;500;600;700;800;900&family=Courier+Prime&display=swap" rel="stylesheet"/><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/><style>body{{background:#F8F9FA;color:#191C1D;font-family:'Libre Franklin',sans-serif}}.material-symbols-outlined{{font-variation-settings:'FILL'0,'wght'400,'GRAD'0,'opsz'24;vertical-align:middle}}.glass-panel{{background:rgba(255,255,255,0.7);backdrop-filter:blur(12px);border:1px solid #e6e8eb}}</style></head><body class="p-8">
                <div class="max-w-4xl mx-auto">
                <div class="flex items-center gap-4 mb-8">
                <a href="/admin/salones" class="w-10 h-10 rounded-full bg-surface-container-low flex items-center justify-center text-secondary hover:bg-surface-container-highest transition-colors"><span class="material-symbols-outlined">arrow_back</span></a>
                <div><h1 class="text-2xl font-bold">Historial de Reservas</h1><p class="text-sm text-secondary">{espacio["nombre"]} ({espacio.get("tipo_nombre","")})</p></div>
                </div>
                <div class="glass-panel rounded-2xl overflow-hidden">
                <table class="w-full text-left"><thead class="bg-surface-container-low/50"><tr><th class="px-4 py-3 text-xs uppercase text-secondary font-bold">Reserva</th><th class="px-4 py-3 text-xs uppercase text-secondary font-bold">Usuario</th><th class="px-4 py-3 text-xs uppercase text-secondary font-bold">Username</th><th class="px-4 py-3 text-xs uppercase text-secondary font-bold">Fecha</th><th class="px-4 py-3 text-xs uppercase text-secondary font-bold">Estado</th></tr></thead><tbody class="divide-y divide-surface-container-highest">{filas_hist}</tbody></table>
                </div>
                <div class="mt-6"><a href="/admin/salones" class="inline-flex items-center gap-2 text-primary font-bold hover:underline"><span class="material-symbols-outlined">arrow_back</span> Volver a Salones</a></div>
                </div></body></html>'''
                self._responder_html(html)
            except Exception as e:
                logger.error(f"Error en historial salon: {e}")
                self._redirect("/admin/salones")

        elif parsed_path == "/api/notificaciones":
            if not usuario:
                self._responder_html('[]', 401)
                return
            db_sc = Database()
            n = Notificacion(db_sc)
            no_leidas = n.contar_no_leidas(usuario["id_usuario"])
            lista = n.listar(usuario["id_usuario"])
            for item in lista:
                item["created_at"] = str(item["created_at"])
            self._responder_html(json.dumps({"no_leidas": no_leidas, "items": lista}, default=str))

        elif parsed_path == "/admin":
            if not self._es_admin():
                self._redirect("/login")
                return
            header = self._render_header()
            try:
                db = Database()
                admin_adm = AdminController(db)
                espacios_adm = admin_adm.obtener_espacios()
                stats = admin_adm.obtener_estadisticas()
                tipo_nombres_clase = {"AULA":"AulaTeorica","LABORATORIO":"AulaLaboratorio","SALA DE COMPUTO":"SalaComputo","AUDITORIO":"Auditorio","TALLER":"Taller"}
                estado_map = {"DISPONIBLE":("text-emerald-600","bg-emerald-500","Disponible"),"OCUPADO":("text-primary","bg-primary","Ocupado"),"MANTENIMIENTO":("text-amber-600","bg-amber-500","Mantenimiento")}
                filas_adm = ""
                for e in espacios_adm:
                    tipo_raw = e.get("tipo","")
                    tipo_clase = tipo_nombres_clase.get(tipo_raw,tipo_raw)
                    estado_str = e.get("estado","DISPONIBLE")
                    ec, ed, estado_text = estado_map.get(estado_str, ("text-secondary","bg-secondary",estado_str))
                    nombre_escapado = escapar(e["nombre"])
                    ubicacion_escapada = escapar(e["ubicacion"])
                    equipamiento = escapar(e.get("equipamiento",""))
                    software = escapar(e.get("software",""))
                    filas_adm += f'''
                    <tr class="hover:bg-surface-container-low transition-colors group">
                    <td class="px-8 py-4 font-bold">{nombre_escapado}</td>
                    <td class="px-8 py-4">{ubicacion_escapada}</td>
                    <td class="px-8 py-4"><span class="flex items-center {ec} font-semibold"><span class="w-1.5 h-1.5 rounded-full {ed} mr-2"></span> {estado_text}</span></td>
                    <td class="px-8 py-4">{e["capacidad"]}</td>
                    <td class="px-8 py-4 text-right relative">
                        <button onclick="toggleAcciones(this)" class="text-secondary hover:text-primary transition-colors relative">
                            <span class="material-symbols-outlined">more_vert</span>
                        </button>
                        <div class="acciones-menu hidden absolute right-0 top-8 w-48 bg-white rounded-2xl shadow-2xl border border-surface-container-highest z-50 overflow-hidden">
                            <button onclick="verDetalle({e['id_espacio']},'{nombre_escapado}','{tipo_clase}','{ubicacion_escapada}',{e['capacidad']},'{equipamiento}','{software}','{estado_text}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low"><span class="material-symbols-outlined text-[18px] text-secondary">visibility</span> Ver detalle</button>
                            <button onclick="cambiarEstado({e['id_espacio']})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low"><span class="material-symbols-outlined text-[18px] text-secondary">sync_alt</span> Cambiar estado</button>
                            <div class="h-px bg-surface-container-higher mx-3"></div>
                            <button onclick="eliminarSalon({e['id_espacio']},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-error hover:bg-error-container/10"><span class="material-symbols-outlined text-[18px]">delete</span> Eliminar</button>
                        </div>
                    </td>
                    </tr>'''
                page_rendered = HTML_ADMIN.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"]).replace("$TABLA_ESPACIOS", filas_adm)
                page_rendered = page_rendered.replace("$KPI_TOTAL_SALONES", str(stats.get("total_espacios", 0)))
                page_rendered = page_rendered.replace("$KPI_TOTAL_DOCENTES", str(stats.get("total_usuarios", 0)))
                page_rendered = page_rendered.replace("$KPI_RESERVAS_PENDIENTES", str(stats.get("reservas_pendientes", 0)))
                page_rendered = page_rendered.replace("$KPI_RESERVAS_HOY", str(stats.get("total_reservas", 0)))
            except Exception:
                page_rendered = HTML_ADMIN.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"]).replace("$TABLA_ESPACIOS", "")
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
                    "OCUPADO": ("bg-red-50 text-red-700", "bg-red-500", "Ocupado"),
                    "MANTENIMIENTO": ("bg-amber-50 text-amber-700", "bg-amber-500", "Mantenimiento"),
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
                    <tr class="hover:bg-surface-container-low/30 transition-colors group" data-nombre="{escapar(e['nombre'])}" data-tipo="{tipo_clase}" data-ubicacion="{escapar(e.get('ubicacion',''))}" data-estado="{estado_str}" data-search="{escapar(e['nombre'])} {tipo_clase} {escapar(e.get('ubicacion',''))} {escapar(software)}">
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
                    <td class="px-6 py-5 text-right relative">
                    <div class="flex justify-end opacity-0 group-hover:opacity-100 transition-opacity">
                    <button onclick="toggleAcciones(this)" class="p-2 hover:bg-surface-container-low rounded-lg text-secondary">
                        <span class="material-symbols-outlined text-[20px]">more_vert</span>
                    </button>
                    </div>
                    <div class="absolute right-4 top-14 w-48 bg-white rounded-2xl shadow-2xl border border-surface-container-highest hidden z-50 overflow-hidden acciones-menu">
                        <button onclick="verDetalle({e['id_espacio']},'{escapar(e['nombre'])}','{tipo_clase}','{escapar(e['ubicacion'])}',{e['capacidad']},'{escapar(e.get('equipamiento',''))}','{escapar(software)}','{estado_text}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">visibility</span> Ver detalle
                        </button>
                        <button onclick="editarSalon({e['id_espacio']})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">edit</span> Editar
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="cambiarEstado({e['id_espacio']},'{estado_str}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">sync_alt</span> Cambiar estado
                        </button>
                        <button onclick="verHistorial({e['id_espacio']})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">history</span> Historial
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="eliminarSalon({e['id_espacio']},'{escapar(e['nombre'])}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-error hover:bg-error-container/10 transition-colors">
                            <span class="material-symbols-outlined text-[18px]">delete</span> Eliminar
                        </button>
                    </div>
                    </td>
                    </tr>
                    '''
                header = self._render_header("Buscar salon, aula o software...")
                stats = admin.obtener_estadisticas()
                page_rendered = HTML_SALONES.replace("$HEADER", header).replace("$NOMBRE_ADMIN", usuario["nombre"])
                page_rendered = page_rendered.replace("$TABLA_SALONES", filas_html)
                page_rendered = page_rendered.replace("$TOTAL_SALONES", str(len(espacios)))
                page_rendered = page_rendered.replace("$KPI_SALONES_DISPONIBLES", str(stats.get("espacios_disponibles", 0)))
                page_rendered = page_rendered.replace("$KPI_TASA_OCUPACION", str(stats.get("tasa_ocupacion", 0)))
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
                estado_map_sw = {
                    "DISPONIBLE": ("bg-emerald-50 text-emerald-700", "bg-emerald-500", "Disponible"),
                    "OCUPADO": ("bg-red-50 text-red-700", "bg-red-500", "Ocupado"),
                    "MANTENIMIENTO": ("bg-amber-50 text-amber-700", "bg-amber-500", "Mantenimiento"),
                }
                filas_html = ""
                for a in activos:
                    id_espacio = a['id_espacio']
                    id_activo = f"ACT-{id_espacio:04d}"
                    tipo_raw = a.get("tipo", "")
                    icono = tipo_iconos.get(tipo_raw, "inventory_2")
                    tipo_label = tipo_nombres.get(tipo_raw, tipo_raw)
                    equipamiento = a.get("equipamiento", "") or ""
                    software_list = a.get("software", "") or ""
                    partes = [p for p in [equipamiento, software_list] if p]
                    software_str = ", ".join(partes) if partes else "N/A"
                    estado_str = a.get("estado", "DISPONIBLE")
                    ec, ed, estado_text = estado_map_sw.get(estado_str, ("bg-surface-container-highest text-secondary", "bg-secondary", estado_str))
                    nombre_escapado = escapar(a["nombre"])
                    eq_escapado = escapar(equipamiento)
                    sw_escapado = escapar(software_list)
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group" data-nombre="{nombre_escapado}" data-tipo="{tipo_label}" data-estado="{estado_str}" data-search="{nombre_escapado} {tipo_label} {sw_escapado}">
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
                    {estado_text}
                    </span>
                    </td>
                    <td class="px-6 py-5">
                    <span class="text-on-surface">{software_str}</span>
                    </td>
                    <td class="px-6 py-5 text-secondary font-mono-sm">-</td>
                    <td class="px-6 py-5 text-right relative">
                    <div class="flex justify-end opacity-0 group-hover:opacity-100 transition-opacity">
                    <button onclick="toggleAcciones(this)" class="p-2 hover:bg-surface-container-low rounded-lg text-secondary">
                        <span class="material-symbols-outlined text-[20px]">more_vert</span>
                    </button>
                    </div>
                    <div class="acciones-menu hidden absolute right-4 top-14 w-48 bg-white rounded-2xl shadow-2xl border border-surface-container-highest z-50 overflow-hidden">
                        <button onclick="verDetalle({id_espacio},'{nombre_escapado}','{tipo_label}','{eq_escapado}','{sw_escapado}','{estado_text}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">visibility</span> Ver detalle
                        </button>
                        <button onclick="editarItem({id_espacio})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">edit</span> Editar
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="cambiarEstado({id_espacio})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">sync_alt</span> Cambiar estado
                        </button>
                        <button onclick="verHistorial({id_espacio})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">history</span> Historial
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="eliminarItem({id_espacio},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-error hover:bg-error-container/10 transition-colors">
                            <span class="material-symbols-outlined text-[18px]">delete</span> Eliminar
                        </button>
                    </div>
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
                    dia_str = str(b.get("dia_semana", "LUNES")).upper().strip()
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
                    id_docente = d.get("id_docente", 0)
                    avatar = d.get("nombre", "?")[0] if d.get("nombre") else "?"
                    estado_texto = "Activo"
                    estado_color = "bg-emerald-500"
                    estado_text_class = "text-emerald-700"
                    nombre_escapado = escapar(d.get("nombre", "Sin nombre"))
                    depto_escapado = escapar(d.get("departamento", "No asignado"))
                    espec_escapado = escapar(d.get("especialidad", "General"))
                    correo_escapado = escapar(d.get("correo", "N/A"))
                    telefono_escapado = escapar(d.get("telefono", "N/A"))
                    filas_html += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group" data-nombre="{nombre_escapado}" data-departamento="{depto_escapado}" data-search="{nombre_escapado} {depto_escapado} {espec_escapado}">
                    <td class="px-6 py-4">
                    <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold">{avatar}</div>
                    <div>
                    <p class="font-bold text-on-surface">{d.get("nombre", "Sin nombre")}</p>
                    <p class="text-label-md text-secondary">ID: DOC-{id_docente}</p>
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
                    <td class="px-6 py-4 text-right relative">
                    <div class="flex justify-end opacity-0 group-hover:opacity-100 transition-opacity">
                    <button onclick="toggleAcciones(this)" class="p-2 hover:bg-surface-container-low rounded-lg text-secondary">
                        <span class="material-symbols-outlined text-[20px]">more_vert</span>
                    </button>
                    </div>
                    <div class="acciones-menu hidden absolute right-4 top-14 w-48 bg-white rounded-2xl shadow-2xl border border-surface-container-highest z-50 overflow-hidden">
                        <button onclick="verDetalleDocente({id_docente},'{nombre_escapado}','{depto_escapado}','{espec_escapado}','{correo_escapado}','{telefono_escapado}','{estado_texto}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">visibility</span> Ver detalle
                        </button>
                        <button onclick="editarDocente({id_docente})" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">edit</span> Editar
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="eliminarDocente({id_docente},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-error hover:bg-error-container/10 transition-colors">
                            <span class="material-symbols-outlined text-[18px]">delete</span> Eliminar
                        </button>
                    </div>
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
                        <div class="flex justify-end gap-2 transition-opacity">
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

        elif parsed_path == "/admin/seed-horarios":
            if not self._es_admin():
                self._redirect("/login")
                return
            try:
                db = Database()
                conn = db.obtener_conexion()
                cursor = conn.cursor()
                bloques_prueba = [
                    ("Clase Teorica (Test)", "08:00", "10:00", "MARTES", "DIURNO"),
                    ("Laboratorio 1 (Test)", "10:00", "12:00", "MARTES", "DIURNO"),
                    ("Inteligencia Art. (Test)", "14:00", "16:00", "MIERCOLES", "TARDE"),
                    ("Seguridad (Test)", "16:00", "18:00", "JUEVES", "TARDE"),
                    ("Desarrollo Web (Test)", "08:00", "10:00", "VIERNES", "DIURNO")
                ]
                for b in bloques_prueba:
                    cursor.execute(
                        "INSERT INTO bloques_horario (nombre, hora_inicio, hora_fin, dia_semana, turno) "
                        "VALUES (%s, %s, %s, %s, %s)", b
                    )
                conn.commit()
                conn.close()
                html = "<h1>Datos semilla insertados correctamente en Supabase</h1><br><a href='/admin/horarios'>Volver a ver los horarios</a>"
                self._responder_html(html)
            except Exception as e:
                self._responder_html(f"<h1>Error REAL de Base de datos: {str(e)}</h1>")
            return

        elif parsed_path == "/admin/debug-horarios":
            if not self._es_admin():
                self._redirect("/login")
                return
            db = Database()
            from app.controllers.admin_controller import AdminController
            admin = AdminController(db)
            bloques = admin.obtener_bloques_horario()
            import json
            html = f"<h1>Datos reales en la Base de Datos</h1><pre style='background:#eee;padding:20px;'>{json.dumps(bloques, default=str, indent=4)}</pre>"
            self._responder_html(html)
            return

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
                    id_usuario = u.get("id_usuario", 0)
                    rol = u.get("rol", "Estudiante")
                    avatar = (u.get("nombre", "?")[:2]).upper() if u.get("nombre") else "??"
                    estado_u = u.get("estado_int") or u.get("estado", 1)
                    if estado_u in (1, "1", "ACTIVO"): 
                        estado_text = "Activo"
                        estado_dot = "bg-emerald-500" 
                    else:
                        estado_text = "Inactivo"
                        estado_dot = "bg-red-500"
                    nombre_escapado = escapar(u["nombre"])
                    username_escapado = escapar(u.get("username", ""))
                    filas_usuarios += f'''
                    <tr class="hover:bg-surface-container-low/30 transition-colors group" data-nombre="{nombre_escapado}" data-rol="{rol}" data-search="{nombre_escapado} {rol}">
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
                    <td class="px-6 py-4 text-right relative">
                    <div class="flex justify-end opacity-0 group-hover:opacity-100 transition-opacity">
                    <button onclick="toggleAcciones(this)" class="p-2 hover:bg-surface-container-low rounded-lg text-secondary transition-colors">
                        <span class="material-symbols-outlined text-[20px]">more_vert</span>
                    </button>
                    </div>
                    <div class="acciones-menu hidden absolute right-4 top-14 w-48 bg-white rounded-2xl shadow-2xl border border-surface-container-highest z-50 overflow-hidden">
                        <button onclick="verDetalleUsuario({id_usuario},'{nombre_escapado}','{username_escapado}','{rol}','{estado_text}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">visibility</span> Ver detalle
                        </button>
                        <button onclick="editarUsuario({id_usuario},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">lock_reset</span> Cambiar Contrasena
                        </button>
                        <button onclick="resetPassword({id_usuario},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-on-surface hover:bg-surface-container-low transition-colors">
                            <span class="material-symbols-outlined text-[18px] text-secondary">password</span> Restablecer Contrasena
                        </button>
                        <div class="h-px bg-surface-container-higher mx-3"></div>
                        <button onclick="eliminarUsuario({id_usuario},'{nombre_escapado}')" class="w-full flex items-center gap-3 px-4 py-3 text-sm text-error hover:bg-error-container/10 transition-colors">
                            <span class="material-symbols-outlined text-[18px]">delete</span> Eliminar
                        </button>
                    </div>
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
            self._skip_refresh = True
            cookies = [
                ("Set-Cookie", "utp_session=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; HttpOnly; SameSite=Lax"),
                ("Set-Cookie", "utp_token=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"),
                ("Set-Cookie", "utp_sesion=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT"),
                ("Set-Cookie", "utp_historial=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT")
            ]
            self._redirect("/login", cookies)

        elif parsed_path == "/force-change-password":
            if not usuario:
                self._redirect("/login")
                return
            repo = UsuarioRepository()
            user_data = repo.get_by_id(usuario["id_usuario"])
            if not user_data or not user_data.get("force_password_change"):
                self._redirect("/chat")
                return
            from app.views.templates.force_change_html import HTML_FORCE_CHANGE
            self._responder_html(HTML_FORCE_CHANGE)

        else:
            self.send_response(404)
            self.end_headers()

    def _get_historial(self):
        from http.cookies import SimpleCookie
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
                        from app.repositories.usuario_repository import UsuarioRepository
                        repo = UsuarioRepository()
                        user_data = repo.get_by_username(usuario["username"])
                        if user_data and user_data.get("force_password_change"):
                            self._redirect("/force-change-password", [("Set-Cookie", cookie)])
                            return
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

            if parsed_path_post == "/api/auth/force-change-password":
                current_password = params.get("current_password", [""])[0]
                new_password = params.get("new_password", [""])[0]
                confirm_password = params.get("confirm_password", [""])[0]
                from app.controllers.password_reset_controller import PasswordResetController
                ctrl = PasswordResetController()
                try:
                    from app.schemas.password_schema import ForceChangePasswordSchema
                    schema = ForceChangePasswordSchema.from_dict({
                        "new_password": new_password,
                        "confirm_password": confirm_password,
                    })
                    errors = schema.validate()
                    if errors:
                        raw = json.dumps({"error": "; ".join(errors)}, ensure_ascii=False)
                        self.send_response(400)
                        self.send_header("Content-Type", "application/json; charset=utf-8")
                        self.end_headers()
                        self.wfile.write(raw.encode("utf-8"))
                        return
                    result = ctrl.force_change_password(
                        usuario["id_usuario"], current_password, new_password
                    )
                    raw = json.dumps(result, ensure_ascii=False)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.send_header("Set-Cookie", make_set_cookie_header(usuario))
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                except Exception as e:
                    raw = json.dumps({"error": str(e)}, ensure_ascii=False)
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                return

            if parsed_path_post.startswith("/api/admin/users/") and parsed_path_post.endswith("/reset-password"):
                if usuario["rol"] != "Admin":
                    raw = json.dumps({"error": "No autorizado"}, ensure_ascii=False)
                    self.send_response(403)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                    return
                try:
                    docente_id = int(parsed_path_post.split("/")[4])
                except (IndexError, ValueError):
                    raw = json.dumps({"error": "ID inválido"}, ensure_ascii=False)
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                    return
                from app.controllers.password_reset_controller import PasswordResetController
                ctrl = PasswordResetController()
                try:
                    result = ctrl.reset_password(usuario["id_usuario"], docente_id)
                    raw = json.dumps(result, ensure_ascii=False)
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                except Exception as e:
                    status = 500
                    if "No encontrado" in str(e): status = 404
                    elif "No puedes" in str(e): status = 400
                    raw = json.dumps({"error": str(e)}, ensure_ascii=False)
                    self.send_response(status)
                    self.send_header("Content-Type", "application/json; charset=utf-8")
                    self.end_headers()
                    self.wfile.write(raw.encode("utf-8"))
                return

            if parsed_path_post == "/query":
                prompt = params.get("prompt", [""])[0]
                if not prompt.strip():
                    self._redirect("/chat")
                    return
                sesion_id = self._get_sesion_id()
                historial = self._get_historial()
                historial.append({"tipo": "user", "texto": prompt})

                sc = SesionChat(db)
                if not sesion_id:
                    titulo = prompt[:60]
                    sesion = sc.crear(usuario["id_usuario"], titulo)
                    if not sesion:
                        self._redirect("/chat")
                        return
                    sesion_id = sesion["id_sesion"]
                elif len(historial) <= 2:
                    sc.repo.update_titulo(sesion_id, prompt[:60])
                sc.guardar_mensaje(sesion_id, "user", json.dumps({"texto": prompt}))

                reserva_ctrl = ReservaController(db)
                aulas = reserva_ctrl.buscar_disponibilidad(prompt)

                try:
                    ors = OpenRouterService()
                    contexto = f"Salones disponibles: {[dict(a) for a in aulas]}" if aulas else "No hay disponibilidad"
                    respuesta = ors.consultar(prompt, contexto)
                except Exception as e:
                    logger.error(f"Error en OpenRouter: {e}")
                    respuesta = "Lo siento, el servicio de IA no está disponible."

                if aulas:
                    historial.append({"tipo": "aulas", "data": [dict(a) for a in aulas], "texto": respuesta})
                else:
                    historial.append({"tipo": "bot", "texto": respuesta})

                cookies = [("Set-Cookie", self._set_historial(historial))]
                if sesion_id:
                    ultimo = historial[-1]
                    if ultimo["tipo"] in ("card", "aulas"):
                        sc.guardar_mensaje(sesion_id, "card", json.dumps(ultimo["data"], default=str))
                    elif ultimo["tipo"] == "bot":
                        sc.guardar_mensaje(sesion_id, "bot", json.dumps({"texto": ultimo["texto"]}))
                    cookies.append(("Set-Cookie", f"utp_sesion={sesion_id}; Path=/; Max-Age=86400"))

                self._redirect("/chat#fin", cookies)
                return

            elif parsed_path_post == "/reservar":
                id_espacio = int(params.get("id_espacio", [0])[0])
                nombre_aula = params.get("nombre_aula", [""])[0]

                reserva_ctrl = ReservaController(db)
                exito = reserva_ctrl.procesar_reserva(
                    usuario["id_usuario"], id_espacio
                )

                historial = self._get_historial()
                if exito:
                    historial.append({"tipo": "success", "texto": nombre_aula})
                    logger.info(f"Reserva exitosa: espacio={id_espacio}, usuario={usuario['id_usuario']}")
                    n = Notificacion(db)
                    n.crear(usuario["id_usuario"], "Reserva Confirmada", f"El ambiente {nombre_aula} ha sido reservado exitosamente.", "success")
                    try:
                        cur = db.obtener_conexion().cursor()
                        cur.execute("SELECT id_usuario FROM usuarios WHERE id_rol = (SELECT id_rol FROM roles WHERE nombre = 'Admin')")
                        for row in cur.fetchall():
                            n.crear(row["id_usuario"], "Nueva Reserva Pendiente", f"{usuario['nombre']} reservo {nombre_aula}.", "warning")
                    except Exception:
                        pass
                cookies = [("Set-Cookie", self._set_historial(historial))]
                if exito:
                    sesion_id = self._get_sesion_id()
                    if sesion_id:
                        sc = SesionChat(db)
                        sc.guardar_mensaje(sesion_id, "success", json.dumps({"texto": nombre_aula}))
                        cookies.append(("Set-Cookie", f"utp_sesion={sesion_id}; Path=/; Max-Age=86400"))

                self._redirect("/chat#reservas", cookies)
                return

            elif parsed_path_post == "/admin/salones/eliminar":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_espacio = int(params.get("id_espacio", [0])[0])
                admin = AdminController(db)
                admin.eliminar_espacio(id_espacio)
                self._redirect("/admin/salones")
                return

            elif parsed_path_post == "/admin/salones/estado":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_espacio = int(params.get("id_espacio", [0])[0])
                estado_nuevo = params.get("estado", ["DISPONIBLE"])[0]
                admin = AdminController(db)
                admin.cambiar_estado_espacio(id_espacio, estado_nuevo)
                self._redirect("/admin/salones")
                return

            elif parsed_path_post == "/admin/salones/actualizar":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_espacio = int(params.get("id_espacio", [0])[0])
                nombre = params.get("nombre", [""])[0]
                id_tipo = int(params.get("id_tipo", [0])[0])
                estado_nuevo = params.get("estado", ["DISPONIBLE"])[0]
                ubicacion = params.get("ubicacion", [""])[0]
                capacidad = int(params.get("capacidad", [0])[0])
                equipos_ids = [int(v) for v in params.get("equipamiento", [])]
                soft_ids = [int(v) for v in params.get("software", [])]
                try:
                    conn_upd = db.obtener_conexion()
                    cur_upd = conn_upd.cursor()
                    cur_upd.execute("UPDATE espacios_academicos SET nombre=%s, id_tipo=%s, ubicacion=%s, capacidad=%s, estado=%s WHERE id_espacio=%s",
                                    (nombre, id_tipo, ubicacion, capacidad, estado_nuevo, id_espacio))
                    cur_upd.execute("DELETE FROM espacio_equipamiento WHERE id_espacio = %s", (id_espacio,))
                    for eq_id in equipos_ids:
                        cur_upd.execute("INSERT INTO espacio_equipamiento (id_espacio, id_equipamiento) VALUES (%s, %s)", (id_espacio, eq_id))
                    cur_upd.execute("DELETE FROM espacio_software WHERE id_espacio = %s", (id_espacio,))
                    for sw_id in soft_ids:
                        cur_upd.execute("INSERT INTO espacio_software (id_espacio, id_software) VALUES (%s, %s)", (id_espacio, sw_id))
                    conn_upd.commit()
                    conn_upd.close()
                except Exception as e:
                    logger.error(f"Error actualizando salon: {e}")
                self._redirect("/admin/salones")
                return

            elif parsed_path_post == "/admin/docentes/eliminar":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_docente = int(params.get("id_docente", [0])[0])
                try:
                    from app.models.docente import Docente
                    d_model = Docente(db)
                    conn = db.obtener_conexion()
                    cur = conn.cursor()
                    cur.execute("DELETE FROM docentes WHERE id_docente = %s", (id_docente,))
                    conn.commit()
                    conn.close()
                except Exception as e:
                    logger.error(f"Error eliminando docente: {e}")
                self._redirect("/admin/docentes")
                return

            elif parsed_path_post == "/admin/usuarios/eliminar":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_usuario_u = int(params.get("id_usuario", [0])[0])
                try:
                    conn = db.obtener_conexion()
                    cur = conn.cursor()
                    cur.execute("UPDATE usuarios SET estado = 'INACTIVO', estado_int = 0 WHERE id_usuario = %s", (id_usuario_u,))
                    conn.commit()
                    conn.close()
                except Exception as e:
                    logger.error(f"Error eliminando usuario: {e}")
                self._redirect("/admin/roles")
                return

            elif parsed_path_post == "/admin/usuarios/password":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_usuario_p = int(params.get("id_usuario", [0])[0])
                new_password = params.get("new_password", [""])[0]
                try:
                    repo = UsuarioRepository()
                    if new_password:
                        import bcrypt
                        hashed = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
                        repo.update_password(id_usuario_p, hashed)
                except Exception as e:
                    logger.error(f"Error configurando acceso: {e}")
                self._redirect("/admin/roles")
                return

            elif parsed_path_post == "/admin/aprobar_reserva":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_reserva = int(params.get("id_reserva", [0])[0])
                admin = AdminController(db)
                admin.aprobar_reserva(id_reserva)
                try:
                    cur = db.obtener_conexion().cursor()
                    cur.execute("SELECT id_usuario FROM reservas WHERE id_reserva = %s", (id_reserva,))
                    row = cur.fetchone()
                    if row:
                        n = Notificacion(db)
                        n.crear(row["id_usuario"], "Reserva Aprobada", "Tu reserva ha sido aprobada por administracion.", "success")
                except Exception:
                    pass
                self._redirect("/admin/reservas")
                return

            elif parsed_path_post == "/admin/rechazar_reserva":
                if usuario["rol"] != "Admin":
                    self._redirect("/admin")
                    return
                id_reserva = int(params.get("id_reserva", [0])[0])
                admin = AdminController(db)
                admin.rechazar_reserva(id_reserva)
                try:
                    cur = db.obtener_conexion().cursor()
                    cur.execute("SELECT id_usuario FROM reservas WHERE id_reserva = %s", (id_reserva,))
                    row = cur.fetchone()
                    if row:
                        n = Notificacion(db)
                        n.crear(row["id_usuario"], "Reserva Rechazada", "Tu reserva ha sido rechazada por administracion.", "error")
                except Exception:
                    pass
                self._redirect("/admin/reservas")
                return

            elif parsed_path_post == "/api/notificaciones/leer":
                n = Notificacion(db)
                n.marcar_todas_leidas(usuario["id_usuario"])
                self._responder_html('{"ok": true}')
                return

            else:
                self._redirect("/chat")
                return

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
