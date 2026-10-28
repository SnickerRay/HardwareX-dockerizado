# HardwareX

**Sistema web para la gestión de equipos, solicitudes de mantenimiento y seguimiento de reparaciones.**

HardwareX es una aplicación web orientada a apoyar a las empresas en la administración de sus equipos y procesos de mantenimiento. El proyecto organiza las funcionalidades relacionadas con usuarios, equipos, piezas, solicitudes, mantenimientos y reportes.

Actualmente, el proyecto utiliza Django como framework del backend, PostgreSQL como base de datos y Docker Compose para ejecutar los servicios.

## Responsable del proyecto

**Iker Romero — [@SnickerRay](https://github.com/SnickerRay)**

Propietario actual del repositorio y líder técnico de HardwareX.

Repositorio: [SnickerRay/HardwareX-dockerizado](https://github.com/SnickerRay/HardwareX-dockerizado)

> HardwareX fue iniciado originalmente por Juan José Fuentes (@Dova68) y ha continuado evolucionando mediante el trabajo y las contribuciones del equipo.

## Tabla de contenido

- [HardwareX](#hardwarex)
  - [Responsable del proyecto](#responsable-del-proyecto)
  - [Tabla de contenido](#tabla-de-contenido)
  - [Tecnologías](#tecnologías)
  - [Módulos del sistema](#módulos-del-sistema)
  - [Requisitos previos](#requisitos-previos)
  - [Instalación y ejecución](#instalación-y-ejecución)
    - [1. Clonar el repositorio](#1-clonar-el-repositorio)
    - [2. Entrar en el proyecto](#2-entrar-en-el-proyecto)
    - [3. Configurar las variables de entorno](#3-configurar-las-variables-de-entorno)
    - [4. Iniciar los servicios](#4-iniciar-los-servicios)
    - [5. Verificar el estado de los contenedores](#5-verificar-el-estado-de-los-contenedores)
    - [6. Aplicar migraciones pendientes](#6-aplicar-migraciones-pendientes)
    - [7. Abrir la aplicación](#7-abrir-la-aplicación)
  - [Base de datos](#base-de-datos)
    - [Comandos de administración](#comandos-de-administración)
    - [Copias de seguridad y restauración](#copias-de-seguridad-y-restauración)
  - [Pruebas](#pruebas)
  - [Estructura del proyecto](#estructura-del-proyecto)
  - [Acceso por roles](#acceso-por-roles)
  - [Contribución](#contribución)
  - [Equipo](#equipo)
  - [Licencia](#licencia)

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lenguaje del backend. |
| Django | Framework de desarrollo web. |
| Django REST Framework | Herramientas para el desarrollo de API. |
| PostgreSQL | Sistema de gestión de bases de datos. |
| Psycopg | Conexión entre Python y PostgreSQL. |
| Gunicorn | Servidor de aplicaciones Python. |
| WhiteNoise | Gestión de archivos estáticos en el despliegue. |
| Docker | Ejecución de servicios en contenedores. |
| Docker Compose | Configuración y coordinación de los servicios. |
| HTML, CSS y JavaScript | Tecnologías de la interfaz web. |

Las dependencias de Python se encuentran declaradas en `backend/requirements.txt`.

## Módulos del sistema

El backend está organizado en seis aplicaciones funcionales:

- **Usuarios (`usuarios`):** funcionalidades relacionadas con usuarios, registro y autenticación.
- **Equipos (`equipos`):** módulo para la gestión de equipos.
- **Piezas (`piezas`):** módulo para la gestión de piezas.
- **Solicitudes (`solicitudes`):** gestión de solicitudes relacionadas con los procesos de mantenimiento.
- **Mantenimientos (`mantenimientos`):** funcionalidades relacionadas con el mantenimiento de equipos.
- **Reportes (`reportes`):** funcionalidades relacionadas con los reportes del sistema.

Las operaciones disponibles y los permisos aplicables dependen de la implementación de cada módulo.

## Requisitos previos

Antes de ejecutar el proyecto, instala:

- [Git](https://git-scm.com/).
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) o Docker Engine con Docker Compose.
- Un editor de código, como [Visual Studio Code](https://code.visualstudio.com/).

Con la configuración de Docker Compose, no necesitas instalar PostgreSQL directamente en tu equipo.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/SnickerRay/HardwareX-dockerizado.git
```

### 2. Entrar en el proyecto

```bash
cd HardwareX-dockerizado
```

### 3. Configurar las variables de entorno

Crea tu archivo `.env` a partir de la plantilla incluida:

En PowerShell:

```powershell
Copy-Item .env.example .env
```

En Linux o macOS:

```bash
cp .env.example .env
```

Edita el archivo `.env` y configura las siguientes variables:

| Variable | Descripción |
|---|---|
| `DB_NAME` | Nombre de la base de datos. |
| `DB_USER` | Usuario de PostgreSQL. |
| `DB_PASSWORD` | Contraseña del usuario de PostgreSQL. |
| `DB_HOST` | Host de la base de datos. |
| `DB_PORT` | Puerto de conexión a PostgreSQL. |
| `DJANGO_ALLOWED_HOSTS` | Hosts permitidos para Django. |

La plantilla contiene valores de ejemplo. Sustituye la contraseña de ejemplo por una contraseña segura antes de utilizar el entorno.

**Importante:** no publiques ni compartas tu archivo `.env`. Este archivo puede contener credenciales privadas y está excluido del control de versiones mediante `.gitignore`.

### 4. Iniciar los servicios

Comprueba que Docker esté ejecutándose y ejecuta:

```bash
docker compose up --build -d
```

Docker Compose construirá la imagen de la aplicación cuando corresponda e iniciará los servicios definidos en `compose.yaml`.

### 5. Verificar el estado de los contenedores

```bash
docker compose ps
```

El servicio de PostgreSQL incluye una comprobación de salud. La aplicación web depende de que la base de datos alcance el estado saludable antes de iniciarse.

### 6. Aplicar migraciones pendientes

```bash
docker compose exec web python manage.py migrate
```

Este comando aplica las migraciones pendientes de Django. No restaura automáticamente una copia de seguridad ni recupera datos de una base anterior.

### 7. Abrir la aplicación

Visita:

[http://localhost:8000](http://localhost:8000)

La aplicación estará disponible si los servicios están activos y la configuración del entorno es correcta.

## Base de datos

HardwareX utiliza PostgreSQL mediante el servicio `db` definido en `compose.yaml`.

La configuración incluye:

- Un servicio de PostgreSQL.
- Un servicio web para la aplicación Django.
- Un volumen persistente llamado `pgdata`.
- Una comprobación de salud para PostgreSQL.
- Una dependencia entre el servicio web y la disponibilidad de la base de datos.

### Comandos de administración

Consultar el estado de los servicios:

```bash
docker compose ps
```

Consultar los registros de Django:

```bash
docker compose logs web
```

Consultar los registros de PostgreSQL:

```bash
docker compose logs db
```

Detener los servicios sin eliminar los datos:

```bash
docker compose stop
```

Iniciar nuevamente los servicios detenidos:

```bash
docker compose start
```

### Copias de seguridad y restauración

Si necesitas recuperar datos desde una copia de seguridad, verifica el formato del archivo y prepara la base de datos de destino antes de restaurar.

Antes de restaurar sobre una base que ya contiene información importante, realiza una copia de seguridad de su estado actual.

**Advertencia:** evita ejecutar `docker compose down -v` si necesitas conservar los datos almacenados en el volumen de PostgreSQL, porque ese comando elimina los volúmenes asociados al proyecto.

## Pruebas

El proyecto incluye pruebas automatizadas mediante el sistema de pruebas de Django.

Para ejecutarlas dentro del contenedor web:

```bash
docker compose exec web python manage.py test
```

Durante la verificación local del proyecto se ejecutaron **32 pruebas**, que finalizaron con el resultado `OK`. Esta comprobación corresponde al estado del código en el momento de la ejecución y no garantiza que futuras modificaciones mantengan el mismo resultado.

## Estructura del proyecto

La estructura principal del repositorio es la siguiente:

```text
HardwareX-dockerizado/
├── backend/
│   ├── apps/
│   │   ├── equipos/
│   │   ├── mantenimientos/
│   │   ├── piezas/
│   │   ├── reportes/
│   │   ├── solicitudes/
│   │   └── usuarios/
│   ├── config/
│   ├── core/
│   ├── tests/
│   ├── manage.py
│   └── requirements.txt
├── frontend/
│   ├── static/
│   └── templates/
├── docs/
├── backups/
├── .env.example
├── .gitignore
├── AGENT.md
├── compose.yaml
├── LICENSE
└── README.md
```

`backups/` corresponde a las copias de seguridad locales y está excluida del control de versiones. La carpeta puede no existir en una instalación recién clonada.

## Acceso por roles

El flujo de acceso documentado en la implementación utiliza el identificador de rol del usuario autenticado para determinar el destino correspondiente:

| Identificador | Destino |
|---|---|
| `1` | `admin_home` |
| `2` | `reportes` |
| `3` | `tecnico` |

Las vistas administrativas deben comprobar la sesión y el rol en el servidor. Ocultar enlaces en la interfaz no sustituye la autorización del lado del servidor.

El flujo documentado también contempla que el registro público cree usuarios con el rol `2`.

Esta descripción debe mantenerse actualizada conforme cambie la implementación del sistema.

## Contribución

Para contribuir al proyecto:

1. Clona el repositorio.
2. Crea una rama independiente para tu tarea.
3. Realiza los cambios respetando la arquitectura y las instrucciones del proyecto.
4. Ejecuta las pruebas pertinentes.
5. Revisa los cambios antes de crear un Pull Request.
6. Describe los archivos modificados, las decisiones tomadas y las verificaciones realizadas.

Consulta `AGENT.md` antes de realizar cambios importantes. Este archivo contiene las reglas de trabajo y las restricciones específicas del repositorio.

## Equipo

- **Iker Romero — [@SnickerRay](https://github.com/SnickerRay):** propietario actual del repositorio y líder técnico.
- **Tania Castiblanco:** integrante del equipo.
- **Adriana Buitrago:** integrante del equipo.
- **Juan José Fuentes — [@Dova68](https://github.com/Dova68):** creador original del repositorio y colaborador.

## Licencia

Este proyecto incluye un archivo `LICENSE` que declara la licencia MIT. Consulta dicho archivo para conocer sus términos y el aviso de copyright correspondiente.
