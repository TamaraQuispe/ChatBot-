HTML_ROLES = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Roles y Permisos</title>
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
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/roles">
<span class="material-symbols-outlined">admin_panel_settings</span>
<span class="font-bold">Roles y Permisos</span>
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
<input class="pl-10 pr-4 py-1.5 bg-surface-container-low border-none rounded-full text-body-md focus:ring-1 focus:ring-primary w-full sm:w-64 transition-all" placeholder="Buscar modulos..." type="text"/>
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
<h1 class="font-headline-lg text-headline-lg text-on-surface">Roles y Permisos</h1>
<p class="text-secondary mt-1">Gestiona los niveles de acceso y privilegios del personal academico y administrativo.</p>
</div>
<div class="flex gap-3">
<button class="flex items-center gap-2 border border-surface-container-highest bg-white px-4 py-2 rounded-lg text-label-md font-label-md hover:bg-surface-container-low transition-all">
<span class="material-symbols-outlined text-[18px]">download</span>
                        Auditoria de Cambios
                    </button>
<button class="flex items-center gap-2 bg-primary text-white px-4 py-2 rounded-lg text-label-md font-label-md hover:opacity-90 transition-all">
<span class="material-symbols-outlined text-[18px]">add</span>
                        Crear Nuevo Rol
                    </button>
