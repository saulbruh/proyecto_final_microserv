# 🎓 Gestión de Cursos en Línea (Proyecto Demo) - Flask + MySQL

Este proyecto permite gestionar cursos en línea donde **profesores** pueden crear cursos, y **estudiantes** pueden visualizarlos. Además, los **administradores** pueden gestionar usuarios y roles. Es el Proyecto 1 dentro de una colección de 11 proyectos desarrollados como práctica final para los estudiantes.

A continuación, capturas de algunas pantallas del front-end:

<figure class="image">
   <img src="images/image-01.png" alt="Login Form">
   <figcaption>Login Page</figcaption>
</figure>

<figure class="image">
   <img src="images/image-02.png" alt="Dashboard">
   <figcaption>Home Page / Dashboard</figcaption>
</figure>

<figure class="image">
   <img src="images/image-03.png" alt="User List">
   <figcaption>Registered Users</figcaption>
</figure>

## 🚀 Tecnologías utilizadas

- **Flask** – Framework backend en Python
- **Flask-Login** – Sistema de autenticación
- **MySQL** – Base de datos relacional
- **SQLAlchemy** – ORM para la base de datos
- **Bootstrap 5** – Framework CSS responsivo
- **Jinja2** – Motor de plantillas para HTML

---

## 📂 Estructura del proyecto

| Archivo / Carpeta                                                 | Descripción                                                                |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `create_demo_users.py`                                            | Script para crear usuarios iniciales con roles y contraseñas               |
| `config.py`                                                       | Configuración de Flask (DB URI, claves, etc.)                              |
| `README.md`                                                       | Este archivo de documentación del proyecto                                 |
| `requirements.txt`                                                | Lista de paquetes Python requeridos                                        |
| **`run.py`**                                                      | Punto de entrada para ejecutar el servidor Flask                           |
| `app/__init__.py`                                                 | Inicializa la aplicación Flask y carga la configuración                    |
| `app/models.py`                                                   | Contiene los modelos SQLAlchemy: User, Role, Curso                         |
| `app/forms.py`                                                    | Formularios de Flask-WTF usados en login, registro, cursos, contraseñas    |
| `app/routes.py`                                                   | Rutas principales del proyecto (dashboard, cursos, cambiar contraseña)     |
| `app/auth_routes.py`                                              | Rutas para autenticación (login, registro, logout)                         |
| `app/templates/layout.html`                                       | Plantilla base HTML con barra de navegación                                |
| `app/templates/index.html`                                        | Página de inicio pública del sitio                                         |
| `app/templates/login.html`                                        | Formulario de login de usuario                                             |
| `app/templates/register.html`                                     | Formulario de registro con selección de rol                                |
| `app/templates/dashboard.html`                                    | Panel principal del usuario autenticado                                    |
| `app/templates/curso_form.html`                                   | Formulario de creación/edición de cursos                                   |
| `app/templates/cursos.html`                                       | Vista de cursos creados por el usuario                                     |
| `app/templates/usuarios.html`                                     | Listado de usuarios con sus roles (solo para admins)                       |
| `app/templates/cambiar_password.html`                             | Formulario para cambiar la contraseña del usuario                          |
| `static/css/styles.css`                                           | Archivo CSS personalizado (opcional)                                       |
| `database_schema/01_cursos.sql`                                   | SQL para crear la base de datos y tablas del proyecto de cursos            |
| `database_schema/02_biblioteca.sql` – `11_biblioteca_digital.sql` | Archivos SQL de los esquemas de bases de datos de los proyectos asignables |

> Los archivos `.sql` en la carpeta `database_schema/` corresponden al esquema de base de datos para cada uno de estos proyectos.

---

## 📚 Proyectos Finales Asignables

Cada estudiante (o grupo) realizará uno de los siguientes proyectos como práctica final:

| Nº  | Proyecto                               | CRUD Principal    | Roles                            |
| --- | -------------------------------------- | ----------------- | -------------------------------- |
| 1   | Gestión de Cursos en Línea             | Cursos            | Estudiante, Profesor, Admin      |
| 2   | Gestor de Biblioteca                   | Libros            | Lector, Bibliotecario, Admin     |
| 3   | Gestor de Proyectos Freelance          | Proyectos         | Cliente, Freelancer, Admin       |
| 4   | Administrador de Eventos               | Eventos           | Participante, Organizador, Admin |
| 5   | Inventario Personal                    | Ítems/Productos   | Usuario, Dueño, Admin            |
| 6   | Sistema de Seguimiento de Tickets      | Tickets           | Usuario, Técnico, Admin          |
| 7   | Gestión de Consultas Médicas           | Citas médicas     | Paciente, Médico, Admin          |
| 8   | Plataforma de Publicación de Artículos | Artículos         | Autor, Editor, Admin             |
| 9   | Sistema de Encuestas y Votaciones      | Encuestas         | Votante, Moderador, Admin        |
| 10  | Gestor de Recetas Culinarias           | Recetas           | Usuario, Chef, Admin             |
| 11  | Gestión de Biblioteca Personal Digital | Libros personales | Lector, Moderador, Admin         |

