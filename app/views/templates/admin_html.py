HTML_ADMIN = """
<!DOCTYPE html>
<html lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Asistente Academico UTP - Control Center</title>
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
</style>
</head>
<body class="bg-surface text-on-surface font-body-md antialiased overflow-hidden">
<div class="flex h-screen w-full">

<!-- Sidebar Overlay (mobile only) -->
<div id="sidebar-overlay" class="fixed inset-0 bg-black/30 z-30 hidden lg:hidden transition-opacity" onclick="toggleSidebar()"></div>

<!-- Sidebar -->
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
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 bg-primary/10 border-l-4 border-primary text-primary rounded-r-lg transition-all duration-200" href="/admin">
<span class="material-symbols-outlined text-[20px]">dashboard</span>
<span class="font-label-md text-[13px]">Inicio</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-6 py-2.5 lg:py-3 text-secondary hover:text-primary hover:bg-surface-container-low rounded-r-lg transition-colors duration-200" href="/admin/salones">
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

<!-- Main Content -->
<main class="flex-1 ml-0 lg:ml-[260px] flex flex-col h-screen overflow-y-auto bg-surface relative">
<!-- Top Bar -->
<header class="h-14 lg:h-16 sticky top-0 z-20 bg-surface-container-lowest/80 backdrop-blur-md border-b border-outline-variant flex items-center justify-between px-3 md:px-6 lg:px-8 shadow-sm gap-3">
<div class="flex items-center gap-3 flex-1 min-w-0">
<button onclick="toggleSidebar()" class="lg:hidden p-2 -ml-1 text-secondary hover:text-primary rounded-lg hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<div class="relative w-full max-w-[200px] sm:max-w-[280px] md:max-w-sm group">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary group-focus-within:text-primary transition-colors text-[18px]">search</span>
<input class="w-full bg-surface-container-low border border-outline-variant rounded-lg py-1.5 lg:py-2 pl-9 pr-3 font-body-sm text-on-surface text-[13px] focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all placeholder:text-secondary/60" placeholder="Buscar..." type="text"/>
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

<!-- Content -->
<div class="px-3 md:px-6 lg:px-8 py-6 lg:py-10 xl:py-12 max-w-[1400px] mx-auto w-full">

<!-- Header -->
<section class="mb-6 lg:mb-10">
<div class="flex flex-col mb-6 lg:mb-8">
<h2 class="font-headline-lg text-[24px] lg:text-[28px] xl:text-headline-lg text-on-surface">Control Center</h2>
<p class="font-body-md lg:font-body-lg text-secondary max-w-2xl mt-1">Supervision integral de la infraestructura academica de UTP Peru. Monitoreo en tiempo real de salones y activos.</p>
</div>

<!-- KPI Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4 lg:gap-6 mb-8 lg:mb-12">
<div class="glass-card p-4 lg:p-6 rounded-xl relative group overflow-hidden">
<div class="absolute top-0 right-0 p-3 lg:p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-[36px] lg:text-[48px] text-on-surface">meeting_room</span>
</div>
<p class="font-label-md text-secondary mb-1 lg:mb-2 text-[11px] lg:text-[12px]">Salones Activos</p>
<div class="flex items-baseline gap-2">
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface" data-count="142">142</h3>
<span class="text-[10px] lg:text-xs text-tertiary-container flex items-center gap-1 font-semibold">
<span class="material-symbols-outlined text-[12px] lg:text-[14px]">trending_up</span> 4.2%</span>
</div>
<div class="mt-3 lg:mt-4 h-1 lg:h-1.5 w-full bg-surface-container-highest rounded-full overflow-hidden">
<div class="h-full bg-primary" style="width:85%"></div>
</div>
</div>

<div class="glass-card p-4 lg:p-6 rounded-xl relative group overflow-hidden">
<div class="absolute top-0 right-0 p-3 lg:p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-[36px] lg:text-[48px] text-on-surface">person</span>
</div>
<p class="font-label-md text-secondary mb-1 lg:mb-2 text-[11px] lg:text-[12px]">Docentes en Linea</p>
<div class="flex items-baseline gap-2">
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface" data-count="88">88</h3>
<span class="text-[10px] lg:text-xs text-secondary font-semibold">de 112 total</span>
</div>
<div class="mt-3 lg:mt-4 flex -space-x-1.5 lg:-space-x-2">
<div class="w-5 h-5 lg:w-6 lg:h-6 rounded-full border-2 border-surface-container-lowest bg-surface-dim flex items-center justify-center text-[8px] lg:text-[10px] text-on-surface font-medium">JD</div>
<div class="w-5 h-5 lg:w-6 lg:h-6 rounded-full border-2 border-surface-container-lowest bg-primary-fixed-dim flex items-center justify-center text-[8px] lg:text-[10px] text-on-primary-fixed font-medium">AM</div>
<div class="w-5 h-5 lg:w-6 lg:h-6 rounded-full border-2 border-surface-container-lowest bg-tertiary-fixed flex items-center justify-center text-[8px] lg:text-[10px] text-on-tertiary-fixed font-medium">RT</div>
<div class="w-5 h-5 lg:w-6 lg:h-6 rounded-full border-2 border-surface-container-lowest bg-surface-variant flex items-center justify-center text-[8px] lg:text-[10px] text-on-surface-variant font-medium">+5</div>
</div>
</div>

<div class="glass-card p-4 lg:p-6 rounded-xl relative group overflow-hidden border-l-4 border-l-primary">
<div class="absolute top-0 right-0 p-3 lg:p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-[36px] lg:text-[48px] text-on-surface">event_upcoming</span>
</div>
<p class="font-label-md text-secondary mb-1 lg:mb-2 text-[11px] lg:text-[12px]">Reservas Pendientes</p>
<div class="flex items-baseline gap-2">
<h3 class="text-2xl lg:text-4xl font-bold text-primary" data-count="24">24</h3>
</div>
<p class="mt-2 lg:mt-4 text-[10px] lg:text-[11px] text-secondary italic">Requieren aprobacion inmediata</p>
</div>

<div class="glass-card p-4 lg:p-6 rounded-xl relative group overflow-hidden">
<div class="absolute top-0 right-0 p-3 lg:p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-[36px] lg:text-[48px] text-on-surface">warning</span>
</div>
<p class="font-label-md text-secondary mb-1 lg:mb-2 text-[11px] lg:text-[12px]">Incidencias Software</p>
<div class="flex items-baseline gap-2">
<h3 class="text-2xl lg:text-4xl font-bold text-on-surface" data-count="3">03</h3>
<span class="text-[10px] lg:text-xs text-error font-semibold">-12% vs ayer</span>
</div>
<div class="mt-3 lg:mt-4 flex gap-0.5 lg:gap-1">
<div class="h-1 lg:h-1.5 flex-1 bg-error rounded-full"></div>
<div class="h-1 lg:h-1.5 flex-1 bg-error rounded-full"></div>
<div class="h-1 lg:h-1.5 flex-1 bg-error rounded-full"></div>
<div class="h-1 lg:h-1.5 flex-1 bg-surface-container-highest rounded-full"></div>
<div class="h-1 lg:h-1.5 flex-1 bg-surface-container-highest rounded-full"></div>
</div>
</div>
</div>
</section>

<!-- Charts + Stats -->
<div class="grid grid-cols-1 xl:grid-cols-3 gap-4 lg:gap-6 items-start">
<div class="xl:col-span-2 glass-card rounded-xl p-4 lg:p-6 xl:p-8">
<div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 mb-6 lg:mb-10">
<div>
<h3 class="font-headline-md text-[18px] lg:text-[20px] text-on-surface">Uso de Laboratorios por Piso</h3>
<p class="font-body-sm text-secondary text-[13px]">Torre Tecnologica - Sede Central</p>
</div>
<select class="bg-surface-container-low border border-outline-variant rounded-lg text-[11px] lg:text-[12px] py-1.5 px-2.5 outline-none text-secondary focus:ring-1 focus:ring-primary">
<option>Ultimos 7 dias</option>
<option>Este mes</option>
</select>
</div>
<div class="flex items-end justify-between h-48 lg:h-56 xl:h-64 gap-2 lg:gap-4 px-1 lg:px-4 relative">
<div class="absolute inset-0 flex flex-col justify-between pointer-events-none">
<div class="border-t border-outline-variant/50 w-full h-0"></div>
<div class="border-t border-outline-variant/50 w-full h-0"></div>
<div class="border-t border-outline-variant/50 w-full h-0"></div>
<div class="border-t border-outline-variant/50 w-full h-0"></div>
<div class="border-t border-outline-variant/50 w-full h-0"></div>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-surface-container-highest rounded-t relative transition-all duration-500 group-hover:bg-primary/20" style="height:45%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">45%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-secondary">P1</span>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-surface-container-highest rounded-t relative transition-all duration-500 group-hover:bg-primary/20" style="height:65%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">65%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-secondary">P2</span>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-primary rounded-t relative transition-all duration-500" style="height:92%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">92%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-on-surface font-bold">P3</span>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-surface-container-highest rounded-t relative transition-all duration-500 group-hover:bg-primary/20" style="height:55%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">55%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-secondary">P4</span>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-surface-container-highest rounded-t relative transition-all duration-500 group-hover:bg-primary/20" style="height:80%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">80%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-secondary">P5</span>
</div>
<div class="flex-1 flex flex-col items-center gap-2 lg:gap-3 z-10 group max-w-[60px] lg:max-w-none">
<div class="w-full bg-surface-container-highest rounded-t relative transition-all duration-500 group-hover:bg-primary/20" style="height:40%">
<div class="absolute -top-7 left-1/2 -translate-x-1/2 bg-on-surface text-surface text-[9px] lg:text-[10px] font-bold px-1.5 lg:px-2 py-0.5 lg:py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">40%</div>
</div>
<span class="text-[9px] lg:text-[11px] font-label-md text-secondary">P6</span>
</div>
</div>
</div>

<div class="space-y-4 lg:space-y-6">
<div class="glass-card p-4 lg:p-6 rounded-xl">
<h4 class="font-label-md text-on-surface mb-3 lg:mb-4 text-[12px]">Estado del Sistema</h4>
<div class="space-y-3 lg:space-y-4">
<div class="flex justify-between items-center">
<span class="text-body-sm text-secondary text-[13px] lg:text-[14px]">Red Principal</span>
<span class="w-2 h-2 lg:w-2.5 lg:h-2.5 rounded-full bg-tertiary-container shadow-[0_0_8px_rgba(71,87,109,0.3)]"></span>
</div>
<div class="flex justify-between items-center">
<span class="text-body-sm text-secondary text-[13px] lg:text-[14px]">Licencias Software</span>
<span class="w-2 h-2 lg:w-2.5 lg:h-2.5 rounded-full bg-tertiary-container"></span>
</div>
<div class="flex justify-between items-center">
<span class="text-body-sm text-secondary text-[13px] lg:text-[14px]">Servidor Reservas</span>
<span class="w-2 h-2 lg:w-2.5 lg:h-2.5 rounded-full bg-tertiary-container"></span>
</div>
<div class="flex justify-between items-center">
<span class="text-body-sm text-secondary text-[13px] lg:text-[14px]">API Academica</span>
<span class="w-2 h-2 lg:w-2.5 lg:h-2.5 rounded-full bg-error animate-pulse"></span>
</div>
</div>
<button class="w-full mt-4 lg:mt-6 py-2 lg:py-2.5 border border-outline-variant rounded-lg text-[10px] lg:text-[11px] font-label-md text-secondary hover:bg-surface-container-low transition-colors">Diagnostico Avanzado</button>
</div>
<div class="rounded-xl overflow-hidden relative group aspect-[4/3] lg:aspect-[4/3] border border-outline-variant">
<img alt="Smart Campus" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDxWTguqhQOs65nBC7rI14byklNlRgxwCfYxfNgXxGiUuCZRYQ6ixxMmUDQ91Kl1OVg9q5_EYGF0JMv_DSdSzQ9lAuX4WOys1TOSsEIwPeKAEjEKkO0MuB1CRaL0gw5N_1io5ETfoFqnrqkT18WiG9OF_IUcNLC_4nOBMhqNhP3eRE3-KqxaMZa3bVhR1mV81LcpftDBRZMmdxoA2mgMQjaXRD7QQuVeWmXQD1rsQdXQH5mG1oE_fzrNaBxZ7zL5LccAMpKGvDwdd4"/>
<div class="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent opacity-60"></div>
<div class="absolute bottom-3 left-3 lg:bottom-4 lg:left-4">
<span class="bg-primary text-white text-[8px] lg:text-[9px] font-bold px-1.5 lg:px-2 py-0.5 rounded uppercase tracking-widest">Live View</span>
<p class="text-white text-[12px] lg:text-sm font-semibold mt-0.5 lg:mt-1">Sede Lima Centro &bull; Lab-302</p>
</div>
</div>
</div>
</div>

<!-- Table -->
<section class="mt-8 lg:mt-12">
<div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 mb-4 lg:mb-6">
<div>
<h3 class="font-headline-md text-[18px] lg:text-[20px] text-on-surface">Gestion de Salones</h3>
<p class="font-body-sm text-secondary text-[13px]">Inventario detallado de laboratorios y aulas magnas.</p>
</div>
<div class="flex gap-2 flex-shrink-0">
<button class="p-1.5 lg:p-2 border border-outline-variant rounded bg-surface-container-lowest hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined text-[18px] lg:text-[20px] text-on-surface">filter_list</span></button>
<button class="p-1.5 lg:p-2 border border-outline-variant rounded bg-surface-container-lowest hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined text-[18px] lg:text-[20px] text-on-surface">download</span></button>
</div>
</div>
<div class="glass-card rounded-xl overflow-hidden border border-outline-variant overflow-x-auto">
<table class="w-full text-left border-collapse min-w-[640px]">
<thead class="bg-surface-container-low border-b border-outline-variant">
<tr>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Aula</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Capacidad</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Estado</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px]">Software Actual</th>
<th class="px-4 lg:px-6 py-3 lg:py-4 font-label-md text-secondary text-[11px] lg:text-[12px] text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-outline-variant">
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex items-center gap-2 lg:gap-3 min-w-0">
<div class="w-7 h-7 lg:w-8 lg:h-8 rounded bg-primary/10 flex items-center justify-center text-primary font-bold text-[10px] lg:text-xs flex-shrink-0">A-301</div>
<span class="font-bold text-[12px] lg:text-sm text-on-surface truncate">Laboratorio de Redes II</span>
</div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-body-sm text-secondary text-[12px] lg:text-[14px]">40 Estudiantes</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<span class="inline-flex items-center gap-1 px-1.5 lg:px-2 py-0.5 lg:py-1 rounded-full bg-tertiary-container/10 text-tertiary-container text-[9px] lg:text-[10px] font-bold uppercase tracking-wide whitespace-nowrap">
<span class="w-1 h-1 lg:w-1.5 lg:h-1.5 rounded-full bg-tertiary-container"></span> Activo</span>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex gap-1 flex-wrap">
<span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">Cisco Packet Tracer</span>
<span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">Wireshark</span>
</div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-right">
<div class="flex justify-end gap-1 lg:gap-2 opacity-100 lg:opacity-0 lg:group-hover:opacity-100 transition-opacity">
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">visibility</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">edit</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">more_vert</span></button>
</div>
</td>
</tr>
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex items-center gap-2 lg:gap-3 min-w-0">
<div class="w-7 h-7 lg:w-8 lg:h-8 rounded bg-surface-variant flex items-center justify-center text-on-surface-variant font-bold text-[10px] lg:text-xs flex-shrink-0">B-104</div>
<span class="font-bold text-[12px] lg:text-sm text-on-surface truncate">Aula Magna Innovacion</span>
</div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-body-sm text-secondary text-[12px] lg:text-[14px]">120 Estudiantes</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<span class="inline-flex items-center gap-1 px-1.5 lg:px-2 py-0.5 lg:py-1 rounded-full bg-error/10 text-error text-[9px] lg:text-[10px] font-bold uppercase tracking-wide whitespace-nowrap">
<span class="w-1 h-1 lg:w-1.5 lg:h-1.5 rounded-full bg-error"></span> Mantenimiento</span>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex gap-1 flex-wrap"><span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">Multimedia Suite</span></div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-right">
<div class="flex justify-end gap-1 lg:gap-2 opacity-100 lg:opacity-0 lg:group-hover:opacity-100 transition-opacity">
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">visibility</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">edit</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">more_vert</span></button>
</div>
</td>
</tr>
<tr class="hover:bg-surface-container-low transition-colors group">
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex items-center gap-2 lg:gap-3 min-w-0">
<div class="w-7 h-7 lg:w-8 lg:h-8 rounded bg-primary/10 flex items-center justify-center text-primary font-bold text-[10px] lg:text-xs flex-shrink-0">C-502</div>
<span class="font-bold text-[12px] lg:text-sm text-on-surface truncate">Laboratorio de IA y Datos</span>
</div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-body-sm text-secondary text-[12px] lg:text-[14px]">32 Estudiantes</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<span class="inline-flex items-center gap-1 px-1.5 lg:px-2 py-0.5 lg:py-1 rounded-full bg-tertiary-container/10 text-tertiary-container text-[9px] lg:text-[10px] font-bold uppercase tracking-wide whitespace-nowrap">
<span class="w-1 h-1 lg:w-1.5 lg:h-1.5 rounded-full bg-tertiary-container"></span> Activo</span>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4">
<div class="flex gap-1 flex-wrap">
<span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">Python 3.11</span>
<span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">Docker</span>
<span class="px-1.5 lg:px-2 py-0.5 rounded bg-surface-container-highest text-[9px] lg:text-[10px] text-on-surface whitespace-nowrap">K8s</span>
</div>
</td>
<td class="px-4 lg:px-6 py-3 lg:py-4 text-right">
<div class="flex justify-end gap-1 lg:gap-2 opacity-100 lg:opacity-0 lg:group-hover:opacity-100 transition-opacity">
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">visibility</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-primary transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">edit</span></button>
<button class="p-1 lg:p-1.5 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[16px] lg:text-[18px]">more_vert</span></button>
</div>
</td>
</tr>
</tbody>
</table>
<div class="px-4 lg:px-6 py-3 lg:py-4 bg-surface-container-low flex flex-col sm:flex-row items-center justify-between gap-2 border-t border-outline-variant">
<span class="text-[10px] lg:text-[11px] text-secondary">Mostrando 3 de 142 laboratorios</span>
<div class="flex gap-2">
<button class="px-2.5 lg:px-3 py-1 lg:py-1.5 text-[10px] lg:text-[11px] font-bold text-on-surface border border-outline-variant rounded bg-surface-container-lowest hover:bg-surface-container-low disabled:opacity-30" disabled>Anterior</button>
<button class="px-2.5 lg:px-3 py-1 lg:py-1.5 text-[10px] lg:text-[11px] font-bold text-on-surface border border-outline-variant rounded bg-surface-container-lowest hover:bg-surface-container-low">Siguiente</button>
</div>
</div>
</div>
</section>

<footer class="mt-16 lg:mt-24 pb-8 lg:pb-12 border-t border-outline-variant pt-6 lg:pt-8 flex flex-col md:flex-row justify-between items-center gap-4 lg:gap-6">
<div class="flex items-center gap-3 lg:gap-4">
<div class="w-7 h-7 lg:w-8 lg:h-8 rounded-full bg-primary/10 flex items-center justify-center text-primary font-bold text-[9px] lg:text-[10px]">UTP</div>
<p class="text-[10px] lg:text-[11px] text-secondary tracking-wide">&copy; 2024 Universidad Tecnologica del Peru. All rights reserved.</p>
</div>
<div class="flex gap-4 lg:gap-8 text-[10px] lg:text-[11px] font-label-md text-secondary">
<a class="hover:text-primary transition-colors" href="#">Terminos de Servicio</a>
<a class="hover:text-primary transition-colors" href="#">Politica de Privacidad</a>
<a class="hover:text-primary transition-colors" href="#">Soporte TI</a>
</div>
</footer>
</div>
</main>
</div>

<div class="fixed inset-0 pointer-events-none -z-10 overflow-hidden">
<div class="absolute -top-[20%] -right-[10%] w-[60%] h-[60%] bg-primary/5 rounded-full blur-[120px]"></div>
<div class="absolute -bottom-[10%] -left-[5%] w-[40%] h-[40%] bg-secondary/5 rounded-full blur-[100px]"></div>
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

document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('h3[data-count]');
  counters.forEach(counter => {
    const target = parseInt(counter.getAttribute('data-count'));
    if (isNaN(target)) return;
    let count = 0;
    const updateCount = () => {
      const increment = target / 40;
      if (count < target) { count += increment; counter.innerText = Math.ceil(count); setTimeout(updateCount, 15); }
      else { counter.innerText = target; }
    };
    updateCount();
  });
});
</script>
</body></html>
"""
