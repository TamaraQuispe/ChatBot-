HTML_CHAT = """
<!DOCTYPE html>
<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&amp;family=Libre+Franklin:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=block" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
try{
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "primary": "#840015",
                        "utp-red-vibrant": "#bc1127",
                        "utp-red-institutional": "#B00020",
                        "text-primary": "#191c1d",
                        "text-secondary": "#5b403e",
                        "surface": "#f8f9fa",
                        "background": "#ffffff",
                        "error": "#ba1a1a"
                    },
                    "borderRadius": {
                        "DEFAULT": "0.5rem",
                        "lg": "0.75rem",
                        "xl": "1rem",
                        "2xl": "1.5rem",
                        "3xl": "2rem",
                        "full": "9999px"
                    },
                    "fontFamily": {
                        "headline-lg": ["Libre Franklin", "sans-serif"],
                        "body-md": ["Libre Franklin", "sans-serif"],
                        "label-md": ["Libre Franklin", "sans-serif"]
                    }
                },
            },
        }
    }catch(_e){}</script>
<style>
  body { font-family: 'Libre Franklin', sans-serif; background: #f8f9fa; }
  .scrollbar-hide::-webkit-scrollbar { display: none; }
  .message-in { animation: slideIn 0.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
  @keyframes slideIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
  .glass-dark { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(0, 0, 0, 0.04); }
  .glass { background: rgba(255, 255, 255, 0.6); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); }
</style>
</head>
<body class="overflow-hidden min-h-screen">

<!-- Mobile Overlay -->
<div id="sidebarOverlay" class="fixed inset-0 bg-black/40 z-30 hidden md:hidden transition-opacity duration-300" onclick="toggleSidebar()"></div>

<!-- Sidebar -->
<aside id="sidebar" class="fixed left-0 top-0 h-screen w-[260px] border-r border-black/5 bg-white/30 backdrop-blur-xl flex flex-col z-50 transform -translate-x-full md:translate-x-0 transition-transform duration-300 ease-in-out">
    <div class="px-8 py-10">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-utp-red-institutional rounded-xl flex items-center justify-center shadow-lg shadow-utp-red-institutional/20">
                <span class="text-white font-bold text-xl">U</span>
            </div>
            <div>
                <h1 class="font-headline-lg text-[18px] font-bold text-utp-red-institutional leading-tight tracking-tight">Asistente</h1>
                <p class="font-label-md text-[10px] text-text-secondary uppercase tracking-widest font-semibold">UTP PERU</p>
            </div>
        </div>
    </div>

    <nav class="flex-1 px-4 space-y-1">
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#">
            <span class="material-symbols-outlined" data-icon="chat">chat</span>
            <span class="font-body-md font-medium">Chat Actual</span>
        </a>
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#">
            <span class="material-symbols-outlined" data-icon="history">history</span>
            <span class="font-body-md font-medium">Historial</span>
        </a>
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#">
            <span class="material-symbols-outlined" data-icon="explore">explore</span>
            <span class="font-body-md font-medium">Explorar</span>
        </a>
    </nav>

    <div class="px-4 pb-10 space-y-1">
        <div class="h-px bg-black/5 mx-4 mb-4"></div>
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-text-secondary hover:bg-black/5 hover:text-text-primary transition-all duration-200" href="#">
            <span class="material-symbols-outlined" data-icon="settings">settings</span>
            <span class="font-body-md font-medium">Configuracion</span>
        </a>
        <a class="flex items-center gap-4 px-4 py-3 rounded-2xl text-error/80 hover:bg-error/5 transition-all duration-200" href="/logout">
            <span class="material-symbols-outlined" data-icon="logout">logout</span>
            <span class="font-body-md font-medium">Cerrar Sesion</span>
        </a>
    </div>
</aside>

<!-- Main Content -->
<main class="ml-0 md:ml-[260px] w-full md:w-[calc(100%-260px)] h-screen flex flex-col relative overflow-hidden">
    <!-- Header -->
    <header class="h-20 flex justify-between items-center px-4 md:px-10 z-40 bg-white/10">
        <div class="flex items-center gap-4 md:gap-6 flex-1">
            <button onclick="toggleSidebar()" class="md:hidden p-2 text-text-secondary hover:text-utp-red-institutional transition-colors">
                <span class="material-symbols-outlined">menu</span>
            </button>
            <div class="flex-1 max-w-lg">
                <div class="relative group">
                    <span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-text-secondary/60 text-[20px]">search</span>
                    <input class="w-full bg-white/40 border border-white/60 rounded-2xl py-2.5 pl-12 pr-4 text-sm focus:ring-2 focus:ring-utp-red-institutional/10 focus:bg-white/80 outline-none transition-all placeholder:text-text-secondary/40 shadow-sm" placeholder="Buscar en la conversacion..." type="text"/>
                </div>
            </div>
        </div>

        <div class="flex items-center gap-6">
            <button class="w-10 h-10 flex items-center justify-center text-text-secondary hover:bg-black/5 rounded-full transition-colors relative">
                <span class="material-symbols-outlined">notifications</span>
                <span class="absolute top-2.5 right-2.5 w-2 h-2 bg-utp-red-institutional rounded-full ring-2 ring-white"></span>
            </button>
            <div class="flex items-center gap-4 pl-6 border-l border-black/5">
                <div class="text-right hidden sm:block">
                    <p class="font-bold text-sm text-text-primary">$NOMBRE_DOCENTE</p>
                    <p class="text-[10px] text-text-secondary font-bold uppercase tracking-wider">DOCENTE PRINCIPAL</p>
                </div>
                <div class="w-10 h-10 rounded-full border-2 border-white shadow-sm bg-utp-red-institutional flex items-center justify-center text-white font-bold text-sm">U</div>
            </div>
        </div>
    </header>

    <!-- Chat Space -->
    <div class="flex-1 flex overflow-hidden">
        <section class="flex-1 flex flex-col relative overflow-y-auto scrollbar-hide w-full">
            <div class="max-w-4xl mx-auto w-full px-12 pt-12 pb-48 space-y-12" id="chat-messages">

                $HISTORIAL_CHAT

            </div>
        </section>
    </div>

    <!-- Floating Input Area -->
    <div class="absolute bottom-0 left-0 w-full px-8 pb-8 pt-12 bg-gradient-to-t from-background via-background/80 to-transparent pointer-events-none">
        <div class="max-w-3xl mx-auto w-full pointer-events-auto">
            <form method="POST" action="/query" class="glass pl-6 pr-2.5 py-2.5 rounded-[28px] flex items-center gap-3 border border-white shadow-[0_10px_40px_rgba(0,0,0,0.06)] focus-within:shadow-[0_15px_50px_rgba(0,0,0,0.1)] focus-within:ring-2 focus-within:ring-utp-red-institutional/5 transition-all bg-white/60 backdrop-blur-2xl">
                <button class="w-10 h-10 flex items-center justify-center text-text-secondary/60 hover:text-utp-red-institutional transition-colors rounded-full hover:bg-black/5" type="button">
                    <span class="material-symbols-outlined">add</span>
                </button>
                <input class="flex-1 bg-transparent border-none focus:ring-0 text-text-primary text-[16px] placeholder:text-text-secondary/30 py-2.5" name="prompt" placeholder="Escribe tu consulta academica..." type="text"/>
                <div class="flex items-center gap-1.5">
                    <button class="w-10 h-10 flex items-center justify-center text-text-secondary/60 hover:text-utp-red-institutional transition-colors rounded-full hover:bg-black/5" type="button">
                        <span class="material-symbols-outlined">mic</span>
                    </button>
                    <button class="w-12 h-12 bg-utp-red-institutional text-white rounded-full flex items-center justify-center shadow-lg shadow-utp-red-institutional/30 hover:scale-105 active:scale-95 transition-all group" type="submit">
                        <span class="material-symbols-outlined group-hover:translate-x-0.5 transition-transform" style="font-variation-settings: 'FILL' 1;">send</span>
                    </button>
                </div>
            </form>
            <p class="text-center text-[10px] text-text-secondary/40 mt-5 font-bold uppercase tracking-[0.25em]">
                Inteligencia Artificial UTP &bull; Modelo Optimizado v2.4
            </p>
        </div>
    </div>
</main>

<script>
    const chatInput = document.querySelector('input[name="prompt"]');
    if(chatInput) {
        chatInput.addEventListener('focus', () => {
            chatInput.closest('form').classList.add('shadow-[0_15px_50px_rgba(0,0,0,0.1)]');
        });
        chatInput.addEventListener('blur', () => {
            chatInput.closest('form').classList.remove('shadow-[0_15px_50px_rgba(0,0,0,0.1)]');
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
