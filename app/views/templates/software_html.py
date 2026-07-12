"""Software page template."""
HTML_SOFTWARE = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Software y Equipos</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100;300;400;500;600;700;800;900&amp;family=Courier+Prime&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "surface-container-lowest": "#ffffff",
                    "surface-container-highest": "#e1e3e4",
                    "secondary": "#585f64",
                    "on-error": "#ffffff",
                    "on-background": "#191c1d",
                    "on-tertiary": "#ffffff",
                    "on-surface-variant": "#5b403e",
                    "surface-container": "#edeeef",
                    "on-primary-container": "#ffbbb8",
                    "primary-container": "#b00020",
                    "on-error-container": "#93000a",
                    "surface-bright": "#f8f9fa",
                    "on-primary": "#ffffff",
                    "primary-fixed": "#ffdad8",
                    "on-primary-fixed-variant": "#930019",
                    "on-secondary-fixed-variant": "#41484c",
                    "error-container": "#ffdad6",
                    "tertiary-container": "#4f575d",
                    "secondary-fixed": "#dce3e9",
                    "on-secondary-fixed": "#161d21",
                    "inverse-on-surface": "#f0f1f2",
                    "surface-container-high": "#e7e8e9",
                    "surface-container-low": "#f3f4f5",
                    "tertiary-fixed": "#dce3ea",
                    "error": "#ba1a1a",
                    "on-tertiary-container": "#c5ccd3",
                    "surface-variant": "#e1e3e4",
                    "surface-dim": "#d9dadb",
                    "secondary-fixed-dim": "#c0c7cd",
                    "inverse-surface": "#2e3132",
                    "on-primary-fixed": "#410006",
                    "on-tertiary-fixed-variant": "#40484d",
                    "on-tertiary-fixed": "#151d21",
                    "tertiary": "#384045",
                    "on-secondary-container": "#5e656a",
                    "background": "#f8f9fa",
                    "secondary-container": "#dce3e9",
                    "primary-fixed-dim": "#ffb3af",
                    "on-surface": "#191c1d",
                    "surface": "#f8f9fa",
                    "surface-tint": "#bc1127",
                    "outline": "#906f6d",
                    "tertiary-fixed-dim": "#c0c7ce",
                    "on-secondary": "#ffffff",
                    "primary": "#840015",
                    "inverse-primary": "#ffb3af",
                    "outline-variant": "#e4bdbb"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "2xl": "1rem",
                    "3xl": "1.25rem",
                    "full": "9999px"
            },
            "spacing": {
                    "gutter": "24px",
                    "container-padding": "32px",
                    "section-gap": "80px",
                    "stack-md": "16px",
                    "stack-lg": "24px",
                    "stack-sm": "8px"
            },
            "fontFamily": {
                    "headline-md": ["Libre Franklin"],
                    "display-lg": ["Libre Franklin"],
                    "body-lg": ["Libre Franklin"],
                    "title-lg": ["Libre Franklin"],
                    "label-md": ["Libre Franklin"],
                    "headline-lg": ["Libre Franklin"],
                    "mono-sm": ["Courier Prime"],
                    "body-md": ["Libre Franklin"]
            },
            "fontSize": {
                    "headline-md": ["24px", {"lineHeight": "1.3", "letterSpacing": "-0.02em", "fontWeight": "600"}],
                    "display-lg": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.04em", "fontWeight": "700"}],
                    "body-lg": ["16px", {"lineHeight": "1.6", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                    "title-lg": ["18px", {"lineHeight": "1.5", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "label-md": ["12px", {"lineHeight": "1", "letterSpacing": "0.02em", "fontWeight": "500"}],
                    "headline-lg": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.03em", "fontWeight": "600"}],
                    "mono-sm": ["13px", {"lineHeight": "1.5", "letterSpacing": "0em", "fontWeight": "400"}],
                    "body-md": ["14px", {"lineHeight": "1.6", "letterSpacing": "0em", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            background-color: #F8F9FA;
            color: #191C1D;
            -webkit-font-smoothing: antialiased;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .glass-panel {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(230, 232, 235, 1);
        }
        .sparkline-svg {
            stroke: #840015;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
        }
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
        }
        .health-bar {
            height: 6px;
            border-radius: 10px;
            background: #e1e3e4;
            overflow: hidden;
        }
        .health-bar-fill {
            height: 100%;
            border-radius: 10px;
            transition: width 0.8s ease;
        }
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #e1e3e4; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #585f64; }
    </style>
</head>
<body class="font-body-md text-body-md">
<!-- Mobile Overlay -->
<div id="sidebarOverlay" class="fixed inset-0 bg-black/40 z-30 hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar()"></div>
<!-- Side Navigation Shell -->
<aside id="sidebar" class="h-screen w-64 fixed left-0 top-0 flex flex-col border-r border-surface-container-highest bg-white z-[60] transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out">
<div class="flex flex-col h-full py-8 px-6">
<div class="mb-10">
<span class="font-headline-md text-headline-md font-bold text-primary">UTP Admin</span>
<p class="text-[10px] uppercase tracking-widest text-secondary font-bold mt-1">SaaS Elite Edition</p>
</div>
<nav class="flex-1 space-y-2">
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin">
<span class="material-symbols-outlined">dashboard</span>
<span class="font-medium">Inicio</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/salones">
<span class="material-symbols-outlined">meeting_room</span>
<span class="font-medium">Salones</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/software">
<span class="material-symbols-outlined">computer</span>
<span class="font-bold">Software y Equipos</span>
</a>

<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined">person</span>
<span class="font-medium">Docentes</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined">event_seat</span>
<span class="font-medium">Reservas</span>
</a>

<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/roles">
<span class="material-symbols-outlined">admin_panel_settings</span>
<span class="font-medium">Roles</span>
</a>
</nav>
<div class="pt-6 border-t border-surface-container-highest space-y-2">
<a class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-error hover:bg-error-container/10 transition-colors" href="/logout">
<span class="material-symbols-outlined">logout</span>
<span class="font-medium text-body-md">Cerrar Sesion</span>
</a>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] min-h-screen pb-20">
$HEADER
<div class="mt-16 px-container-padding pt-10">
<!-- Page Header -->
<section class="flex justify-between items-end mb-12">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Software y Equipos</h1>

</div>
</section>
<!-- KPI Grid -->
<section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-section-gap">
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg">
<span class="material-symbols-outlined text-primary">devices</span>
</div>
<div class="text-right">
<span class="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full">+3.2%</span>
</div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Total de Activos</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">$TOTAL_ACTIVOS</span>
<div class="w-24 h-10">
<svg class="w-full h-full" viewbox="0 0 100 40">
<path class="sparkline-svg" d="M0,35 Q10,30 20,38 T40,25 T60,30 T80,10 T100,15"></path>
</svg>
</div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg">
<span class="material-symbols-outlined text-primary">warning</span>
</div>
<div class="text-right">
<span class="text-[11px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-full">Por vencer</span>
</div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Licencias por Vencer</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">8</span>
<div class="w-24 h-10">
<svg class="w-full h-full" viewbox="0 0 100 40">
<path class="sparkline-svg" d="M0,10 Q10,25 20,20 T40,35 T60,15 T80,25 T100,5" style="stroke: #f59e0b;"></path>
</svg>
</div>
</div>
</div>
</section>
<!-- Filters and Search Bar -->
<section class="mb-12">
<div class="glass-panel p-6 rounded-2xl shadow-sm flex flex-col md:flex-row items-center gap-4">
<div class="flex-1 w-full relative">
<span class="absolute inset-y-0 left-4 flex items-center text-secondary">
<span class="material-symbols-outlined">search</span>
</span>
<input id="searchSoftware" class="w-full pl-12 pr-4 py-3 bg-surface-container-low border border-surface-container-highest rounded-xl focus:ring-1 focus:ring-primary focus:border-primary transition-all" placeholder="Buscar por activo, categoria, software o licencia..." type="text"/>
</div>
<div class="flex items-center gap-3 w-full md:w-auto">
<select id="filterCategoria" class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option value="">Categoria: Todas</option>
<option value="AulaTeorica">AulaTeorica</option>
<option value="AulaLaboratorio">AulaLaboratorio</option>
<option value="SalaComputo">SalaComputo</option>
<option value="Auditorio">Auditorio</option>
<option value="Taller">Taller</option>
</select>
<select id="filterEstado" class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option value="">Estado: Todos</option>
<option value="DISPONIBLE">Disponible</option>
<option value="OCUPADO">Ocupado</option>
<option value="MANTENIMIENTO">Mantenimiento</option>
</select>
<button class="p-3 bg-surface-container-low hover:bg-surface-container-highest rounded-xl transition-colors">
<span class="material-symbols-outlined">tune</span>
</button>
</div>
</div>
</section>
<!-- Premium Data Table -->
<section class="glass-panel rounded-2xl shadow-sm mb-section-gap">
<div class="overflow-x-auto">
<table id="tabla-software" class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low/50">
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Activo / ID</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Categoria</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Estado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Software / Licencia</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Ultimo Mantenimiento</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_SOFTWARE
</tbody>
</table>
</div>
<!-- Pagination -->
<div class="px-6 py-4 flex items-center justify-between border-t border-surface-container-highest bg-white">
<p class="text-secondary text-label-md">Mostrando <span class="font-bold text-on-surface">$TOTAL_ACTIVOS</span> activos</p>
<div class="flex gap-2">
<button class="p-2 rounded-lg border border-surface-container-highest disabled:opacity-50" disabled>
<span class="material-symbols-outlined">chevron_left</span>
</button>
<button class="p-2 rounded-lg border border-surface-container-highest hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined">chevron_right</span>
</button>
</div>
</div>
</section>
</div>
<!-- Modal Detalle -->
<div id="modalDetalle" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalDetalle')">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <button onclick="cerrarModal('modalDetalle')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors">
            <span class="material-symbols-outlined">close</span>
        </button>
        <div class="flex items-center gap-3 mb-6">
            <div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined text-[28px]" id="modal-icon">computer</span>
            </div>
            <div>
                <h3 class="font-bold text-xl text-on-surface" id="modal-nombre">-</h3>
                <p class="text-sm text-secondary" id="modal-tipo">-</p>
            </div>
        </div>
        <div class="space-y-4" id="modal-campos"></div>
        <button onclick="cerrarModal('modalDetalle')" class="mt-6 w-full py-3 bg-primary text-white font-bold rounded-2xl hover:bg-primary/90 transition-all active:scale-[0.98]">Cerrar</button>
    </div>
</div>

<!-- Modal Confirmar Eliminar -->
<div id="modalEliminar" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalEliminar')">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-sm w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <div class="text-center">
            <div class="w-16 h-16 rounded-full bg-error/10 flex items-center justify-center text-error mx-auto mb-4">
                <span class="material-symbols-outlined text-[32px]">delete</span>
            </div>
            <h3 class="font-bold text-xl text-on-surface mb-2">Eliminar Activo</h3>
            <p class="text-sm text-secondary mb-6" id="eliminar-text">¿Estas seguro de eliminar este activo?</p>
            <form id="form-eliminar" method="POST" action="/admin/salones/eliminar" class="flex gap-3">
                <input type="hidden" name="id_espacio" id="eliminar-id">
                <button type="button" onclick="cerrarModal('modalEliminar')" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
                <button type="submit" class="flex-1 py-3 bg-error text-white font-bold rounded-2xl hover:bg-error/90 transition-all">Eliminar</button>
            </form>
        </div>
    </div>
</div>

<!-- Modal Cambiar Estado -->
<div id="modalEstado" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalEstado')">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-sm w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <div class="flex items-center gap-3 mb-6">
            <div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined text-[28px]">sync_alt</span>
            </div>
            <div>
                <h3 class="font-bold text-xl text-on-surface">Cambiar Estado</h3>
                <p class="text-sm text-secondary">Seleccione el nuevo estado del activo</p>
            </div>
        </div>
        <form method="POST" action="/admin/salones/estado" class="space-y-3">
            <input type="hidden" name="id_espacio" id="estado-id">
            <button type="submit" name="estado" value="DISPONIBLE" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-emerald-200 hover:bg-emerald-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Disponible</p><p class="text-xs text-secondary">Activo libre para uso</p></div>
            </button>
            <button type="submit" name="estado" value="OCUPADO" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-red-200 hover:bg-red-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-red-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Ocupado</p><p class="text-xs text-secondary">Activo en uso actualmente</p></div>
            </button>
            <button type="submit" name="estado" value="MANTENIMIENTO" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-amber-200 hover:bg-amber-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-amber-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Mantenimiento</p><p class="text-xs text-secondary">Activo fuera de servicio</p></div>
            </button>
            <button type="button" onclick="cerrarModal('modalEstado')" class="w-full py-3 text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
        </form>
    </div>
</div>

<!-- Footer Shell -->
<footer class="w-full py-stack-lg mt-section-gap border-t border-surface-container-highest bg-surface">
<div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center px-container-padding gap-4">
<span class="font-label-md text-label-md font-medium text-secondary">© 2024 UTP Academic Management. SaaS Elite Tier.</span>
<div class="flex gap-6 text-secondary text-label-md">
<a class="hover:text-on-surface transition-colors" href="#">Privacidad</a>
<a class="hover:text-on-surface transition-colors" href="#">Soporte</a>
<a class="hover:text-on-surface transition-colors" href="#">API Docs</a>
</div>
</div>
</footer>
</main>
<script>
        document.querySelectorAll('tr').forEach(row => {
            row.addEventListener('mouseenter', () => {
                row.style.cursor = 'pointer';
            });
        });
        function filtrarSoftware() {
            var q = document.getElementById('searchSoftware').value.toLowerCase();
            var cat = document.getElementById('filterCategoria').value;
            var est = document.getElementById('filterEstado').value;
            document.querySelectorAll('#tabla-software tbody tr').forEach(function(r) {
                var search = r.getAttribute('data-search').toLowerCase();
                var match = (!q || search.indexOf(q) !== -1) && (!cat || r.getAttribute('data-tipo') === cat) && (!est || r.getAttribute('data-estado') === est);
                r.style.display = match ? '' : 'none';
            });
        }
        document.getElementById('searchSoftware').addEventListener('input', filtrarSoftware);
        document.getElementById('filterCategoria').addEventListener('change', filtrarSoftware);
        document.getElementById('filterEstado').addEventListener('change', filtrarSoftware);
        const searchInput = document.querySelector('input[type="text"]');
        if (searchInput) {
            searchInput.addEventListener('focus', () => {
                searchInput.parentElement.classList.add('ring-1', 'ring-primary');
            });
            searchInput.addEventListener('blur', () => {
                searchInput.parentElement.classList.remove('ring-1', 'ring-primary');
            });
        }
        var menuAbierto = null;
        function toggleAcciones(btn) {
            var td = btn.closest('td');
            var menu = td.querySelector('.acciones-menu');
            if(!menu) return;
            if(menuAbierto && menuAbierto !== menu) menuAbierto.classList.add('hidden');
            menu.classList.toggle('hidden');
            menuAbierto = menu.classList.contains('hidden') ? null : menu;
        }
        function cerrarModal(id) { document.getElementById(id).classList.add('hidden'); }
        function verDetalle(id, nombre, tipo, equipamiento, software, estado) {
            document.getElementById('modal-nombre').textContent = nombre;
            document.getElementById('modal-tipo').textContent = tipo + ' • ' + estado;
            var icon = document.getElementById('modal-icon');
            var tipos = {'AulaTeorica':'meeting_room','AulaLaboratorio':'biotech','SalaComputo':'computer','Auditorio':'theater_comedy','Taller':'handyman'};
            icon.textContent = tipos[tipo] || 'computer';
            var html = '';
            var campos = [
                ['devices', 'Tipo', tipo],
                ['check_circle', 'Estado', estado],
                ['memory', 'Equipamiento', equipamiento || 'Ninguno'],
                ['code', 'Software', software || 'Ninguno'],
            ];
            campos.forEach(function(c) {
                html += '<div class="flex justify-between py-3 border-b border-surface-container-highest">';
                html += '<span class="flex items-center gap-2 text-secondary"><span class="material-symbols-outlined text-[18px]">' + c[0] + '</span>' + c[1] + '</span>';
                html += '<span class="font-semibold text-on-surface text-right">' + c[2] + '</span>';
                html += '</div>';
            });
            document.getElementById('modal-campos').innerHTML = html;
            document.getElementById('modalDetalle').classList.remove('hidden');
        }
        function editarItem(id) { window.location.href = '/admin/salones/editar?id=' + id; }
        function cambiarEstado(id) {
            document.getElementById('estado-id').value = id;
            document.getElementById('modalEstado').classList.remove('hidden');
        }
        function verHistorial(id) { window.location.href = '/admin/salones/historial?id=' + id; }
        function eliminarItem(id, nombre) {
            document.getElementById('eliminar-id').value = id;
            document.getElementById('eliminar-text').textContent = '¿Estas seguro de eliminar "' + nombre + '"? Esta accion no se puede deshacer.';
            document.getElementById('modalEliminar').classList.remove('hidden');
        }
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.acciones-menu') && !e.target.closest('button[onclick*="toggleAcciones"]')) {
                document.querySelectorAll('.acciones-menu').forEach(function(m) { m.classList.add('hidden'); });
                menuAbierto = null;
            }
        });
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('sidebarOverlay');
            const isOpen = sidebar.classList.contains('translate-x-0');
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
    </script>
</body></html>
"""
