"""Docentes page template."""
from app.views.page import render_docentes

_MODAL_DETALLE = """<div id="modalDetalle" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalDetalle')" role="dialog" aria-modal="true" aria-labelledby="modal-nombre">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full p-8 transform transition-all" onclick="event.stopPropagation()">
<button onclick="cerrarModal('modalDetalle')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors" aria-label="Cerrar"><span class="material-symbols-outlined">close</span></button>
<div class="flex items-center gap-3 mb-6">
<div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary"><span class="material-symbols-outlined text-[28px]" id="modal-icon">person</span></div>
<div>
<h3 class="font-bold text-xl text-on-surface" id="modal-nombre">-</h3>
<p class="text-sm text-secondary" id="modal-info">-</p>
</div>
</div>
<div class="space-y-4" id="modal-campos"></div>
<button onclick="cerrarModal('modalDetalle')" class="mt-6 w-full py-3 bg-primary text-white font-bold rounded-2xl hover:bg-primary/90 transition-all active:scale-[0.98]">Cerrar</button>
</div>
</div>"""

_MODAL_ELIMINAR = """<div id="modalEliminar" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalEliminar')" role="dialog" aria-modal="true" aria-labelledby="eliminar-text">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-sm w-full p-8 transform transition-all" onclick="event.stopPropagation()">
<div class="text-center">
<div class="w-16 h-16 rounded-full bg-error/10 flex items-center justify-center text-error mx-auto mb-4"><span class="material-symbols-outlined text-[32px]">delete</span></div>
<h3 class="font-bold text-xl text-on-surface mb-2">Eliminar Docente</h3>
<p class="text-sm text-secondary mb-6" id="eliminar-text">¿Estas seguro de eliminar este docente?</p>
<form id="form-eliminar" method="POST" action="/admin/docentes/eliminar" class="flex gap-3">
<input type="hidden" name="id_docente" id="eliminar-id">
<button type="button" onclick="cerrarModal('modalEliminar')" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
<button type="submit" class="flex-1 py-3 bg-error text-white font-bold rounded-2xl hover:bg-error/90 transition-all">Eliminar</button>
</form>
</div>
</div>
</div>"""

