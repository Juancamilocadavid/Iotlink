/* ============================================================
   Header y footer compartidos de IoT Link.
   ÚNICA fuente de verdad: edita aquí y TODAS las páginas
   se actualizan. Los placeholders <div id="site-header">
   y <div id="site-footer"> se rellenan al cargar.
   ============================================================ */
(function () {
    // ── CONFIGURACIÓN ────────────────────────────────────────
    // Número de WhatsApp en formato internacional SIN "+"
    // (Colombia = 57 + número). Vacío => el botón lleva al formulario.
    var WHATSAPP = '573246526040';

    // ID de Google Analytics 4 (formato 'G-XXXXXXXXXX').
    // Mientras esté vacío, NO se carga Analytics. Pega tu ID aquí
    // cuando crees la propiedad y empezarás a medir visitas.
    var GA_ID = '';
    // ─────────────────────────────────────────────────────────

    // Ruta actual normalizada (sin /index.html final).
    var path = location.pathname.replace(/index\.html$/, '');
    if (path.length > 1) path = path.replace(/\/$/, '/'); // mantener barra final
    var isHome = path === '/' || path === '';

    // En el home los anclajes hacen scroll suave; fuera del home
    // saltan primero a la home y luego a la sección.
    function sec(hash) { return isHome ? hash : '/' + hash; }

    // ¿La ruta actual coincide con este enlace? (estado activo)
    function active(match) {
        if (!match) return false;
        var p = path.replace(/\/$/, '');
        var m = match.replace(/\/$/, '');
        return p === m;
    }

    var navItems = [
        { label: 'Inicio',     href: isHome ? '#inicio' : '/', match: isHome ? null : '/' },
        { label: 'Nosotros',   href: sec('#nosotros'),         match: null },
        { label: 'Soluciones', href: sec('#soluciones'),       match: null },
        { label: 'Soporte',    href: sec('#soporte'),          match: null },
        { label: 'FAQ',        href: '/faq',                   match: '/faq' }
    ];

    var navLinks = navItems.map(function (i) {
        var cls = active(i.match) ? ' class="active" aria-current="page"' : '';
        return '<li><a href="' + i.href + '"' + cls + '>' + i.label + '</a></li>';
    }).join('\n                    ');

    var contactCls = 'btn-contacto' + (active('/contacto') ? ' active' : '');

    var headerHtml =
        '<header class="header">' +
        '<div class="container">' +
            '<div class="logo">' +
                '<a href="/" aria-label="IoT Link - Inicio" style="display:flex;align-items:center;">' +
                    '<img src="/imagenes/iotlink-logo.png" alt="IoT Link" class="logo-img">' +
                '</a>' +
            '</div>' +
            '<button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false">' +
                '<span></span><span></span><span></span>' +
            '</button>' +
            '<nav class="nav" aria-label="Navegación principal">' +
                '<ul>' +
                    navLinks +
                    '<li><a href="/contacto" class="' + contactCls + '">Contactar</a></li>' +
                    '<li><a href="https://app.iotlink.com.co/login" class="btn-contacto">Iniciar sesión</a></li>' +
                '</ul>' +
            '</nav>' +
        '</div>' +
        '</header>';

    var footerHtml =
        '<footer class="footer">' +
        '<div class="container">' +
            '<div class="footer-grid">' +
                '<div class="footer-col">' +
                    '<h4>IoT Link</h4>' +
                    '<p>Soluciones IoT innovadoras para tu negocio</p>' +
                '</div>' +
                '<div class="footer-col">' +
                    '<h4>Navegación</h4>' +
                    '<ul>' +
                        '<li><a href="' + sec('#inicio') + '">Inicio</a></li>' +
                        '<li><a href="' + sec('#nosotros') + '">Nosotros</a></li>' +
                        '<li><a href="' + sec('#soluciones') + '">Soluciones</a></li>' +
                        '<li><a href="' + sec('#soporte') + '">Soporte</a></li>' +
                        '<li><a href="/faq">FAQ</a></li>' +
                        '<li><a href="/testimonios">Testimonios</a></li>' +
                    '</ul>' +
                '</div>' +
                '<div class="footer-col">' +
                    '<h4>Contacto</h4>' +
                    '<p class="footer-contact-text"><strong>Email:</strong> <a href="mailto:contacto@iotlink.com.co">contacto@iotlink.com.co</a></p>' +
                    '<p class="footer-contact-text"><strong>Proyectos:</strong> <a href="mailto:proyectos@iotlink.com.co">proyectos@iotlink.com.co</a></p>' +
                    '<a href="/contacto" class="footer-contact-btn">Enviar Mensaje</a>' +
                '</div>' +
                '<div class="footer-col">' +
                    '<h4>Legal</h4>' +
                    '<ul>' +
                        '<li><a href="/privacidad">Política de Privacidad</a></li>' +
                        '<li><a href="/terminos">Términos y Condiciones</a></li>' +
                        '<li><a href="/cookies">Política de Cookies</a></li>' +
                        '<li><a href="/legal">Información Legal</a></li>' +
                        '<li><a href="/datos">Datos y Protección</a></li>' +
                        '<li><a href="/seguridad">Seguridad</a></li>' +
                    '</ul>' +
                '</div>' +
            '</div>' +
            '<div class="footer-bottom">' +
                '<p>&copy; 2026 IoT Link. Todos los derechos reservados.</p>' +
            '</div>' +
        '</div>' +
        '</footer>';

    var headerSlot = document.getElementById('site-header');
    if (headerSlot) headerSlot.outerHTML = headerHtml;

    var footerSlot = document.getElementById('site-footer');
    if (footerSlot) footerSlot.outerHTML = footerHtml;

    // Botón flotante de contacto (WhatsApp si hay número, si no al formulario)
    var floatHref, floatIcon, floatLabel;
    if (WHATSAPP) {
        floatHref = 'https://wa.me/' + WHATSAPP + '?text=' +
            encodeURIComponent('Hola, me interesa una demo de IoT Link.');
        floatIcon = '💬';
        floatLabel = 'WhatsApp';
    } else {
        floatHref = '/contacto';
        floatIcon = '💬';
        floatLabel = 'Escríbenos';
    }
    var fab = document.createElement('a');
    fab.className = 'float-cta';
    fab.href = floatHref;
    if (WHATSAPP) { fab.target = '_blank'; fab.rel = 'noopener'; }
    fab.setAttribute('aria-label', floatLabel);
    fab.innerHTML = '<span class="float-icon">' + floatIcon + '</span>' +
                    '<span class="float-label">' + floatLabel + '</span>';
    document.body.appendChild(fab);

    // Datos estructurados (JSON-LD) para Google — mejora cómo apareces
    // en los resultados de búsqueda. Una sola fuente para todas las páginas.
    var orgLd = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "IoT Link",
        "url": "https://iotlink.com.co",
        "logo": "https://iotlink.com.co/imagenes/iotlink-logo.png",
        "description": "Soluciones IoT para monitoreo, automatización y analítica en tiempo real para empresas e industria.",
        "email": "contacto@iotlink.com.co",
        "telephone": "+57 324 652 6040",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Medellín",
            "addressRegion": "Antioquia",
            "addressCountry": "CO"
        },
        "areaServed": "CO",
        "sameAs": []
    };
    var ldEl = document.createElement('script');
    ldEl.type = 'application/ld+json';
    ldEl.textContent = JSON.stringify(orgLd);
    document.head.appendChild(ldEl);

    // Google Analytics 4 (solo si se configuró GA_ID)
    if (GA_ID) {
        var ga = document.createElement('script');
        ga.async = true;
        ga.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
        document.head.appendChild(ga);
        window.dataLayer = window.dataLayer || [];
        function gtag() { window.dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', GA_ID);
    }

    // Menú hamburguesa (móvil)
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.nav');
    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            var open = nav.classList.toggle('open');
            toggle.classList.toggle('open', open);
            toggle.setAttribute('aria-expanded', String(open));
        });
        // Cerrar el menú al pulsar un enlace
        nav.querySelectorAll('a').forEach(function (a) {
            a.addEventListener('click', function () {
                nav.classList.remove('open');
                toggle.classList.remove('open');
                toggle.setAttribute('aria-expanded', 'false');
            });
        });
    }
})();
