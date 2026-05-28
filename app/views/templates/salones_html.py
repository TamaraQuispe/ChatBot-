HTML_SALONES = """
<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Gestion de Salones - Asistente Academico UTP</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Libre+Franklin:wght@400;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "tertiary-fixed-dim": "#b7c8e1","inverse-primary": "#ffb3af","on-secondary": "#ffffff","on-surface-variant": "#5b403e","surface-tint": "#bc1127","primary-container": "#b00020","secondary": "#5f5e5e","surface-container-low": "#f3f4f5","on-primary": "#ffffff","on-surface": "#191c1d","outline": "#906f6d","primary-fixed-dim": "#ffb3af","inverse-on-surface": "#f0f1f2","surface-container": "#edeeef","inverse-surface": "#2e3132","on-secondary-fixed-variant": "#474746","surface-container-lowest": "#ffffff","surface-container-high": "#e7e8e9","on-tertiary-fixed": "#0b1c30","primary": "#840015","surface": "#f8f9fa","on-primary-container": "#ffbbb8","tertiary": "#304055","surface-container-highest": "#e1e3e4","error-container": "#ffdad6","outline-variant": "#e4bdbb","secondary-fixed-dim": "#c8c6c5","background": "#f8f9fa","surface-dim": "#d9dadb","error": "#ba1a1a","secondary-container": "#e2dfde","on-error-container": "#93000a","surface-bright": "#f8f9fa","on-primary-fixed": "#410006","surface-variant": "#e1e3e4","primary-fixed": "#ffdad8","on-error": "#ffffff","on-tertiary-fixed-variant": "#38485d","tertiary-container": "#47576d","on-secondary-fixed": "#1c1b1b","on-secondary-container": "#636262","secondary-fixed": "#e5e2e1","tertiary-fixed": "#d3e4fe","on-tertiary": "#ffffff","on-primary-fixed-variant": "#930019","on-tertiary-container": "#bccde6","on-background": "#191c1d"
      },
      borderRadius: { DEFAULT: "0.5rem", lg: "0.5rem", xl: "0.75rem", full: "9999px" },
      spacing: { xs: "4px", gutter: "24px", "margin-mobile": "16px", "margin-desktop": "40px", sm: "12px", xl: "80px", base: "8px", lg: "48px", md: "24px", "container-max": "1280px" },
      fontFamily: { "headline-lg-mobile": ["Libre Franklin"], "headline-lg": ["Libre Franklin"], "label-md": ["Libre Franklin"], "body-sm": ["Libre Franklin"], "headline-md": ["Libre Franklin"], "display-lg": ["Libre Franklin"], "body-lg": ["Libre Franklin"], "body-md": ["Libre Franklin"], "label-caps": ["Libre Franklin"] },
      fontSize: {
        "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "600"}],
        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
        "label-md": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}],
        "label-caps": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}]
      }
    }
  }
}
</script>
<style>
.material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
.glass-card { background: #ffffff; border: 1px solid #e1e3e4; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.scrollbar-hide::-webkit-scrollbar { display: none; }
.soft-shadow { box-shadow: 0px 4px 6px -1px rgba(0, 0, 0, 0.05), 0px 2px 4px -2px rgba(0, 0, 0, 0.03); }
</style>
</head>
<body class="bg-surface text-on-surface font-body-md antialiased overflow-hidden">
<div class="flex h-screen w-full">

<div id="sidebar-overlay" class="fixed inset-0 bg-black/30 z-30 hidden lg:hidden transition-opacity" onclick="toggleSidebar()"></div>

<aside id="sidebar" class="fixed left-0 top-0 h-screen w-[260px] -translate-x-full lg:translate-x-0 transition-transform duration-300 ease-in-out z-40 border-r border-outline-variant bg-surface-container-lowest flex flex-col py-6 lg:py-8 shadow-lg lg:shadow-none">
<div class="px-5 lg:px-6 mb-6 lg:mb-8 flex items-center justify-between">
<div class="flex items-center gap-3">
<div class="w-9 h-9 lg:w-10 lg:h-10 rounded-lg bg-primary flex items-center justify-center text-white font-bold text-sm lg:text-base">UTP</div>
<div>
<h1 class="font-headline-md text-[16px] lg:text-[18px] font-bold text-primary leading-none">Asistente Academico</h1>
<p class="text-[9px] lg:text-[10px] font-label-md uppercase tracking-widest text-secondary">UTP PERU &bull; ADMIN</p>
</div>
</div>
<button onclick="toggleSidebar()" class="lg:hidden text-secondary hover:text-primary p-1">
<span class="material-symbols-outlined">close</span>
</button>
</div>
<nav class="flex-1 overflow-y-auto scrollbar-hide space-y-1 px-2 lg:px-0">
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="/admin">
<span class="material-symbols-outlined text-[20px]">dashboard</span>
<span class="font-label-md text-[13px]">Inicio</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 bg-primary/10 border-l-4 border-primary text-primary rounded-r-lg transition-all duration-200" href="/admin/salones">
<span class="material-symbols-outlined text-[20px]">meeting_room</span>
<span class="font-label-md text-[13px]">Salones</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">terminal</span>
<span class="font-label-md text-[13px]">Software y Equipos</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">calendar_today</span>
<span class="font-label-md text-[13px]">Horarios</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">school</span>
<span class="font-label-md text-[13px]">Docentes</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">event_seat</span>
<span class="font-label-md text-[13px]">Reservas</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">analytics</span>
<span class="font-label-md text-[13px]">Reportes</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="#">
<span class="material-symbols-outlined text-[20px]">admin_panel_settings</span>
<span class="font-label-md text-[13px]">Roles y Permisos</span>
</a>
</nav>
<div class="px-5 lg:px-6 mt-auto pt-6 border-t border-outline-variant">
<a class="flex items-center gap-3 px-3 lg:px-4 py-2.5 lg:py-3 text-secondary hover:text-primary rounded-lg transition-colors duration-200" href="/logout">
<span class="material-symbols-outlined text-[20px]">logout</span>
<span class="font-label-md text-[13px]">Cerrar Sesion</span>
</a>
<div class="mt-3 p-3 lg:p-4 rounded-xl border border-outline-variant bg-surface-container-low flex items-center gap-3">
<img alt="Admin" class="w-7 h-7 lg:w-8 lg:h-8 rounded-full border border-primary/50 object-cover" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDiOfXbwigm_HZNHZ9SrUhOBKbE5iFfE_mHoef0bOfi4pZMEZczTpajTnbYXHikILt_VUr6tKluEEigfsiZlfw9wxawtRa_WHtWogOXcyExp3azEK69n2e0zl5X-Pv4YOulv4E20sFFHVNPtdgzjeUIDR87pBUZgzk8QYeR5YoyiAMcM8D6ZJDhCUDzyy48uFL1sBL6eNO7XhyvJD1XmwXZQdJSFpqXGAjjLnQJblIT_EFKkcgPpQDpWBjqa5evwZv5B6q_M4MSvBg"/>
<div class="overflow-hidden min-w-0">
<p class="font-label-md text-[11px] truncate text-on-surface">$NOMBRE_ADMIN</p>
<p class="text-[9px] text-secondary truncate">Director TI</p>
</div>
</div>
</div>
</aside>

<main class="flex-1 ml-0 lg:ml-[260px] flex flex-col h-screen overflow-y-auto bg-surface relative">
<header class="h-14 lg:h-16 sticky top-0 z-20 bg-surface-container-lowest/80 backdrop-blur-md border-b border-outline-variant flex items-center justify-between px-3 md:px-6 lg:px-8 shadow-sm gap-3">
<div class="flex items-center gap-3 flex-1 min-w-0">
<button onclick="toggleSidebar()" class="lg:hidden p-2 -ml-1 text-secondary hover:text-primary rounded-lg hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<div class="relative w-full max-w-[200px] sm:max-w-[280px] md:max-w-sm group">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary group-focus-within:text-primary transition-colors text-[18px]">search</span>
<input class="w-full bg-surface-container-low border border-outline-variant rounded-lg py-1.5 lg:py-2 pl-9 pr-3 font-body-sm text-on-surface text-[13px] focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all placeholder:text-secondary/60" placeholder="Buscar salones, pabellones o IDs..." type="text"/>
</div>
</div>
<div class="flex items-center gap-2 sm:gap-4 lg:gap-6 flex-shrink-0">
<button class="relative p-1.5 lg:p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined text-[20px] lg:text-[24px]">notifications</span>
<span class="absolute top-1 right-1 lg:top-1.5 lg:right-1.5 w-1.5 h-1.5 lg:w-2 lg:h-2 bg-primary rounded-full border-2 border-surface-container-lowest"></span>
</button>
<button class="bg-primary hover:bg-primary-container text-white px-3 lg:px-4 py-1.5 lg:py-2 rounded-lg font-label-md text-[12px] lg:text-[13px] flex items-center gap-1.5 lg:gap-2 transition-all active:scale-95 whitespace-nowrap">
<span class="material-symbols-outlined text-[16px] lg:text-[18px]">add</span>
<span class="hidden sm:inline">Nueva Reserva</span>
</button>
</div>
</header>

<div class="px-3 md:px-6 lg:px-8 py-6 lg:py-10 xl:py-12 max-w-[1400px] mx-auto w-full">

<div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 mb-6 lg:mb-8">
<div>
<h2 class="font-headline-lg text-[24px] lg:text-[28px] xl:text-headline-lg text-on-surface">Gestion de Salones</h2>
<p class="font-body-md lg:font-body-lg text-secondary mt-1">Monitorea y administra la disponibilidad de espacios academicos en tiempo real.</p>
</div>

</div>

<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 lg:gap-6 mb-6 lg:mb-8">
<div class="glass-card p-4 lg:p-6 rounded-xl relative overflow-hidden">
<div class="flex justify-between items-start mb-3 lg:mb-4">
<div class="p-2 bg-surface-container-low rounded-lg text-on-surface">
<span class="material-symbols-outlined text-[20px] lg:text-[24px]">inventory_2</span>
</div>
<span class="text-[10px] lg:text-xs font-bold text-green-600 bg-green-50 px-2 py-1 rounded">+2 hoy</span>
</div>
<p class="font-label-md text-secondary mb-1 text-[11px] lg:text-[12px]">Total Salones</p>
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface">142</h3>
</div>
<div class="glass-card p-4 lg:p-6 rounded-xl relative overflow-hidden">
<div class="flex justify-between items-start mb-3 lg:mb-4">
<div class="p-2 bg-primary/10 rounded-lg text-primary">
<span class="material-symbols-outlined text-[20px] lg:text-[24px]">personal_video</span>
</div>
<span class="text-[10px] lg:text-xs font-bold text-primary">64% ocupado</span>
</div>
<p class="font-label-md text-secondary mb-1 text-[11px] lg:text-[12px]">En Uso</p>
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface">91</h3>
</div>
<div class="glass-card p-4 lg:p-6 rounded-xl relative overflow-hidden">
<div class="flex justify-between items-start mb-3 lg:mb-4">
<div class="p-2 bg-blue-50 rounded-lg text-blue-600">
<span class="material-symbols-outlined text-[20px] lg:text-[24px]">check_circle</span>
</div>
<span class="text-[10px] lg:text-xs font-bold text-blue-600">Listo reserva</span>
</div>
<p class="font-label-md text-secondary mb-1 text-[11px] lg:text-[12px]">Disponibles</p>
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface">43</h3>
</div>
</div>

<div class="flex items-center gap-2 mb-4 lg:mb-6 overflow-x-auto pb-2 scrollbar-hide">
<button class="px-4 lg:px-5 py-1.5 lg:py-2 rounded-full bg-primary text-white font-bold text-[12px] lg:text-body-sm transition-all shadow-md shadow-primary/20 whitespace-nowrap">Todos</button>
<button class="px-4 lg:px-5 py-1.5 lg:py-2 rounded-full bg-white border border-outline-variant text-secondary font-bold text-[12px] lg:text-body-sm hover:border-primary hover:text-primary transition-all whitespace-nowrap">Laboratorios</button>
<button class="px-4 lg:px-5 py-1.5 lg:py-2 rounded-full bg-white border border-outline-variant text-secondary font-bold text-[12px] lg:text-body-sm hover:border-primary hover:text-primary transition-all whitespace-nowrap">Aulas de Computo</button>
<button class="px-4 lg:px-5 py-1.5 lg:py-2 rounded-full bg-white border border-outline-variant text-secondary font-bold text-[12px] lg:text-body-sm hover:border-primary hover:text-primary transition-all whitespace-nowrap">Aulas Teoricas</button>
</div>

<div class="glass-card rounded-xl overflow-hidden border border-outline-variant overflow-x-auto">
<table class="w-full text-left border-collapse min-w-[640px]">
<thead class="bg-surface-container-low border-b border-outline-variant">
<tr>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Salon / ID</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Tipo de Espacio</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px] text-center">Capacidad</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Ubicacion</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Estado</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px] text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
$TABLA_SALONES
</tbody>
</table>
<div class="px-4 lg:px-6 py-3 lg:py-4 bg-surface-container-low flex flex-col sm:flex-row items-center justify-between gap-2 border-t border-outline-variant">
<span class="text-[10px] lg:text-[11px] text-secondary">Mostrando <span class="font-bold text-on-surface">$TOTAL_SALONES</span> salones</span>
</div>
</div>

<div class="mt-6 lg:mt-8">
<div class="bg-primary p-4 lg:p-6 rounded-xl relative overflow-hidden group max-w-2xl">
<div class="relative z-10 text-white">
<h4 class="font-headline-md text-[18px] lg:text-headline-md mb-2">Reportes de Espacio</h4>
<p class="font-body-md text-body-md text-white/80 mb-4">Genera reportes de ocupacion y uso de recursos por facultad.</p>
<button class="px-4 lg:px-5 py-2 lg:py-2.5 bg-white text-primary rounded-lg font-bold text-[12px] lg:text-sm shadow-lg hover:bg-surface-container-high transition-all">
Descargar Excel (XLSX)
</button>
</div>
<div class="absolute -bottom-10 -right-10 opacity-10 group-hover:scale-110 transition-transform duration-500 pointer-events-none">
<span class="material-symbols-outlined text-[120px] lg:text-[160px] text-white">analytics</span>
</div>
</div>
</div>

</div>
</main>
</div>
<script>
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebar-overlay');
  const isOpen = sidebar.classList.contains('translate-x-0');
  sidebar.classList.toggle('-translate-x-full', isOpen);
  sidebar.classList.toggle('translate-x-0', !isOpen);
  overlay.classList.toggle('hidden', isOpen);
}
document.querySelectorAll('tbody tr').forEach(row => {
    row.addEventListener('mouseenter', () => {
        const icon = row.querySelector('.material-symbols-outlined');
        if (icon) { icon.style.transform = 'translateX(4px)'; icon.style.transition = 'transform 0.2s ease-out'; }
    });
    row.addEventListener('mouseleave', () => {
        const icon = row.querySelector('.material-symbols-outlined');
        if (icon) { icon.style.transform = 'translateX(0)'; }
    });
});
const chips = document.querySelectorAll('.flex.items-center.gap-2.mb-\\[1\\.5rem\\] button, .flex.items-center.gap-2.mb-4 button, .flex.items-center.gap-2.mb-6 button');
chips.forEach(chip => {
    chip.addEventListener('click', () => {
        chips.forEach(c => { c.classList.remove('bg-primary', 'text-white', 'shadow-md', 'shadow-primary/20'); c.classList.add('bg-white', 'text-secondary', 'border-outline-variant'); });
        chip.classList.add('bg-primary', 'text-white', 'shadow-md', 'shadow-primary/20');
        chip.classList.remove('bg-white', 'text-secondary', 'border-outline-variant');
    });
});
</script>
</body></html>
"""
