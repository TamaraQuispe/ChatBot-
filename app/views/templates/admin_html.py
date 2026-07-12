"""Admin dashboard template."""
from app.views.page import render_admin
from app.views.components.modals import MODAL_DETALLE, MODAL_ELIMINAR, MODAL_ESTADO

_CONTENT = """<section class="mb-stack-lg">
<nav class="flex items-center space-x-2 text-label-md text-secondary mb-2">
<span>UTP Academic</span>
<span class="material-symbols-outlined text-[14px]">chevron_right</span>
<span class="text-on-surface">Panel de Control</span>
</nav>
<div class="flex justify-between items-end">
<div>
<h2 class="font-headline-lg text-headline-lg text-on-surface">Panel de Control</h2>
<p class="text-body-lg text-secondary mt-1">Supervision en tiempo real de recursos academicos y operativos.</p>
</div>
</div>
</section>
<section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-section-gap">
<div class="glass-card p-6 border-l-4 border-l-primary">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-primary p-2 bg-primary-fixed rounded-lg">domain</span>
<span class="bg-green-100 text-green-700 px-2 py-1 rounded text-label-md font-bold">+12%</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Salones Activos</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">142</h3>
<svg class="w-20 h-10" viewbox="0 0 100 40"><path d="M0 35 Q 25 10, 50 25 T 100 5" stroke="#b00020" stroke-width="2" fill="none"></path></svg>
</div>
</div>
<div class="glass-card p-6">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-tertiary p-2 bg-surface-container-high rounded-lg">group</span>
<span class="bg-green-100 text-green-700 px-2 py-1 rounded text-label-md font-bold">98%</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Cantidad de Docentes</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">84</h3>
<svg class="w-20 h-10" viewbox="0 0 100 40"><path d="M0 30 Q 20 20, 40 30 T 60 10 T 100 15" stroke="#b00020" stroke-width="2" fill="none"></path></svg>
</div>
</div>
<div class="glass-card p-6">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-amber-600 p-2 bg-amber-50 rounded-lg">event_busy</span>
<span class="bg-amber-100 text-amber-700 px-2 py-1 rounded text-label-md font-bold">24 Pend.</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Reservas Hoy</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">312</h3>
<svg class="w-20 h-10" viewbox="0 0 100 40"><path d="M0 10 Q 30 40, 60 20 T 100 30" stroke="#f59e0b" stroke-width="2" fill="none"></path></svg>
</div>
</div>
</section>
<section class="grid grid-cols-12 gap-gutter">
<div class="col-span-12 lg:col-span-8 glass-card overflow-hidden">
<div class="p-8 border-b border-surface-container-highest flex justify-between items-center">
<h3 class="font-title-lg text-title-lg text-on-surface">Gestion de Salones</h3>
<div class="flex space-x-2">
<span class="px-3 py-1 bg-surface-container text-secondary text-label-md rounded-full">Total: 48</span>
</div>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead class="bg-surface font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">
<tr>
<th class="px-8 py-4">Salon</th>
<th class="px-8 py-4">Pabellon</th>
<th class="px-8 py-4">Estado</th>
<th class="px-8 py-4">Capacidad</th>
<th class="px-8 py-4 text-right">Acciones</th>
</tr>
</thead>
<tbody class="font-body-md text-body-md divide-y divide-surface-container-highest">
$TABLA_ESPACIOS
</tbody>
</table>
</div>
</div>
</section>"""

_JS = """
function verDetalle(id, nombre, tipo, ubicacion, capacidad, equipamiento, software, estado) {
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-tipo').textContent = tipo + ' • ' + estado;
    document.getElementById('modal-icon').textContent = ({AulaTeorica:'meeting_room',AulaLaboratorio:'biotech',SalaComputo:'computer',Auditorio:'theater_comedy',Taller:'handyman'}[tipo]||'domain');
    var html = '';
    [
        ['location_on', 'Ubicacion', ubicacion],
        ['groups', 'Capacidad', capacidad + ' personas'],
        ['memory', 'Equipamiento', equipamiento || 'Ninguno'],
        ['code', 'Software', software || 'Ninguno'],
    ].forEach(function(c) {
        html += '<div class="flex justify-between py-3 border-b border-surface-container-highest"><span class="flex items-center gap-2 text-secondary"><span class="material-symbols-outlined text-[18px]">' + c[0] + '</span>' + c[1] + '</span><span class="font-semibold text-on-surface text-right">' + c[2] + '</span></div>';
    });
    document.getElementById('modal-campos').innerHTML = html;
    document.getElementById('modalDetalle').classList.remove('hidden');
}
function cambiarEstado(id) { document.getElementById('estado-id').value = id; document.getElementById('modalEstado').classList.remove('hidden'); }
function eliminarSalon(id, nombre) { document.getElementById('eliminar-id').value = id; document.getElementById('eliminar-text').textContent = 'Eliminar "'+nombre+'"?'; document.getElementById('modalEliminar').classList.remove('hidden'); }
"""

_MODALS = (
    MODAL_DETALLE
    + MODAL_ELIMINAR.replace("$TITULO", "Eliminar Salon").replace("$MENSAJE", "Estas seguro?").replace("$ACTION", "/admin/salones/eliminar")
    + MODAL_ESTADO.replace("$ESTADO_ACTION", "/admin/salones/estado")
)

HTML_ADMIN = render_admin(_CONTENT, extra_js=_JS, after_footer=_MODALS)
