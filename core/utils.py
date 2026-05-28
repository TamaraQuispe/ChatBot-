import html


def escapar(texto):
    if texto is None:
        return ""
    return html.escape(str(texto), quote=True)
