"""Estilos CSS compartidos entre todas las páginas."""
# ruff: noqa: E501

SHARED_STYLES = """
body {
    background-color: #f8f9fa;
    color: #191c1d;
    font-family: 'Libre Franklin', sans-serif;
    -webkit-font-smoothing: antialiased;
}
.material-symbols-outlined {
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    display: inline-block;
    vertical-align: middle;
}
.glass-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(8px);
    border: 1px solid #e6e8eb;
    border-radius: 16px;
    box-shadow: 0 4px 20px -4px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease-out, box-shadow 0.2s ease-out;
}
.glass-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px -8px rgba(0, 0, 0, 0.1);
}
.glass-panel {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(230, 232, 235, 1);
}
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #e1e3e4; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #585f64; }
"""

TAILWIND_CONFIG = """
tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "surface-container-lowest": "#ffffff",
                "surface-container-highest": "#e1e3e4",
                "secondary": "#585f64",
                "on-error": "#ffffff",
                "on-background": "#191c1d",
                "on-tertiary": "#ffffff",
                "on-surface-variant": "#5b403e",
                "surface-container": "#edeeef",
                "on-primary-container": "#ffbbb8",
                "primary-container": "#b00020",
                "on-error-container": "#93000a",
                "surface-bright": "#f8f9fa",
                "on-primary": "#ffffff",
                "primary-fixed": "#ffdad8",
                "on-primary-fixed-variant": "#930019",
                "on-secondary-fixed-variant": "#41484c",
                "error-container": "#ffdad6",
                "tertiary-container": "#4f575d",
                "secondary-fixed": "#dce3e9",
                "on-secondary-fixed": "#161d21",
                "inverse-on-surface": "#f0f1f2",
                "surface-container-high": "#e7e8e9",
                "surface-container-low": "#f3f4f5",
                "tertiary-fixed": "#dce3ea",
                "error": "#ba1a1a",
                "on-tertiary-container": "#c5ccd3",
                "surface-variant": "#e1e3e4",
                "surface-dim": "#d9dadb",
                "secondary-fixed-dim": "#c0c7cd",
                "inverse-surface": "#2e3132",
                "on-primary-fixed": "#410006",
                "on-tertiary-fixed-variant": "#40484d",
                "on-tertiary-fixed": "#151d21",
                "tertiary": "#384045",
                "on-secondary-container": "#5e656a",
                "background": "#f8f9fa",
                "secondary-container": "#dce3e9",
                "primary-fixed-dim": "#ffb3af",
                "on-surface": "#191c1d",
                "surface": "#f8f9fa",
                "surface-tint": "#bc1127",
                "outline": "#906f6d",
                "tertiary-fixed-dim": "#c0c7ce",
                "on-secondary": "#ffffff",
                "primary": "#840015",
                "inverse-primary": "#ffb3af",
                "outline-variant": "#e4bdbb"
            },
            borderRadius: {
                DEFAULT: "0.25rem", lg: "0.5rem", xl: "0.75rem", "2xl": "1rem", "3xl": "1.25rem", full: "9999px"
            },
            spacing: {
                "gutter": "24px", "container-padding": "32px", "section-gap": "80px",
                "stack-md": "16px", "stack-lg": "24px", "stack-sm": "8px"
            },
            fontFamily: {
                "headline-md": ["Libre Franklin"], "display-lg": ["Libre Franklin"],
                "body-lg": ["Libre Franklin"], "title-lg": ["Libre Franklin"],
                "label-md": ["Libre Franklin"], "headline-lg": ["Libre Franklin"],
                "mono-sm": ["Courier Prime"], "body-md": ["Libre Franklin"]
            },
            fontSize: {
                "headline-md": ["24px", {"lineHeight": "1.3", "letterSpacing": "-0.02em", "fontWeight": "600"}],
                "display-lg": ["48px", {"lineHeight": "1.1", "letterSpacing": "-0.04em", "fontWeight": "700"}],
                "body-lg": ["16px", {"lineHeight": "1.6", "letterSpacing": "-0.01em", "fontWeight": "400"}],
                "title-lg": ["18px", {"lineHeight": "1.5", "letterSpacing": "-0.01em", "fontWeight": "600"}],
                "label-md": ["12px", {"lineHeight": "1", "letterSpacing": "0.02em", "fontWeight": "500"}],
                "headline-lg": ["32px", {"lineHeight": "1.2", "letterSpacing": "-0.03em", "fontWeight": "600"}],
                "mono-sm": ["13px", {"lineHeight": "1.5", "letterSpacing": "0em", "fontWeight": "400"}],
                "body-md": ["14px", {"lineHeight": "1.6", "letterSpacing": "0em", "fontWeight": "400"}]
            }
        }
    }
}
"""  # noqa
