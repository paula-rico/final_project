Apps


product

Se ingresan los productos de la tienda, los campos son: name, price y category


store

Se ingresa la ubicacion de las tiendas fisicas, los campos son: name, address, city, region y postal_code


order

Se ingresan las ordenes de compra, los campos son: client, product y creation_time





HTML 

Se encuentran en la carpeta 'templates'. El archivo 'base' contiene la Navbar y search form que heredan los restantes archivos
Mediante la navbar se puede acceder al listado de productos, tiendas y ordenes

'index' es la pantalla incial que muestra las imagenes de los productos

Cada app tiene una subcarpeta, dentro de cada una de ellas hay dos archivos uno para crear registros y otro para listarlos




Apps order, product y store

Dentro de 'models.py' se encuentran las clases de cada app
En 'views.py' se crean dos vistas, una para crear registros y otra para listarlos
En 'forms.py' se crean los formularios para que los usuarios ingresen la informacion