</div>
</section>
<!-- Role Cards -->
<section class="grid grid-cols-1 md:grid-cols-3 gap-gutter mb-section-gap">
<div class="bg-white border border-surface-container-highest rounded-2xl p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
<div class="flex justify-between items-start mb-4">
<div class="p-3 bg-primary-container/10 rounded-lg">
<span class="material-symbols-outlined text-primary">admin_panel_settings</span>
</div>
<span class="flex items-center gap-1 text-label-md text-secondary">
<span class="w-2 h-2 rounded-full bg-emerald-500"></span> 5 Activos
</span>
</div>
<div>
<h3 class="font-title-lg text-title-lg mb-1">Administrador</h3>
<p class="text-body-md text-secondary mb-4">Acceso total al sistema, configuracion de seguridad y gestion de usuarios.</p>
</div>
<button class="w-full py-2 bg-surface-container-low text-on-surface font-label-md text-label-md rounded-lg hover:bg-surface-container-highest transition-colors">Configurar Permisos</button>
</div>
<div class="bg-white border border-surface-container-highest rounded-2xl p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
<div class="flex justify-between items-start mb-4">
<div class="p-3 bg-blue-50 rounded-lg text-blue-600">
<span class="material-symbols-outlined">history_edu</span>
</div>
<span class="flex items-center gap-1 text-label-md text-secondary">
<span class="w-2 h-2 rounded-full bg-emerald-500"></span> 124 Activos
</span>
</div>
<div>
<h3 class="font-title-lg text-title-lg mb-1">Docente</h3>
<p class="text-body-md text-secondary mb-4">Gestion de cursos, calificaciones, asistencia y comunicacion con estudiantes.</p>
</div>
<button class="w-full py-2 bg-surface-container-low text-on-surface font-label-md text-label-md rounded-lg hover:bg-surface-container-highest transition-colors">Configurar Permisos</button>
</div>
<div class="bg-white border border-surface-container-highest rounded-2xl p-6 shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
<div class="flex justify-between items-start mb-4">
<div class="p-3 bg-amber-50 rounded-lg text-amber-600">
<span class="material-symbols-outlined">badge</span>
</div>
<span class="flex items-center gap-1 text-label-md text-secondary">
<span class="w-2 h-2 rounded-full bg-emerald-500"></span> 42 Activos
</span>
</div>
<div>
<h3 class="font-title-lg text-title-lg mb-1">Personal</h3>
<p class="text-body-md text-secondary mb-4">Acceso a reportes, gestion de infraestructura y servicios administrativos.</p>
</div>
<button class="w-full py-2 bg-surface-container-low text-on-surface font-label-md text-label-md rounded-lg hover:bg-surface-container-highest transition-colors">Configurar Permisos</button>
</div>
</section>
<!-- Permissions Matrix -->
<section class="mb-section-gap">
<div class="flex items-center gap-3 mb-6">
<span class="material-symbols-outlined text-primary">key</span>
<h3 class="font-headline-md text-headline-md text-on-surface">Matriz de Permisos: <span class="font-normal text-secondary italic">Administrador</span></h3>
</div>
<div class="bg-white border border-surface-container-highest rounded-2xl shadow-sm">
<div class="overflow-x-auto">
<div class="grid grid-cols-12 border-b border-surface-container-highest bg-surface-container-low p-4">
<div class="col-span-5 font-label-md text-label-md text-secondary uppercase tracking-wider">Modulo / Funcionalidad</div>
<div class="col-span-1 text-center font-label-md text-label-md text-secondary uppercase tracking-wider">Ver</div>
<div class="col-span-1 text-center font-label-md text-label-md text-secondary uppercase tracking-wider">Crear</div>
<div class="col-span-1 text-center font-label-md text-label-md text-secondary uppercase tracking-wider">Editar</div>
<div class="col-span-1 text-center font-label-md text-label-md text-secondary uppercase tracking-wider">Borrar</div>
<div class="col-span-3 text-right font-label-md text-label-md text-secondary uppercase tracking-wider">Acciones Especiales</div>
</div>
$FILAS_PERMISOS
</div>
<div class="p-4 bg-white flex justify-end gap-4">
<button class="px-6 py-2 border border-surface-container-highest rounded-lg text-label-md font-label-md hover:bg-surface-container-low transition-all">Revertir Cambios</button>
<button class="px-6 py-2 bg-on-background text-white rounded-lg text-label-md font-label-md hover:opacity-90 transition-all">Guardar Configuracion</button>
</div>
</div>
</section>
<!-- Active Users -->
<section class="mb-section-gap">
<div class="flex justify-between items-center mb-6">
<div class="flex items-center gap-3">
<span class="material-symbols-outlined text-primary">group</span>
<h3 class="font-headline-md text-headline-md text-on-surface">Usuarios Activos</h3>
</div>
<div class="flex items-center gap-2">
<span class="text-label-md text-secondary">Filtrar por:</span>
<select class="border border-surface-container-highest rounded-lg text-label-md py-1 px-3 focus:ring-primary">
<option>Todos los Roles</option>
<option>Admin</option>
<option>Docente</option>
<option>Personal</option>
</select>
</div>
</div>
<div class="bg-white border border-surface-container-highest rounded-2xl overflow-x-auto shadow-sm">
<table class="w-full text-left">
<thead class="bg-surface-container-low border-b border-surface-container-highest">
<tr>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Usuario</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Rol Asignado</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Departamento</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Ultimo Acceso</th>
<th class="px-6 py-4 font-label-md text-label-md text-secondary uppercase">Estado</th>
<th class="px-6 py-4"></th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_USUARIOS
</tbody>
</table>
<div class="px-6 py-4 bg-surface-container-low flex justify-between items-center">
<span class="text-label-md text-secondary">Mostrando 1-10 de 171 usuarios</span>
<div class="flex gap-2">
<button class="p-1 border border-surface-container-highest rounded hover:bg-white transition-colors disabled:opacity-50" disabled><span class="material-symbols-outlined">chevron_left</span></button>
<button class="p-1 border border-surface-container-highest rounded hover:bg-white transition-colors"><span class="material-symbols-outlined">chevron_right</span></button>
</div>
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
        document.querySelectorAll('input[type="checkbox"]').forEach(checkbox => {
            checkbox.addEventListener('change', (e) => {
                const row = e.target.closest('.grid');
                if(e.target.checked) {
                    row.classList.add('bg-primary-container/[0.02]');
                } else {
                    row.classList.remove('bg-primary-container/[0.02]');
                }
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
