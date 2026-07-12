"""Reservas page template."""
from app.views.page import render_reservas

_CONTENT = """<section class="mb-10 flex justify-between items-end">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Gestion de Reservas</h1>
<div class="flex items-center gap-4 mt-1">
<div class="flex items-center text-label-md text-secondary">
<span class="w-2 h-2 rounded-full bg-emerald-500 inline-block mr-1.5"></span>
Sistema Operativo
</div>
<span class="text-surface-container-highest">|</span>
<span class="text-body-md text-secondary">24 Solicitudes pendientes de revision</span>
</div>
</div>
</section>
<div class="grid grid-cols-12 gap-gutter">
<div class="col-span-12 lg:col-span-8 space-y-stack-lg">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-center mb-6">
<h3 class="font-title-lg text-title-lg">Solicitudes Recientes</h3>
<div class="flex bg-surface-container-low p-1 rounded-lg">
<button class="px-4 py-1 text-label-md bg-white shadow-sm rounded-md font-semibold">Pendientes</button>
<button class="px-4 py-1 text-label-md text-secondary hover:text-on-surface">Historial</button>
</div>
</div>
<div class="overflow-x-auto">
<table class="w-full text-left">
<thead>
<tr class="border-b border-surface-container-highest text-label-md text-secondary uppercase tracking-wider">
<th class="pb-4 font-medium">Solicitante</th>
<th class="pb-4 font-medium">Espacio / Aula</th>
<th class="pb-4 font-medium">Fecha y Hora</th>
<th class="pb-4 font-medium">Estado</th>
<th class="pb-4 font-medium text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_RESERVAS
</tbody>
</table>
</div>
</div>
<div class="grid grid-cols-1 sm:grid-cols-2 gap-gutter">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start mb-2">
<span class="text-label-md text-secondary font-medium">Tasa de Ocupacion</span>
<span class="text-emerald-600 font-bold text-xs">+12.5%</span>
</div>
<div class="text-headline-md font-headline-md">78.4%</div>
<div class="h-8 mt-4 flex items-end gap-1">
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-1/2"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-3/4"></div>
<div class="flex-1 bg-primary rounded-t-sm h-full"></div>
<div class="flex-1 bg-primary rounded-t-sm h-2/3"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-4/5"></div>
<div class="flex-1 bg-surface-container-highest rounded-t-sm h-1/2"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start mb-2">
<span class="text-label-md text-secondary font-medium">Promedio Respuesta</span>
<span class="text-amber-500 font-bold text-xs">-2m</span>
</div>
<div class="text-headline-md font-headline-md">14.2 min</div>
<div class="h-8 mt-4 flex items-center justify-center">
<div class="w-full h-1 bg-surface-container-highest rounded-full relative overflow-hidden">
<div class="absolute left-0 top-0 h-full w-[65%] bg-primary"></div>
</div>
</div>
</div>
</div>
</div>
</div>"""

HTML_RESERVAS = render_reservas(_CONTENT)
