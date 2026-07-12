"""Header template for admin pages."""
HEADER_HTML = """
<!-- TopNavBar -->
<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-40 bg-white/70 backdrop-blur-md border-b border-surface-container-highest">
<div class="flex justify-between items-center h-14 sm:h-16 px-3 sm:px-container-padding">
<div class="flex items-center space-x-4 md:space-x-8">
<button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
<div class="flex items-center space-x-2 sm:space-x-4">
<div class="relative" id="notif-container">
<button onclick="toggleNotificaciones()" class="p-2 text-secondary hover:text-primary transition-transform active:scale-95 relative">
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
</header>
<script>
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
</script>
"""
