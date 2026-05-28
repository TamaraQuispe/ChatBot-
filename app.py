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
                    <div class="flex justify-end message-in">
                        <div class="max-w-[80%] bg-[#465f88] text-white p-4 rounded-xl rounded-tr-none shadow-sm">
                            <p class="text-sm">{texto}</p>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "bot":
                    texto = escapar(msg["texto"])
                    historial_rendered += f'''
                    <div class="flex justify-start gap-3 message-in">
                        <div class="w-8 h-8 rounded-full bg-[#9e001f] flex items-center justify-center text-white text-xs">🤖</div>
                        <div class="bg-white border p-4 rounded-xl rounded-tl-none shadow-sm text-gray-800 max-w-[85%]">
                            <p class="text-sm">{texto}</p>
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
                    <div class="flex items-start gap-3 message-in">
                        <div class="flex flex-col items-center">
                            <div class="w-8 h-8 rounded-full bg-[#9e001f] flex items-center justify-center text-white text-xs shrink-0">🤖</div>
                            <div class="w-0.5 flex-1 min-h-[20px] bg-[#9e001f]/20 mt-1"></div>
                        </div>
                        <div class="bg-white border border-l-4 border-[#9e001f] rounded-xl overflow-hidden shadow-lg max-w-sm flex-1">
                            <div class="p-4 bg-gray-50 border-b flex justify-between items-center">
                                <div>
                                    <h3 class="font-bold text-lg text-[#9e001f]">{nombre}</h3>
                                    <p class="text-xs text-gray-500 font-bold uppercase">{ubicacion}</p>
                                </div>
                                <span class="text-[10px] font-bold bg-green-100 text-green-700 px-2 py-0.5 rounded-full">DISPONIBLE</span>
                            </div>
                            <div class="p-4 grid grid-cols-2 gap-3 text-xs text-gray-600">
                                <div>👥 <strong>Capacidad:</strong> {capacidad} Alumnos</div>
                                <div>💻 <strong>Equipamiento:</strong> {equipamiento}</div>
                                <div class="col-span-2">🛠️ <strong>Software:</strong> {software}</div>
                                <div class="col-span-2">⏰ <strong>Horario Propuesto:</strong> 15:00 - 17:00 (Jueves)</div>
                            </div>
                            <div class="p-4 pt-0">
                                <form method="POST" action="/reservar">
                                    <input type="hidden" name="id_espacio" value="{id_espacio}">
                                    <input type="hidden" name="nombre_aula" value="{nombre}">
                                    <button type="submit" class="w-full bg-[#9e001f] text-white py-2 rounded-lg font-bold hover:bg-[#c8102e] transition-all text-xs">
                                        Confirmar Reserva
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>
                    '''
                elif msg["tipo"] == "success":
                    texto = escapar(msg["texto"])
                    historial_rendered += f'''
                    <div class="flex justify-start gap-3 message-in">
                        <div class="w-8 h-8 rounded-full bg-green-600 flex items-center justify-center text-white text-xs">&#10003;</div>
                        <div class="bg-green-50 border border-green-200 p-4 rounded-xl rounded-tl-none shadow-sm text-green-800">
                            <p class="text-sm font-bold">Reserva Confirmada Exitosamente</p>
                            <p class="text-xs mt-1">El ambiente <strong>{texto}</strong> ha sido asignado y el estado cambio a OCUPADO en PostgreSQL.</p>
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