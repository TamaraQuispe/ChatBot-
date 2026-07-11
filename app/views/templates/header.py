"""Header template for admin pages."""
HEADER_HTML = """
<!-- TopNavBar -->
<header class="fixed top-0 right-0 w-full md:w-[calc(100%-16rem)] z-40 bg-white/70 backdrop-blur-md border-b border-surface-container-highest">
<div class="flex justify-between items-center h-14 sm:h-16 px-3 sm:px-container-padding">
<div class="flex items-center space-x-4 md:space-x-8">
<button onclick="toggleSidebar()" class="md:hidden p-2 text-secondary hover:text-primary transition-colors">
<span class="material-symbols-outlined">menu</span>
</button>
</div>
<div class="flex items-center space-x-2 sm:space-x-4">
<button class="p-2 text-secondary hover:text-primary transition-transform active:scale-95">
<span class="material-symbols-outlined">notifications</span>
</button>
</div>
</div>
</header>
"""
