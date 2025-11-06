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

El proyecto inicial contaba con dos contenedores de Docker. En el primero se ejecutaba la aplicación, creada en Python usando Flask, mientras que en el segundo se ejecutaba la base de datos en MySQL. Se articulaban usando un Docker Compose.

## Compilación y ejecución

Anteriormente el proyecto se ejecutaba en una única máquina virtual usando el comando ```docker compose up```.

Actualmente el proyecto se ejecuta utilizando dos máquinas vituales de AWS EC2. En la primera se ejecuta la app, el proxy NGINX, el SSL y el dominio, mientras que en la segunda se ejecuta la base de datos MySQL. Se configuró el Docker Compose.

## Detalles del desarrollo



## Detalles técnicos
## Configuración de los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)



## Resultados

# 4. Ambiente de ejecución

## IP o nombres de dominio en nube o en la máquina servidor.

## Configuración de los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## Ejecución del servidor en nube

## Guía de uso

Al entrar a la plataforma Bookstore, lo primero que aparece es un menú con 3 opciones: "Ver catálogo de libros", "Ver mis libros" y "Listar usuarios registrados".

Al presionar "Ver catálogo de libros", aparecerá un listado de todos los libros con su título, autor, precio y unidades disponibles. Adicionalmente aparecerá un campo de cantidad donde se puede comprar.

Al presionar "Ver mis libros" se debe iniciar sesión para obtener la información de los libros que ha adquirido el usuario.

Al presionar "Listar usuarios registrados" se debe iniciar sesión para obtener la información de los usuarios registrados en la plataforma.

## Resultados 



# 5. Información adicional

# Referencias:
Bookstore original: https://github.com/st0263eafit/st0263-252/blob/main/proyecto2/BookStore.zip

