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
<body class="flex">
<!-- SideNavBar -->
<aside class="h-screen w-64 fixed left-0 top-0 flex flex-col border-r border-surface-container-highest bg-white z-50">
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
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/horarios">
<span class="material-symbols-outlined mr-3">calendar_today</span>
<span class="font-body-md text-body-md">Horarios</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined mr-3">person</span>
<span class="font-body-md text-body-md">Docentes</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined mr-3">event_seat</span>
<span class="font-body-md text-body-md">Reservas</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reportes">
<span class="material-symbols-outlined mr-3">assessment</span>
<span class="font-body-md text-body-md">Reportes</span>
</a>
<a class="flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/roles">
<span class="material-symbols-outlined mr-3">admin_panel_settings</span>
<span class="font-body-md text-body-md">Roles y Permisos</span>
</a>
</nav>
<div class="px-4 pt-10 border-t border-surface-container-highest space-y-2">
<button class="w-full flex items-center px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined mr-3">account_circle</span>
<span class="font-body-md text-body-md">Perfil</span>
</button>
<a class="w-full flex items-center px-4 py-3 rounded-xl text-error hover:bg-error-container/10 transition-colors" href="/logout">
<span class="material-symbols-outlined mr-3">logout</span>
<span class="font-body-md text-body-md">Cerrar Sesion</span>
</a>
</div>
</div>
</aside>
<!-- Main Content Area -->
<main class="ml-64 w-[calc(100%-16rem)] min-h-screen pb-20">
<!-- TopNavBar -->
<header class="fixed top-0 right-0 w-[calc(100%-16rem)] z-40 bg-white/70 backdrop-blur-md border-b border-surface-container-highest">
<div class="flex justify-between items-center h-16 px-container-padding">
<div class="flex items-center space-x-8">
<div class="relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary">search</span>
<input class="pl-10 pr-4 py-2 bg-surface border-none rounded-full text-label-md w-64 focus:ring-1 focus:ring-primary" placeholder="Buscador global..." type="text"/>
</div>
<nav class="hidden md:flex space-x-6">
<a class="text-primary font-semibold border-b-2 border-primary pb-1 font-label-md text-label-md" href="#">Hoy</a>
<a class="text-on-surface-variant hover:text-on-surface font-label-md text-label-md transition-all" href="#">Calendario</a>
<a class="text-on-surface-variant hover:text-on-surface font-label-md text-label-md transition-all" href="#">Directorio</a>
</nav>
</div>
<div class="flex items-center space-x-6">
<button class="p-2 text-secondary hover:text-primary transition-transform active:scale-95">
<span class="material-symbols-outlined">notifications</span>
</button>
<button class="p-2 text-secondary hover:text-primary transition-transform active:scale-95">
<span class="material-symbols-outlined">apps</span>
</button>
<button class="bg-primary text-on-primary px-5 py-2 rounded-lg font-label-md text-label-md font-bold transition-all hover:opacity-90 active:scale-95">
                        Nueva Reserva
                    </button>
<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">A</div>
</div>
</div>
</header>
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
<div class="flex space-x-3">
<button class="flex items-center px-4 py-2 glass-card font-label-md text-label-md hover:bg-surface transition-colors">
<span class="material-symbols-outlined mr-2">filter_list</span> Filtrar Vista
                        </button>
