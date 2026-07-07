HTML_REPORTES = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Reportes y Analitica</title>
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
        .sparkline-red { stroke: #B00020; stroke-width: 2; fill: none; }
        .sparkline-gray { stroke: #585f64; stroke-width: 2; fill: none; }
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
<!-- Side Navigation Shell -->
<aside class="h-screen w-64 fixed left-0 top-0 flex flex-col border-r border-surface-container-highest bg-white z-[60]">
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
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined">event_seat</span>
<span class="font-medium">Reservas</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/reportes">
<span class="material-symbols-outlined">assessment</span>
<span class="font-bold">Reportes</span>
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
<main class="ml-64 min-h-screen pb-20">
<!-- Top Navigation Bar -->
<header class="fixed top-0 right-0 w-[calc(100%-16rem)] z-50 glass-panel h-16 px-container-padding flex justify-between items-center border-b border-surface-container-highest">
<div class="flex items-center gap-8">
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
<input class="pl-10 pr-4 py-1.5 bg-surface-container-low border-none rounded-full text-body-md focus:ring-1 focus:ring-primary w-64 transition-all" placeholder="Buscar metricas..." type="text"/>
</div>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">notifications</button>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">apps</button>
<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">A</div>
</div>
</header>
<div class="mt-16 px-container-padding pt-10">
<!-- Dashboard Header -->
<section class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-stack-lg">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Panel de Analitica Avanzada</h1>
<p class="text-body-md text-secondary mt-1">Monitoreo en tiempo real del rendimiento institucional</p>
</div>
<div class="flex items-center gap-3">
<div class="flex items-center bg-white border border-surface-container-highest rounded-lg px-3 py-1.5 shadow-sm">
<span class="material-symbols-outlined text-[18px] text-secondary mr-2">calendar_today</span>
<select class="border-none bg-transparent font-label-md text-label-md focus:ring-0 p-0 pr-8">
<option>Ultimos 30 dias</option>
<option>Semestre Actual</option>
<option>Ano 2024</option>
<option>Personalizado</option>
</select>
</div>
<button class="bg-white border border-surface-container-highest text-on-surface font-label-md px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-surface-container-low transition-all shadow-sm">
<span class="material-symbols-outlined text-[18px]">picture_as_pdf</span>
                        PDF
                    </button>
<button class="bg-white border border-surface-container-highest text-on-surface font-label-md px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-surface-container-low transition-all shadow-sm">
<span class="material-symbols-outlined text-[18px]">table_chart</span>
                        XLSX
                    </button>
</div>
</section>
<!-- Top Summary Cards -->
<section class="grid grid-cols-1 md:grid-cols-4 gap-gutter mb-stack-lg">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Ocupacion Promedio</span>
<span class="flex items-center text-emerald-600 text-label-md font-bold">
<span class="material-symbols-outlined text-[14px]">trending_up</span> 12%
</span>
</div>
<div class="text-display-lg font-display-lg mt-2">84.2%</div>
<div class="mt-4 h-12 w-full flex items-end gap-1">
<div class="flex-1 bg-surface-container-highest h-4 rounded-t-sm"></div>
<div class="flex-1 bg-surface-container-highest h-6 rounded-t-sm"></div>
<div class="flex-1 bg-primary h-10 rounded-t-sm"></div>
<div class="flex-1 bg-surface-container-highest h-8 rounded-t-sm"></div>
<div class="flex-1 bg-primary h-12 rounded-t-sm"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Software Activo</span>
<span class="flex items-center text-on-surface-variant text-label-md">Estable</span>
</div>
<div class="text-display-lg font-display-lg mt-2">1,204</div>
<div class="mt-4 flex items-center gap-2">
<div class="flex -space-x-2">
<div class="w-6 h-6 rounded-full bg-blue-100 border-2 border-white"></div>
<div class="w-6 h-6 rounded-full bg-red-100 border-2 border-white"></div>
<div class="w-6 h-6 rounded-full bg-gray-100 border-2 border-white"></div>
</div>
<span class="text-label-md text-secondary">+12 herramientas</span>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Rendimiento Acad.</span>
<span class="flex items-center text-primary text-label-md font-bold">
<span class="material-symbols-outlined text-[14px]">trending_down</span> 2.4%
</span>
</div>
<div class="text-display-lg font-display-lg mt-2">4.12</div>
<div class="mt-4">
<div class="w-full bg-surface-container-highest h-1.5 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[82%]"></div>
</div>
<p class="text-[10px] mt-1 text-secondary">Promedio General Institucional</p>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl bg-inverse-surface border-none shadow-xl">
<div class="text-on-primary-fixed">
<span class="text-label-md opacity-70 uppercase tracking-wider">Estado del Sistema</span>
<div class="flex items-center gap-2 mt-2">
<div class="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-pulse"></div>
<span class="font-title-lg text-title-lg text-white">100% Operativo</span>
</div>
</div>
<button class="mt-6 w-full py-2 bg-white/10 hover:bg-white/20 text-white rounded-lg text-label-md transition-all border border-white/20">
                        Ver Logs Tecnicos
                    </button>
</div>
</section>
<!-- Charts Section -->
<section class="grid grid-cols-1 lg:grid-cols-3 gap-gutter mb-section-gap">
<div class="lg:col-span-2 glass-panel p-8 rounded-2xl shadow-sm">
<div class="flex justify-between items-center mb-8">
<h3 class="font-title-lg text-title-lg">Tendencias de Ocupacion por Edificio</h3>
<div class="flex gap-4">
<label class="flex items-center gap-2 cursor-pointer">
<div class="w-3 h-3 rounded-full bg-primary"></div>
<span class="text-label-md text-secondary">Edificio A</span>
</label>
<label class="flex items-center gap-2 cursor-pointer">
<div class="w-3 h-3 rounded-full bg-secondary"></div>
<span class="text-label-md text-secondary">Laboratorios</span>
</label>
</div>
</div>
<div class="relative h-64 w-full flex items-end justify-between px-4 pb-4 border-b border-surface-container-highest">
<div class="absolute inset-0 flex flex-col justify-between pointer-events-none opacity-50">
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
</div>
<div class="absolute inset-0 top-12">
<svg class="w-full h-full" preserveaspectratio="none" viewbox="0 0 100 100">
<path d="M0,80 Q20,30 40,50 T80,10 T100,40" fill="none" stroke="#B00020" stroke-width="2" vector-effect="non-scaling-stroke"></path>
<path d="M0,90 Q25,70 50,85 T90,60 T100,70" fill="none" stroke="#585f64" stroke-dasharray="4" stroke-width="1.5" vector-effect="non-scaling-stroke"></path>
</svg>
</div>
<div class="text-[10px] text-secondary">Lun</div>
<div class="text-[10px] text-secondary">Mar</div>
<div class="text-[10px] text-secondary">Mie</div>
<div class="text-[10px] text-secondary">Jue</div>
<div class="text-[10px] text-secondary">Vie</div>
<div class="text-[10px] text-secondary">Sab</div>
<div class="text-[10px] text-secondary">Dom</div>
</div>
<div class="mt-6 flex justify-around">
<div class="text-center">
<p class="text-label-md text-secondary">Pico Maximo</p>
<p class="font-title-lg text-title-lg">98% (Jue)</p>
</div>
<div class="text-center">
<p class="text-label-md text-secondary">Tasa de Desercion</p>
<p class="font-title-lg text-title-lg">4.2%</p>
</div>
<div class="text-center">
<p class="text-label-md text-secondary">Uso Promedio</p>
<p class="font-title-lg text-title-lg">6.5 hrs/dia</p>
</div>
</div>
</div>
<div class="glass-panel p-8 rounded-2xl shadow-sm">
<h3 class="font-title-lg text-title-lg mb-6">Uso de Software Academico</h3>
<div class="space-y-6">
<div class="space-y-2">
<div class="flex justify-between items-center text-body-md">
<span class="font-medium">MATLAB Advanced</span>
<span class="text-secondary">820 licencias</span>
</div>
<div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[85%]"></div>
</div>
</div>
<div class="space-y-2">
<div class="flex justify-between items-center text-body-md">
<span class="font-medium">AutoCAD 2024</span>
<span class="text-secondary">645 licencias</span>
</div>
<div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden">
<div class="bg-primary h-full w-[65%]"></div>
</div>
</div>
<div class="space-y-2">
<div class="flex justify-between items-center text-body-md">
<span class="font-medium">Wolfram Alpha Pro</span>
<span class="text-secondary">310 licencias</span>
</div>
<div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden">
<div class="bg-secondary h-full w-[40%]"></div>
</div>
</div>
<div class="space-y-2">
<div class="flex justify-between items-center text-body-md">
<span class="font-medium">IBM SPSS Statistics</span>
<span class="text-secondary">112 licencias</span>
</div>
<div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden">
<div class="bg-secondary h-full w-[22%]"></div>
</div>
</div>
</div>
<div class="mt-8 p-4 bg-surface-container-low rounded-xl border border-surface-container-highest">
<p class="text-label-md text-secondary italic">"Recomendacion: Incrementar licencias de MATLAB para el proximo trimestre basado en proyeccion de uso."</p>
</div>
</div>
</section>
<!-- Faculty Performance Table -->
<section class="mb-section-gap">
<div class="flex justify-between items-end mb-stack-lg">
<div>
<h3 class="font-headline-md text-headline-md">Metricas de Facultad</h3>
<p class="text-body-md text-secondary">Evaluacion integral por departamentos y decanos</p>
</div>
<button class="text-primary font-label-md flex items-center gap-1 hover:underline">
                        Ver todas las facultades
                        <span class="material-symbols-outlined text-[16px]">chevron_right</span>
</button>
</div>
<div class="glass-panel rounded-2xl shadow-sm overflow-hidden">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low border-b border-surface-container-highest">
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Facultad</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Tasa Retencion</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Publicaciones Q1</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Tendencia Trim.</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_FACULTADES
</tbody>
</table>
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
        document.addEventListener('DOMContentLoaded', () => {
            const progressBars = document.querySelectorAll('.bg-primary.h-full, .bg-secondary.h-full');
            progressBars.forEach(bar => {
                const finalWidth = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => { bar.style.width = finalWidth; }, 300);
            });
        });
    </script>
</body></html>
"""
