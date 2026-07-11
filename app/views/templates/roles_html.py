"""Roles page template."""
HTML_ROLES = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>UTP Academic | Roles</title>
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

<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/docentes">
<span class="material-symbols-outlined">person</span>
<span class="font-medium">Docentes</span>
</a>
<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors duration-200" href="/admin/reservas">
<span class="material-symbols-outlined">event_seat</span>
<span class="font-medium">Reservas</span>
</a>

<a class="flex items-center gap-3 px-4 py-3 rounded-xl text-primary font-bold border-r-4 border-primary bg-surface-container-low" href="/admin/roles">
<span class="material-symbols-outlined">admin_panel_settings</span>
<span class="font-bold">Roles</span>
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
<h1 class="font-headline-lg text-headline-lg text-on-surface">Roles</h1>
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
