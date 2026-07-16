"""Horarios page template."""
from app.views.page import render_horarios

_CONTENT = """<section class="px-0 pt-6 bg-surface flex-shrink-0">
<div class="flex justify-between items-end mb-6">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Gestion de Horarios Academicos</h1>
<p class="text-secondary mt-1">Planificacion semanal de infraestructura y facultades - Semestre 2024-II</p>
</div>
<div class="flex gap-3">
<div class="flex bg-white border border-surface-container-highest rounded-lg p-1">
<button class="px-4 py-1.5 bg-surface-container-high rounded font-label-md text-label-md">Semana</button>
<button class="px-4 py-1.5 hover:bg-surface-container-low rounded font-label-md text-label-md transition-colors">Mes</button>
</div>
<button class="flex items-center gap-2 px-4 py-2 border border-surface-container-highest bg-white rounded-lg font-label-md text-label-md hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-sm">filter_list</span> Filtros Avanzados
</button>
</div>
</div>
<div class="grid grid-cols-2 sm:grid-cols-4 gap-gutter mb-6">
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Edificio</span>
<select class="bg-transparent border-none p-0 focus:ring-0 font-title-lg text-title-lg text-on-surface">
<option>Torre Tecnologica A</option>
<option>Pabellon de Ciencias</option>
<option>Campus Central</option>
</select>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Tipo de Aula</span>
<select class="bg-transparent border-none p-0 focus:ring-0 font-title-lg text-title-lg text-on-surface">
<option>Laboratorio High-End</option>
<option>Aula Magistral</option>
<option>Taller Creativo</option>
</select>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Franja Horaria</span>
<div class="flex items-center justify-between">
<span class="font-title-lg text-title-lg">07:00 - 22:00</span>
<span class="material-symbols-outlined text-primary">schedule</span>
</div>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2 border-l-4 border-l-primary">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Ocupacion Actual</span>
<div class="flex items-baseline gap-2">
<span class="font-display-lg text-display-lg text-primary">84%</span>
<span class="text-label-md font-label-md text-green-600 flex items-center"><span class="material-symbols-outlined text-xs">trending_up</span> 12%</span>
</div>
</div>
</div>
</section>"""

_CALENDAR = """<section class="flex-1 px-0 pb-0 overflow-hidden flex flex-col">
<div class="bg-white border border-surface-container-highest rounded-2xl flex-1 flex flex-col overflow-hidden shadow-sm">
<div class="overflow-x-auto w-full">
<div class="calendar-grid border-b border-surface-container-highest bg-surface-container-lowest">
<div class="p-4 border-r border-surface-container-highest"></div>
<div class="p-4 border-r border-surface-container-highest text-center"><span class="block text-label-md font-label-md text-secondary mb-1">LUNES</span><span class="font-title-lg text-title-lg">18</span></div>
<div class="p-4 border-r border-surface-container-highest text-center bg-primary-fixed/20"><span class="block text-label-md font-label-md text-primary mb-1">MARTES</span><span class="font-title-lg text-title-lg text-primary">19</span></div>
<div class="p-4 border-r border-surface-container-highest text-center"><span class="block text-label-md font-label-md text-secondary mb-1">MIERCOLES</span><span class="font-title-lg text-title-lg">20</span></div>
<div class="p-4 border-r border-surface-container-highest text-center"><span class="block text-label-md font-label-md text-secondary mb-1">JUEVES</span><span class="font-title-lg text-title-lg">21</span></div>
<div class="p-4 text-center"><span class="block text-label-md font-label-md text-secondary mb-1">VIERNES</span><span class="font-title-lg text-title-lg">22</span></div>
</div>
<div class="flex-1 overflow-y-auto custom-scrollbar relative">
<div class="calendar-grid min-h-[800px]">
<div class="bg-surface-container-lowest border-r border-surface-container-highest">
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary">07:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">08:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">09:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">10:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">11:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">12:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">13:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">14:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">15:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">16:00</div>
</div>
$CONTENIDO_CALENDARIO
</div>
</div>
</div>
</div>
</section>"""

_JS = """
var calendarBody = document.querySelector('.overflow-y-auto');
if (calendarBody) calendarBody.scrollTop = 150;
document.querySelectorAll('[style*="height"]').forEach(function(card) {
    card.addEventListener('mouseenter', function() { card.style.zIndex = '30'; });
    card.addEventListener('mouseleave', function() { card.style.zIndex = '10'; });
});
"""

_EXTRA_CSS = """
.calendar-grid {
    display: grid;
    grid-template-columns: 80px repeat(5, 1fr);
    min-width: 600px;
    overflow-x: auto;
}
.custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
.custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
.custom-scrollbar::-webkit-scrollbar-thumb { background: #e1e3e4; border-radius: 10px; }
"""

HTML_HORARIOS = render_horarios(
    _CONTENT + _CALENDAR,
    extra_js=_JS,
    extra_css=_EXTRA_CSS,
    main_class="ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] h-screen flex flex-col overflow-hidden",
    content_class="mt-16 flex-1 flex flex-col overflow-hidden",
    body_class="font-body-md text-body-md overflow-hidden",
    sidebar_extra='<button class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined">account_circle</span><span class="font-medium text-body-md">Perfil</span></button>'
)
