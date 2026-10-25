#!/usr/bin/env python3
"""
Genera las páginas de soluciones de iotlink.com.co a partir de SOLUCIONES:

    soluciones/index.html
    soluciones/<slug>/index.html

Uso (desde la raíz del repo):

    python3 _herramientas/generar_soluciones.py

Para cambiar un texto o agregar una solución, edita SOLUCIONES y vuelve a
correr el script. No edites a mano los HTML generados: se sobrescriben.

Captura del dashboard (opcional): si existe imagenes/soluciones/<slug>.jpg,
la landing la muestra. Si no, queda solo un comentario HTML.

Sin dependencias: solo la librería estándar de Python 3.
GitHub Pages (Jekyll) no publica carpetas que empiezan por "_", así que este
script no queda visible en el sitio.
"""
import json
import os
from html import escape
from urllib.parse import quote

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITIO = "https://iotlink.com.co"
WHATSAPP = "573246526040"
OG_IMAGE = f"{SITIO}/imagenes/og-image.png"

PRECIO = ("Se paga una mensualidad según la cantidad de sensores o equipos "
          "conectados. Cotiza por WhatsApp y te decimos cuánto sería para tu caso.")


SOLUCIONES = [
    {
        "slug": "monitoreo-temperatura-humedad",
        "nombre": "Monitoreo de temperatura y humedad",
        "corto": "Temperatura y humedad",
        "icono": "termometro",
        "icono_clase": "icon-connectivity",
        "resumen": "Cuartos fríos, neveras, bodegas de café y cadena de frío.",
        "title": "Monitoreo de temperatura y humedad en Medellín | IoT Link",
        "description": ("Sensores de temperatura y humedad para cuartos fríos, neveras, bodegas de café "
                        "y cadena de frío en Medellín y Colombia. Mira los datos en línea y recibe una "
                        "alerta cuando algo se sale del rango."),
        "h1": "Monitoreo de temperatura y humedad",
        "h1_resalte": "para cuartos fríos, neveras y bodegas",
        "intro": ("Sabes en todo momento a qué temperatura y humedad están tus productos, "
                  "y te llega una alerta si algo se sale del rango."),
        "wa": "Hola, quiero información sobre el monitoreo de temperatura y humedad.",
        "problemas": [
            ("Te enteras tarde", "Si una nevera o un cuarto frío se calienta en la noche, lo descubres al otro día, cuando el producto ya se dañó."),
            ("Registros a mano", "Anotar la temperatura en una planilla toma tiempo, se olvida y no deja un historial confiable."),
            ("No ves lo que pasa entre revisiones", "Una lectura cada tantas horas no muestra los picos ni cuánto tiempo estuvo fuera de rango."),
        ],
        "pasos": [
            ("Instalamos los sensores", "Ubicamos sensores de temperatura, y de humedad si la necesitas, en tus cuartos fríos, neveras o bodegas."),
            ("Los datos suben a la plataforma", "Los sensores envían sus lecturas por internet a la plataforma de IoT Link, en la nube."),
            ("Ves todo y te avisamos", "Consultas los datos desde el celular o el computador, y te llega una alerta si un valor se sale del rango que definas."),
        ],
        "obtienes": [
            "Temperatura y humedad en tiempo real",
            "Historial con gráficas por sensor",
            "Límites de alerta para cada sensor",
            "Una alerta cuando un valor sale del rango",
            "Tablero por equipo, zona o sede",
            "Reportes con el historial descargable",
        ],
        "usos": ["Cuartos fríos", "Neveras y congeladores", "Bodegas de café", "Cadena de frío",
                 "Centros de acopio", "Cuartos de servidores"],
    },
    {
        "slug": "monitoreo-nivel-tanques",
        "nombre": "Monitoreo de nivel de tanques",
        "corto": "Nivel de tanques",
        "icono": "tanque",
        "icono_clase": "icon-analytics",
        "resumen": "Agua, combustible y químicos, sin tener que ir a revisar.",
        "title": "Monitoreo de nivel de tanques en Medellín | IoT Link",
        "description": ("Monitoreo de nivel de tanques de agua, combustible y químicos en Medellín y "
                        "Colombia. Mira el nivel desde el celular y recibe una alerta antes de que el "
                        "tanque se vacíe o se rebose."),
        "h1": "Monitoreo de nivel de tanques",
        "h1_resalte": "de agua, combustible y químicos",
        "intro": ("Mira el nivel de tus tanques desde el celular y recibe una alerta antes de que "
                  "se vacíen o se rebosen."),
        "wa": "Hola, quiero información sobre el monitoreo de nivel de tanques.",
        "problemas": [
            ("Hay que ir a revisar", "Subir al tanque o mandar a alguien a mirar el nivel cuesta tiempo y no siempre es seguro."),
            ("Quedarse sin producto", "El tanque se vacía sin que nadie lo note y se para la operación."),
            ("Reboses y pérdidas", "Un tanque que se llena de más se rebosa y se pierde agua, combustible o insumos."),
        ],
        "pasos": [
            ("Instalamos el sensor de nivel", "Ponemos un sensor de nivel en cada tanque, según el tipo de tanque y el líquido."),
            ("El nivel sube a la plataforma", "El sensor envía la medición por internet a la plataforma de IoT Link, en la nube."),
            ("Ves el nivel y te avisamos", "Consultas el nivel desde el celular o el computador, y te llega una alerta cuando baja o sube del límite que definas."),
        ],
        "obtienes": [
            "Nivel de cada tanque en tiempo real",
            "Historial de llenado y consumo",
            "Una alerta por nivel bajo o nivel alto",
            "Límites de alerta para cada tanque",
            "Tablero con todos tus tanques",
            "Reportes con el historial descargable",
        ],
        "usos": ["Tanques de agua", "Tanques de combustible", "Químicos e insumos",
                 "Plantas de producción", "Edificios", "Fincas"],
    },
    {
        "slug": "rastreo-gps",
        "nombre": "Rastreo GPS de vehículos y activos",
        "corto": "Rastreo GPS",
        "icono": "gps",
        "icono_clase": "icon-security",
        "resumen": "Ubicación en tiempo real, historial de recorridos y geocercas.",
        "title": "Rastreo GPS de vehículos y activos en Medellín | IoT Link",
        "description": ("Rastreo GPS de vehículos, maquinaria y activos en Medellín y Colombia: "
                        "ubicación en tiempo real, historial de recorridos y geocercas desde el celular."),
        "h1": "Rastreo GPS de vehículos y activos",
        "h1_resalte": "en tiempo real, desde el celular",
        "intro": ("Mira dónde están tus vehículos y equipos, revisa por dónde anduvieron y define "
                  "zonas en el mapa."),
        "wa": "Hola, quiero información sobre el rastreo GPS de vehículos y activos.",
        "problemas": [
            ("No sabes dónde está", "Para saber dónde va un vehículo hay que llamar al conductor y esperar a que conteste."),
            ("Sin historial", "No hay cómo revisar qué ruta hizo un vehículo ni dónde paró."),
            ("Te enteras tarde", "Si un vehículo o un equipo sale de la zona donde debería estar, lo descubres cuando ya pasó."),
        ],
        "pasos": [
            ("Instalamos el rastreador", "Ponemos un rastreador GPS en cada vehículo o activo que quieras seguir."),
            ("La posición sube a la plataforma", "El rastreador envía su ubicación por internet a la plataforma de IoT Link, en la nube."),
            ("Ves el mapa y el historial", "Consultas la ubicación y los recorridos desde el celular o el computador, y defines geocercas por zona."),
        ],
        "obtienes": [
            "Ubicación en tiempo real en el mapa",
            "Historial de recorridos",
            "Geocercas por zona",
            "Una alerta cuando un vehículo entra o sale de una geocerca",
            "Tablero con toda tu flota",
            "Reportes con el historial descargable",
        ],
        "usos": ["Flotas de reparto", "Vehículos de empresa", "Transporte de carga",
                 "Maquinaria y equipos", "Activos de alto valor"],
    },
    {
        "slug": "automatizacion-dashboards",
        "nombre": "Automatización y dashboards a medida",
        "corto": "Automatización y dashboards",
        "icono": "automatizacion",
        "icono_clase": "icon-automation",
        "resumen": "Control remoto de equipos, reglas automáticas y tableros por proceso.",
        "title": "Automatización y dashboards IoT en Medellín | IoT Link",
        "description": ("Automatización y dashboards a medida en Medellín y Colombia: controla tus "
                        "equipos a distancia, crea reglas automáticas y mira cada proceso en un tablero."),
        "h1": "Automatización y dashboards",
        "h1_resalte": "a la medida de tu proceso",
        "intro": ("Controla tus equipos a distancia, deja que las reglas automáticas hagan el trabajo "
                  "repetitivo y mira cada proceso en un tablero."),
        "wa": "Hola, quiero información sobre automatización y dashboards a medida.",
        "problemas": [
            ("Todo se hace en sitio", "Para prender, apagar o revisar un equipo hay que ir hasta donde está."),
            ("Información regada", "Los datos de cada proceso están en planillas, en equipos distintos o en ninguna parte."),
            ("Depende de que alguien esté pendiente", "Si nadie está mirando, la acción no se hace a tiempo."),
        ],
        "pasos": [
            ("Diagnóstico del proceso", "Revisamos tus equipos y definimos qué medir, qué controlar y qué reglas necesitas."),
            ("Conectamos tus equipos", "Instalamos los sensores y controladores necesarios y los conectamos a la plataforma."),
            ("Tablero y reglas", "Armamos los tableros de tu proceso y configuramos las reglas automáticas y las alertas."),
        ],
        "obtienes": [
            "Control remoto de equipos desde el celular o el computador",
            "Reglas automáticas, por ejemplo encender o apagar un equipo cuando un valor pasa un límite",
            "Tableros por proceso, área o sede",
            "Una alerta cuando algo se sale de lo normal",
            "Acceso por roles para cada persona de tu equipo",
            "Reportes con el historial descargable",
        ],
        "usos": ["Plantas de producción", "Bombas y motores", "Riego", "Iluminación",
                 "Edificios", "Procesos industriales"],
    },
]


