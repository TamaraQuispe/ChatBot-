"""Componente de sidebar administrativo."""

NAV_ITEMS = [
    ("/admin", "dashboard", "Inicio"),
    ("/admin/salones", "meeting_room", "Salones"),
    ("/admin/software", "computer", "Software y Equipos"),
    ("/admin/docentes", "person", "Docentes"),
    ("/admin/reservas", "event_seat", "Reservas"),
    ("/admin/horarios", "calendar_month", "Horarios"),
    ("/admin/reportes", "bar_chart", "Reportes"),
    ("/admin/roles", "admin_panel_settings", "Roles"),
]


def sidebar_html(active: str = "/admin", extra_items: str = "") -> str:
    items_html = ""
    for url, icon, label in NAV_ITEMS:
        is_active = url == active
        classes = (
            "flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low"
            if is_active else
            "flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200"
        )
        items_html += f"""<a class="{classes}" href="{url}">
            <span class="material-symbols-outlined">{icon}</span>
            <span class="font-medium">{label}</span>
        </a>"""

    return f"""<aside id="sidebar" class="h-screen w-64 fixed left-0 top-0 flex flex-col border-r border-surface-container-highest bg-white z-50 transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out">
    <div class="flex flex-col h-full py-8 px-6">
        <div class="mb-10">
            <span class="font-headline-md text-headline-md font-bold text-primary">UTP Admin</span>
            <p class="text-[10px] uppercase tracking-widest text-secondary font-bold mt-1">SaaS Elite Edition</p>
        </div>
        <nav class="flex-1 space-y-2">
            {items_html}
        </nav>
        <div class="pt-6 border-t border-surface-container-highest space-y-2">
            {extra_items}
            <a class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-error hover:bg-error-container/10 transition-colors" href="/logout">
                <span class="material-symbols-outlined">logout</span>
                <span class="font-medium text-body-md">Cerrar Sesion</span>
            </a>
        </div>
    </div>
</aside>"""
