Mi nombre es Paula Rico y realice un proyecto de una pagina web con productos tecnologicos

Apps


product

Se ingresan los productos de la tienda, los campos son: name, price y category
Hay vistas para crear, listar, borrar y actualizar productos
Los botones para crear, actualizar o borrar productos esta solo disponible para el administrador
En forms se encuentran los formularios respectivos para que el usuario ingrese la informacion

store

Se ingresa la ubicacion de las tiendas fisicas, los campos son: name, address, city, region y postal_code
Hay vistas para crear y listar tiendas
El boton para crear tiendas esta solo disponible para el administrador
En forms se encuentran los formularios respectivos para que el usuario ingrese la informacion


order

Se ingresan las ordenes de compra, los campos son: client, product y creation_time
Hay vistas para crear y listar ordenes, el listado de ordenes es solo visible para el administrador
En forms se encuentran los formularios respectivos para que el usuario ingrese la informacion



user

Se encuentran las vistas de login y registro visibles si la persona no esta autenticada y de estarlo aparece la posibilidad de actualizar los datos de usuario y el perfil
En forms se encuentran los formularios respectivos para que el usuario ingrese la informacion




HTML 

Se encuentran en la carpeta 'templates'. El archivo 'base' contiene la Navbar y search form que heredan los restantes archivos
Mediante la navbar se puede acceder al listado de productos, tiendas y ordenes

'index' es la pantalla incial que muestra las imagenes de los productos en una galeria carousel

Cada app tiene una subcarpeta. 
Ordenes y Tiendas tienen dos templates para crear y listar los elementos. 
Productos en adicion a esos dor archivos tiene la posiblidad de Editar y borrar
Usuarios tiene el login, logout, registro, actualizar usuario y actualizar perfil

Ademas esta el archivo 'about_me' con mi informacion personal





