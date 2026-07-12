"""Reportes page template."""
from app.views.page import render_reportes

_CONTENT = """<section class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-stack-lg">
<div>
<h1 class="font-headline-lg text-headline-lg text-on-surface">Panel de Analitica Avanzada</h1>
<p class="text-body-md text-secondary mt-1">Monitoreo en tiempo real del rendimiento institucional</p>
</div>
<div class="flex items-center gap-3">
<div class="flex items-center bg-white border border-surface-container-highest rounded-lg px-3 py-1.5 shadow-sm">
<span class="material-symbols-outlined text-[18px] text-secondary mr-2">calendar_today</span>
<select class="border-none bg-transparent font-label-md text-label-md focus:ring-0 p-0 pr-8">
<option>Ultimos 30 dias</option>
<option>Semestre Actual</option>
<option>Ano 2024</option>
<option>Personalizado</option>
</select>
</div>
<button class="bg-white border border-surface-container-highest text-on-surface font-label-md px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-surface-container-low transition-all shadow-sm">
<span class="material-symbols-outlined text-[18px]">picture_as_pdf</span> PDF
</button>
<button class="bg-white border border-surface-container-highest text-on-surface font-label-md px-4 py-2 rounded-lg flex items-center gap-2 hover:bg-surface-container-low transition-all shadow-sm">
<span class="material-symbols-outlined text-[18px]">table_chart</span> XLSX
</button>
</div>
</section>
<section class="grid grid-cols-1 md:grid-cols-4 gap-gutter mb-stack-lg">
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Ocupacion Promedio</span>
<span class="flex items-center text-emerald-600 text-label-md font-bold"><span class="material-symbols-outlined text-[14px]">trending_up</span> 12%</span>
</div>
<div class="text-display-lg font-display-lg mt-2">84.2%</div>
<div class="mt-4 h-12 w-full flex items-end gap-1">
<div class="flex-1 bg-surface-container-highest h-4 rounded-t-sm"></div>
<div class="flex-1 bg-surface-container-highest h-6 rounded-t-sm"></div>
<div class="flex-1 bg-primary h-10 rounded-t-sm"></div>
<div class="flex-1 bg-surface-container-highest h-8 rounded-t-sm"></div>
<div class="flex-1 bg-primary h-12 rounded-t-sm"></div>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Software Activo</span>
<span class="flex items-center text-on-surface-variant text-label-md">Estable</span>
</div>
<div class="text-display-lg font-display-lg mt-2">1,204</div>
<div class="mt-4 flex items-center gap-2">
<div class="flex -space-x-2"><div class="w-6 h-6 rounded-full bg-blue-100 border-2 border-white"></div><div class="w-6 h-6 rounded-full bg-red-100 border-2 border-white"></div><div class="w-6 h-6 rounded-full bg-gray-100 border-2 border-white"></div></div>
<span class="text-label-md text-secondary">+12 herramientas</span>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl shadow-sm">
<div class="flex justify-between items-start">
<span class="text-label-md text-secondary uppercase tracking-wider">Rendimiento Acad.</span>
<span class="flex items-center text-primary text-label-md font-bold"><span class="material-symbols-outlined text-[14px]">trending_down</span> 2.4%</span>
</div>
<div class="text-display-lg font-display-lg mt-2">4.12</div>
<div class="mt-4">
<div class="w-full bg-surface-container-highest h-1.5 rounded-full overflow-hidden"><div class="bg-primary h-full w-[82%]"></div></div>
<p class="text-[10px] mt-1 text-secondary">Promedio General Institucional</p>
</div>
</div>
<div class="glass-panel p-6 rounded-2xl bg-inverse-surface border-none shadow-xl">
<div class="text-on-primary-fixed">
<span class="text-label-md opacity-70 uppercase tracking-wider">Estado del Sistema</span>
<div class="flex items-center gap-2 mt-2"><div class="w-2.5 h-2.5 bg-emerald-500 rounded-full animate-pulse"></div><span class="font-title-lg text-title-lg text-white">100% Operativo</span></div>
</div>
<button class="mt-6 w-full py-2 bg-white/10 hover:bg-white/20 text-white rounded-lg text-label-md transition-all border border-white/20">Ver Logs Tecnicos</button>
</div>
</section>
<section class="grid grid-cols-1 lg:grid-cols-3 gap-gutter mb-section-gap">
<div class="lg:col-span-2 glass-panel p-8 rounded-2xl shadow-sm">
<div class="flex justify-between items-center mb-8">
<h3 class="font-title-lg text-title-lg">Tendencias de Ocupacion por Edificio</h3>
<div class="flex gap-4">
<label class="flex items-center gap-2 cursor-pointer"><div class="w-3 h-3 rounded-full bg-primary"></div><span class="text-label-md text-secondary">Edificio A</span></label>
<label class="flex items-center gap-2 cursor-pointer"><div class="w-3 h-3 rounded-full bg-secondary"></div><span class="text-label-md text-secondary">Laboratorios</span></label>
</div>
</div>
<div class="relative h-64 w-full flex items-end justify-between px-4 pb-4 border-b border-surface-container-highest">
<div class="absolute inset-0 flex flex-col justify-between pointer-events-none opacity-50">
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
<div class="border-t border-dashed border-surface-container-highest w-full h-px"></div>
</div>
<div class="absolute inset-0 top-12">
<svg class="w-full h-full" preserveaspectratio="none" viewbox="0 0 100 100"><path d="M0,80 Q20,30 40,50 T80,10 T100,40" fill="none" stroke="#B00020" stroke-width="2" vector-effect="non-scaling-stroke"></path><path d="M0,90 Q25,70 50,85 T90,60 T100,70" fill="none" stroke="#585f64" stroke-dasharray="4" stroke-width="1.5" vector-effect="non-scaling-stroke"></path></svg>
</div>
<div class="text-[10px] text-secondary">Lun</div>
<div class="text-[10px] text-secondary">Mar</div>
<div class="text-[10px] text-secondary">Mie</div>
<div class="text-[10px] text-secondary">Jue</div>
<div class="text-[10px] text-secondary">Vie</div>
<div class="text-[10px] text-secondary">Sab</div>
<div class="text-[10px] text-secondary">Dom</div>
</div>
<div class="mt-6 flex justify-around">
<div class="text-center"><p class="text-label-md text-secondary">Pico Maximo</p><p class="font-title-lg text-title-lg">98% (Jue)</p></div>
<div class="text-center"><p class="text-label-md text-secondary">Tasa de Desercion</p><p class="font-title-lg text-title-lg">4.2%</p></div>
<div class="text-center"><p class="text-label-md text-secondary">Uso Promedio</p><p class="font-title-lg text-title-lg">6.5 hrs/dia</p></div>
</div>
</div>
<div class="glass-panel p-8 rounded-2xl shadow-sm">
<h3 class="font-title-lg text-title-lg mb-6">Uso de Software Academico</h3>
<div class="space-y-6">
<div class="space-y-2"><div class="flex justify-between items-center text-body-md"><span class="font-medium">MATLAB Advanced</span><span class="text-secondary">820 licencias</span></div><div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden"><div class="bg-primary h-full w-[85%]"></div></div></div>
<div class="space-y-2"><div class="flex justify-between items-center text-body-md"><span class="font-medium">AutoCAD 2024</span><span class="text-secondary">645 licencias</span></div><div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden"><div class="bg-primary h-full w-[65%]"></div></div></div>
<div class="space-y-2"><div class="flex justify-between items-center text-body-md"><span class="font-medium">Wolfram Alpha Pro</span><span class="text-secondary">310 licencias</span></div><div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden"><div class="bg-secondary h-full w-[40%]"></div></div></div>
<div class="space-y-2"><div class="flex justify-between items-center text-body-md"><span class="font-medium">IBM SPSS Statistics</span><span class="text-secondary">112 licencias</span></div><div class="w-full bg-surface-container-low h-2 rounded-full overflow-hidden"><div class="bg-secondary h-full w-[22%]"></div></div></div>
</div>
<div class="mt-8 p-4 bg-surface-container-low rounded-xl border border-surface-container-highest"><p class="text-label-md text-secondary italic">"Recomendacion: Incrementar licencias de MATLAB para el proximo trimestre basado en proyeccion de uso."</p></div>
</div>
</section>
<section class="mb-section-gap">
<div class="flex justify-between items-end mb-stack-lg">
<div>
<h3 class="font-headline-md text-headline-md">Metricas de Facultad</h3>
<p class="text-body-md text-secondary">Evaluacion integral por departamentos y decanos</p>
</div>
<button class="text-primary font-label-md flex items-center gap-1 hover:underline">Ver todas las facultades<span class="material-symbols-outlined text-[16px]">chevron_right</span></button>
</div>
<div class="glass-panel rounded-2xl shadow-sm overflow-x-auto">
<table class="w-full text-left border-collapse">
<thead>
<tr class="bg-surface-container-low border-b border-surface-container-highest">
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Facultad</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Tasa Retencion</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Publicaciones Q1</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider">Tendencia Trim.</th>
<th class="p-4 font-label-md text-label-md text-secondary uppercase tracking-wider text-right">Acciones</th>
</tr>
</thead>
<tbody class="divide-y divide-surface-container-highest">
$TABLA_FACULTADES
</tbody>
</table>
</div>
</section>"""

_JS = """
document.addEventListener('DOMContentLoaded', () => {
    const progressBars = document.querySelectorAll('.bg-primary.h-full, .bg-secondary.h-full');
    progressBars.forEach(bar => {
        const finalWidth = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => { bar.style.width = finalWidth; }, 300);
    });
});
"""

HTML_REPORTES = render_reportes(
    _CONTENT,
    extra_js=_JS,
    sidebar_extra='<button class="w-full flex items-center gap-3 px-4 py-3 rounded-xl text-secondary hover:bg-surface-container-low transition-colors"><span class="material-symbols-outlined">account_circle</span><span class="font-medium text-body-md">Perfil</span></button>',
)