_CONTENT = """<section class="flex justify-between items-end mb-12">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Directorio de Docentes</h1>
<p class="text-secondary mt-1">Gestion integral de la plana docente y asignaciones academicas.</p>
</div>
</section>
<section class="grid grid-cols-1 md:grid-cols-2 gap-gutter mb-section-gap">
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg"><span class="material-symbols-outlined text-primary">groups</span></div>
<div class="text-right"><span class="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">trending_up</span> +12%</span></div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Total Docentes</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">$TOTAL_DOCENTES</span>
</div>
<div class="mt-4 h-1 w-full bg-surface-container rounded-full overflow-hidden"><div class="h-full bg-primary w-3/4"></div></div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg"><span class="material-symbols-outlined text-primary">event_available</span></div>
<div class="text-right"><div class="flex items-center gap-1"><div class="w-2 h-2 rounded-full bg-emerald-500"></div><span class="text-[11px] font-bold text-secondary bg-surface-container-low px-2 py-0.5 rounded-full">Online</span></div></div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Activos Hoy</h3>
<div class="flex items-end justify-between"><span class="text-headline-md font-bold">412</span></div>
<div class="flex gap-1 mt-4"><div class="w-2 h-2 rounded-full bg-primary/20"></div><div class="w-2 h-2 rounded-full bg-primary/40"></div><div class="w-2 h-2 rounded-full bg-primary/60"></div><div class="w-2 h-2 rounded-full bg-primary/80"></div><div class="w-2 h-2 rounded-full bg-primary"></div></div>
</div>
</section>
<section class="mb-12">
<div class="glass-panel p-4 rounded-2xl shadow-sm flex flex-col md:flex-row items-center gap-4">
<div class="flex-1 w-full relative">
<span class="absolute inset-y-0 left-4 flex items-center text-secondary"><span class="material-symbols-outlined">filter_alt</span></span>
<input id="searchDocentes" class="w-full pl-12 pr-4 py-2.5 bg-surface-container-low border border-surface-container-highest rounded-xl focus:ring-1 focus:ring-primary focus:border-primary transition-all" placeholder="Filtrar por departamento, grado academico o curso..." type="text"/>
</div>
<select id="filterDepartamento" class="bg-white border border-surface-container-highest rounded-xl px-4 py-2.5 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[200px]">
<option value="">Todos los Departamentos</option>
<option>Ingenieria de Sistemas</option>
<option>Arquitectura</option>
<option>Derecho</option>
<option>Medicina</option>
</select>
<button class="p-2.5 bg-white border border-surface-container-highest rounded-xl hover:bg-surface transition-colors"><span class="material-symbols-outlined text-secondary">grid_view</span></button>
<button class="p-2.5 bg-white border border-surface-container-highest rounded-xl hover:bg-surface transition-colors"><span class="material-symbols-outlined text-primary">view_list</span></button>
</div>
</section>
<section class="glass-panel rounded-2xl shadow-sm mb-section-gap">
<div class="overflow-x-auto">
<table id="tabla-docentes" class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low/50">
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Docente</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Departamento</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Cursos Asignados</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Contacto</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Estado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_DOCENTES
</tbody>
</table>
</div>
<div class="px-6 py-4 flex items-center justify-between border-t border-surface-container-highest bg-white">
<p class="text-secondary text-label-md">Mostrando <span class="font-bold text-on-surface">$TOTAL_DOCENTES</span> docentes</p>
<div class="flex gap-2">
<button class="px-3 py-1.5 border border-surface-container-highest rounded-lg text-label-md font-medium text-secondary disabled:opacity-50" disabled>Anterior</button>
<button class="px-3 py-1.5 bg-white border border-surface-container-highest rounded-lg text-label-md font-bold text-primary shadow-sm">1</button>
<button class="px-3 py-1.5 border border-surface-container-highest rounded-lg text-label-md font-medium text-secondary hover:bg-white transition-colors">2</button>
<button class="px-3 py-1.5 border border-surface-container-highest rounded-lg text-label-md font-medium text-secondary hover:bg-white transition-colors">3</button>
<span class="px-2 self-center text-secondary">...</span>
<button class="px-3 py-1.5 border border-surface-container-highest rounded-lg text-label-md font-medium text-secondary hover:bg-white transition-colors">Siguiente</button>
</div>
</div>
</section>"""

_JS = """
function verDetalleDocente(id, nombre, depto, especialidad, correo, telefono, estado) {
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-info').textContent = depto + ' • ' + estado;
    var html = '';
    [
        ['school', 'Departamento', depto],
        ['psychiatry', 'Especialidad', especialidad],
        ['mail', 'Correo', correo],
        ['call', 'Telefono', telefono],
    ].forEach(function(c) {
        html += '<div class="flex justify-between py-3 border-b border-surface-container-highest"><span class="flex items-center gap-2 text-secondary"><span class="material-symbols-outlined text-[18px]">' + c[0] + '</span>' + c[1] + '</span><span class="font-semibold text-on-surface text-right">' + c[2] + '</span></div>';
    });
    document.getElementById('modal-campos').innerHTML = html;
    document.getElementById('modalDetalle').classList.remove('hidden');
}
function editarDocente(id) { window.location.href = '/admin/docentes/editar?id=' + id; }
function eliminarDocente(id, nombre) {
    document.getElementById('eliminar-id').value = id;
    document.getElementById('eliminar-text').textContent = '¿Estas seguro de eliminar a "' + nombre + '"? Esta accion no se puede deshacer.';
    document.getElementById('modalEliminar').classList.remove('hidden');
}
function filtrarDocentes() {
    var q = document.getElementById('searchDocentes').value.toLowerCase();
    var depto = document.getElementById('filterDepartamento').value;
    document.querySelectorAll('#tabla-docentes tbody tr').forEach(function(r) {
        var search = r.getAttribute('data-search').toLowerCase();
        var match = (!q || search.indexOf(q) !== -1) && (!depto || r.getAttribute('data-departamento').toLowerCase().indexOf(depto.toLowerCase()) !== -1);
        r.style.display = match ? '' : 'none';
    });
}
document.getElementById('searchDocentes').addEventListener('input', filtrarDocentes);
document.getElementById('filterDepartamento').addEventListener('change', filtrarDocentes);
"""

HTML_DOCENTES = render_docentes(_CONTENT, extra_js=_JS, after_footer=_MODAL_DETALLE + _MODAL_ELIMINAR)
