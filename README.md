# IoT Link — Sitio web

Sitio estático (HTML/CSS/JS, sin framework) servido en **GitHub Pages** bajo `iotlink.com.co`.

---

## 🧱 Cómo está construido (importante)

El **header y el footer NO se editan en cada página**. Son una sola fuente de verdad en
[`components.js`](components.js), que rellena los `<div id="site-header">` y `<div id="site-footer">`
de cada página. **Si quieres cambiar el menú, el logo o el footer, edita solo `components.js`.**

- Logo único en todo el sitio: `imagenes/iotlink-logo.png`.
- El menú resalta la página activa y trae menú hamburguesa en celular.
- Botón flotante de WhatsApp en todas las páginas.

### Configuración rápida (arriba de `components.js`)

```js
var WHATSAPP = '573246526040';  // tu número (57 + número, sin "+")
var GA_ID    = '';              // ⬅️ PEGA AQUÍ tu ID de Google Analytics
```

---

## 🧩 Páginas de soluciones (se generan, no se editan a mano)

Las páginas `/soluciones/` y `/soluciones/<slug>/` salen de **una sola plantilla**:
[`_herramientas/generar_soluciones.py`](_herramientas/generar_soluciones.py).
Jekyll/GitHub Pages no publica carpetas que empiezan por `_`, así que el script no queda visible en el sitio.

```bash
# desde la raíz del repo (solo necesita Python 3, sin instalar nada)
python3 _herramientas/generar_soluciones.py
```

- **Cambiar un texto o agregar una solución:** edita la lista `SOLUCIONES` al inicio del script y vuelve a correrlo.
  Si los HTML de `soluciones/` se editan a mano, el script los sobrescribe.
- **Captura del dashboard:** guarda la imagen como `imagenes/soluciones/<slug>.jpg` y vuelve a correr el script.
  La landing la muestra sola; si no existe, queda un comentario HTML en su lugar.
- **Si agregas una solución:** súmala también a `SOLUCIONES` en `components.js` (footer) y a `sitemap.xml`.
  En el home, las tarjetas de `#soluciones` están escritas en el HTML (para que Google vea los enlaces).
- Slugs actuales: `monitoreo-temperatura-humedad`, `monitoreo-nivel-tanques`, `rastreo-gps`, `automatizacion-dashboards`.

---

## ✅ Lo que ya quedó hecho

- [x] Header/footer unificados (se acabó el menú distinto en cada página).
- [x] Logo consistente en todas las páginas.
- [x] **Responsive** en celulares (menú hamburguesa, formularios y secciones que se adaptan).
- [x] Botón flotante de **WhatsApp** (`324 652 6040`).
- [x] CTA más fuerte: "Agenda una demo gratis".
- [x] SEO: `title`, `description`, Open Graph y Twitter Card en todas las páginas.
- [x] **Imagen para compartir** (`imagenes/og-image.png`, 1200×630) — así se ve bonito al pegar el link en WhatsApp/LinkedIn.
- [x] Datos estructurados JSON-LD: empresa (`Organization`) en todo el sitio y `FAQPage` en la página de FAQ → posibles resultados enriquecidos en Google.
- [x] `robots.txt`, `sitemap.xml` y página `404.html`.
- [x] Google Analytics **cableado** (solo falta pegar el ID, ver abajo).
- [x] Una landing por solución (`/soluciones/...`) con datos estructurados `Service` y `BreadcrumbList`.
- [x] Se quitaron las afirmaciones que no se podían sostener (testimonios, 24/7, SLA, certificaciones, auditorías).

---

## 📋 Lo que tienes que hacer TÚ

### 1. Google Analytics 4 (medir visitas) — 10 min
1. Entra a https://analytics.google.com → crea una propiedad para `iotlink.com.co`.
2. Copia el **ID de medición** (formato `G-XXXXXXXXXX`).
3. Pégalo en [`components.js`](components.js): `var GA_ID = 'G-XXXXXXXXXX';`
4. Sube el cambio. Listo, empezarás a ver visitas.

### 2. Google Search Console (aparecer en Google) — 15 min
1. Entra a https://search.google.com/search-console → agrega `iotlink.com.co`.
2. Verifica la propiedad (te da un archivo o un registro DNS).
3. En "Sitemaps" envía: `https://iotlink.com.co/sitemap.xml`
4. Esto le dice a Google que indexe el sitio. Es lo que más ayuda a salir en búsquedas.

### 3. Perfil de Empresa en Google (Maps / búsquedas locales) — 20 min
1. Entra a https://business.google.com → crea el perfil de **IoT Link**, Medellín.
2. Categoría sugerida: "Servicio de tecnología" / "Empresa de software".
3. Agrega teléfono (324 652 6040), web, horario y fotos.
4. Esto te hace aparecer cuando busquen "IoT Medellín" y similares.

### 4. LinkedIn de empresa (canal B2B #1) — 20 min
1. Crea la **página de empresa** en LinkedIn.
2. Publica los casos de uso y, más adelante, los artículos del blog.
3. Es donde están los gerentes que compran soluciones IoT.

### 5. Redes sociales en el sitio (opcional)
Cuando tengas LinkedIn/Instagram, pásamelos y los agrego al footer y al JSON-LD
(campo `sameAs`), que también ayuda al SEO.

---

## 🚀 Ideas para captar más audiencia (orden recomendado)

1. **Contenido / blog**: 1 artículo cada 2 semanas con búsquedas reales:
   *"mantenimiento predictivo con IoT"*, *"monitoreo de plantas industriales"*, etc.
   Cada artículo atrae tráfico de Google a largo plazo.
2. **Casos de éxito reales con números**: "Reducimos X% el tiempo de inactividad".
   Vale más que cualquier texto de marketing.
3. **Capturas reales del dashboard** en cada landing (`imagenes/soluciones/<slug>.jpg`).
4. **Optimizar imágenes a WebP** para que el sitio cargue más rápido (Google premia la velocidad).

> Cualquiera de estos puntos te los puedo implementar; solo pídemelo.

---

## 💻 Desarrollo local

```bash
# desde la carpeta del proyecto
python -m http.server 8099
# abre http://localhost:8099
```

## 📁 Estructura

```
index.html            # Home
soluciones/           # GENERADO por _herramientas/generar_soluciones.py
_herramientas/        # Scripts (no se publican)
contacto/ faq/ ...    # Cada sección en su carpeta con index.html
components.js          # Header + footer + WhatsApp + Analytics (FUENTE ÚNICA)
script.js             # Animaciones y scroll suave
styles.css            # Estilos globales
imagenes/             # Logo, favicon, og-image, etc.
robots.txt sitemap.xml 404.html
```
