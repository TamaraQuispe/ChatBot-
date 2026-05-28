HTML_LOGIN = """
<!DOCTYPE html>

<html lang="es"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Login | Asistente Academico UTP</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@400;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "tertiary-fixed-dim": "#b7c8e1",
                    "inverse-primary": "#ffb3af",
                    "on-secondary": "#ffffff",
                    "on-surface-variant": "#5b403e",
                    "surface-tint": "#bc1127",
                    "primary-container": "#b00020",
                    "secondary": "#5f5e5e",
                    "surface-container-low": "#f3f4f5",
                    "on-primary": "#ffffff",
                    "on-surface": "#191c1d",
                    "outline": "#906f6d",
                    "primary-fixed-dim": "#ffb3af",
                    "inverse-on-surface": "#f0f1f2",
                    "surface-container": "#edeeef",
                    "inverse-surface": "#2e3132",
                    "on-secondary-fixed-variant": "#474746",
                    "surface-container-lowest": "#ffffff",
                    "surface-container-high": "#e7e8e9",
                    "on-tertiary-fixed": "#0b1c30",
                    "primary": "#840015",
                    "surface": "#f8f9fa",
                    "on-primary-container": "#ffbbb8",
                    "tertiary": "#304055",
                    "surface-container-highest": "#e1e3e4",
                    "error-container": "#ffdad6",
                    "outline-variant": "#e4bdbb",
                    "secondary-fixed-dim": "#c8c6c5",
                    "background": "#f8f9fa",
                    "surface-dim": "#d9dadb",
                    "error": "#ba1a1a",
                    "secondary-container": "#e2dfde",
                    "on-error-container": "#93000a",
                    "surface-bright": "#f8f9fa",
                    "on-primary-fixed": "#410006",
                    "surface-variant": "#e1e3e4",
                    "primary-fixed": "#ffdad8",
                    "on-error": "#ffffff",
                    "on-tertiary-fixed-variant": "#38485d",
                    "tertiary-container": "#47576d",
                    "on-secondary-fixed": "#1c1b1b",
                    "on-secondary-container": "#636262",
                    "secondary-fixed": "#e5e2e1",
                    "tertiary-fixed": "#d3e4fe",
                    "on-tertiary": "#ffffff",
                    "on-primary-fixed-variant": "#930019",
                    "on-tertiary-container": "#bccde6",
                    "on-background": "#191c1d"
            },
            "borderRadius": {
                    "DEFAULT": "0.5rem",
                    "lg": "0.5rem",
                    "xl": "0.75rem",
                    "full": "9999px"
            },
            "spacing": {
                    "xs": "4px",
                    "gutter": "24px",
                    "margin-mobile": "16px",
                    "margin-desktop": "40px",
                    "sm": "12px",
                    "xl": "80px",
                    "base": "8px",
                    "lg": "48px",
                    "md": "24px"
            },
            "fontFamily": {
                    "headline-lg-mobile": ["Libre Franklin"],
                    "headline-lg": ["Libre Franklin"],
                    "label-md": ["Libre Franklin"],
                    "body-sm": ["Libre Franklin"],
                    "headline-md": ["Libre Franklin"],
                    "display-lg": ["Libre Franklin"],
                    "body-lg": ["Libre Franklin"],
                    "body-md": ["Libre Franklin"]
            },
            "fontSize": {
                    "headline-lg-mobile": ["28px", {"lineHeight": "36px", "fontWeight": "600"}],
                    "headline-lg": ["32px", {"lineHeight": "40px", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                    "label-md": ["12px", {"lineHeight": "16px", "letterSpacing": "0.05em", "fontWeight": "600"}],
                    "body-sm": ["14px", {"lineHeight": "20px", "fontWeight": "400"}],
                    "headline-md": ["24px", {"lineHeight": "32px", "fontWeight": "600"}],
                    "display-lg": ["48px", {"lineHeight": "56px", "letterSpacing": "-0.02em", "fontWeight": "700"}],
                    "body-lg": ["18px", {"lineHeight": "28px", "fontWeight": "400"}],
                    "body-md": ["16px", {"lineHeight": "24px", "fontWeight": "400"}]
            }
          },
        },
      }
    </script>
<style>
        body {
            font-family: 'Libre Franklin', sans-serif;
            background-image: url('https://lh3.googleusercontent.com/aida-public/AB6AXuCyy-kSoGFOOqTPDq8N97CxJG54vsGcdflKwmyflmroxVdFGZXYl9bV13m9Cg3GWF9j2Fh7W6AOCdImvSVR8quZBnWpOEh6v-xjyWRuAF7ToWLNXBnlsqVfkBW5VFFP-lp0_vAyuoRSy3_wDgGqtp_YwBgkrxerYc8TcEyKBfkkf2Ef03Sxss3UZ5XldBOA4KzKWIXAFpZAlj-zI-yrAU_wWck4w7CN9a1ZGIwJze95nue18Ulv_p21UWBUrUfkmQOlvoD4HHgOqgY');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }

        body::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.45);
            backdrop-filter: blur(2px);
            z-index: 0;
        }

        .login-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3);
            position: relative;
        }
        
        .input-field:focus-within {
            border-color: #bc1127;
            box-shadow: 0 0 0 2px rgba(188, 17, 39, 0.1);
        }

        .btn-primary-utp {
            background-color: #bc1127;
            transition: all 0.2s ease;
        }

        .btn-primary-utp:hover {
            background-color: #840015;
            transform: translateY(-1px);
        }

        .btn-primary-utp:active {
            transform: translateY(0);
        }

        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24;
        }
    </style>
</head>
<body class="min-h-screen flex items-center justify-center p-margin-mobile md:p-0">
<main class="w-full max-w-[440px] z-10">
<div class="login-card p-8 md:p-12 rounded-lg flex flex-col items-center">
<div class="mb-10 text-center">
<div class="mb-6 flex justify-center">
<div class="w-16 h-16 bg-primary-fixed rounded-lg flex items-center justify-center">
<span class="material-symbols-outlined text-primary text-4xl" style="font-variation-settings: 'FILL' 1;">school</span>
</div>
</div>
<h1 class="font-headline-lg text-headline-lg text-on-surface mb-2 tracking-tight">
                Asistente Academico UTP
            </h1>
<p class="font-label-md text-label-md text-secondary uppercase tracking-widest">
                Portal Inteligente de Gestion Docente
            </p>
</div>
<form class="w-full space-y-6" action="/login" method="POST">
<div class="space-y-2">
<label class="font-label-md text-label-md text-on-surface-variant block px-1" for="username">Usuario</label>
<div class="relative group input-field border border-outline-variant bg-surface-container-lowest rounded-lg transition-all duration-200">
<span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant group-focus-within:text-primary transition-colors">person</span>
<input autocomplete="username" class="w-full bg-transparent border-none py-3.5 pl-12 pr-4 text-on-surface font-body-md placeholder:text-on-surface-variant/50 focus:ring-0" id="username" name="username" placeholder="Ej. C1234567" type="text"/>
</div>
</div>
<div class="space-y-2">
<div class="flex justify-between items-center px-1">
<label class="font-label-md text-label-md text-on-surface-variant block" for="password">Contrasena</label>
<a class="font-label-md text-label-md text-primary hover:underline transition-colors" href="#">¿Olvidaste tu contrasena?</a>
</div>
<div class="relative group input-field border border-outline-variant bg-surface-container-lowest rounded-lg transition-all duration-200">
<span class="material-symbols-outlined absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant group-focus-within:text-primary transition-colors">lock</span>
<input autocomplete="current-password" class="w-full bg-transparent border-none py-3.5 pl-12 pr-12 text-on-surface font-body-md placeholder:text-on-surface-variant/50 focus:ring-0" id="password" name="password" placeholder="********" type="password"/>
<button class="absolute right-4 top-1/2 -translate-y-1/2 text-on-surface-variant hover:text-on-surface transition-colors" type="button">
<span class="material-symbols-outlined text-[20px]">visibility</span>
</button>
</div>
</div>
<div class="flex items-center gap-3 px-1">
<div class="relative flex items-center h-5">
<input class="w-4 h-4 rounded border-outline bg-surface-container-lowest text-primary focus:ring-primary/30 focus:ring-offset-0" id="remember" type="checkbox"/>
</div>
<label class="font-body-sm text-body-sm text-on-surface-variant cursor-pointer select-none" for="remember">Recordar sesion</label>
</div>
<button class="w-full btn-primary-utp py-4 rounded-lg text-on-primary font-headline-md text-headline-md flex items-center justify-center gap-2 group" type="submit">
<span>Iniciar Sesion</span>
<span class="material-symbols-outlined group-hover:translate-x-1 transition-transform">arrow_forward</span>
</button>
</form>
<div class="mt-10 pt-8 border-t border-outline-variant w-full flex flex-col items-center gap-4">
<p class="font-label-md text-label-md text-secondary text-center">
                Acceso exclusivo para personal academico UTP
            </p>
<div class="flex items-center gap-2">
<div class="w-2 h-2 rounded-full bg-green-600"></div>
<span class="font-label-md text-label-md text-on-surface-variant uppercase tracking-widest text-[10px]">Sistemas Operativos</span>
</div>
</div>
</div>
<footer class="mt-8 flex justify-between px-2 relative z-10">
<p class="font-label-md text-label-md text-white/80">&copy; 2024 UTP Peru</p>
<div class="flex gap-4">
<a class="font-label-md text-label-md text-white/80 hover:text-white transition-colors" href="#">Privacidad</a>
<a class="font-label-md text-label-md text-white/80 hover:text-white transition-colors" href="#">Ayuda</a>
</div>
</footer>
</main>
<script>
    const toggleBtn = document.querySelector('button[type="button"]');
    const passInput = document.getElementById('password');
    
    toggleBtn?.addEventListener('click', () => {
        const isPass = passInput.type === 'password';
        passInput.type = isPass ? 'text' : 'password';
        toggleBtn.querySelector('span').textContent = isPass ? 'visibility_off' : 'visibility';
    });

    document.addEventListener('DOMContentLoaded', () => {
        const main = document.querySelector('main');
        main.style.opacity = '0';
        main.style.transform = 'translateY(10px)';
        
        setTimeout(() => {
            main.style.transition = 'all 0.6s cubic-bezier(0.2, 0.8, 0.2, 1)';
            main.style.opacity = '1';
            main.style.transform = 'translateY(0)';
        }, 50);
    });
</script>
</body></html>
"""
