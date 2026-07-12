"""Salones page template."""
from app.views.page import render_salones
from app.views.components.modals import MODAL_DETALLE, MODAL_ELIMINAR, MODAL_ESTADO

_CONTENT = """<section class="flex justify-between items-end mb-12">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Gestion de Salones</h1>
<p class="text-secondary mt-1">Supervision en tiempo real, asignacion de espacios e inventario tecnologico.</p>
</div>
</section>
<section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-section-gap">
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg"><span class="material-symbols-outlined text-primary">domain</span></div>
<div class="text-right"><span class="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">+2.5%</span></div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Total de Salones</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">$TOTAL_SALONES</span>
<div class="w-24 h-10"><svg class="w-full h-full" viewbox="0 0 100 40"><path class="sparkline-svg" d="M0,35 Q10,30 20,38 T40,25 T60,30 T80,10 T100,15"></path></svg></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg"><span class="material-symbols-outlined text-primary">event_available</span></div>
<div class="text-right"><span class="text-[11px] font-bold text-secondary bg-surface-container-low px-2 py-0.5 rounded-full">Actual</span></div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Salones Disponibles</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">88</span>
<div class="w-24 h-10 opacity-50"><svg class="w-full h-full" viewbox="0 0 100 40"><path class="sparkline-svg" d="M0,10 Q10,25 20,20 T40,35 T60,15 T80,25 T100,5"></path></svg></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg"><span class="material-symbols-outlined text-primary">pie_chart</span></div>
<div class="text-right"><span class="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">Alto</span></div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Tasa de Ocupacion</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">76.4%</span>
<div class="w-24 h-10"><svg class="w-full h-full" viewbox="0 0 100 40"><path class="sparkline-svg" d="M0,38 C20,38 20,10 40,10 C60,10 60,25 80,25 C100,25 100,5 100,5"></path></svg></div>
</div>
</div>
</section>
<section class="mb-12">
<div class="glass-panel p-6 rounded-2xl shadow-sm flex flex-col md:flex-row items-center gap-4">
<div class="flex-1 w-full relative">
<span class="absolute inset-y-0 left-4 flex items-center text-secondary"><span class="material-symbols-outlined">search</span></span>
<input id="searchSalones" class="w-full pl-12 pr-4 py-3 bg-surface-container-low border border-surface-container-highest rounded-xl focus:ring-1 focus:ring-primary focus:border-primary transition-all" placeholder="Filtrar por nombre, aula o software (AutoCAD, SAP...)" type="text"/>
</div>
<div class="flex items-center gap-3 w-full md:w-auto">
<select id="filterTipo" class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option value="">Tipo: Todos</option>
<option>SalaComputo</option>
<option>AulaTeorica</option>
<option>AulaLaboratorio</option>
</select>
<select id="filterPabellon" class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option value="">Pabellon</option>
<option value="Pabellon A">Pabellon A</option>
<option value="Pabellon B">Pabellon B</option>
<option value="Pabellon C">Pabellon C</option>
</select>
<button class="p-3 bg-surface-container-low hover:bg-surface-container-highest rounded-xl transition-colors"><span class="material-symbols-outlined">tune</span></button>
</div>
</div>
</section>
<section class="glass-panel rounded-2xl shadow-sm mb-section-gap">
<div class="overflow-x-auto">
<table id="tabla-salones" class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low/50">
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Salon / Tipo</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Ubicacion</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Capacidad</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Software</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Estado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_SALONES
</tbody>
</table>
</div>
<div class="px-6 py-4 flex items-center justify-between border-t border-surface-container-highest bg-white">
<p class="text-secondary text-label-md">Mostrando <span class="font-bold text-on-surface">$TOTAL_SALONES</span> salones</p>
<div class="flex gap-2">
<button class="p-2 rounded-lg border border-surface-container-highest disabled:opacity-50" disabled><span class="material-symbols-outlined">chevron_left</span></button>
<button class="p-2 rounded-lg border border-surface-container-highest hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined">chevron_right</span></button>
</div>
</div>
</section>"""

_JS = """
function verDetalle(id, nombre, tipo, ubicacion, capacidad, equipamiento, software, estado) {
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-tipo').textContent = tipo + ' • ' + estado;
    var icon = document.getElementById('modal-icon');
    var tipos = {'AulaTeorica':'meeting_room','AulaLaboratorio':'biotech','SalaComputo':'computer','Auditorio':'theater_comedy','Taller':'handyman'};
    icon.textContent = tipos[tipo] || 'domain';
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
function editarSalon(id) { window.location.href = '/admin/salones/editar?id=' + id; }
function cambiarEstado(id, actual) { document.getElementById('estado-id').value = id; document.getElementById('modalEstado').classList.remove('hidden'); }
function verHistorial(id) { window.location.href = '/admin/salones/historial?id=' + id; }
function eliminarSalon(id, nombre) {
    document.getElementById('eliminar-id').value = id;
    document.getElementById('eliminar-text').textContent = '¿Estas seguro de eliminar "' + nombre + '"? Esta accion no se puede deshacer.';
    document.getElementById('modalEliminar').classList.remove('hidden');
}
function filtrarSalones() {
    var q = document.getElementById('searchSalones').value.toLowerCase();
    var tipo = document.getElementById('filterTipo').value;
    var pab = document.getElementById('filterPabellon').value;
    document.querySelectorAll('#tabla-salones tbody tr').forEach(function(r) {
        var search = r.getAttribute('data-search').toLowerCase();
        var match = (!q || search.indexOf(q) !== -1) && (!tipo || r.getAttribute('data-tipo') === tipo) && (!pab || r.getAttribute('data-ubicacion').indexOf(pab) !== -1);
        r.style.display = match ? '' : 'none';
    });
}
document.getElementById('searchSalones').addEventListener('input', filtrarSalones);
document.getElementById('filterTipo').addEventListener('change', filtrarSalones);
document.getElementById('filterPabellon').addEventListener('change', filtrarSalones);
"""

_MODALS = (
    MODAL_DETALLE
    + MODAL_ELIMINAR.replace("$TITULO", "Eliminar Salon").replace("$MENSAJE", "Estas seguro de eliminar este salon?").replace("$ACTION", "/admin/salones/eliminar")
    + MODAL_ESTADO.replace("$ESTADO_ACTION", "/admin/salones/estado")
)

HTML_SALONES = render_salones(_CONTENT, extra_js=_JS, after_footer=_MODALS)
