"""Force change password page template."""
HTML_FORCE_CHANGE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cambiar Contraseña - UTP</title>
<script src="https://cdn.tailwindcss.com"></script>
<script>
tailwind.config={theme:{extend:{colors:{primary:{DEFAULT:'#B5100F',hover:'#8C0D0C',container:'#F9DEDC','fixed':'#F9DEDC','fixed-dim':'#F2B8B5',on:'#FFFFFF'},secondary:{DEFAULT:'#655758',hover:'#4B4041',container:'#EBE0DE','fixed-dim':'#CEC4C2',on:'#FFFFFF'},tertiary:{DEFAULT:'#3F5E5B',hover:'#2C4341',container:'#C3E4E0','fixed-dim':'#A7C8C4',on:'#FFFFFF'},error:{DEFAULT:'#BA1A1A',container:'#FFDAD6',on:'#FFFFFF'},'on-surface':'#1D1B1B','surface-container-low':'#F7F2F1','surface-container':'#F1ECEB','surface-container-high':'#EBE6E5','surface-container-highest':'#E6E1E0','outline-variant':'#CAC4C3','on-primary-fixed':'#3F0908','on-tertiary-container':'#001B19','on-error-container':'#410002'},fontFamily:{sans:['Inter','system-ui','sans-serif']},fontSize:{'headline-lg':['32px','40px'],'headline-md':['28px','36px'],'body-md':['14px','20px'],'label-md':['12px','16px']}}}}
</script>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400;14..32,500;14..32,600;14..32,700&family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0,200" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,sans-serif;background:#F7F2F1;min-height:100vh;display:flex;align-items:center;justify-content:center}
.is-focused label{color:#B5100F}
.material-symbols-outlined{font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 200,'opsz' 24}
.password-strength{height:4px;border-radius:2px;transition:all .3s;overflow:hidden}
.password-strength-bar{height:100%;transition:all .3s;border-radius:2px}
</style>
</head>
<body>
<main class="w-full min-h-screen flex">
<div class="hidden lg:flex w-1/2 bg-gradient-to-br from-primary via-[#8C0D0C] to-[#5A0808] relative overflow-hidden items-center justify-center">
<div class="absolute inset-0 opacity-10" style="background-image:radial-gradient(circle at 25% 50%,white 0%,transparent 50%),radial-gradient(circle at 75% 30%,white 0%,transparent 50%)"></div>
<div class="relative z-10 text-center px-12 max-w-lg">
<div class="w-20 h-20 bg-white/15 backdrop-blur rounded-3xl flex items-center justify-center mx-auto mb-8"><span class="material-symbols-outlined text-white text-[40px]">lock_reset</span></div>
<h1 class="text-white font-headline-lg text-headline-lg mb-4 font-bold">Cambio de Contraseña</h1>
<p class="text-white/80 text-body-md leading-relaxed">Tu administrador ha solicitado que actualices tu contraseña. Ingresa una nueva contraseña segura para continuar.</p>
</div>
</div>
<div class="w-full lg:w-1/2 flex items-center justify-center p-6">
<div class="w-full max-w-md">
<div class="text-center mb-10">
<div class="w-16 h-16 bg-primary-container rounded-2xl flex items-center justify-center mx-auto mb-4"><span class="material-symbols-outlined text-primary text-[32px]">password</span></div>
<h2 class="font-headline-md text-headline-md text-on-surface font-bold">Nueva Contraseña</h2>
<p class="text-body-md text-secondary mt-1">Debe cumplir los requisitos de seguridad</p>
</div>
<div id="error-msg" class="hidden mb-6 p-4 bg-error-container rounded-xl flex items-start gap-3">
<span class="material-symbols-outlined text-error text-[20px] mt-0.5">error</span>
<p class="text-sm text-on-error-container font-medium" id="error-text">Error al cambiar la contraseña</p>
</div>
<form id="force-form" class="space-y-5" onsubmit="return cambiarContraseña(event)">
<div>
<label class="block text-sm font-bold text-secondary mb-1.5">Contraseña Temporal</label>
<div class="relative">
<input id="current-password" type="password" class="w-full px-4 py-3.5 border border-outline-variant rounded-xl focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary pr-12" placeholder="Ingresa la contraseña temporal" required>
<button type="button" onclick="togglePass('current-password',this)" class="absolute right-3 top-1/2 -translate-y-1/2 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[20px]">visibility</span></button>
</div>
</div>
<div>
<label class="block text-sm font-bold text-secondary mb-1.5">Nueva Contraseña</label>
<div class="relative">
<input id="new-password" type="password" class="w-full px-4 py-3.5 border border-outline-variant rounded-xl focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary pr-12" placeholder="Min. 8 caracteres" oninput="checkStrength(this.value)" required>
<button type="button" onclick="togglePass('new-password',this)" class="absolute right-3 top-1/2 -translate-y-1/2 text-secondary hover:text-on-surface transition-colors"><span class="material-symbols-outlined text-[20px]">visibility</span></button>
</div>
<div class="password-strength mt-2 bg-surface-container-highest"><div id="strength-bar" class="password-strength-bar w-0"></div></div>
<div class="flex flex-wrap gap-x-4 gap-y-1 mt-2 text-xs">
<span id="rule-length" class="text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">circle</span> Min. 8 caracteres</span>
<span id="rule-upper" class="text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">circle</span> Una mayuscula</span>
<span id="rule-lower" class="text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">circle</span> Una minuscula</span>
<span id="rule-digit" class="text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">circle</span> Un numero</span>
<span id="rule-special" class="text-secondary flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">circle</span> Un caracter especial</span>
</div>
</div>
<div>
<label class="block text-sm font-bold text-secondary mb-1.5">Confirmar Contraseña</label>
<input id="confirm-password" type="password" class="w-full px-4 py-3.5 border border-outline-variant rounded-xl focus:outline-none focus:border-primary focus:ring-1 focus:ring-primary" placeholder="Repite la nueva contraseña" required>
</div>
<button id="submit-btn" type="submit" class="w-full py-4 bg-primary text-white font-bold rounded-xl shadow-lg shadow-primary/25 hover:bg-primary-hover active:scale-[0.98] transition-all duration-200 flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed" disabled>
<span>Cambiar Contraseña</span>
<span class="material-symbols-outlined hidden animate-spin" id="spinner">refresh</span>
</button>
</form>
</div>
</div>
</main>
<script>
function togglePass(id,btn){
var i=document.getElementById(id);
if(i.type==='password'){i.type='text';btn.querySelector('span').textContent='visibility_off'}
else{i.type='password';btn.querySelector('span').textContent='visibility'}
}
function checkStrength(val){
var upper=/[A-Z]/.test(val),lower=/[a-z]/.test(val),digit=/[0-9]/.test(val),special=/[!@#$%^&*(),.?":{}|<>_-]/.test(val),len=val.length>=8;
var rules=[{id:'rule-length',ok:len},{id:'rule-upper',ok:upper},{id:'rule-lower',ok:lower},{id:'rule-digit',ok:digit},{id:'rule-special',ok:special}];
var passed=rules.filter(function(r){return r.ok}).length;
rules.forEach(function(r){
var el=document.getElementById(r.id);
if(el){
el.style.color=r.ok?'#1D7A3D':'#655758';
el.querySelector('span').textContent=r.ok?'check_circle':'cancel';
}
});
var bar=document.getElementById('strength-bar');
var pct=passed/rules.length*100;
var colors=['#BA1A1A','#E3742A','#E3A02A','#5BA85A','#1D7A3D'];
bar.style.width=pct+'%';
bar.style.background=colors[Math.min(passed,5)-1]||'#E6E1E0';
var allOk=len&&upper&&lower&&digit&&special;
document.getElementById('submit-btn').disabled=!allOk;
}
function cambiarContraseña(e){
e.preventDefault();
var current=document.getElementById('current-password').value.trim();
var np=document.getElementById('new-password').value;
var cp=document.getElementById('confirm-password').value;
if(!current||!np||!cp){document.getElementById('error-text').textContent='Todos los campos son obligatorios';document.getElementById('error-msg').classList.remove('hidden');return false}
if(np!==cp){document.getElementById('error-text').textContent='Las contraseñas no coinciden';document.getElementById('error-msg').classList.remove('hidden');return false}
if(document.getElementById('submit-btn').disabled)return false;
var btn=document.getElementById('submit-btn');btn.disabled=true;btn.querySelector('span').textContent='Cambiando...';document.getElementById('spinner').classList.remove('hidden');
fetch('/api/auth/force-change-password',{method:'POST',body:new URLSearchParams({current_password:current,new_password:np,confirm_password:cp}),headers:{'Content-Type':'application/x-www-form-urlencoded'}})
.then(function(r){return r.json().then(function(d){return{status:r.status,data:d}})})
.then(function(res){
if(res.data.error||res.status>=400){document.getElementById('error-text').textContent=res.data.error||'Error al cambiar la contraseña';document.getElementById('error-msg').classList.remove('hidden');btn.disabled=false;btn.querySelector('span').textContent='Cambiar Contraseña';document.getElementById('spinner').classList.add('hidden');return}
window.location.href='/chat'
})
.catch(function(){document.getElementById('error-text').textContent='Error de conexion';document.getElementById('error-msg').classList.remove('hidden');btn.disabled=false;btn.querySelector('span').textContent='Cambiar Contraseña';document.getElementById('spinner').classList.add('hidden')});
return false;
}
</script>
</body>
</html>"""