> Los archivos `.sql` en la carpeta `database_schema/` corresponden al esquema de base de datos para cada uno de estos proyectos.

---

## 🧪 Requisitos previos

- Python 3.8 o superior
- MySQL Server corriendo localmente (`localhost:3306`)
- Un entorno virtual activo (recomendado)

---

## ⚙️ Instalación del proyecto

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/javierdastas/comp2052.git
   cd comp2052/final_project
   ```

2. **Crear entorno virtual y activarlo**

   > Todos los comandos en este paso 2 son opcionales. No requiere correrlos si VSCode no solicita hacerlo. Los comandos en este paso permitirán crear un ambiente virtual para instalar las librería requeridas solamente para este proyecto.

   ```bash
   python -m venv venv   # En Linux/Windows requiere esto
   ```

   ```bash
   python3 -m venv venv     # En Mac requiere esto
   ```

   > Para activar el virtual environment:

   ```bash
   venv\Scripts\activate.bat  # Solo para Windows
   ```

   ```bash
   source venv/bin/activate   # Solo en Linux/Mac requiere esto
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crear la base de datos en MySQL**

   > Para ejecutar el archivo SQL para el proyecto directamente en MySQL:

   ```bash
   mysql -u root -p < database_schema/01_cursos.sql
   ```

   > Puedes utilizar Visual Studio Code u otra herramienta gráfica que se conecte a tu DBMS (servidor) de MySQL y correr el archivo correspondiente al proyecto para crear tu base de datos:

   ```bash
   01_cursos.sql
   ```

5. **Crear usuarios de prueba**

   ```bash
   python create_demo_users.py
   ```

6. **Ejecutar la aplicación**

   ```bash
   python run.py
   ```

   > Luego abre en tu navegador:

   ```bash
   http://127.0.0.1:5000
   ```

## 👤 Credenciales de prueba

Estas credenciales puedes crearlas utilizano el archivo `create_demo_users.py`. De igual manera puedes modificar el archivo según los roles de tu proyecto.

| Rol        | Usuario       | Email               | Contraseña |
| ---------- | ------------- | ------------------- | ---------- |
| Admin      | Administrator | admin@example.com   | admin123   |
| Profesor   | John Doe      | prof@example.com    | prof123    |
| Estudiante | Steve Jobs    | student@example.com | student123 |

## 📌 Archivos a crear o modificar por el estudiante según el proyecto asignado

Puedes utilizar este proyecto de Gestión de Cursos en Línea como base para desarrollar cualquier otro proyecto asignado (por ejemplo: Recetas, Artículos, Tickets, etc.), debes crear o modificar los siguientes archivos:

| Archivo                              | Qué debes modificar o crear                                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app/models.py`                      | Renombrar el modelo Curso al nuevo recurso principal (e.g. Receta, Articulo). Cambiar atributos de la entidad principal según el nuevo CRUD.                                                                              |
| `app/forms.py`                       | Modificar CursoForm para reflejar los datos o campos de tu entidad principal. Especifica el tipo de control de entrada según corresponda al dato de tu entidad principal.                                                 |
| `app/routes.py`                      | Cambiar las rutas relacionadas con cursos (/cursos, /editar, /eliminar) al nuevo recurso. Asegúrate de actualizar las consultas y las plantillas usadas.                                                                  |
| `templates/curso_form.html`          | Renombrar el archivo (ej. receta_form.html) y cambia los datos (cajas de texto, etc.) o campos que se muestran en el formulario.                                                                                          |
| `templates/cursos.html`              | Renombrar el archivo (ej. recetas.html) y actualiza la tabla para mostrar los datos específicos de tu entidad principal (tabla).                                                                                          |
| `database_schema/XX_tu_proyecto.sql` | Verifica que el archivo .sql correspondiente a tu proyecto esté actualizado según los datos que solicitarás para tu proyecto. Puedes editarlo o usarlo como guía para crear la base de datos y las tablas de tu proyecto. |
| `create_demo_users.py`               | No es necesario modificar sino quieres crear usuarios previos a correr la aplicación. Pero puedes agregar datos iniciales para probar tu base de datos y conexión si lo deseas.                                           |
| `templates/dashboard.html`           | Cambiar los títulos o enlaces para que hagan referencia al nombre de tu entidad principal y proyecto.                                                                                                                     |
| `README.md`                          | Si haces un fork o copia del proyecto, personaliza este archivo con el nombre de tu proyecto final y la documentación correspondiente.                                                                                    |

## 🧠 Licencia

Este proyecto es de uso académico y puede ser reutilizado con fines educativos. El creador de este proyecto y la lista de proyectos es el profesor Javier A. Dastas de Ciencias de Computadoras.
