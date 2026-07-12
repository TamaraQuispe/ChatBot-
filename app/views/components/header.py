"""Header administrativo con barra superior y notificaciones."""

HEADER_HTML = """<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-40 bg-white/70 backdrop-blur-md border-b border-surface-container-highest">
    <div class="flex justify-between items-center h-14 sm:h-16 px-3 sm:px-container-padding">
        <div class="flex items-center space-x-4 md:space-x-8">
            <button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors" aria-label="Abrir menú lateral">
                <span class="material-symbols-outlined">menu</span>
            </button>
            <div class="hidden md:flex items-center space-x-2 text-label-md text-secondary">
                <span>UTP Academic</span>
                <span class="material-symbols-outlined text-[14px]">chevron_right</span>
                <span class="text-on-surface">Panel de Control</span>
            </div>
        </div>
        <div class="flex items-center space-x-2 sm:space-x-4">
            <div class="relative" id="notif-container">
                <button onclick="toggleNotificaciones()" class="p-2 text-secondary hover:text-primary transition-transform active:scale-95 relative" aria-label="Notificaciones">
                    <span class="material-symbols-outlined">notifications</span>
                    <span id="notif-badge" class="absolute top-1.5 right-1.5 min-w-[8px] h-2 bg-error rounded-full ring-2 ring-white hidden"></span>
                </button>
                <div id="notif-dropdown" class="absolute right-0 top-10 w-80 bg-white rounded-2xl shadow-2xl border border-surface-container-highest hidden overflow-hidden z-50">
                    <div class="flex items-center justify-between px-5 py-4 border-b border-surface-container-highest">
                        <h3 class="font-bold text-sm text-on-surface">Notificaciones</h3>
                        <button onclick="marcarLeidas()" class="text-[11px] text-primary font-bold uppercase hover:underline">Marcar todas leidas</button>
                    </div>
                    <div id="notif-lista" class="max-h-80 overflow-y-auto divide-y divide-surface-container-highest">
                        <div class="px-5 py-8 text-center text-secondary text-sm">Cargando...</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>"""
