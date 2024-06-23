document.addEventListener("DOMContentLoaded", function () {
    function getFooter() {
      return `
      <div class="footer-content">
  
              <!-- Columna 1 footer -->
              <div class="column">
                  <h3>Accesos</h3>
                  <ul>
                    <li><a href="../index.html">Inicio</a></li>
                    <li><a href="../templates/destinos.html">Destinos</a></li>
                    <li><a href="../templates/galería.html">Galeria</a></li>
                    <li><a href="../templates/contacto.html">Contacto</a></li>
                  </ul>
                  
                  <h3 class="seguinos">Seguinos en</h3>
                  
                  <a href="https://x.com/"><img class="icons" src="../static/imgs/gorjeo_blanco.png" alt="twitter"></a>
          <a href="https://web.facebook.com/"><img class="icons" src="../static/imgs/facebook_blanco.png" alt="facebook"></a>
          <a href="https://www.instagram.com/"><img class="icons" src="../static/imgs/instagram_blanco.png" alt="instagram"></a>
  
              </div>
  
              <!-- Columna 2 footer -->
              <div class="column">
                  <h3>Contacto</h3>
                   <div>
                      <div>
                        <dl>
                          <dt>
                            <img class="icon" src="../static/imgs/reloj_blanco.png" alt="" >
                             Horario de atención:
                          </dt>
                          <dd>Lunes a Sábados</dd>
                          <dd>De 9 a 12 hs y de 16 a 20 hs.</dd>
                          
                          <dt>
                            <img class="icon" src="../static/imgs/llamada-telefonica_blanco.png" alt="">
                            Teléfonos:
                          </dt>
                          <dd>(+54.11) 566.7184</dd>
                          <dd>(+54.11) 566.4255</dd>
                          
                          <dt>
                            <img class="icon" src="../static/imgs/correo-electronico_blanco.png"alt="">
                            Dirección de e-mail:
                          </dt>
                          <dd>catorce_viajes@gmail.com</dd>
                        </dl>
                      </div>
                    </div>
              </div>
              
  
              <!-- Columna 3 footer -->
              <div class="column">
                  <div>
                      <article>
                      <h3>Donde estamos:</h3>
                      <div class="map-container">
                          <iframe
                              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3284.989384528038!2d-58.437490025317416!3d-34.57913515619849!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcb593e76100f7%3A0x63591629e2c44a2b!2sSoler%205820%2C%20C1425BYL%20Cdad.%20Aut%C3%B3noma%20de%20Buenos%20Aires!5e0!3m2!1ses!2sar!4v1714589036380!5m2!1ses!2sar"
                              width="300"
                              height="300"
                              style="border: 0; border-radius: 5%"
                              allowfullscreen=""
                              loading="lazy"
                              referrerpolicy="no-referrer-when-downgrade"
                          ></iframe>
                      </div>
                      </article>
                    </div>
              </div>
      </div>
  
      <div class="footer-bottom">
        <p>&copy; 2024 GRUPO14FS. Todos los derechos reservados.</p>
        <p>Diseño web desarrollado por GRUPO14FS.</p>
      </div>`
    }
  
    const footerElement = document.querySelector("footer")
  
    if (footerElement) {
      footerElement.innerHTML = getFooter()
    } else {
      console.error("No se encontró el elemento <footer> en el DOM.")
    }
  })
  
  