HTML_HORARIOS = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Gestion de Horarios</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100;300;400;500;600;700;800;900&amp;family=Courier+Prime&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
            vertical-align: middle;
        }
        .glass-panel {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(230, 232, 235, 1);
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #e1e3e4;
            border-radius: 10px;
        }
        .calendar-grid {
            display: grid;
            grid-template-columns: 80px repeat(5, 1fr);
            min-width: 600px;
            overflow-x: auto;
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
                    "full": "9999px"
            },
            "spacing": {
                    "stack-md": "16px",
                    "stack-lg": "24px",
                    "stack-sm": "8px",
                    "gutter": "24px",
                    "container-padding": "32px",
                    "section-gap": "80px"
            },
            "fontFamily": {
                    "body-md": ["Libre Franklin"],
                    "mono-sm": ["Courier Prime"],
                    "label-md": ["Libre Franklin"],
                    "headline-lg": ["Libre Franklin"],
                    "title-lg": ["Libre Franklin"],
                    "display-lg": ["Libre Franklin"],
                    "body-lg": ["Libre Franklin"],
                    "headline-md": ["Libre Franklin"]
            },
            "fontSize": {
                    "body-md": ["14px", {"lineHeight": "1.6", "letterSpacing": "0em", "fontWeight": "400"}],
                    "mono-sm": ["13px", {"lineHeight": "1.5", "letterSpacing": "0em", "fontWeight": "400"}],
                    "label-md": ["12px", {"lineHeight": "1", "letterSpacing": "0.02em", "fontWeight": "500"}],
                    "headline-lg": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.03em", "fontWeight": "600"}],
                    "title-lg": ["18px", {"lineHeight": "1.5", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "display-lg": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.04em", "fontWeight": "700"}],
                    "body-lg": ["16px", {"lineHeight": "1.6", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                    "headline-md": ["24px", {"lineHeight": "1.3", "letterSpacing": "-0.02em", "fontWeight": "600"}]
            }
          },
        },
      }
    </script>
</head>
<body class="font-body-md text-body-md overflow-hidden">
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
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/horarios">
<span class="material-symbols-outlined">calendar_today</span>
<span class="font-bold">Horarios</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined">person</span>
<span class="font-medium">Docentes</span>
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
<main class="ml-0 md:ml-64 w-full md:w-[calc(100%-16rem)] h-screen flex flex-col overflow-hidden">
<!-- Top Navigation Bar -->
<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-50 glass-panel h-16 px-container-padding flex justify-between items-center border-b border-surface-container-highest">
<div class="flex items-center gap-4 md:gap-8">
<button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<span class="font-title-lg text-title-lg font-black tracking-tight text-on-surface">UTP Academic</span>
<div class="hidden md:flex gap-6 text-label-md font-label-md">
<a class="text-on-surface-variant hover:text-on-surface" href="#">Calendario</a>
<a class="text-on-surface-variant hover:text-on-surface" href="#">Hoy</a>
<a class="text-on-surface-variant hover:text-on-surface" href="#">Directorio</a>
</div>
</div>
<div class="flex items-center gap-4">
<div class="relative group">
<span class="absolute inset-y-0 left-3 flex items-center text-secondary">
<span class="material-symbols-outlined text-[20px]">search</span>
</span>
<input class="pl-10 pr-4 py-1.5 bg-surface-container-low border-none rounded-full text-body-md focus:ring-1 focus:ring-primary w-full sm:w-64 transition-all" placeholder="Buscar horario..." type="text"/>
</div>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">notifications</button>
<button class="material-symbols-outlined text-secondary hover:text-primary transition-colors">apps</button>
<button class="px-4 py-2 bg-primary text-white rounded-lg font-label-md text-label-md font-bold hover:opacity-90 transition-all">
                    Nueva Reserva
                </button>
<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">A</div>
</div>
</header>
<!-- Page Content -->
<div class="mt-16 flex-1 flex flex-col overflow-hidden">
<!-- Header Section -->
<section class="px-container-padding pt-6 bg-surface flex-shrink-0">
<div class="flex justify-between items-end mb-6">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Gestion de Horarios Academicos</h1>
<p class="text-secondary mt-1">Planificacion semanal de infraestructura y facultades - Semestre 2024-II</p>
</div>
<div class="flex gap-3">
<div class="flex bg-white border border-surface-container-highest rounded-lg p-1">
<button class="px-4 py-1.5 bg-surface-container-high rounded font-label-md text-label-md">Semana</button>
<button class="px-4 py-1.5 hover:bg-surface-container-low rounded font-label-md text-label-md transition-colors">Mes</button>
</div>
<button class="flex items-center gap-2 px-4 py-2 border border-surface-container-highest bg-white rounded-lg font-label-md text-label-md hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-sm">filter_list</span>
                        Filtros Avanzados
                    </button>
</div>
</div>
<!-- Quick Filters (Bento Style) -->
<div class="grid grid-cols-2 sm:grid-cols-4 gap-gutter mb-6">
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Edificio</span>
<select class="bg-transparent border-none p-0 focus:ring-0 font-title-lg text-title-lg text-on-surface">
<option>Torre Tecnologica A</option>
<option>Pabellon de Ciencias</option>
<option>Campus Central</option>
</select>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Tipo de Aula</span>
<select class="bg-transparent border-none p-0 focus:ring-0 font-title-lg text-title-lg text-on-surface">
<option>Laboratorio High-End</option>
<option>Aula Magistral</option>
<option>Taller Creativo</option>
</select>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Franja Horaria</span>
<div class="flex items-center justify-between">
<span class="font-title-lg text-title-lg">07:00 - 22:00</span>
<span class="material-symbols-outlined text-primary">schedule</span>
</div>
</div>
<div class="glass-panel p-stack-md rounded-xl flex flex-col gap-2 border-l-4 border-l-primary">
<span class="text-label-md font-label-md text-secondary uppercase tracking-wider">Ocupacion Actual</span>
<div class="flex items-baseline gap-2">
<span class="font-display-lg text-display-lg text-primary">84%</span>
<span class="text-label-md font-label-md text-green-600 flex items-center">
<span class="material-symbols-outlined text-xs">trending_up</span> 12%
                        </span>
</div>
</div>
</div>
</section>
<!-- Interactive Calendar View -->
<section class="flex-1 px-container-padding pb-container-padding overflow-hidden flex flex-col">
<div class="bg-white border border-surface-container-highest rounded-2xl flex-1 flex flex-col overflow-hidden shadow-sm">
<div class="overflow-x-auto w-full">
<!-- Days Header -->
<div class="calendar-grid border-b border-surface-container-highest bg-surface-container-lowest">
<div class="p-4 border-r border-surface-container-highest"></div>
<div class="p-4 border-r border-surface-container-highest text-center">
<span class="block text-label-md font-label-md text-secondary mb-1">LUNES</span>
<span class="font-title-lg text-title-lg">18</span>
</div>
<div class="p-4 border-r border-surface-container-highest text-center bg-primary-fixed/20">
<span class="block text-label-md font-label-md text-primary mb-1">MARTES</span>
<span class="font-title-lg text-title-lg text-primary">19</span>
</div>
<div class="p-4 border-r border-surface-container-highest text-center">
<span class="block text-label-md font-label-md text-secondary mb-1">MIERCOLES</span>
<span class="font-title-lg text-title-lg">20</span>
</div>
<div class="p-4 border-r border-surface-container-highest text-center">
<span class="block text-label-md font-label-md text-secondary mb-1">JUEVES</span>
<span class="font-title-lg text-title-lg">21</span>
</div>
<div class="p-4 text-center">
<span class="block text-label-md font-label-md text-secondary mb-1">VIERNES</span>
<span class="font-title-lg text-title-lg">22</span>
</div>
</div>
<!-- Scrollable Body -->
<div class="flex-1 overflow-y-auto custom-scrollbar relative">
<div class="calendar-grid min-h-[800px]">
<!-- Time Column -->
<div class="bg-surface-container-lowest border-r border-surface-container-highest">
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary">07:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">08:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">09:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">10:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">11:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">12:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">13:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">14:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">15:00</div>
<div class="h-20 flex items-start justify-center pt-2 text-label-md text-secondary border-t border-surface-container-highest/30">16:00</div>
</div>
<!-- Grid Columns (Days) -->
<div class="border-r border-surface-container-highest/30 relative">
<div class="absolute top-0 left-0 right-0 m-1 p-2 bg-primary-container text-on-primary-container rounded-lg shadow-sm border-l-4 border-primary z-10 hover:scale-[1.02] transition-transform cursor-pointer overflow-hidden text-ellipsis whitespace-nowrap" style="height: 152px;">
<div class="flex justify-between items-start">
<span class="text-label-md font-bold">CALCULO VECTORIAL</span>
<span class="material-symbols-outlined text-xs">lock</span>
</div>
<p class="text-xs opacity-90 mb-2">Pabellon A - Lab 302</p>
<div class="flex items-center gap-1 mt-auto">
<div class="w-5 h-5 rounded-full bg-surface-container-highest flex items-center justify-center text-[8px] font-bold text-secondary">RM</div>
<span class="text-[10px] font-medium">Dr. Mendez, R.</span>
</div>
</div>
</div>
<div class="border-r border-surface-container-highest/30 bg-primary-fixed/5 relative">
<div class="absolute top-[160px] left-0 right-0 m-1 p-2 bg-white text-on-surface border border-surface-container-highest rounded-lg shadow-sm z-10 hover:border-primary transition-all cursor-pointer overflow-hidden text-ellipsis whitespace-nowrap" style="height: 76px;">
<div class="flex justify-between items-start">
<span class="text-label-md font-bold">REUNION FACULTAD</span>
<div class="w-2 h-2 rounded-full bg-amber-500"></div>
</div>
<p class="text-xs text-secondary">Sala de Juntas 1</p>
</div>
</div>
<div class="border-r border-surface-container-highest/30 relative">
<div class="absolute top-[80px] left-0 right-0 m-1 p-2 bg-tertiary-container text-on-tertiary-container rounded-lg shadow-sm z-10 overflow-hidden text-ellipsis whitespace-nowrap" style="height: 152px;">
<span class="text-label-md font-bold">INGENIERIA DE SOFTWARE</span>
<p class="text-xs opacity-90">Auditorio Principal</p>
<div class="mt-4 flex -space-x-2">
<div class="w-6 h-6 rounded-full border-2 border-tertiary-container bg-surface-dim"></div>
<div class="w-6 h-6 rounded-full border-2 border-tertiary-container bg-surface-dim"></div>
<div class="w-6 h-6 rounded-full border-2 border-tertiary-container bg-surface-dim"></div>
</div>
</div>
</div>
<div class="border-r border-surface-container-highest/30 relative"></div>
<div class="relative">
<div class="absolute top-[320px] left-0 right-0 m-1 p-2 bg-primary/10 border border-primary/20 text-primary rounded-lg shadow-sm z-10 overflow-hidden text-ellipsis whitespace-nowrap" style="height: 152px;">
<span class="text-label-md font-bold">TALLER DE ROBOTICA</span>
<p class="text-xs font-medium">Laboratorio de Manufactura</p>
</div>
</div>
</div>
</div>
</div>
</div>
</section>
</div>
<!-- Footer -->
<footer class="flex-shrink-0 bg-surface border-t border-surface-container-highest py-stack-lg">
<div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center px-container-padding gap-4">
<div class="flex items-center gap-4">
<span class="font-label-md text-label-md font-medium text-secondary">© 2024 UTP Academic Management. SaaS Elite Tier.</span>
<div class="flex items-center gap-2">
<div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
<span class="text-label-md font-label-md text-secondary">Sistema Operativo</span>
</div>
</div>
<div class="flex gap-6">
<a class="text-secondary hover:text-on-surface transition-colors font-body-md text-body-md" href="#">Privacidad</a>
<a class="text-secondary hover:text-on-surface transition-colors font-body-md text-body-md" href="#">Soporte</a>
<a class="text-secondary hover:text-on-surface transition-colors font-body-md text-body-md" href="#">API Docs</a>
</div>
</div>
</footer>
</main>
<script>
        const calendarBody = document.querySelector('.overflow-y-auto');
        if (calendarBody) calendarBody.scrollTop = 150;

        document.querySelectorAll('[style*="height"]').forEach(card => {
            card.addEventListener('mouseenter', () => {
                card.style.zIndex = '30';
            });
            card.addEventListener('mouseleave', () => {
                card.style.zIndex = '10';
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
