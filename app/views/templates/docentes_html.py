HTML_DOCENTES = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Directivo de Docentes</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100;300;400;500;600;700;800;900&amp;family=Courier+Prime&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
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
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb { background: #e1e3e4; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: #585f64; }
    </style>
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
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/software">
<span class="material-symbols-outlined">computer</span>
<span class="font-medium">Software y Equipos</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/horarios">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-medium">Horarios</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/docentes">
<span class="material-symbols-outlined">person</span>
<span class="font-bold">Docentes</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined">event_seat</span>
<span class="font-medium">Reservas</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reportes">
<span class="material-symbols-outlined">assessment</span>
<span class="font-medium">Reportes</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/roles">
<span class="material-symbols-outlined">admin_panel_settings</span>
<span class="font-medium">Roles y Permisos</span>
</a>
</nav>
<div class="pt-6 border-t border-surface-container-highest space-y-2">
<button class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined">account_circle</span>
<span class="font-medium text-body-md">Perfil</span>
</button>
<a class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-error hover:bg-error-container/10 transition-colors" href="/logout">
<span class="material-symbols-outlined">logout</span>
<span class="font-medium text-body-md">Cerrar Sesion</span>
</a>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] min-h-screen pb-20">
<!-- Top Navigation Bar -->
<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-50 glass-panel h-16 px-container-padding flex justify-between items-center border-b border-surface-container-highest">
<div class="flex items-center gap-4 md:gap-8">
<button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<span class="font-title-lg text-title-lg font-black tracking-tight text-on-surface">UTP Academic</span>
<div class="hidden md:flex gap-6 text-label-md font-label-md">
<a class="text-on-surface-variant hover:text-on-surface" href="#">Hoy</a>
<a class="text-on-surface-variant hover:text-on-surface" href="#">Calendario</a>
<a class="text-on-surface-variant hover:text-on-surface" href="#">Directorio</a>
</div>
</div>
<div class="flex items-center gap-4">
<div class="relative group">
<span class="absolute inset-y-0 left-3 flex items-center text-secondary">
<span class="material-symbols-outlined text-[20px]">search</span>
</span>
<input class="pl-10 pr-4 py-1.5 bg-surface-container-low border-none rounded-full text-body-md focus:ring-1 focus:ring-primary w-64 transition-all" placeholder="Buscar docente, curso o ID..." type="text"/>
</div>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">notifications</button>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">apps</button>
<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">A</div>
</div>
</header>
<div class="mt-16 px-container-padding pt-10">
<!-- Page Header -->
<section class="flex justify-between items-end mb-12">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Directorio de Docentes</h1>
<p class="text-secondary mt-1">Gestion integral de la plana docente y asignaciones academicas.</p>
</div>
<div class="flex gap-3">
<button class="px-5 py-2.5 rounded-xl border border-surface-container-highest bg-white text-on-surface font-medium hover:bg-surface-container-low transition-all flex items-center gap-2">
<span class="material-symbols-outlined text-[18px]">ios_share</span>
                        Exportar
                    </button>
<button class="px-5 py-2.5 rounded-xl bg-primary text-white font-bold hover:opacity-90 transition-all flex items-center gap-2 shadow-lg shadow-primary/20">
<span class="material-symbols-outlined text-[18px]">person_add</span>
                        Nuevo Docente
                    </button>
