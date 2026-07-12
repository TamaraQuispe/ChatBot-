"""JavaScript compartido entre todas las páginas admin."""
# ruff: noqa: E501

SHARED_ADMIN_JS = """
var menuAbierto = null;

function toggleAcciones(btn) {
    var td = btn.closest('td');
    var menu = td.querySelector('.acciones-menu');
    if(!menu) return;
    if(menuAbierto && menuAbierto !== menu) menuAbierto.classList.add('hidden');
    menu.classList.toggle('hidden');
    menuAbierto = menu.classList.contains('hidden') ? null : menu;
}

function cerrarModal(id) {
    document.getElementById(id).classList.add('hidden');
}

function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var overlay = document.getElementById('sidebarOverlay');
    if (!sidebar || !overlay) return;
    var isOpen = sidebar.classList.contains('translate-x-0');
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

document.addEventListener('click', function(e) {
    if (!e.target.closest('.acciones-menu') && !e.target.closest('button[onclick*="toggleAcciones"]')) {
        document.querySelectorAll('.acciones-menu').forEach(function(m) { m.classList.add('hidden'); });
        menuAbierto = null;
    }
});
"""

NOTIFICACION_JS = """
function toggleNotificaciones() {
    var dd = document.getElementById('notif-dropdown');
    if (!dd) return;
    var isHidden = dd.classList.contains('hidden');
    if (isHidden) { dd.classList.remove('hidden'); cargarNotificaciones(); }
    else { dd.classList.add('hidden'); }
}

function cargarNotificaciones() {
    fetch('/api/notificaciones').then(function(r){return r.json()}).then(function(data){
        var lista = document.getElementById('notif-lista');
        var badge = document.getElementById('notif-badge');
        if (!lista || !badge) return;
        if (data.no_leidas > 0) { badge.classList.remove('hidden'); } else { badge.classList.add('hidden'); }
        if (data.items.length === 0) {
            lista.innerHTML = '<div class="px-5 py-8 text-center text-secondary text-sm">No tienes notificaciones.</div>';
            return;
        }
        var html = '';
        data.items.forEach(function(n){
            var bg = n.leida ? '' : 'bg-primary/5';
            var icon = 'info'; var iconColor = 'text-primary';
            if (n.tipo === 'success') { icon = 'check_circle'; iconColor = 'text-green-600'; }
            else if (n.tipo === 'error') { icon = 'cancel'; iconColor = 'text-red-600'; }
            else if (n.tipo === 'warning') { icon = 'warning'; iconColor = 'text-amber-600'; }
            html += '<div class="flex items-start gap-3 px-5 py-4 ' + bg + '">';
            html += '<span class="material-symbols-outlined text-[20px] ' + iconColor + ' mt-0.5">' + icon + '</span>';
            html += '<div class="flex-1 min-w-0">';
            html += '<p class="font-bold text-sm text-on-surface">' + n.titulo + '</p>';
            html += '<p class="text-xs text-secondary mt-0.5">' + n.mensaje + '</p>';
            html += '<p class="text-[10px] text-secondary/50 mt-1">' + n.created_at + '</p>';
            html += '</div></div>';
        });
        lista.innerHTML = html;
    }).catch(function(){ var l=document.getElementById('notif-lista'); if(l) l.innerHTML='<div class="px-5 py-8 text-center text-secondary text-sm">Error al cargar.</div>'; });
}

function marcarLeidas() {
    fetch('/api/notificaciones/leer', {method:'POST'}).then(function(){
        var b=document.getElementById('notif-badge'); if(b) b.classList.add('hidden');
        cargarNotificaciones();
    });
}

document.addEventListener('click', function(e){
    var dd = document.getElementById('notif-dropdown');
    var btn = document.getElementById('notif-container');
    if (dd && !dd.classList.contains('hidden') && btn && !btn.contains(e.target)) dd.classList.add('hidden');
});

document.addEventListener('DOMContentLoaded', function(){
    fetch('/api/notificaciones').then(function(r){return r.json()}).then(function(data){
        var b=document.getElementById('notif-badge'); if(!b) return;
        if(data.no_leidas>0) b.classList.remove('hidden'); else b.classList.add('hidden');
    });
});
"""
