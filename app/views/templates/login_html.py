"""Login page template."""
HTML_LOGIN = """
<!DOCTYPE html>

<html class="light" lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Asistente Academico UTP - Login</title>
<!-- Google Fonts: Libre Franklin -->
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;600;700;800&amp;display=swap" rel="stylesheet"/>
<!-- Material Symbols Outlined -->
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    "colors": {
                        "background": "#f8f9fa",
                        "tertiary-fixed-dim": "#b7c8e1",
                        "surface-container-lowest": "#ffffff",
                        "tertiary": "#304055",
                        "surface": "#f8f9fa",
                        "on-tertiary-fixed": "#0b1c30",
                        "surface-tint": "#bc1127",
                        "on-tertiary-fixed-variant": "#38485d",
                        "on-tertiary": "#ffffff",
                        "primary": "#840015",
                        "on-tertiary-container": "#bccde6",
                        "tertiary-container": "#47576d",
                        "surface-bright": "#f8f9fa",
                        "on-surface": "#191c1d",
                        "primary-fixed-dim": "#ffb3af",
                        "on-surface-variant": "#5b403e",
                        "surface-container-high": "#e7e8e9",
                        "error-container": "#ffdad6",
                        "secondary-fixed-dim": "#c8c6c5",
                        "on-secondary": "#ffffff",
                        "secondary-fixed": "#e5e2e1",
                        "on-background": "#191c1d",
                        "error": "#ba1a1a",
                        "surface-dim": "#d9dadb",
                        "surface-container-low": "#f3f4f5",
                        "inverse-primary": "#ffb3af",
                        "on-primary-container": "#ffbbb8",
                        "on-error": "#ffffff",
                        "primary-fixed": "#ffdad8",
                        "on-secondary-container": "#636262",
                        "on-primary": "#ffffff",
                        "on-secondary-fixed-variant": "#474746",
                        "on-primary-fixed": "#410006",
                        "surface-variant": "#e1e3e4",
                        "inverse-surface": "#2e3132",
                        "secondary-container": "#e2dfde",
                        "on-secondary-fixed": "#1c1b1b",
                        "tertiary-fixed": "#d3e4fe",
                        "on-primary-fixed-variant": "#930019",
                        "secondary": "#5f5e5e",
                        "primary-container": "#b00020",
                        "on-error-container": "#93000a",
                        "outline": "#906f6d",
                        "outline-variant": "#e4bdbb",
                        "inverse-on-surface": "#f0f1f2",
                        "surface-container": "#edeeef",
                        "surface-container-highest": "#e1e3e4",
                        "utp-red": {
                            "vibrant": "#B00020",
                            "muted": "#840015"
                        }
                    },
                    "borderRadius": {
                        "DEFAULT": "0.25rem",
                        "lg": "0.5rem",
                        "xl": "0.75rem",
                        "full": "9999px"
                    },
                    "spacing": {
                        "xs": "4px",
                        "xl": "80px",
                        "gutter": "24px",
                        "base": "8px",
                        "margin-desktop": "40px",
                        "lg": "48px",
                        "margin-mobile": "16px",
                        "sm": "12px",
                        "md": "24px"
                    },
                    "fontFamily": {
                        "body-lg": ["Libre Franklin"],
                        "headline-md": ["Libre Franklin"],
                        "label-md": ["Libre Franklin"],
                        "body-sm": ["Libre Franklin"],
                        "headline-lg-mobile": ["Libre Franklin"],
                        "headline-lg": ["Libre Franklin"],
                        "display-lg": ["Libre Franklin"],
                        "body-md": ["Libre Franklin"]
                    },
                    "fontSize": {
                        "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                        "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                        "label-md": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                        "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                        "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "600"}],
                        "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                        "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                        "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
                    }
                },
            },
        }
    </script>
<style>
        body {
            font-family: 'Libre Franklin', sans-serif;
            background-color: #f8f9fa;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .benefit-card {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: transform 0.2s ease;
        }
        .benefit-card:hover {
            transform: translateY(-2px);
            background: rgba(255, 255, 255, 0.2);
        }
        .left-panel-image {
            clip-path: polygon(0 0, 100% 0, 85% 100%, 0% 100%);
        }
        @media (max-width: 768px) {
            .left-panel-image {
                clip-path: none;
            }
        }
    </style>
</head>
<body class="min-h-screen overflow-x-hidden">
<main class="flex flex-col md:flex-row min-h-screen w-full">
<!-- Left Panel: Brand & Vision -->
<section class="relative w-full md:w-[60%] min-h-[40vh] md:min-h-screen overflow-hidden left-panel-image">
<div class="absolute inset-0 z-0">
<img alt="Frontis Universidad Tecnológica del Perú" class="w-full h-full object-cover" src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Frontis_de_la_Universidad_Tecnol%C3%B3gica_del_Per%C3%BA_1.jpg/960px-Frontis_de_la_Universidad_Tecnol%C3%B3gica_del_Per%C3%BA_1.jpg"/>
<div class="absolute inset-0 bg-gradient-to-r from-utp-red-muted/80 to-transparent"></div>
</div>
<!-- Content Overlay -->
<div class="relative z-10 flex flex-col justify-center h-full px-margin-mobile md:px-margin-desktop text-white max-w-2xl py-12">
<div class="mb-8">
<span class="inline-block py-1 px-3 bg-white/20 backdrop-blur-md rounded-full font-label-md text-label-md uppercase mb-4 tracking-wider">
                        UTP Peru • Sede Norte
                    </span>
<h1 class="font-display-lg text-display-lg leading-tight md:text-5xl lg:text-6xl font-extrabold mb-6">
                        Tu asistente academico, <span class="text-primary-fixed">impulsado por IA</span>
</h1>
<p class="font-body-lg text-body-lg opacity-90 mb-10 max-w-lg">
                        Reserva tus aulas de forma rapida y sencilla en cualquier momento.
                    </p>
</div>
<!-- Benefits Grid -->
<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
<div class="benefit-card p-4 rounded-xl flex items-center gap-4">
<div class="w-10 h-10 rounded-lg bg-white/20 flex items-center justify-center">
<span class="material-symbols-outlined text-white">schedule</span>
</div>
<span class="font-body-md text-body-md font-semibold">Consultas en tiempo real</span>
</div>
<div class="benefit-card p-4 rounded-xl flex items-center gap-4">
<div class="w-10 h-10 rounded-lg bg-white/20 flex items-center justify-center">
<span class="material-symbols-outlined text-white">smart_toy</span>
</div>
<span class="font-body-md text-body-md font-semibold">Gestion de aulas inteligente</span>
</div>
</div>
</div>
</section>
<!-- Right Panel: Login Interface -->
<section class="w-full md:w-[40%] flex items-center justify-center bg-surface relative p-margin-mobile md:p-12">
<!-- Abstract background shape for subtle depth -->
<div class="absolute top-0 right-0 w-64 h-64 bg-primary-fixed-dim/10 rounded-full blur-3xl -mr-32 -mt-32"></div>
<div class="absolute bottom-0 left-0 w-48 h-48 bg-primary/5 rounded-full blur-2xl -ml-24 -mb-24"></div>
<!-- Login Card -->
<div class="glass-card w-full max-w-md p-8 md:p-10 rounded-3xl shadow-xl z-10 transition-all duration-300 hover:shadow-2xl">
<!-- Institutional Identity -->
<div class="flex flex-col items-center mb-8">
<div class="w-16 h-16 bg-primary rounded-2xl flex items-center justify-center mb-4 shadow-lg shadow-primary/20">
<span class="material-symbols-outlined text-white text-3xl" style="font-variation-settings: 'FILL' 1;">school</span>
</div>
<h2 class="font-headline-md text-headline-md text-on-surface mb-2">Bienvenido</h2>
<p class="font-body-sm text-body-sm text-secondary text-center">Ingresa para interactuar con tu asistente academico virtual</p>
</div>
<div id="error-msg" class="hidden bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-xl mb-6 flex items-center gap-3">
<span class="material-symbols-outlined text-red-500">error</span>
<span id="error-text">Credenciales incorrectas. Intenta de nuevo.</span>
</div>
<!-- Form -->
<form class="space-y-6" action="/login" method="POST">
<div class="space-y-1.5">
<label class="font-label-md text-label-md text-on-surface-variant block ml-1" for="username">Codigo de Docente</label>
<div class="relative group">
<div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-secondary group-focus-within:text-primary transition-colors">
<span class="material-symbols-outlined text-body-lg">person</span>
</div>
<input class="block w-full pl-11 pr-4 py-3.5 bg-white border border-outline-variant rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all outline-none font-body-md text-on-surface" id="username" name="username" placeholder="C0000000" required="" type="text"/>
</div>
</div>
<div class="space-y-1.5">
<label class="font-label-md text-label-md text-on-surface-variant block ml-1" for="password">Contrasena</label>
<div class="relative group">
<div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-secondary group-focus-within:text-primary transition-colors">
<span class="material-symbols-outlined text-body-lg">lock_open</span>
</div>
<input class="block w-full pl-11 pr-12 py-3.5 bg-white border border-outline-variant rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all outline-none font-body-md text-on-surface" id="password" name="password" placeholder="********" required="" type="password"/>
<button class="absolute inset-y-0 right-0 pr-4 flex items-center text-secondary hover:text-primary transition-colors" type="button">
<span class="material-symbols-outlined text-body-md">visibility</span>
</button>
</div>
</div>
<div class="flex items-center justify-between">
<div class="flex items-center">
<input class="w-4 h-4 text-primary border-outline-variant rounded focus:ring-primary" id="remember" name="remember" type="checkbox"/>
<label class="ml-2 font-body-sm text-body-sm text-secondary cursor-pointer select-none" for="remember">Recordarme</label>
</div>
<a class="font-label-md text-label-md text-primary hover:underline font-semibold cursor-pointer" onclick="document.getElementById('reset-modal').classList.remove('hidden')">¿Olvidaste tu contrasena?</a>
</div>
<button class="w-full py-4 bg-utp-red-vibrant text-white font-body-md font-bold rounded-xl shadow-lg shadow-utp-red-vibrant/25 hover:bg-utp-red-muted active:scale-[0.98] transition-all duration-200 flex items-center justify-center gap-2 group" type="submit">
                        Iniciar Sesion
                        <span class="material-symbols-outlined transition-transform group-hover:translate-x-1">arrow_forward</span>
</button>
</form>
<!-- Password Reset Info Modal -->
<div id="reset-modal" class="fixed inset-0 z-50 hidden flex items-center justify-center p-4" onclick="if(event.target===this)document.getElementById('reset-modal').classList.add('hidden')">
<div class="absolute inset-0 bg-black/40 backdrop-blur-sm"></div>
<div class="relative bg-white rounded-3xl shadow-2xl max-w-md w-full p-8 transform transition-all text-center" onclick="event.stopPropagation()">
<button onclick="document.getElementById('reset-modal').classList.add('hidden')" class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center text-secondary hover:bg-surface-container-low rounded-full transition-colors"><span class="material-symbols-outlined">close</span></button>
<div class="w-16 h-16 rounded-2xl bg-amber-50 flex items-center justify-center text-amber-600 mx-auto mb-6"><span class="material-symbols-outlined text-[32px]">lock_reset</span></div>
<h3 class="font-bold text-xl text-on-surface mb-3">Restablecer Contrasena</h3>
<p class="text-secondary text-sm leading-relaxed mb-8">La recuperacion de contrasena solo puede ser realizada por el administrador del sistema. Comuniquese con el para solicitar un restablecimiento.</p>
<button onclick="document.getElementById('reset-modal').classList.add('hidden')" class="w-full py-3.5 bg-primary text-white font-bold rounded-xl hover:bg-primary-hover transition-all active:scale-[0.98]">Entendido</button>
</div>
</div>
<!-- Footer Info -->
<div class="mt-8 pt-6 border-t border-surface-variant flex items-center justify-center gap-2 text-secondary">
<span class="material-symbols-outlined text-sm">lock</span>
<p class="font-label-md text-label-md">Acceso seguro para personal academico</p>
</div>
</div>
<!-- Version / Brand Footer -->
<div class="absolute bottom-6 flex items-center gap-4 text-secondary/60">
<p class="font-label-md text-label-md tracking-widest">© 2024 UTP PERU</p>
<div class="h-1 w-1 bg-secondary/40 rounded-full"></div>
<p class="font-label-md text-label-md">V2.4.0</p>
</div>
</section>
</main>
<script>
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            input.addEventListener('focus', () => {
                input.parentElement.parentElement.classList.add('is-focused');
            });
            input.addEventListener('blur', () => {
                input.parentElement.parentElement.classList.remove('is-focused');
            });
        });

        const togglePass = document.querySelector('button[type="button"]');
        const passInput = document.getElementById('password');
        if (togglePass && passInput) {
            togglePass.addEventListener('click', () => {
                const isPassword = passInput.type === 'password';
                passInput.type = isPassword ? 'text' : 'password';
                togglePass.querySelector('span').textContent = isPassword ? 'visibility_off' : 'visibility';
            });
        }
    </script>
    <script>
        const params = new URLSearchParams(window.location.search);
        if (params.get('error') === '1') {
            document.getElementById('error-msg').classList.remove('hidden');
        }
    </script>
</body></html>
"""
