"""Roles page template."""
from app.views.page import render_roles

_MODAL_DETALLE = """<div id="modalDetalle" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalDetalle')" role="dialog" aria-modal="true" aria-labelledby="modal-nombre">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full p-8 transform transition-all" onclick="event.stopPropagation()">
<button onclick="cerrarModal('modalDetalle')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors" aria-label="Cerrar"><span class="material-symbols-outlined">close</span></button>
<div class="flex items-center gap-3 mb-6">
<div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary"><span class="material-symbols-outlined text-[28px]" id="modal-icon">person</span></div>
<div>
<h3 class="font-bold text-xl text-on-surface" id="modal-nombre">-</h3>
<p class="text-sm text-secondary" id="modal-roles">-</p>
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
<h3 class="font-bold text-xl text-on-surface mb-2">Eliminar Usuario</h3>
<p class="text-sm text-secondary mb-6" id="eliminar-text">¿Estas seguro de eliminar este usuario?</p>
<form id="form-eliminar" method="POST" action="/admin/usuarios/eliminar" class="flex gap-3">
<input type="hidden" name="id_usuario" id="eliminar-id">
<button type="button" onclick="cerrarModal('modalEliminar')" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
<button type="submit" class="flex-1 py-3 bg-error text-white font-bold rounded-2xl hover:bg-error/90 transition-all">Eliminar</button>
</form>
</div>
</div>
</div>"""

_MODAL_PASSWORD = """<div id="modalPassword" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalPassword')" role="dialog" aria-modal="true">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-md w-full p-8 transform transition-all" onclick="event.stopPropagation()">
<button onclick="cerrarModal('modalPassword')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors" aria-label="Cerrar"><span class="material-symbols-outlined">close</span></button>
<div class="flex items-center gap-3 mb-6">
<div class="w-12 h-12 rounded-2xl bg-amber-50 flex items-center justify-center text-amber-600"><span class="material-symbols-outlined text-[28px]">lock_reset</span></div>
<div>
<h3 class="font-bold text-xl text-on-surface">Cambiar Contrasena</h3>
<p class="text-sm text-secondary" id="password-nombre">-</p>
</div>
</div>
<form method="POST" action="/admin/usuarios/password" class="space-y-4">
<input type="hidden" name="id_usuario" id="password-id">
<div>
<label class="block text-sm font-bold text-secondary mb-1">Nueva Contrasena</label>
<input type="text" name="new_password" required class="w-full px-4 py-3 border border-surface-container-highest rounded-xl focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Escribe la nueva contrasena">
</div>
<button type="submit" class="w-full py-3 bg-amber-600 text-white font-bold rounded-2xl hover:bg-amber-700 transition-all">Actualizar Contrasena</button>
</form>
</div>
</div>"""

_CONTENT = """<section class="flex justify-between items-end mb-12">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Roles</h1>
</div>
</section>
<section class="mb-section-gap">
<div class="flex justify-between items-center mb-6">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-primary">group</span>
<h3 class="font-headline-md text-headline-md text-on-surface">Usuarios Activos</h3>
</div>
<div class="flex items-center gap-2">
<span class="text-label-md text-secondary">Filtrar por:</span>
<select id="filterRol" class="border border-surface-container-highest rounded-lg text-label-md py-1 px-3 focus:ring-primary">
<option value="">Todos los Roles</option>
<option value="Admin">Admin</option>
<option value="Docente">Docente</option>
<option value="Estudiante">Estudiante</option>
</select>
</div>
</div>
<div class="bg-white border border-surface-container-highest rounded-2xl overflow-x-auto shadow-sm">
<table id="tabla-roles" class="w-full text-left">
<thead class="bg-surface-container-low border-b border-surface-container-highest">
<tr>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Usuario</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Rol Asignado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Estado</th>
<th class="px-6 py-4"></th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_USUARIOS
</tbody>
</table>
<div class="px-6 py-4 bg-surface-container-low flex justify-between items-center">
<span class="text-label-md text-secondary">Mostrando 1-10 de 171 usuarios</span>
<div class="flex gap-2">
<button class="p-1 border border-surface-container-highest rounded hover:bg-white transition-colors disabled:opacity-50" disabled><span class="material-symbols-outlined">chevron_left</span></button>
<button class="p-1 border border-surface-container-highest rounded hover:bg-white transition-colors"><span class="material-symbols-outlined">chevron_right</span></button>
</div>
</div>
</div>
</section>"""

_JS = """
function verDetalleUsuario(id, nombre, username, rol, estado) {
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-roles').textContent = '@' + username + ' • ' + rol;
    var html = '';
    [
        ['badge', 'Username', '@' + username],
        ['admin_panel_settings', 'Rol', rol],
        ['check_circle', 'Estado', estado],
    ].forEach(function(c) {
        html += '<div class="flex justify-between py-3 border-b border-surface-container-highest"><span class="flex items-center gap-2 text-secondary"><span class="material-symbols-outlined text-[18px]">' + c[0] + '</span>' + c[1] + '</span><span class="font-semibold text-on-surface text-right">' + c[2] + '</span></div>';
    });
    document.getElementById('modal-campos').innerHTML = html;
    document.getElementById('modalDetalle').classList.remove('hidden');
}
function editarUsuario(id, nombre) { 
    document.getElementById('password-id').value = id;
    document.getElementById('password-nombre').textContent = nombre;
    document.getElementById('modalPassword').classList.remove('hidden');
}
function eliminarUsuario(id, nombre) {
    document.getElementById('eliminar-id').value = id;
    document.getElementById('eliminar-text').textContent = '¿Estas seguro de eliminar a "' + nombre + '"? Esta accion no se puede deshacer.';
    document.getElementById('modalEliminar').classList.remove('hidden');
}
function filtrarRoles() {
    var q = document.getElementById('searchRoles') ? document.getElementById('searchRoles').value.toLowerCase() : '';
    var rol = document.getElementById('filterRol').value;
    document.querySelectorAll('#tabla-roles tbody tr').forEach(function(r) {
        var search = r.getAttribute('data-search').toLowerCase();
        var match = (!q || search.indexOf(q) !== -1) && (!rol || r.getAttribute('data-rol') === rol);
        r.style.display = match ? '' : 'none';
    });
}
document.getElementById('filterRol').addEventListener('change', filtrarRoles);
"""

HTML_ROLES = render_roles(_CONTENT, extra_js=_JS, after_footer=_MODAL_DETALLE + _MODAL_ELIMINAR + _MODAL_PASSWORD)
