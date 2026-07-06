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

            iconos = {"COMPUTO": "computer", "TEORICA": "school"}
            filas_html = ""
            for e in espacios:
                icono = iconos.get(e["tipo"], "meeting_room")
                inicial = e["nombre"][0] if e["nombre"] else "?"
                color_estado = "bg-green-100 text-green-700 bg-green-500" if e["estado"] == "DISPONIBLE" else "bg-primary/10 text-primary bg-primary"
                texto_estado = "Disponible" if e["estado"] == "DISPONIBLE" else "Ocupado"
                filas_html += f'''
                <tr class="hover:bg-surface-bright transition-colors group">
                <td class="px-4 lg:px-6 py-3 lg:py-4">
                <div class="flex items-center gap-2 lg:gap-3">
                <div class="w-8 h-8 lg:w-10 lg:h-10 rounded bg-surface-container-high flex items-center justify-center text-primary font-bold text-[11px] lg:text-sm flex-shrink-0">{inicial}</div>
                <div>
                <p class="font-body-md font-bold text-on-surface text-[13px] lg:text-[15px]">{e["nombre"]}</p>
                <p class="text-[10px] lg:text-xs text-secondary">ID: UTP-ARE-{e["id_espacio"]:03d}</p>
                </div>
                </div>
                </td>
                <td class="px-4 lg:px-6 py-3 lg:py-4">
                <div class="flex items-center gap-1.5 lg:gap-2">
                <span class="material-symbols-outlined text-[16px] lg:text-sm text-secondary">{icono}</span>
                <span class="font-body-sm text-on-surface text-[12px] lg:text-[14px]">{e["tipo"].capitalize()}</span>
                </div>
                </td>
                <td class="px-4 lg:px-6 py-3 lg:py-4 text-center">
                <span class="font-body-sm text-on-surface text-[12px] lg:text-[14px]">{e["capacidad"]} pax</span>
                </td>
                <td class="px-4 lg:px-6 py-3 lg:py-4">
                <p class="font-body-sm text-on-surface text-[12px] lg:text-[14px]">{e["ubicacion"]}</p>
                </td>
                <td class="px-4 lg:px-6 py-3 lg:py-4">
                <span class="inline-flex items-center gap-1 px-2 lg:px-2.5 py-0.5 lg:py-1 rounded-full {color_estado.split()[0]} {color_estado.split()[1]} text-[10px] lg:text-xs font-bold whitespace-nowrap">
                <span class="w-1 h-1 lg:w-1.5 lg:h-1.5 rounded-full {color_estado.split()[2]}"></span> {texto_estado}
                </span>
                </td>
                <td class="px-4 lg:px-6 py-3 lg:py-4 text-right">
                <button class="text-primary font-bold text-[11px] lg:text-body-sm hover:underline flex items-center gap-1 justify-end ml-auto">
                Ver Detalles <span class="material-symbols-outlined text-[14px] lg:text-sm">arrow_forward</span>
                </button>
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