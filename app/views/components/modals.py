"""Modales reutilizables."""

MODAL_DETALLE = """<div id="modalDetalle" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalDetalle')" role="dialog" aria-modal="true" aria-labelledby="modal-nombre">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-lg w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <button onclick="cerrarModal('modalDetalle')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors" aria-label="Cerrar">
            <span class="material-symbols-outlined">close</span>
        </button>
        <div class="flex items-center gap-3 mb-6">
            <div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined text-[28px]" id="modal-icon">meeting_room</span>
            </div>
            <div>
                <h3 class="font-bold text-xl text-on-surface" id="modal-nombre">-</h3>
                <p class="text-sm text-secondary" id="modal-tipo">-</p>
            </div>
        </div>
        <div class="space-y-4" id="modal-campos"></div>
        <button onclick="cerrarModal('modalDetalle')" class="mt-6 w-full py-3 bg-primary text-white font-bold rounded-2xl hover:bg-primary/90 transition-all active:scale-[0.98]">Cerrar</button>
    </div>
</div>"""

MODAL_ELIMINAR = """<div id="modalEliminar" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalEliminar')" role="dialog" aria-modal="true" aria-labelledby="eliminar-text">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-sm w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <div class="text-center">
            <div class="w-16 h-16 rounded-full bg-error/10 flex items-center justify-center text-error mx-auto mb-4">
                <span class="material-symbols-outlined text-[32px]">delete</span>
            </div>
            <h3 class="font-bold text-xl text-on-surface mb-2">$TITULO</h3>
            <p class="text-sm text-secondary mb-6" id="eliminar-text">$MENSAJE</p>
            <form id="form-eliminar" method="POST" action="$ACTION" class="flex gap-3">
                <input type="hidden" name="id_espacio" id="eliminar-id">
                <input type="hidden" name="id" id="eliminar-id-alt">
                <button type="button" onclick="cerrarModal('modalEliminar')" class="flex-1 py-3 border border-surface-container-highest text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
                <button type="submit" class="flex-1 py-3 bg-error text-white font-bold rounded-2xl hover:bg-error/90 transition-all">Eliminar</button>
            </form>
        </div>
    </div>
</div>"""

MODAL_ESTADO = """<div id="modalEstado" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this) cerrarModal('modalEstado')" role="dialog" aria-modal="true">
    <div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
    <div class="relative bg-white rounded-3xl shadow-2xl max-w-sm w-full p-8 transform transition-all" onclick="event.stopPropagation()">
        <div class="flex items-center gap-3 mb-6">
            <div class="w-12 h-12 rounded-2xl bg-primary/10 flex items-center justify-center text-primary">
                <span class="material-symbols-outlined text-[28px]">sync_alt</span>
            </div>
            <div>
                <h3 class="font-bold text-xl text-on-surface">Cambiar Estado</h3>
                <p class="text-sm text-secondary">Seleccione el nuevo estado</p>
            </div>
        </div>
        <form method="POST" action="$ESTADO_ACTION" class="space-y-3">
            <input type="hidden" name="id_espacio" id="estado-id">
            <button type="submit" name="estado" value="DISPONIBLE" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-emerald-200 hover:bg-emerald-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Disponible</p><p class="text-xs text-secondary">Salon libre para reservas</p></div>
            </button>
            <button type="submit" name="estado" value="OCUPADO" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-red-200 hover:bg-red-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-red-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Ocupado</p><p class="text-xs text-secondary">Salon en uso actualmente</p></div>
            </button>
            <button type="submit" name="estado" value="MANTENIMIENTO" class="w-full flex items-center gap-3 px-4 py-4 rounded-2xl border-2 border-amber-200 hover:bg-amber-50 transition-colors text-left">
                <span class="w-3 h-3 rounded-full bg-amber-500"></span>
                <div><p class="font-bold text-sm text-on-surface">Mantenimiento</p><p class="text-xs text-secondary">Salon fuera de servicio</p></div>
            </button>
            <button type="button" onclick="cerrarModal('modalEstado')" class="w-full py-3 text-secondary font-bold rounded-2xl hover:bg-surface-container-low transition-all">Cancelar</button>
        </form>
    </div>
</div>"""
