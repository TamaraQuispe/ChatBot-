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
<input class="w-full pl-12 pr-4 py-3 bg-surface-container-low border border-surface-container-highest rounded-xl focus:ring-1 focus:ring-primary focus:border-primary transition-all" placeholder="Buscar por activo, categoria, software o licencia..." type="text"/>
</div>
<div class="flex items-center gap-3 w-full md:w-auto">
<select class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option>Categoria: Todas</option>
<option>Hardware</option>
<option>Software</option>
<option>Licencia</option>
<option>Equipo</option>
</select>
<select class="bg-white border border-surface-container-highest rounded-xl px-4 py-3 text-body-md focus:ring-1 focus:ring-primary w-full sm:min-w-[140px]">
<option>Estado: Todos</option>
<option>Activo</option>
<option>Inactivo</option>
<option>Mantenimiento</option>
<option>Vencido</option>
</select>
<button class="p-3 bg-surface-container-low hover:bg-surface-container-highest rounded-xl transition-colors">
<span class="material-symbols-outlined">tune</span>
</button>
</div>
</div>
</section>
<!-- Premium Data Table -->
<section class="glass-panel rounded-2xl shadow-sm overflow-x-auto overflow-y-hidden mb-section-gap">
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low/50">
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Activo / ID</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Categoria</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Estado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Software / Licencia</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest">Ultimo Mantenimiento</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase tracking-wider border-b border-surface-container-highest text-right">Uso Historico</th>
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
        const searchInput = document.querySelector('input[type="text"]');
        if (searchInput) {
            searchInput.addEventListener('focus', () => {
                searchInput.parentElement.classList.add('ring-1', 'ring-primary');
            });
            searchInput.addEventListener('blur', () => {
                searchInput.parentElement.classList.remove('ring-1', 'ring-primary');
            });
        }
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
