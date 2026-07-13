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
<h3 class="font-bold text-xl text-on-surface">Configurar Acceso</h3>
<p class="text-sm text-secondary" id="password-nombre">-</p>
</div>
</div>
<form method="POST" action="/admin/usuarios/password" class="space-y-4">
<input type="hidden" name="id_usuario" id="password-id">
<div>
<label class="block text-sm font-bold text-secondary mb-1">Nueva Contrasena</label>
<input type="text" name="new_password" class="w-full px-4 py-3 border border-surface-container-highest rounded-xl focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Dejar vacio para no cambiar">
</div>
<button type="submit" class="w-full py-3 bg-amber-600 text-white font-bold rounded-2xl hover:bg-amber-700 transition-all">Guardar Cambios</button>
</form>
</div>
</div>"""

_MODAL_RESET_CONFIRM = """<div id="modalResetConfirm" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalResetConfirm')" role="dialog" aria-modal="true">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-md w-full p-8 transform transition-all text-center" onclick="event.stopPropagation()">
<button onclick="cerrarModal('modalResetConfirm')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors"><span class="material-symbols-outlined">close</span></button>
<div class="w-16 h-16 rounded-full bg-amber-50 flex items-center justify-center text-amber-600 mx-auto mb-4"><span class="material-symbols-outlined text-[32px]">password</span></div>
<h3 class="font-bold text-xl text-on-surface mb-2">Restablecer Contrasena</h3>
<p class="text-sm text-secondary mb-6" id="reset-confirm-text">¿Desea generar una nueva contraseña temporal para este docente?<br><br>La contraseña anterior dejara de ser valida y el docente debera cambiar la contraseña al iniciar sesion.</p>
<div class="flex gap-3">
<button onclick="cerrarModal('modalResetConfirm')" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
<button id="btn-confirm-reset" onclick="ejecutarReset()" class="flex-1 py-3 bg-amber-600 text-white font-bold rounded-2xl hover:bg-amber-700 transition-all disabled:opacity-50">Restablecer</button>
</div>
</div>
</div>"""

_MODAL_RESULT = """<div id="modalResult" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalResult')" role="dialog" aria-modal="true">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-md w-full p-8 transform transition-all text-center" onclick="event.stopPropagation()">
<button onclick="cerrarModal('modalResult')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors"><span class="material-symbols-outlined">close</span></button>
<div class="w-16 h-16 rounded-full bg-emerald-50 flex items-center justify-center text-emerald-600 mx-auto mb-4"><span class="material-symbols-outlined text-[32px]">check_circle</span></div>
<h3 class="font-bold text-xl text-on-surface mb-2">Contraseña Restablecida</h3>
<p class="text-sm text-secondary mb-4">Contraseña temporal generada para <strong id="result-user">-</strong>:</p>
<div id="result-password-box" class="bg-surface-container-low rounded-xl p-4 mb-6 font-mono text-lg font-bold text-on-surface select-all tracking-wider break-all" style="user-select: all;">-</div>
<p class="text-xs text-secondary mb-6">Esta contraseña solo se muestra una vez. Compartala unicamente con el docente.</p>
<div class="flex gap-3">
<button onclick="copiarPassword()" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all"><span class="material-symbols-outlined text-[18px] align-middle">content_copy</span> Copiar Contraseña</button>
<button onclick="cerrarModal('modalResult')" class="flex-1 py-3 bg-primary text-white font-bold rounded-2xl hover:bg-primary/90 transition-all">Cerrar</button>
</div>
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
var resetUserId = 0;
function verDetalleUsuario(id, nombre, username, rol, estado) {
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-roles').textContent = '@' + username + ' • ' + rol;
    var html = '';
    [
        ['badge', 'Username', '@' + username],
        ['admin_panel_settings', 'Rol', rol],
        ['check_circle', 'Estado', estado],
    ].forEach(function(c) {
        html += '<div class="flex justify-between py-3 border-b border-surface-container-highest"><span class="flex items-center gap-2 text-secondary"><span class="material-symbols-outlined text-[18px]">' + c[0] + '</span>' + c[1] + '</span><span class="font-semibold text-on-surface text-right">' + c[2] + '</div>';
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
function resetPassword(id, nombre) {
    resetUserId = id;
    document.getElementById('reset-confirm-text').innerHTML = 'Desea generar una nueva contraseña temporal para <strong>' + nombre + '</strong>?<br><br>La contraseña anterior dejara de ser valida y el docente debera cambiar la contraseña al iniciar sesion.';
    document.getElementById('modalResetConfirm').classList.remove('hidden');
}
function ejecutarReset() {
    var btn = document.getElementById('btn-confirm-reset');
    btn.disabled = true; btn.textContent = 'Restableciendo...';
    fetch('/api/admin/users/' + resetUserId + '/reset-password', {method:'POST'})
    .then(function(r) { return r.json().then(function(d) { return {status: r.status, data: d}; }); })
    .then(function(res) {
        btn.disabled = false; btn.textContent = 'Restablecer';
        cerrarModal('modalResetConfirm');
        if (res.data.error || res.status >= 400) {
            alert(res.data.error || 'Error al restablecer la contrasena');
            return;
        }
        document.getElementById('result-user').textContent = res.data.nombre + ' (@' + res.data.username + ')';
        document.getElementById('result-password-box').textContent = res.data.temp_password;
        document.getElementById('modalResult').classList.remove('hidden');
    })
    .catch(function() {
        btn.disabled = false; btn.textContent = 'Restablecer';
        alert('Error de conexion');
    });
}
function copiarPassword() {
    var text = document.getElementById('result-password-box').textContent;
    navigator.clipboard.writeText(text).then(function() {
        var btn = event.target;
        if (btn.tagName !== 'BUTTON') btn = btn.closest('button');
        btn.innerHTML = '<span class="material-symbols-outlined text-[18px] align-middle">check</span> Copiado';
        setTimeout(function() { btn.innerHTML = '<span class="material-symbols-outlined text-[18px] align-middle">content_copy</span> Copiar Contraseña'; }, 2000);
    }).catch(function() {});
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

HTML_ROLES = render_roles(_CONTENT, extra_js=_JS, after_footer=_MODAL_DETALLE + _MODAL_ELIMINAR + _MODAL_PASSWORD + _MODAL_RESET_CONFIRM + _MODAL_RESULT)
