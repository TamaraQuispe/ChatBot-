"""Chat page template."""
HTML_CHAT = """
<!DOCTYPE html>
<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Libre+Franklin:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=block" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
try{
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary": "#840015",
                        "utp-red-vibrant": "#bc1127",
                        "utp-red-institutional": "#B00020",
                        "text-primary": "#191c1d",
                        "text-secondary": "#5b403e",
                        "surface": "#f8f9fa",
                        "background": "#ffffff",
                        "error": "#ba1a1a"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.5rem",
                        "lg": "0.75rem",
                        "xl": "1rem",
                        "2xl": "1.5rem",
                        "3xl": "2rem",
                        "full": "9999px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Libre Franklin", "sans-serif"],
                        "body-md": ["Libre Franklin", "sans-serif"],
                        "label-md": ["Libre Franklin", "sans-serif"]
                    }
                },
            },
        }
    }catch(_e){}</script>
<style>
  body { font-family: 'Libre Franklin', sans-serif; background: #f8f9fa; }
  .scrollbar-hide::-webkit-scrollbar { display: none; }
  .message-in { animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
  @keyframes slideIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  .glass-dark { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(0, 0, 0, 0.04); }
  .glass { background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); }
</style>
</head>
<body class="overflow-hidden min-h-screen">

<!-- Mobile Overlay -->
<div id="sidebarOverlay" class="fixed inset-0 bg-black/40 z-30 hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar()"></div>

<!-- Sidebar -->
<aside id="sidebar" class="fixed left-0 top-0 h-screen w-[260px] border-r border-black/5 bg-white/30 backdrop-blur-xl flex flex-col z-50 transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out">
    <div class="px-8 py-10">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-utp-red-institutional rounded-xl flex items-center justify-center shadow-lg shadow-utp-red-institutional/20">
                <span class="text-white font-bold text-xl">U</span>
            </div>
            <div>
                <h1 class="font-headline-lg text-[18px] font-bold text-utp-red-institutional leading-tight tracking-tight">Asistente</h1>
                <p class="font-label-md text-[10px] text-text-secondary uppercase tracking-widest font-semibold">UTP PERU</p>
            </div>
        </div>
    </div>

    <div class="px-4 mb-2">
        <a href="/api/sesion/nueva" class="w-full flex items-center gap-3 px-4 py-3 rounded-2xl bg-utp-red-institutional/10 text-utp-red-institutional hover:bg-utp-red-institutional/20 transition-all duration-200 font-bold text-sm">
            <span class="material-symbols-outlined text-[20px]">add</span>
            <span>Nuevo Chat</span>
        </a>
    </div>
    <nav class="flex-1 px-4 space-y-1 overflow-y-auto scrollbar-hide">
        <a id="nav-chat" class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#" onclick="showView('chat'); return false;">
            <span class="material-symbols-outlined" data-icon="chat">chat</span>
            <span class="font-body-md font-medium">Chat Actual</span>
        </a>
        <div class="h-px bg-black/5 mx-2 my-2"></div>
        <p class="px-4 text-[10px] text-text-secondary/60 font-bold uppercase tracking-widest mb-1">Sesiones Anteriores</p>
        <div id="lista-sesiones" class="space-y-0.5">
            $LISTA_SESIONES
        </div>
        <a id="nav-reservas" class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#" onclick="showView('reservas'); return false;">
            <span class="material-symbols-outlined" data-icon="event_available">event_available</span>
            <span class="font-body-md font-medium">Mis Reservas</span>
        </a>
    </nav>

    <div class="px-4 pb-10 space-y-1">
        <div class="h-px bg-black/5 mx-4 mb-4"></div>
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-error/80 hover:bg-error/5 transition-all duration-200" href="/logout">
            <span class="material-symbols-outlined" data-icon="logout">logout</span>
            <span class="font-body-md font-medium">Cerrar Sesion</span>
        </a>
    </div>
</aside>

<!-- Main Content -->
<main class="ml-0 md:ml-[260px] w-full md:w-[calc(100%-260px)] h-screen flex flex-col relative overflow-hidden">
    <!-- Header -->
    <header class="h-20 flex justify-between items-center px-4 md:px-10 z-40 bg-white/10">
        <div class="flex items-center gap-4 md:gap-6 flex-1">
            <button onclick="toggleSidebar()" class="md:hidden p-2 text-text-secondary hover:text-utp-red-institutional transition-colors">
                <span class="material-symbols-outlined">menu</span>
            </button>
        </div>

        <div class="flex items-center gap-6">
            <div class="relative" id="notif-container">
                <button onclick="toggleNotificaciones()" class="w-10 h-10 flex items-center justify-center text-text-secondary hover:bg-black/5 rounded-full transition-colors relative">
                    <span class="material-symbols-outlined">notifications</span>
                    <span id="notif-badge" class="absolute top-2 right-2 min-w-[8px] h-2 bg-utp-red-institutional rounded-full ring-2 ring-white hidden"></span>
                </button>
                <div id="notif-dropdown" class="absolute right-0 top-12 w-80 bg-white rounded-2xl shadow-2xl border border-black/5 hidden overflow-hidden z-50">
                    <div class="flex items-center justify-between px-5 py-4 border-b border-black/5">
                        <h3 class="font-bold text-sm text-text-primary">Notificaciones</h3>
                        <button onclick="marcarLeidas()" class="text-[11px] text-utp-red-institutional font-bold uppercase hover:underline">Marcar todas leidas</button>
                    </div>
                    <div id="notif-lista" class="max-h-80 overflow-y-auto divide-y divide-black/5">
                        <div class="px-5 py-8 text-center text-text-secondary text-sm">Cargando...</div>
                    </div>
                </div>
            </div>
            <div class="flex items-center gap-4 pl-6 border-l border-black/5">
                <div class="text-right hidden sm:block">
                    <p class="font-bold text-sm text-text-primary">$NOMBRE_DOCENTE</p>
                    <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider">DOCENTE PRINCIPAL</p>
                </div>
                <div class="w-10 h-10 rounded-full border-2 border-white shadow-sm bg-utp-red-institutional flex items-center justify-center text-white font-bold text-sm">U</div>
            </div>
        </div>
    </header>

    <!-- Chat Space -->
    <div class="flex-1 flex overflow-hidden">
        <section class="flex-1 flex flex-col relative overflow-y-auto scrollbar-hide w-full" id="view-chat">
            <div class="max-w-4xl mx-auto w-full px-12 pt-12 pb-48 space-y-12" id="chat-messages">

                $HISTORIAL_CHAT

                <div id="fin"></div>
            </div>
        </section>

        <!-- Mis Reservas View -->
        <section class="hidden flex-1 flex flex-col relative overflow-y-auto scrollbar-hide w-full" id="view-reservas">
            <div class="max-w-6xl mx-auto w-full px-6 md:px-12 pt-12 pb-12">
                <div class="mb-8">
                    <h1 class="font-headline-lg text-2xl font-bold text-text-primary">Historial de Reservas y Reprogramaciones</h1>
                    <p class="text-sm text-text-secondary mt-1">Gestione sus espacios academicos asignados y solicitudes pendientes.</p>
                </div>
                <div class="bg-white rounded-2xl border border-black/5 overflow-hidden shadow-[0_2px_4px_rgba(0,0,0,0.04)]">
                    <div class="p-4 border-b border-black/5 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white">
                        <div class="relative w-full sm:w-72">
                            <span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-text-secondary/60 text-[20px]">search</span>
                            <input class="w-full pl-10 pr-4 py-2.5 border border-black/10 rounded-xl text-sm text-text-primary focus:border-utp-red-institutional focus:ring-2 focus:ring-utp-red-institutional/10 outline-none transition-all bg-white" placeholder="Buscar por aula o ID..." type="text">
                        </div>
                        <button class="flex items-center gap-2 text-sm font-medium text-text-secondary hover:text-text-primary transition-colors border border-black/10 px-4 py-2.5 rounded-xl hover:bg-black/5">
                            <span class="material-symbols-outlined text-[18px]">filter_list</span> Filtrar
                        </button>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full text-left border-collapse">
                            <thead>
                                <tr class="bg-white border-b border-black/5">
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">ID Reserva</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">Aula / Ambiente</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">Tipo de Espacio</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">Fecha</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">Bloque Horario / Turno</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider">Estado</th>
                                    <th class="py-3 px-4 text-[12px] font-bold text-text-secondary uppercase tracking-wider text-right">Acciones</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-black/5 text-sm">
                                $TABLA_RESERVAS
                            </tbody>
                        </table>
                    </div>
                    <div class="p-3 px-4 border-t border-black/5 flex items-center justify-between text-sm text-text-secondary bg-white">
                        <span>Mostrando 1 a 3 de 12 reservas</span>
                        <div class="flex gap-1">
                            <button class="p-1 rounded hover:bg-black/5 disabled:opacity-50"><span class="material-symbols-outlined text-[18px]">chevron_left</span></button>
                            <button class="p-1 rounded hover:bg-black/5"><span class="material-symbols-outlined text-[18px]">chevron_right</span></button>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <!-- Floating Input Area -->
    <div class="absolute bottom-0 left-0 w-full px-8 pb-8 pt-12 bg-gradient-to-t from-background via-background/80 to-transparent pointer-events-none">
        <div class="max-w-3xl mx-auto w-full pointer-events-auto">
            <form method="POST" action="/query" class="glass pl-6 pr-2.5 py-2.5 rounded-[28px] flex items-center gap-3 border border-white shadow-[0_10px_40px_rgba(0,0,0,0.06)] focus-within:shadow-[0_15px_50px_rgba(0,0,0,0.1)] focus-within:ring-2 focus-within:ring-utp-red-institutional/5 transition-all bg-white/60 backdrop-blur-2xl">
                <input class="flex-1 bg-transparent border-none focus:ring-0 text-text-primary text-[16px] placeholder:text-text-secondary/30 py-2.5" name="prompt" placeholder="Escribe tu consulta academica..." type="text"/>
                <button class="w-12 h-12 bg-utp-red-institutional text-white rounded-full flex items-center justify-center shadow-lg shadow-utp-red-institutional/30 hover:scale-105 active:scale-95 transition-all group" type="submit">
                    <span class="material-symbols-outlined group-hover:translate-x-0.5 transition-transform" style="font-variation-settings: 'FILL' 1;">send</span>
                </button>
            </form>
            <p class="text-center text-[10px] text-text-secondary/40 mt-5 font-bold uppercase tracking-[0.25em]">
                Inteligencia Artificial UTP &bull; Modelo Optimizado v2.4
            </p>
        </div>
    </div>

    <!-- Modal Detalles Reserva -->
    <div id="modalDetalles" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="cerrarModal(event)">
        <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
        <div class="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full p-8 transform transition-all" onclick="event.stopPropagation()">
            <button onclick="cerrarModal()" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-text-secondary hover:bg-black/5 rounded-full transition-colors">
                <span class="material-symbols-outlined">close</span>
            </button>
            <div class="flex items-center gap-3 mb-6">
                <div class="w-12 h-12 rounded-2xl bg-utp-red-institutional/10 flex items-center justify-center text-utp-red-institutional">
                    <span class="material-symbols-outlined text-[28px]">assignment</span>
                </div>
                <div>
                    <h3 class="font-bold text-xl text-text-primary">Detalle de Reserva</h3>
                    <p class="text-sm text-text-secondary" id="modal-id">#RES-000</p>
                </div>
            </div>
            <div class="space-y-4">
                <div class="flex justify-between py-3 border-b border-black/5">
                    <span class="text-text-secondary">Aula / Ambiente</span>
                    <span class="font-semibold text-text-primary" id="modal-aula">-</span>
                </div>
                <div class="flex justify-between py-3 border-b border-black/5">
                    <span class="text-text-secondary">Tipo de Espacio</span>
                    <span class="font-semibold text-text-primary" id="modal-tipo">-</span>
                </div>
                <div class="flex justify-between py-3 border-b border-black/5">
                    <span class="text-text-secondary">Ubicacion</span>
                    <span class="font-semibold text-text-primary" id="modal-ubicacion">-</span>
                </div>
                <div class="flex justify-between py-3 border-b border-black/5">
                    <span class="text-text-secondary">Fecha</span>
                    <span class="font-semibold text-text-primary" id="modal-fecha">-</span>
                </div>
                <div class="flex justify-between py-3 border-b border-black/5">
                    <span class="text-text-secondary">Estado</span>
                    <span class="font-semibold" id="modal-estado">-</span>
                </div>
                <div class="flex justify-between py-3">
                    <span class="text-text-secondary">Curso</span>
                    <span class="font-semibold text-text-primary" id="modal-curso">-</span>
                </div>
            </div>
            <button onclick="cerrarModal()" class="mt-6 w-full py-3 bg-utp-red-institutional text-white font-bold rounded-2xl hover:bg-primary transition-all active:scale-[0.98]">
                Cerrar
            </button>
        </div>
    </div>
</main>

<script>
    function showView(view) {
        var chatView = document.getElementById('view-chat');
        var reservasView = document.getElementById('view-reservas');
        var chatInput = document.querySelector('.absolute.bottom-0');

        chatView.classList.add('hidden');
        reservasView.classList.add('hidden');
        if(chatInput) chatInput.classList.add('hidden');

        var navChat = document.getElementById('nav-chat');
        var navReservas = document.getElementById('nav-reservas');
        [navChat, navReservas].forEach(function(el) {
            if(el) { el.classList.remove('bg-utp-red-institutional/10', 'text-utp-red-institutional'); el.classList.add('text-text-secondary'); }
        });

        if (view === 'chat') {
            chatView.classList.remove('hidden');
            if(chatInput) chatInput.classList.remove('hidden');
            if(navChat) { navChat.classList.remove('text-text-secondary'); navChat.classList.add('bg-utp-red-institutional/10', 'text-utp-red-institutional'); }
        } else if (view === 'reservas') {
            reservasView.classList.remove('hidden');
            if(navReservas) { navReservas.classList.remove('text-text-secondary'); navReservas.classList.add('bg-utp-red-institutional/10', 'text-utp-red-institutional'); }
        }
    }

    const chatInput = document.querySelector('input[name="prompt"]');
    if(chatInput) {
        chatInput.addEventListener('focus', () => {
            chatInput.closest('form').classList.add('shadow-[0_15px_50px_rgba(0,0,0,0.1)]');
        });
        chatInput.addEventListener('blur', () => {
            chatInput.closest('form').classList.remove('shadow-[0_15px_50px_rgba(0,0,0,0.1)]');
        });
    }
    function abrirModal(rid, aula, tipo, ubicacion, fecha, estado, estadoClass, curso) {
        document.getElementById('modal-id').textContent = '#RES-' + rid;
        document.getElementById('modal-aula').textContent = aula;
        document.getElementById('modal-tipo').textContent = tipo;
        document.getElementById('modal-ubicacion').textContent = ubicacion || '-';
        document.getElementById('modal-fecha').textContent = fecha;
        document.getElementById('modal-estado').textContent = estado;
        document.getElementById('modal-estado').className = 'font-semibold inline-flex items-center px-2 py-0.5 rounded text-[12px] ' + estadoClass;
        document.getElementById('modal-curso').textContent = curso || '-';
        document.getElementById('modalDetalles').classList.remove('hidden');
    }
    function cerrarModal(e) {
        if(!e || e.target === document.getElementById('modalDetalles')) {
            document.getElementById('modalDetalles').classList.add('hidden');
        }
    }
    function toggleNotificaciones() {
        var dd = document.getElementById('notif-dropdown');
        var isHidden = dd.classList.contains('hidden');
        if (isHidden) {
            dd.classList.remove('hidden');
            cargarNotificaciones();
        } else {
            dd.classList.add('hidden');
        }
    }
    function cargarNotificaciones() {
        fetch('/api/notificaciones').then(function(r) { return r.json(); }).then(function(data) {
            var lista = document.getElementById('notif-lista');
            var badge = document.getElementById('notif-badge');
            if (data.no_leidas > 0) { badge.classList.remove('hidden'); } else { badge.classList.add('hidden'); }
            if (data.items.length === 0) {
                lista.innerHTML = '<div class="px-5 py-8 text-center text-text-secondary text-sm">No tienes notificaciones.</div>';
                return;
            }
            var html = '';
            data.items.forEach(function(n) {
                var bg = n.leida ? '' : 'bg-utp-red-institutional/5';
                var icon = 'info';
                var iconColor = 'text-utp-red-institutional';
                if (n.tipo === 'success') { icon = 'check_circle'; iconColor = 'text-green-600'; }
                else if (n.tipo === 'error') { icon = 'cancel'; iconColor = 'text-red-600'; }
                else if (n.tipo === 'warning') { icon = 'warning'; iconColor = 'text-amber-600'; }
                html += '<div class="flex items-start gap-3 px-5 py-4 ' + bg + '">';
                html += '<span class="material-symbols-outlined text-[20px] ' + iconColor + ' mt-0.5">' + icon + '</span>';
                html += '<div class="flex-1 min-w-0">';
                html += '<p class="font-bold text-sm text-text-primary">' + n.titulo + '</p>';
                html += '<p class="text-xs text-text-secondary mt-0.5">' + n.mensaje + '</p>';
                html += '<p class="text-[10px] text-text-secondary/50 mt-1">' + n.created_at + '</p>';
                html += '</div></div>';
            });
            lista.innerHTML = html;
        }).catch(function() {
            document.getElementById('notif-lista').innerHTML = '<div class="px-5 py-8 text-center text-text-secondary text-sm">Error al cargar.</div>';
        });
    }
    function marcarLeidas() {
        fetch('/api/notificaciones/leer', {method:'POST'}).then(function() {
            document.getElementById('notif-badge').classList.add('hidden');
            cargarNotificaciones();
        });
    }
    document.addEventListener('click', function(e) {
        var dd = document.getElementById('notif-dropdown');
        var btn = document.getElementById('notif-container');
        if (dd && !dd.classList.contains('hidden') && !btn.contains(e.target)) {
            dd.classList.add('hidden');
        }
    });
    document.addEventListener('DOMContentLoaded', function() {
        fetch('/api/notificaciones').then(function(r) { return r.json(); }).then(function(data) {
            var badge = document.getElementById('notif-badge');
            if (data.no_leidas > 0) { badge.classList.remove('hidden'); } else { badge.classList.add('hidden'); }
        });
    });
    function toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const overlay = document.getElementById('sidebarOverlay');
        const isOpen = sidebar.classList.contains('translate-x-0');
        if (isOpen) {
            sidebar.classList.remove('translate-x-0');
            sidebar.classList.add('-translate-x-full');
            overlay.classList.add('hidden');
        } else {
            sidebar.classList.remove('-translate-x-full');
            sidebar.classList.add('translate-x-0');
            overlay.classList.remove('hidden');
        }
    }
</script>
</body></html>
"""