<button class="flex items-center px-4 py-2 bg-white border border-outline-variant rounded-lg font-label-md text-label-md hover:bg-surface transition-colors">
<span class="material-symbols-outlined mr-2">download</span> Descargar Reporte
                        </button>
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
<p class="text-label-md text-secondary uppercase font-medium">Docentes en Linea</p>
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
<div class="glass-card p-6">
<div class="flex justify-between items-start mb-4">
<span class="material-symbols-outlined text-error p-2 bg-error-container rounded-lg">warning</span>
<span class="bg-red-100 text-red-700 px-2 py-1 rounded text-label-md font-bold">Critico</span>
</div>
<p class="text-label-md text-secondary uppercase font-medium">Incidencias</p>
<div class="flex items-end justify-between">
<h3 class="text-display-lg font-display-lg leading-none mt-2">03</h3>
<svg class="w-20 h-10 sparkline" style="stroke: #ba1a1a;" viewbox="0 0 100 40">
<path d="M0 35 L 20 25 L 40 35 L 60 5 L 80 15 L 100 0" fill="none"></path>
</svg>
</div>
</div>
</section>
<!-- Data Visualization Section -->
<section class="grid grid-cols-12 gap-gutter mb-section-gap">
<div class="col-span-12 lg:col-span-8 glass-card p-8">
<div class="flex justify-between items-center mb-8">
<div>
<h3 class="font-title-lg text-title-lg text-on-surface">Ocupacion de Laboratorios</h3>
<p class="text-body-md text-secondary">Comparativa de uso semanal vs proyectado.</p>
</div>
<div class="flex bg-surface-container-low p-1 rounded-lg">
<button class="px-3 py-1 bg-white rounded-md text-label-md shadow-sm font-bold">Semana</button>
<button class="px-3 py-1 text-label-md text-secondary">Mes</button>
</div>
</div>
<div class="relative h-64 w-full bg-surface-container-lowest rounded-xl flex items-end p-4">
<div class="absolute inset-0 flex items-center justify-center opacity-10">
<span class="material-symbols-outlined scale-[5]">stacked_line_chart</span>
</div>
<div class="flex-1 flex items-end justify-around h-full space-x-4">
<div class="w-12 bg-primary/10 hover:bg-primary/20 transition-all rounded-t-lg h-[40%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">40%</div>
</div>
<div class="w-12 bg-primary/20 hover:bg-primary/30 transition-all rounded-t-lg h-[65%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">65%</div>
</div>
<div class="w-12 bg-primary rounded-t-lg h-[92%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">92%</div>
</div>
<div class="w-12 bg-primary/40 hover:bg-primary/50 transition-all rounded-t-lg h-[50%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">50%</div>
</div>
<div class="w-12 bg-primary/30 hover:bg-primary/40 transition-all rounded-t-lg h-[75%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">75%</div>
</div>
<div class="w-12 bg-primary/15 hover:bg-primary/25 transition-all rounded-t-lg h-[35%] relative group">
<div class="absolute -top-10 left-1/2 -translate-x-1/2 bg-inverse-surface text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity">35%</div>
</div>
</div>
</div>
</div>
<div class="col-span-12 lg:col-span-4 glass-card p-8">
<h3 class="font-title-lg text-title-lg text-on-surface mb-6">Estado del Sistema</h3>
<div class="grid grid-cols-2 gap-4">
<div class="bg-surface-container-low p-4 rounded-xl border border-outline-variant">
<div class="flex items-center space-x-2 mb-2">
<span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
<span class="text-label-md font-bold">API Central</span>
</div>
<p class="text-[10px] text-secondary font-mono-sm">99.9% Uptime</p>
</div>
<div class="bg-surface-container-low p-4 rounded-xl border border-outline-variant">
<div class="flex items-center space-x-2 mb-2">
<span class="w-2 h-2 rounded-full bg-green-500"></span>
<span class="text-label-md font-bold">Servidores</span>
</div>
<p class="text-[10px] text-secondary font-mono-sm">Lat: 12ms</p>
</div>
<div class="bg-surface-container-low p-4 rounded-xl border border-outline-variant">
<div class="flex items-center space-x-2 mb-2">
<span class="w-2 h-2 rounded-full bg-amber-500"></span>
<span class="text-label-md font-bold">Red</span>
</div>
<p class="text-[10px] text-secondary font-mono-sm">Trafico: 85%</p>
</div>
<div class="bg-surface-container-low p-4 rounded-xl border border-outline-variant">
<div class="flex items-center space-x-2 mb-2">
<span class="w-2 h-2 rounded-full bg-green-500"></span>
<span class="text-label-md font-bold">Base Datos</span>
</div>
<p class="text-[10px] text-secondary font-mono-sm">Sincronizada</p>
</div>
</div>
<div class="mt-8 p-4 bg-primary-fixed text-on-primary-fixed-variant rounded-xl flex items-center">
<span class="material-symbols-outlined mr-3">info</span>
<p class="text-label-md leading-snug">Proximo mantenimiento programado: 24/05/2025 - 02:00 AM</p>
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
<div class="col-span-12 lg:col-span-4 space-y-gutter">
<div class="glass-card p-8">
<h3 class="font-title-lg text-title-lg text-on-surface mb-6">Actividad Reciente</h3>
<div class="space-y-6 relative before:absolute before:left-[11px] before:top-2 before:bottom-2 before:w-[2px] before:bg-surface-container-high">
<div class="relative pl-10">
<div class="absolute left-0 top-1.5 w-[24px] h-[24px] rounded-full bg-primary-fixed border-2 border-white flex items-center justify-center">
<span class="material-symbols-outlined text-[14px] text-primary">edit</span>
</div>
<p class="text-body-md font-bold">Cambio en Horario AUL-105</p>
<p class="text-label-md text-secondary">Hace 15 min • Admin Garcia</p>
</div>
<div class="relative pl-10">
<div class="absolute left-0 top-1.5 w-[24px] h-[24px] rounded-full bg-green-100 border-2 border-white flex items-center justify-center">
<span class="material-symbols-outlined text-[14px] text-green-700">check_circle</span>
</div>
<p class="text-body-md font-bold">Sistema Back-up Completado</p>
<p class="text-label-md text-secondary">Hace 2 horas • Automatico</p>
</div>
<div class="relative pl-10">
<div class="absolute left-0 top-1.5 w-[24px] h-[24px] rounded-full bg-error-container border-2 border-white flex items-center justify-center">
<span class="material-symbols-outlined text-[14px] text-error">warning</span>
</div>
<p class="text-body-md font-bold">Falla Aire Acond. LAB-302</p>
<p class="text-label-md text-secondary">Hace 3 horas • Reporte Docente</p>
</div>
</div>
<button class="w-full mt-8 py-2 text-label-md font-bold text-primary border border-primary/20 rounded-lg hover:bg-primary-fixed transition-colors">
                            Ver historial completo
                        </button>
