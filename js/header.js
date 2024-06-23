document.addEventListener("DOMContentLoaded", function () {
    function getHeader() {
        return `
        <div class="logo">
        <a href="../index.html">
            <img src="../static/imgs/logonuevo_1-sin-fondo.png" alt="logo-catorce" />
        </a>
        </div>
        <!--menu hamburguesa-->
        <button class="menu-btn" aria-label="Abrir menú">
            <span class="menu-btn_bar"></span>
            <span class="menu-btn_bar"></span>
            <span class="menu-btn_bar"></span>
        </button>
        <nav class=nav-menu>
            <a href="../index.html">Inicio</a>
            <a href="../templates/destinos.html">Destinos</a>
            <a href="../templates/galería.html">Galería</a>
            <a href="../templates/contacto.html">Contacto</a>
        </nav>`;
    }

    const headerElement = document.querySelector("header");

    if (headerElement) {
        headerElement.innerHTML = getHeader();
    } else {
        console.error("No se encontró el elemento <header> en el DOM.")
    }

})
