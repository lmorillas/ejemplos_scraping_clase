'''
# Objetivo
Leer lista de películas de nuestro CMS wagtail

La url es http://localhost:8000/admin/pelis/pelicula/ pero
hay que estar autenticados.

Si inspeccionamos el formulario de login http://localhost:8000/admin/login/, 
vemos que hacen falta 3 input:
* csrfmiddlewaretoken
* login
* password
Para obtener el csrfmiddleware hay que hacer antes un get a la página
de login usando una sesión.

Crear fichero .env con 

```
username=usuario
password=password
```

'''

import requests
from lxml import html
import dotenv
import os

url = "http://localhost:8000/admin/pelis/pelicula/"
urllogin = "http://localhost:8000/admin/login/"

dotenv.load_dotenv()  # carga fichero .env

sesion = requests.session()

datos = {}
datos["username"] = os.getenv('username')
datos["password"] = os.getenv('password')

respuesta = sesion.get(url)
doc = html.fromstring(respuesta.content)
csrf = doc.xpath("//input[@name='csrfmiddlewaretoken']/@value")[0]
datos["csrfmiddlewaretoken"] = csrf

resp = sesion.post(urllogin, data=datos)

# Ahora ya podemos acceder al admin
resp = sesion.get("http://localhost:8000/admin/pelis/pelicula/")

doc = html.fromstring(resp.content)
pelis = [t.text_content() for t in doc.xpath('//div[@class="title-wrapper"]')]
for p in pelis:
    print(p)