</div>
<div class="glass-card p-6">
<h3 class="font-label-md text-label-md text-secondary uppercase font-bold mb-4">Accesos Rapidos</h3>
<div class="grid grid-cols-2 gap-3">
<button class="flex flex-col items-center justify-center p-4 bg-surface rounded-xl hover:bg-primary hover:text-white transition-all group">
<span class="material-symbols-outlined mb-2 group-hover:scale-110 transition-transform">add_task</span>
<span class="text-[11px] font-bold">Nueva Reserva</span>
</button>
<button class="flex flex-col items-center justify-center p-4 bg-surface rounded-xl hover:bg-primary hover:text-white transition-all group">
<span class="material-symbols-outlined mb-2 group-hover:scale-110 transition-transform">terminal</span>
<span class="text-[11px] font-bold">Gestion SW</span>
</button>
<button class="flex flex-col items-center justify-center p-4 bg-surface rounded-xl hover:bg-primary hover:text-white transition-all group">
<span class="material-symbols-outlined mb-2 group-hover:scale-110 transition-transform">description</span>
<span class="text-[11px] font-bold">Reportes PDF</span>
</button>
<button class="flex flex-col items-center justify-center p-4 bg-surface rounded-xl hover:bg-primary hover:text-white transition-all group">
<span class="material-symbols-outlined mb-2 group-hover:scale-110 transition-transform">broadcast_on_home</span>
<span class="text-[11px] font-bold">Aviso Global</span>
</button>
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
    </script>
</body></html>
"""