</div>
</section>
<!-- KPI Cards -->
<section class="grid grid-cols-1 md:grid-cols-3 gap-gutter mb-section-gap">
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg">
<span class="material-symbols-outlined text-primary">groups</span>
</div>
<div class="text-right">
<span class="text-[11px] font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-full flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">trending_up</span> +12%
</span>
</div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Total Docentes</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">$TOTAL_DOCENTES</span>
</div>
<div class="mt-4 h-1 w-full bg-surface-container rounded-full overflow-hidden">
<div class="h-full bg-primary w-3/4"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg">
<span class="material-symbols-outlined text-primary">event_available</span>
</div>
<div class="text-right">
<div class="flex items-center gap-1">
<div class="w-2 h-2 rounded-full bg-emerald-500"></div>
<span class="text-[11px] font-bold text-secondary bg-surface-container-low px-2 py-0.5 rounded-full">Online</span>
</div>
</div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Activos Hoy</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">412</span>
</div>
<div class="flex gap-1 mt-4">
<div class="w-2 h-2 rounded-full bg-primary/20"></div>
<div class="w-2 h-2 rounded-full bg-primary/40"></div>
<div class="w-2 h-2 rounded-full bg-primary/60"></div>
<div class="w-2 h-2 rounded-full bg-primary/80"></div>
<div class="w-2 h-2 rounded-full bg-primary"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm hover:shadow-md transition-all">
<div class="flex justify-between items-start mb-4">
<div class="p-2 bg-surface-container-low rounded-lg">
<span class="material-symbols-outlined text-error">pending_actions</span>
</div>
<div class="text-right">
<span class="text-[11px] font-bold text-error bg-error-container/20 px-2 py-0.5 rounded-full flex items-center gap-1">
<span class="material-symbols-outlined text-[14px]">priority_high</span> Urgente
</span>
</div>
</div>
<h3 class="text-secondary text-label-md uppercase tracking-wider mb-1">Solicitudes Pendientes</h3>
<div class="flex items-end justify-between">
<span class="text-headline-md font-bold">24</span>
</div>
<p class="text-label-md text-secondary mt-4 font-mono-sm">Queue ID: UTP-ADM-24-X</p>
</div>
</section>
<!-- Main Filter Bar -->
<section class="mb-12">
<div class="glass-panel p-4 rounded-2xl shadow-sm flex flex-col md:flex-row items-center gap-4">
<div class="flex-1 w-full relative">
<span class="absolute inset-y-0 left-4 flex items-center text-secondary">
<span class="material-symbols-outlined">filter_alt</span>
</span>
<input class="w-full pl-12 pr-4 py-2.5 bg-surface-container-low border border-surface-container-highest rounded-xl focus:ring-1 focus:ring-primary focus:border-primary transition-all" placeholder="Filtrar por departamento, grado academico o curso..." type="text"/>
</div>
<select class="bg-white border border-surface-container-highest rounded-xl px-4 py-2.5 text-body-md focus:ring-1 focus:ring-primary min-w-[200px]">
<option>Todos los Departamentos</option>
<option>Ingenieria de Sistemas</option>
<option>Arquitectura</option>
<option>Derecho</option>
<option>Medicina</option>
</select>
<button class="p-2.5 bg-white border border-surface-container-highest rounded-xl hover:bg-surface transition-colors">
<span class="material-symbols-outlined text-secondary">grid_view</span>
</button>
<button class="p-2.5 bg-white border border-surface-container-highest rounded-xl hover:bg-surface transition-colors">
<span class="material-symbols-outlined text-primary">view_list</span>
</button>
</div>
</section>
<!-- Faculty Table -->
<section class="glass-panel rounded-2xl shadow-sm overflow-hidden mb-section-gap">
<div class="overflow-x-auto">
<table class="w-full text-left border-collapse">
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
<!-- Pagination -->
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
</section>
</div>
<!-- Footer -->
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
            row.addEventListener('mousedown', function() {
                this.classList.add('opacity-90');
                this.classList.add('transition-opacity');
            });
            row.addEventListener('mouseup', function() {
                this.classList.remove('opacity-90');
            });
        });
        const searchInput = document.querySelector('input[type="text"]');
        if (searchInput) {
            searchInput.addEventListener('focus', function() {
                this.parentElement.classList.add('scale-[1.02]');
                this.parentElement.classList.add('transition-transform');
            });
            searchInput.addEventListener('blur', function() {
                this.parentElement.classList.remove('scale-[1.02]');
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
