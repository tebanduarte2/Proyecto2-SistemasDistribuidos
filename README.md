# Sistemas Distribuidos - S2566-0672

# Estudiantes
| Estudiante            | Correo                 |
|-----------------------|------------------------|
| John Esteban Duarte   | jeusugad@eafit.edu.co  |
| Nathaly Ramirez Henao | nramirezh@eafit.edu.co |
| Gia Mariana Calle      | gmcalleh@eafit.edu.co  |
# Profesor
| Profesor            | Correo                 |
|-----------------------|------------------------|
| Edwin Nelson Montoya  | emontoya@eafit.edu.co  |

# Proyecto 2 - Sistemas Distribuidos

# 1. Breve descripción de la actividad
El proyecto tiene como objetivo utilizar los conceptos aprendidos en el curso para realizar 4 objetivos relacionados a una plataforma llamada BookStore, una aplicación monolítica. Nuestro objetivo es transformar esta aplicación monolítica que se ejecuta en una máquina con Docker y convertirla en una aplicación desplegada en un dominio propio, con certificación SSL, proxy inverso y escalamiento.

## 1.1. Objetivos cumplidos

## 1.2. Objetivos no cumplidos

# 2. Diseño, arquitectura, patrones y buenas prácticas

Inicialmente se contó con una aplicación monolítica que se ejecutaba en una sola máquina. Esta práctica, si bien rápida y suficiente para un desarrollo inicial, es inviable si se desea llevar el proyecto a mayor escala, ya que ejecutar la aplicación en una sola máquina viola los principios de los sistemas distribuidos y nos hace propensos a grandes fallos que pueden afectar el sistema.

Al ejecutarse en dos máquinas, se están teniendo en cuenta principios como la concurrencia, la tolerancia a fallos, la transparencia y el balanceo de carga.

# 3. Ambiente de desarrollo y técnico

El proyecto inicial contaba con dos contenedores de Docker. En el primero se ejecutaba la aplicación, creada en Python usando Flask, mientras que en el segundo se ejecutaba la base de datos en MySQL. Se articulaban usando Docker Compose.

## Compilación y ejecución

Anteriormente el proyecto se ejecutaba en una única máquina virtual usando el comando ```docker compose up```.

Actualmente el proyecto se ejecuta utilizando dos máquinas vituales de AWS EC2. En la primera se ejecuta la app, el proxy NGINX, el SSL y el dominio, mientras que en la segunda se ejecuta la base de datos MySQL. Se configuró usando los Docker Compose.

## Configuración de los parámetros del proyecto
En ambas máquinas fue necesario habilitar el puerto 22 para conectarnos a través de SSH desde nuestra dirección IP.
El puerto que utilizamos para hacer la conexión entre las máquinas virtuales de la app y de la base de datos es el puerto 3306 a través de la IP 172.31.30.49, configuración que hicimos en la máquina virtual de la base de datos. 
Finalmente, se habilitaron los puertos 443, 80 y 5000 en la aplicación para conectarse a internet usado HTTPS, HTTP y TCP respectivamente.

## Resultados

<img width="1648" height="754" alt="image" src="https://github.com/user-attachments/assets/ccfe970f-7ce1-4fe8-b87c-b7d3069e3280" />

<img width="1654" height="765" alt="image" src="https://github.com/user-attachments/assets/5e76d9a0-fbf0-402a-bb32-cb6b2df23a7e" />

# 4. Ambiente de ejecución

## Dominio

El dominio que utilizamos para desplegar la aplicación es https://bookstoreeafit.giize.com/. Este es un dominio gratuito.

## Configuración de los parámetros del proyecto
En la máquina virtual de la aplicación se configuró una IP pública elástica debido a que era necesario que nuestro dominio apuntara siempre a nuestra IP pública.
IP Pública Elástica: 3.217.130.194/

## Guía de uso

Al entrar a la plataforma Bookstore, lo primero que aparece es un menú con 3 opciones: "Ver catálogo de libros", "Ver mis libros" y "Listar usuarios registrados".

Al presionar "Ver catálogo de libros", aparecerá un listado de todos los libros con su título, autor, precio y unidades disponibles. Adicionalmente aparecerá un campo de cantidad donde se puede comprar.

Al presionar "Ver mis libros" se debe iniciar sesión para obtener la información de los libros que ha adquirido el usuario.

Al presionar "Listar usuarios registrados" se debe iniciar sesión para obtener la información de los usuarios registrados en la plataforma.

## Resultados 

<img width="900" height="281" alt="image" src="https://github.com/user-attachments/assets/ab184ea3-2728-4749-9a03-fdab41dd6dc5" />

<img width="354" height="322" alt="image" src="https://github.com/user-attachments/assets/ada3656c-a317-4c81-abf7-b5114cae22a4" />

<img width="917" height="249" alt="image" src="https://github.com/user-attachments/assets/b1561000-a0e7-4cc6-8a8b-563e67f40e9a" />

<img width="921" height="306" alt="image" src="https://github.com/user-attachments/assets/e230f411-955d-4767-bf95-97d5ac087960" />

# 5. Información adicional

## Referencias:
Bookstore original: https://github.com/st0263eafit/st0263-252/blob/main/proyecto2/BookStore.zip

