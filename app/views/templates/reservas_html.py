HTML_RESERVAS = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Gestion de Reservas</title>
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
        .status-dot { width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 6px; }
        .timeline-line::before {
            content: '';
            position: absolute;
            left: 20px;
            top: 0;
            bottom: 0;
            width: 2px;
            background: #e1e3e4;
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
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined">person</span>
<span class="font-medium">Docentes</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/reservas">
<span class="material-symbols-outlined">event_seat</span>
<span class="font-bold">Reservas</span>
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
$HEADER
<div class="mt-16 px-container-padding pt-10">
<!-- Header Section -->
<section class="mb-10 flex justify-between items-end">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Gestion de Reservas</h1>
<div class="flex items-center gap-4 mt-1">
<div class="flex items-center text-label-md text-secondary">
<span class="status-dot bg-emerald-500"></span>
                        Sistema Operativo
                    </div>
<span class="text-surface-container-highest">|</span>
<span class="text-body-md text-secondary">24 Solicitudes pendientes de revision</span>
</div>
</div>
<div class="flex gap-3">
<button class="flex items-center gap-2 border border-surface-container-highest bg-white px-4 py-2 rounded-lg font-label-md text-label-md text-on-surface hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-sm">filter_list</span> Filtrar
                </button>
<button class="flex items-center gap-2 border border-surface-container-highest bg-white px-4 py-2 rounded-lg font-label-md text-label-md text-on-surface hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-sm">download</span> Descargar Reporte
                </button>
</div>
</section>
<!-- Bento Layout -->
<div class="grid grid-cols-12 gap-gutter">
<!-- Main Reservations List -->
<div class="col-span-12 lg:col-span-8 space-y-stack-lg">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-center mb-6">
<h3 class="font-title-lg text-title-lg">Solicitudes Recientes</h3>
<div class="flex bg-surface-container-low p-1 rounded-lg">
<button class="px-4 py-1 text-label-md bg-white shadow-sm rounded-md font-semibold">Pendientes</button>
<button class="px-4 py-1 text-label-md text-secondary hover:text-on-surface">Historial</button>
</div>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b border-surface-container-highest text-label-md text-secondary uppercase tracking-wider">
<th class="pb-4 font-medium">Solicitante</th>
<th class="pb-4 font-medium">Espacio / Aula</th>
<th class="pb-4 font-medium">Fecha y Hora</th>
<th class="pb-4 font-medium">Estado</th>
<th class="pb-4 font-medium text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_RESERVAS
</tbody>
</table>
</div>
</div>
<!-- Usage Analytics -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-gutter">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start mb-2">
<span class="text-label-md text-secondary font-medium">Tasa de Ocupacion</span>
<span class="text-emerald-600 font-bold text-xs">+12.5%</span>
</div>
<div class="text-headline-md font-headline-md">78.4%</div>
<div class="h-8 mt-4 flex items-end gap-1">
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-1/2"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-3/4"></div>
<div class="flex-1 bg-primary rounded-t-sm h-full"></div>
<div class="flex-1 bg-primary rounded-t-sm h-2/3"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-4/5"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-1/2"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start mb-2">
<span class="text-label-md text-secondary font-medium">Promedio Respuesta</span>
<span class="text-amber-500 font-bold text-xs">-2m</span>
</div>
<div class="text-headline-md font-headline-md">14.2 min</div>
<div class="h-8 mt-4 flex items-center justify-center">
<div class="w-full h-1 bg-surface-container-highest rounded-full relative overflow-hidden">
<div class="absolute left-0 top-0 h-full w-[65%] bg-primary"></div>
</div>
</div>
</div>
</div>
</div>
<!-- Timeline -->
<div class="col-span-12 lg:col-span-4 space-y-stack-lg">
<div class="glass-panel p-6 rounded-2xl shadow-sm h-full">
<div class="flex justify-between items-center mb-8">
<h3 class="font-title-lg text-title-lg">Timeline Proximo</h3>
<button class="material-symbols-outlined text-secondary hover:text-on-surface">more_vert</button>
</div>
<div class="relative timeline-line space-y-8 pl-10">
<div class="relative">
<div class="absolute -left-10 top-0 w-6 h-6 rounded-full bg-white border-4 border-primary z-10"></div>
<div class="flex flex-col">
<span class="text-label-md font-bold text-primary mb-1">HOY - 14:00</span>
<h4 class="font-body-md text-body-md font-semibold">Consejo Universitario</h4>
<p class="text-label-md text-secondary">Sala de Juntas B</p>
<div class="mt-2 flex -space-x-2">
<div class="w-6 h-6 rounded-full border-2 border-white bg-surface-container-highest"></div>
<div class="w-6 h-6 rounded-full border-2 border-white bg-surface-container-high"></div>
<div class="w-6 h-6 rounded-full border-2 border-white bg-surface-container"></div>
<div class="w-6 h-6 rounded-full border-2 border-white bg-surface-container-highest flex items-center justify-center text-[8px] font-bold">+8</div>
</div>
</div>
</div>
<div class="relative">
<div class="absolute -left-10 top-0 w-6 h-6 rounded-full bg-white border-4 border-surface-container-highest z-10"></div>
<div class="flex flex-col">
<span class="text-label-md font-bold text-secondary mb-1">HOY - 16:30</span>
<h4 class="font-body-md text-body-md font-semibold">Taller de Innovacion</h4>
<p class="text-label-md text-secondary">Laboratorio 102</p>
</div>
</div>
<div class="relative">
<div class="absolute -left-10 top-0 w-6 h-6 rounded-full bg-white border-4 border-surface-container-highest z-10"></div>
<div class="flex flex-col">
<span class="text-label-md font-bold text-secondary mb-1">MANANA - 08:00</span>
<h4 class="font-body-md text-body-md font-semibold">Examen Parcial de Fisica</h4>
<p class="text-label-md text-secondary">Auditorio Sur</p>
<div class="mt-3 p-3 bg-surface-container-low rounded-lg border border-surface-container-highest">
<div class="flex items-center gap-2 text-label-md text-primary font-bold">
<span class="material-symbols-outlined text-sm">warning</span>
                                        Requiere Proyector 4K
                                    </div>
</div>
</div>
</div>
<div class="relative">
<div class="absolute -left-10 top-0 w-6 h-6 rounded-full bg-white border-4 border-surface-container-highest z-10"></div>
<div class="flex flex-col">
<span class="text-label-md font-bold text-secondary mb-1">MANANA - 11:30</span>
<h4 class="font-body-md text-body-md font-semibold">Entrevista Docente</h4>
<p class="text-label-md text-secondary">Oficina Administrativa 3</p>
</div>
</div>
</div>
<button class="w-full mt-10 py-3 border border-dashed border-surface-container-highest rounded-xl text-label-md text-secondary hover:border-primary hover:text-primary transition-all">
                        Ver calendario completo
                    </button>
</div>
</div>
</div>
<!-- System Alerts -->
<section class="mt-gutter grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-gutter mb-section-gap">
<div class="glass-panel p-5 rounded-2xl shadow-sm flex items-center gap-4">
<div class="w-12 h-12 rounded-xl bg-primary-fixed flex items-center justify-center text-primary">
<span class="material-symbols-outlined">event_busy</span>
</div>
<div>
<div class="text-label-md text-secondary">Conflictos detectados</div>
<div class="font-title-lg text-title-lg">03 Salas</div>
</div>
</div>
<div class="glass-panel p-5 rounded-2xl shadow-sm flex items-center gap-4">
<div class="w-12 h-12 rounded-xl bg-secondary-fixed flex items-center justify-center text-on-secondary-fixed-variant">
<span class="material-symbols-outlined">cleaning_services</span>
</div>
<div>
<div class="text-label-md text-secondary">Tareas de Mantenimiento</div>
<div class="font-title-lg text-title-lg">12 Pendientes</div>
</div>
</div>
<div class="glass-panel p-5 rounded-2xl shadow-sm flex items-center gap-4">
<div class="w-12 h-12 rounded-xl bg-tertiary-fixed flex items-center justify-center text-tertiary">
<span class="material-symbols-outlined">energy_savings_leaf</span>
</div>
<div>
<div class="text-label-md text-secondary">Ahorro Energetico (Aulas)</div>
<div class="font-title-lg text-title-lg">Optimizado</div>
</div>
</div>
</section>
</div>
<!-- Footer -->
<footer class="w-full py-stack-lg border-t border-surface-container-highest bg-surface">
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
                row.style.transform = 'scale(1.002)';
            });
            row.addEventListener('mouseleave', () => {
                row.style.transform = 'scale(1)';
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
