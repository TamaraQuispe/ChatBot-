"""Admin dashboard template."""
HTML_ADMIN = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Admin Dashboard</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;400;500;600;700;900&amp;family=Courier+Prime&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-fixed": "#dce3ea",
                    "on-surface-variant": "#5b403e",
                    "secondary-container": "#dce3e9",
                    "surface": "#f8f9fa",
                    "on-tertiary-container": "#c5ccd3",
                    "on-secondary": "#ffffff",
                    "secondary": "#585f64",
                    "tertiary": "#384045",
                    "surface-tint": "#bc1127",
                    "surface-dim": "#d9dadb",
                    "on-primary-fixed": "#410006",
                    "on-tertiary-fixed-variant": "#40484d",
                    "on-primary": "#ffffff",
                    "secondary-fixed": "#dce3e9",
                    "on-error-container": "#93000a",
                    "inverse-on-surface": "#f0f1f2",
                    "background": "#f8f9fa",
                    "on-tertiary-fixed": "#151d21",
                    "surface-bright": "#f8f9fa",
                    "outline": "#906f6d",
                    "inverse-primary": "#ffb3af",
                    "on-error": "#ffffff",
                    "error": "#ba1a1a",
                    "primary-container": "#b00020",
                    "error-container": "#ffdad6",
                    "on-secondary-fixed-variant": "#41484c",
                    "surface-container-highest": "#e1e3e4",
                    "surface-container-lowest": "#ffffff",
                    "on-background": "#191c1d",
                    "primary": "#840015",
                    "on-primary-container": "#ffbbb8",
                    "on-surface": "#191c1d",
                    "outline-variant": "#e4bdbb",
                    "tertiary-container": "#4f575d",
                    "primary-fixed": "#ffdad8",
                    "on-secondary-fixed": "#161d21",
                    "surface-container-high": "#e7e8e9",
                    "surface-container": "#edeeef",
                    "inverse-surface": "#2e3132",
                    "on-primary-fixed-variant": "#930019",
                    "surface-container-low": "#f3f4f5",
                    "primary-fixed-dim": "#ffb3af",
                    "secondary-fixed-dim": "#c0c7cd",
                    "surface-variant": "#e1e3e4",
                    "on-secondary-container": "#5e656a",
                    "on-tertiary": "#ffffff",
                    "tertiary-fixed-dim": "#c0c7ce"
            },
            "borderRadius": {
                    "DEFAULT": "0.25rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "spacing": {
                    "stack-sm": "8px",
                    "gutter": "24px",
                    "stack-md": "16px",
                    "container-padding": "32px",
                    "section-gap": "80px",
                    "stack-lg": "24px"
            },
            "fontFamily": {
                    "headline-lg": ["Libre Franklin"],
                    "body-md": ["Libre Franklin"],
                    "label-md": ["Libre Franklin"],
                    "headline-md": ["Libre Franklin"],
                    "body-lg": ["Libre Franklin"],
                    "mono-sm": ["Courier Prime"],
                    "display-lg": ["Libre Franklin"],
                    "title-lg": ["Libre Franklin"]
            },
            "fontSize": {
                    "headline-lg": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.03em", "fontWeight": "600"}],
                    "body-md": ["14px", {"lineHeight": "1.6", "letterSpacing": "0em", "fontWeight": "400"}],
                    "label-md": ["12px", {"lineHeight": "1", "letterSpacing": "0.02em", "fontWeight": "500"}],
                    "headline-md": ["24px", {"lineHeight": "1.3", "letterSpacing": "-0.02em", "fontWeight": "600"}],
                    "body-lg": ["16px", {"lineHeight": "1.6", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                    "mono-sm": ["13px", {"lineHeight": "1.5", "letterSpacing": "0em", "fontWeight": "400"}],
                    "display-lg": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.04em", "fontWeight": "700"}],
                    "title-lg": ["18px", {"lineHeight": "1.5", "letterSpacing": "-0.01em", "fontWeight": "600"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            background-color: #f8f9fa;
            color: #191c1d;
            font-family: 'Libre Franklin', sans-serif;
            -webkit-font-smoothing: antialiased;
        }
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            display: inline-block;
            vertical-align: middle;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(8px);
            border: 1px solid #e6e8eb;
            border-radius: 16px;
            box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.05);
        }
        .sidebar-active {
            color: #840015;
            font-weight: 700;
            border-right: 4px solid #840015;
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e4;
            border-radius: 10px;
        }
        .sparkline {
            stroke: #b00020;
            stroke-width: 2;
            fill: transparent;
        }
    </style>
</head>
<body class="flex min-h-screen">
<!-- Mobile Overlay -->
<div id="sidebarOverlay" class="fixed inset-0 bg-black/40 z-30 hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar()"></div>
<!-- SideNavBar -->
<aside id="sidebar" class="h-screen w-64 fixed left-0 top-0 flex flex-col border-r border-surface-container-highest bg-white z-50 transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out">
<div class="flex flex-col h-full py-8">
<div class="px-8 mb-10">
<h1 class="font-headline-md text-headline-md font-bold text-primary">UTP Admin</h1>
<p class="text-label-md text-secondary uppercase tracking-widest mt-1">SaaS Elite Edition</p>
</div>
<nav class="flex-1 px-4 space-y-2">
<a class="flex items-center px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low transition-colors duration-200" href="/admin">
<span class="material-symbols-outlined mr-3">dashboard</span>
<span class="font-body-md text-body-md">Inicio</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/salones">
<span class="material-symbols-outlined mr-3">meeting_room</span>
<span class="font-body-md text-body-md">Salones</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/software">
<span class="material-symbols-outlined mr-3">computer</span>
<span class="font-body-md text-body-md">Software y Equipos</span>
</a>

<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined mr-3">person</span>
<span class="font-body-md text-body-md">Docentes</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined mr-3">event_seat</span>
<span class="font-body-md text-body-md">Reservas</span>
</a>

<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/roles">
<span class="material-symbols-outlined mr-3">admin_panel_settings</span>
<span class="font-body-md text-body-md">Roles</span>
</a>
</nav>
<div class="px-4 pt-10 border-t border-surface-container-highest space-y-2">
<a class="w-full flex items-center px-4 py-3 rounded-xl text-error hover:bg-error-container/10 transition-colors" href="/logout">
<span class="material-symbols-outlined mr-3">logout</span>
<span class="font-body-md text-body-md">Cerrar Sesion</span>
</a>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] min-h-screen pb-20">
$HEADER
<!-- Page Canvas -->
<div class="mt-24 px-container-padding">
<!-- Hero Header Section -->
<section class="mb-stack-lg">
<nav class="flex items-center space-x-2 text-label-md text-secondary mb-2">
<span>UTP Academic</span>
<span class="material-symbols-outlined text-[14px]">chevron_right</span>
<span class="text-on-surface">Panel de Control</span>
</nav>
<div class="flex justify-between items-end">
<div>
<h2 class="font-headline-lg text-headline-lg text-on-surface">Panel de Control</h2>
<p class="text-body-lg text-secondary mt-1">Supervision en tiempo real de recursos academicos y operativos.</p>
</div>
</div>
</section>
<!-- KPI Row -->
<section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-gutter mb-section-gap">
<div class="glass-card p-6 border-l-4 border-l-primary">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-primary p-2 bg-primary-fixed rounded-lg">domain</span>
<span class="bg-green-100 text-green-700 px-2 py-1 rounded text-label-md font-bold">+12%</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Salones Activos</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">142</h3>
<svg class="w-20 h-10 sparkline" viewbox="0 0 100 40">
<path d="M0 35 Q 25 10, 50 25 T 100 5" fill="none"></path>
</svg>
</div>
</div>
<div class="glass-card p-6">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-tertiary p-2 bg-surface-container-high rounded-lg">group</span>
<span class="bg-green-100 text-green-700 px-2 py-1 rounded text-label-md font-bold">98%</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Cantidad de Docentes</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">84</h3>
<svg class="w-20 h-10 sparkline" viewbox="0 0 100 40">
<path d="M0 30 Q 20 20, 40 30 T 60 10 T 100 15" fill="none"></path>
</svg>
</div>
</div>
<div class="glass-card p-6">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-amber-600 p-2 bg-amber-50 rounded-lg">event_busy</span>
<span class="bg-amber-100 text-amber-700 px-2 py-1 rounded text-label-md font-bold">24 Pend.</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Reservas Hoy</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">312</h3>
<svg class="w-20 h-10 sparkline" style="stroke: #f59e0b;" viewbox="0 0 100 40">
<path d="M0 10 Q 30 40, 60 20 T 100 30" fill="none"></path>
</svg>
</div>
</div>
</section>
<!-- Activity & Operations -->
<section class="grid grid-cols-12 gap-gutter">
<div class="col-span-12 lg:col-span-8 glass-card overflow-hidden">
<div class="p-8 border-b border-surface-container-highest flex justify-between items-center">
<h3 class="font-title-lg text-title-lg text-on-surface">Gestion de Salones</h3>
<div class="flex space-x-2">
<span class="px-3 py-1 bg-surface-container text-secondary text-label-md rounded-full">Total: 48</span>
</div>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead class="bg-surface font-label-md text-label-md text-on-surface-variant uppercase tracking-wider">
<tr>
<th class="px-8 py-4">Salon</th>
<th class="px-8 py-4">Pabellon</th>
<th class="px-8 py-4">Estado</th>
<th class="px-8 py-4">Capacidad</th>
<th class="px-8 py-4 text-right">Acciones</th>
</tr>
</thead>
<tbody class="font-body-md text-body-md divide-y divide-surface-container-highest">
<tr class="hover:bg-surface-container-low transition-colors">
<td class="px-8 py-4 font-bold">LAB-302</td>
<td class="px-8 py-4">Pabellon A</td>
<td class="px-8 py-4">
<span class="flex items-center text-primary font-semibold">
<span class="w-1.5 h-1.5 rounded-full bg-primary mr-2"></span> Ocupado
                                        </span>
</td>
<td class="px-8 py-4">40 / 40</td>
<td class="px-8 py-4 text-right">
<button class="text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined">more_vert</span></button>
</td>
</tr>
<tr class="hover:bg-surface-container-low transition-colors">
<td class="px-8 py-4 font-bold">AUL-105</td>
<td class="px-8 py-4">Pabellon C</td>
<td class="px-8 py-4">
<span class="flex items-center text-green-600 font-semibold">
<span class="w-1.5 h-1.5 rounded-full bg-green-500 mr-2"></span> Libre
                                        </span>
</td>
<td class="px-8 py-4">0 / 60</td>
<td class="px-8 py-4 text-right">
<button class="text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined">more_vert</span></button>
</td>
</tr>
<tr class="hover:bg-surface-container-low transition-colors">
<td class="px-8 py-4 font-bold">SIM-01</td>
<td class="px-8 py-4">Centro Simulacion</td>
<td class="px-8 py-4">
<span class="flex items-center text-amber-600 font-semibold">
<span class="w-1.5 h-1.5 rounded-full bg-amber-500 mr-2"></span> Limpieza
                                        </span>
</td>
<td class="px-8 py-4">--</td>
<td class="px-8 py-4 text-right">
<button class="text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined">more_vert</span></button>
</td>
</tr>
<tr class="hover:bg-surface-container-low transition-colors">
<td class="px-8 py-4 font-bold">LAB-505</td>
<td class="px-8 py-4">Pabellon B</td>
<td class="px-8 py-4">
<span class="flex items-center text-primary font-semibold">
<span class="w-1.5 h-1.5 rounded-full bg-primary mr-2"></span> Ocupado
                                        </span>
</td>
<td class="px-8 py-4">25 / 30</td>
<td class="px-8 py-4 text-right">
<button class="text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined">more_vert</span></button>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</section>
</div>
<footer class="w-full py-stack-lg mt-section-gap border-t border-surface-container-highest bg-surface">
<div class="max-w-7xl mx-auto flex justify-between items-center px-container-padding">
<p class="font-body-md text-body-md text-secondary opacity-80 hover:opacity-100 transition-opacity">© 2024 UTP Academic Management. SaaS Elite Tier.</p>
<div class="flex space-x-6">
<a class="font-label-md text-label-md font-medium text-secondary hover:text-primary transition-colors" href="#">Privacidad</a>
<a class="font-label-md text-label-md font-medium text-secondary hover:text-primary transition-colors" href="#">Soporte</a>
<a class="font-label-md text-label-md font-medium text-secondary hover:text-primary transition-colors" href="#">API Docs</a>
</div>
</div>
</footer>
</main>
<script>
        document.querySelectorAll('.glass-card').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.transform = 'translateY(-2px)';
                card.style.transition = 'transform 0.2s ease-out';
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'translateY(0px)';
            });
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