# ============================================================
# PIEZAS COMUNES
# ============================================================

def wa_link(texto):
    return f"https://wa.me/{WHATSAPP}?text={quote(texto)}"


def e(texto):
    return escape(texto, quote=True)


def head(title, description, url, json_ld):
    bloques = "\n".join(
        f'    <script type="application/ld+json">\n    {json.dumps(d, ensure_ascii=False)}\n    </script>'
        for d in json_ld
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{e(title)}</title>
    <meta name="description" content="{e(description)}">
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{e(title)}">
    <meta property="og:description" content="{e(description)}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{OG_IMAGE}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="es_CO">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="{OG_IMAGE}">
    <link rel="icon" href="/imagenes/favicon.ico" type="image/x-icon" sizes="192x192">
    <link rel="shortcut icon" href="/imagenes/favicon.ico" type="image/x-icon">
    <link rel="apple-touch-icon" href="/imagenes/logoiot.png">
    <link rel="stylesheet" href="/styles.css">
{bloques}
</head>"""


def pie():
    return """
    <div id="site-footer"></div>

    <script src="/components.js"></script>
    <script src="/script.js"></script>
</body>
</html>
"""


def migas(items):
    """items: lista de (nombre, url o None para la página actual)."""
    lis = []
    for nombre, url in items:
        if url:
            lis.append(f'<li><a href="{url}">{e(nombre)}</a></li>')
        else:
            lis.append(f'<li aria-current="page">{e(nombre)}</li>')
    return f'<nav class="migas" aria-label="Migas de pan"><ol>{"".join(lis)}</ol></nav>'


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": nombre, "item": url}
            for i, (nombre, url) in enumerate(items)
        ]
    }


def tarjeta(s):
    return f"""
                <a class="solucion-card" href="/soluciones/{s['slug']}/">
                    <div class="solucion-icon {s['icono_clase']}" aria-hidden="true"><svg class="icono"><use href="/imagenes/iconos.svg#i-{s['icono']}"/></svg></div>
                    <h3>{e(s['nombre'])}</h3>
                    <p>{e(s['resumen'])}</p>
                    <span class="solucion-link">Ver solución →</span>
                </a>"""


# ============================================================
# LANDING DE CADA SOLUCION
# ============================================================

def landing(s):
    url = f"{SITIO}/soluciones/{s['slug']}/"
    ruta = [("Inicio", f"{SITIO}/"), ("Soluciones", f"{SITIO}/soluciones/"), (s["nombre"], url)]

    servicio = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": s["nombre"],
        "serviceType": s["nombre"],
        "description": s["description"],
        "url": url,
        "provider": {"@type": "Organization", "name": "IoT Link", "url": f"{SITIO}/"},
        "areaServed": [
            {"@type": "City", "name": "Medellín"},
            {"@type": "Country", "name": "Colombia"}
        ]
    }

    problemas = "".join(f"""
                <div class="solucion-card">
                    <h3>{e(t)}</h3>
                    <p>{e(d)}</p>
                </div>""" for t, d in s["problemas"])

    pasos = "".join(f"""
                <div class="caso-card">
                    <div class="caso-number">{i + 1:02d}</div>
                    <h3>{e(t)}</h3>
                    <p>{e(d)}</p>
                </div>""" for i, (t, d) in enumerate(s["pasos"]))

    obtienes = "".join(f"\n                        <li>{e(x)}</li>" for x in s["obtienes"])
    usos = "".join(f'\n                        <span class="chip">{e(x)}</span>' for x in s["usos"])

    otras = "".join(tarjeta(o) for o in SOLUCIONES if o["slug"] != s["slug"])

    imagen_rel = f"imagenes/soluciones/{s['slug']}.jpg"
    if os.path.exists(os.path.join(RAIZ, imagen_rel)):
        captura = f"""
    <section class="soluciones">
        <div class="container">
            <h2>Así se ve el tablero</h2>
            <figure class="captura">
                <img src="/{imagen_rel}" alt="Tablero de {e(s['nombre'].lower())} en la plataforma de IoT Link" loading="lazy">
            </figure>
        </div>
    </section>
"""
    else:
        captura = f"\n    <!-- Captura del tablero: agrega /{imagen_rel} y vuelve a generar -->\n"

    return f"""{head(s['title'], s['description'], url, [servicio, breadcrumb_ld(ruta)])}
<body data-wa="{e(s['wa'])}">
    <div id="site-header"></div>

    <section class="hero sol-hero">
        <div class="hero-bg-full">
            <div class="container">
                {migas([("Inicio", "/"), ("Soluciones", "/soluciones/"), (s["nombre"], None)])}
                <h1 class="hero-title">
                    {e(s['h1'])}
                    <span class="title-highlight">{e(s['h1_resalte'])}</span>
                </h1>
                <p class="hero-description">{e(s['intro'])}</p>
                <div class="hero-actions">
                    <a href="{e(wa_link(s['wa']))}" class="btn-cta" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
                    <a href="/contacto" class="btn-cta btn-secundario">Agenda una demo</a>
                </div>
            </div>
        </div>
    </section>

    <section class="soluciones" id="problema">
        <div class="container">
            <h2>El problema</h2>
            <div class="soluciones-grid grid-3">{problemas}
            </div>
        </div>
    </section>

    <section class="casos" id="como-funciona">
        <div class="container">
            <h2>Cómo funciona</h2>
            <div class="casos-grid grid-3">{pasos}
            </div>
        </div>
    </section>
{captura}
    <section class="nosotros" id="que-obtienes">
        <div class="container">
            <div class="nosotros-content sol-columnas">
                <div>
                    <h2 style="font-size: 32px; margin-bottom: 24px; text-align: left;">Qué obtienes</h2>
                    <ul class="lista-check">{obtienes}
                    </ul>
                </div>
                <div>
                    <h3>Dónde se usa</h3>
                    <div class="chips">{usos}
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="precio-seccion" id="precio">
        <div class="container">
            <div class="precio-box">
                <h2>¿Cuánto cuesta?</h2>
                <p>{e(PRECIO)}</p>
                <a href="{e(wa_link(s['wa']))}" class="btn-cta btn-claro" target="_blank" rel="noopener">Cotizar por WhatsApp</a>
            </div>
        </div>
    </section>

    <section class="soluciones" id="otras">
        <div class="container">
            <h2>Otras soluciones</h2>
            <div class="soluciones-grid grid-3">{otras}
            </div>
        </div>
    </section>
{pie()}"""


# ============================================================
# INDICE /soluciones/
# ============================================================

def indice():
    url = f"{SITIO}/soluciones/"
    ruta = [("Inicio", f"{SITIO}/"), ("Soluciones", url)]
    wa = "Hola, quiero saber si IoT Link tiene una solución para mi caso."
    description = ("Soluciones IoT en Medellín y Colombia: monitoreo de temperatura y humedad, "
                   "nivel de tanques, rastreo GPS de vehículos y automatización con dashboards a medida.")

    lista = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": s["nombre"],
             "url": f"{SITIO}/soluciones/{s['slug']}/"}
            for i, s in enumerate(SOLUCIONES)
        ]
    }

    tarjetas = "".join(tarjeta(s) for s in SOLUCIONES)

    return f"""{head("Soluciones IoT en Medellín | IoT Link", description, url, [breadcrumb_ld(ruta), lista])}
<body data-wa="{e(wa)}">
    <div id="site-header"></div>

    <section class="hero sol-hero">
        <div class="hero-bg-full">
            <div class="container">
                {migas([("Inicio", "/"), ("Soluciones", None)])}
                <h1 class="hero-title">
                    Soluciones IoT
                    <span class="title-highlight">para controlar tu operación</span>
                </h1>
                <p class="hero-description">Instalamos los sensores, los conectamos a la plataforma y te damos un tablero para verlo todo desde el celular. Elige la solución que necesitas.</p>
            </div>
        </div>
    </section>

    <section class="soluciones" id="lista">
        <div class="container">
            <h2>Nuestras soluciones</h2>
            <div class="soluciones-grid">{tarjetas}
            </div>
        </div>
    </section>

    <section class="precio-seccion">
        <div class="container">
            <div class="precio-box">
                <h2>¿Tu caso no está en la lista?</h2>
                <p>Cuéntanos qué necesitas medir o controlar y te decimos si lo podemos hacer.</p>
                <a href="{e(wa_link(wa))}" class="btn-cta btn-claro" target="_blank" rel="noopener">Escríbenos por WhatsApp</a>
            </div>
        </div>
    </section>
{pie()}"""


def escribir(ruta_rel, html):
    ruta = os.path.join(RAIZ, ruta_rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ", ruta_rel)


def main():
    print("Generando páginas de soluciones:")
    escribir("soluciones/index.html", indice())
    for s in SOLUCIONES:
        escribir(f"soluciones/{s['slug']}/index.html", landing(s))
    print("Listo.")


if __name__ == "__main__":
    main()
