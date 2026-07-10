HEADER_HTML = """
<!-- TopNavBar -->
<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-40 bg-white/70 backdrop-blur-md border-b border-surface-container-highest">
<div class="flex justify-between items-center h-14 sm:h-16 px-3 sm:px-container-padding">
<div class="flex items-center space-x-4 md:space-x-8">
<button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
<div class="relative">
<span class="material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-secondary">search</span>
<input class="pl-10 pr-4 py-2 bg-surface border-none rounded-full text-label-md w-36 sm:w-64 focus:ring-1 focus:ring-primary" placeholder="$SEARCH_PLACEHOLDER" type="text"/>
</div>
<nav class="hidden md:flex space-x-6">
<a class="text-primary font-semibold border-b-2 border-primary pb-1 font-label-md text-label-md" href="#">Hoy</a>
<a class="text-on-surface-variant hover:text-on-surface font-label-md text-label-md transition-all" href="#">Calendario</a>
<a class="text-on-surface-variant hover:text-on-surface font-label-md text-label-md transition-all" href="#">Directorio</a>
</nav>
</div>
<div class="flex items-center space-x-2 sm:space-x-4">
<button class="p-2 text-secondary hover:text-primary transition-transform active:scale-95">
<span class="material-symbols-outlined">notifications</span>
</button>
<button class="p-2 text-secondary hover:text-primary transition-transform active:scale-95">
<span class="material-symbols-outlined">apps</span>
</button>
<button class="bg-primary text-on-primary px-3 sm:px-5 py-2 rounded-lg font-label-md text-label-md font-bold transition-all hover:opacity-90 active:scale-95 whitespace-nowrap">
<span class="hidden sm:inline">Nueva Reserva</span>
<span class="sm:hidden material-symbols-outlined text-[20px]">add</span>
</button>
<div class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm shrink-0">$AVATAR_LETTER</div>
</div>
</div>
</header>
"""
