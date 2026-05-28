HTML_CHAT = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Asistente Academico UTP - Chat Docente</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Libre+Franklin:wght@400;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "tertiary-fixed-dim": "#b7c8e1","inverse-primary": "#ffb3af","on-secondary": "#ffffff","on-surface-variant": "#5b403e","surface-tint": "#bc1127","primary-container": "#b00020","secondary": "#5f5e5e","surface-container-low": "#f3f4f5","on-primary": "#ffffff","on-surface": "#191c1d","outline": "#906f6d","primary-fixed-dim": "#ffb3af","inverse-on-surface": "#f0f1f2","surface-container": "#edeeef","inverse-surface": "#2e3132","on-secondary-fixed-variant": "#474746","surface-container-lowest": "#ffffff","surface-container-high": "#e7e8e9","on-tertiary-fixed": "#0b1c30","primary": "#840015","surface": "#f8f9fa","on-primary-container": "#ffbbb8","tertiary": "#304055","surface-container-highest": "#e1e3e4","error-container": "#ffdad6","outline-variant": "#e4bdbb","secondary-fixed-dim": "#c8c6c5","background": "#f8f9fa","surface-dim": "#d9dadb","error": "#ba1a1a","secondary-container": "#e2dfde","on-error-container": "#93000a","surface-bright": "#f8f9fa","on-primary-fixed": "#410006","surface-variant": "#e1e3e4","primary-fixed": "#ffdad8","on-error": "#ffffff","on-tertiary-fixed-variant": "#38485d","tertiary-container": "#47576d","on-secondary-fixed": "#1c1b1b","on-secondary-container": "#636262","secondary-fixed": "#e5e2e1","tertiary-fixed": "#d3e4fe","on-tertiary": "#ffffff","on-primary-fixed-variant": "#930019","on-tertiary-container": "#bccde6","on-background": "#191c1d",
        "utp-red-vibrant": "#bc1127","utp-red-muted": "#840015","text-primary": "#191c1d","text-secondary": "#5b403e","border-subtle": "#e1e3e4"
      },
      borderRadius: { DEFAULT: "0.5rem", lg: "0.75rem", xl: "1rem", full: "9999px" },
      spacing: { xs: "4px", gutter: "24px", "margin-mobile": "16px", "margin-desktop": "40px", sm: "12px", xl: "80px", base: "8px", lg: "48px", md: "24px" },
      fontFamily: { "headline-lg-mobile": ["Libre Franklin"], "headline-lg": ["Libre Franklin"], "label-md": ["Libre Franklin"], "body-sm": ["Libre Franklin"], "headline-md": ["Libre Franklin"], "display-lg": ["Libre Franklin"], "body-lg": ["Libre Franklin"], "body-md": ["Libre Franklin"] },
      fontSize: {
        "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "600"}],
        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
        "label-md": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
      }
    }
  }
}
</script>
<style>
body {
    background: radial-gradient(60% 50% at 30% 40%, #ffecee 0%, #f0f4f9 60%, #e8edf5 100%);
    color: #191c1d;
    font-family: 'Libre Franklin', sans-serif;
}
.material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
.glass { background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(255, 255, 255, 0.4); }
.scrollbar-hide::-webkit-scrollbar { display: none; }
.message-in { animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
@keyframes slideIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.gemini-bg { background: radial-gradient(circle at 70% 20%, rgba(188, 17, 39, 0.08) 0%, transparent 50%), radial-gradient(circle at 20% 80%, rgba(71, 87, 109, 0.06) 0%, transparent 40%); }
</style>
</head>
<body class="overflow-hidden">
<div id="sidebar-overlay" class="fixed inset-0 bg-black/30 z-30 hidden lg:hidden transition-opacity" onclick="toggleSidebar()"></div>

<aside id="sidebar" class="fixed left-0 top-0 h-screen w-[240px] -translate-x-full lg:translate-x-0 transition-transform duration-300 ease-in-out z-40 border-r border-border-subtle bg-surface-container-lowest flex flex-col py-6 lg:py-8 shadow-lg lg:shadow-none">
<div class="px-5 lg:px-6 mb-6 lg:mb-10 flex items-center justify-between">
<div class="flex items-center gap-3">
<div class="w-9 h-9 lg:w-10 lg:h-10 bg-utp-red-vibrant rounded-lg flex items-center justify-center shadow-md">
<span class="text-white font-bold text-lg lg:text-xl">U</span>
</div>
<div>
<h1 class="font-headline-lg text-[16px] lg:text-[18px] font-bold text-utp-red-vibrant leading-tight">Asistente</h1>
<p class="font-label-md text-[9px] lg:text-[10px] text-text-secondary">UTP PERU</p>
</div>
</div>
<button onclick="toggleSidebar()" class="lg:hidden text-text-secondary hover:text-utp-red-vibrant p-1">
<span class="material-symbols-outlined">close</span>
</button>
</div>
<nav class="flex-1 space-y-1">
<a class="flex items-center gap-3 px-4 lg:px-4 py-2.5 lg:py-3 text-text-secondary hover:bg-surface-container-low transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="history">history</span>
<span class="font-body-md text-body-md">Historial</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-4 py-2.5 lg:py-3 text-text-secondary hover:bg-surface-container-low transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="search">search</span>
<span class="font-body-md text-body-md">Buscar historial</span>
</a>
</nav>
<div class="px-4 lg:px-4 mt-auto space-y-1">
<a class="flex items-center gap-3 px-4 lg:px-4 py-2.5 lg:py-3 text-text-secondary hover:bg-surface-container-low transition-all duration-200" href="#">
<span class="material-symbols-outlined text-[20px]" data-icon="settings">settings</span>
<span class="font-body-md text-body-md">Configuracion</span>
</a>
<a class="flex items-center gap-3 px-4 lg:px-4 py-2.5 lg:py-3 text-text-secondary hover:bg-surface-container-low transition-all duration-200" href="/logout">
<span class="material-symbols-outlined text-[20px]" data-icon="logout">logout</span>
<span class="font-body-md text-body-md">Cerrar Sesion</span>
</a>
</div>
</aside>

<main class="ml-0 lg:ml-[240px] h-screen flex flex-col relative gemini-bg">
<header class="h-14 lg:h-16 flex justify-between lg:justify-end items-center px-3 md:px-6 lg:px-8 border-b border-border-subtle bg-surface/80 backdrop-blur-[20px] z-30">
<div class="flex items-center gap-3 lg:hidden">
<button onclick="toggleSidebar()" class="p-2 -ml-1 text-text-secondary hover:text-utp-red-vibrant rounded-lg hover:bg-surface-container-low transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<p class="font-headline-md text-[14px] text-text-primary truncate">$NOMBRE_DOCENTE</p>
</div>
<div class="flex items-center gap-4 lg:gap-6">
<button class="relative text-text-secondary hover:text-utp-red-vibrant transition-colors">
<span class="material-symbols-outlined text-[20px] lg:text-[24px]" data-icon="notifications">notifications</span>
<span class="absolute top-0.5 right-0.5 w-1.5 h-1.5 lg:w-2 lg:h-2 bg-utp-red-vibrant rounded-full border-2 border-surface"></span>
</button>
<div class="hidden lg:flex items-center gap-3 pl-6 border-l border-border-subtle">
<div class="text-right">
<p class="font-headline-md text-[14px] text-text-primary">$NOMBRE_DOCENTE</p>
<p class="font-label-md text-[10px] text-text-secondary uppercase">DOCENTE PRINCIPAL</p>
</div>
</div>
</div>
</header>

<div class="flex-1 flex overflow-hidden">
<section class="flex-1 flex flex-col bg-background relative">
<div class="flex-1 overflow-y-auto scrollbar-hide">
<div class="max-w-4xl mx-auto w-full px-4 md:px-8 py-6 lg:py-12 space-y-6 lg:space-y-8" id="chat-messages">

$HISTORIAL_CHAT

</div>
</div>
<div class="w-full p-4 md:p-8 bg-gradient-to-t from-background via-background/90 to-transparent">
<div class="max-w-4xl mx-auto w-full px-0 md:px-8">
<form method="POST" action="/query" class="glass p-1.5 lg:p-2 pl-4 lg:pl-6 pr-1.5 lg:pr-2 rounded-2xl flex items-center gap-2 lg:gap-4 border border-border-subtle shadow-xl focus-within:ring-2 focus-within:ring-utp-red-vibrant/10 transition-all">
<input class="flex-1 bg-transparent border-none focus:ring-0 text-text-primary text-body-sm lg:text-body-md placeholder:text-text-secondary/50 py-3 lg:py-4" name="prompt" placeholder="Escribe tu consulta academica..." type="text"/>
<button class="w-10 h-10 lg:w-12 lg:h-12 rounded-xl bg-utp-red-vibrant text-white flex items-center justify-center hover:scale-105 active:scale-95 transition-all shadow-md" type="submit">
<span class="material-symbols-outlined text-[18px] lg:text-[24px]" data-icon="send">send</span>
</button>
</form>
<p class="text-center text-[9px] lg:text-[10px] text-text-secondary mt-2 lg:mt-3 font-label-md uppercase tracking-widest">IA ACADEMICA UTP &bull; VERIFICA SIEMPRE LA DISPONIBILIDAD FINAL.</p>
</div>
</div>
</section>
</main>
<script>
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebar-overlay');
  const isOpen = sidebar.classList.contains('translate-x-0');
  sidebar.classList.toggle('-translate-x-full', isOpen);
  sidebar.classList.toggle('translate-x-0', !isOpen);
  overlay.classList.toggle('hidden', isOpen);
}
const chatInput = document.querySelector('input[name="prompt"]');
if(chatInput) {
    chatInput.addEventListener('focus', () => {
        chatInput.parentElement.classList.add('shadow-utp-red-vibrant/10');
    });
    chatInput.addEventListener('blur', () => {
        chatInput.parentElement.classList.remove('shadow-utp-red-vibrant/10');
    });
}
</script>
</body></html>
"""
