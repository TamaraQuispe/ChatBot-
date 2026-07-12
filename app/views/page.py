"""Constructor de páginas administrativas."""
from app.views.components.sidebar import sidebar_html
from app.views.components.footer import FOOTER_HTML
from app.views.components.modals import MODAL_DETALLE, MODAL_ELIMINAR, MODAL_ESTADO
from app.views.styles import SHARED_STYLES, TAILWIND_CONFIG
from app.views.scripts import SHARED_ADMIN_JS, NOTIFICACION_JS

HEAD_TPL = """<!DOCTYPE html>
<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | %s</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;500;600;700;900&amp;family=Courier+Prime&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script>%s</script>
<style>%s%s</style>
</head>"""


def _head(title: str, extra_css: str = "") -> str:
    return HEAD_TPL % (title, TAILWIND_CONFIG, SHARED_STYLES, extra_css)


def _admin_wrapper(
    title: str,
    sidebar_active: str,
    content: str,
    extra_js: str = "",
    extra_css: str = "",
    after_footer: str = "",
    sidebar_extra: str = "",
    main_class: str = "ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] min-h-screen pb-20",
    content_class: str = "mt-24 px-container-padding",
    body_class: str = "flex min-h-screen",
) -> str:
    return f"""{_head(title, extra_css)}
<body class="{body_class}">
<div id="sidebarOverlay" class="fixed inset-0 bg-black/40 z-30 hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar()"></div>
{sidebar_html(sidebar_active, sidebar_extra)}
<main class="{main_class}">
$HEADER
<div class="{content_class}">
{content}
</div>
{FOOTER_HTML}
{after_footer}
</main>
<script>{SHARED_ADMIN_JS}{NOTIFICACION_JS}{extra_js}</script>
</body></html>"""


def render_admin(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Admin Dashboard", "/admin", content, extra_js, extra_css, **kw)


def render_salones(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Gestion de Salones", "/admin/salones", content, extra_js, extra_css, **kw)


def render_software(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Software y Equipos", "/admin/software", content, extra_js, extra_css, **kw)


def render_docentes(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Gestion de Docentes", "/admin/docentes", content, extra_js, extra_css, **kw)


def render_reservas(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Gestion de Reservas", "/admin/reservas", content, extra_js, extra_css, **kw)


def render_roles(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Gestion de Roles", "/admin/roles", content, extra_js, extra_css, **kw)


def render_reportes(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Reportes", "/admin/reportes", content, extra_js, extra_css, **kw)


def render_horarios(content: str, extra_js: str = "", extra_css: str = "", **kw) -> str:
    return _admin_wrapper("Horarios", "/admin/horarios", content, extra_js, extra_css, **kw)
