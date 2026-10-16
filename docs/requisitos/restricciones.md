
# Restricciones del Proyecto — Hardwarex

---

## 1. Restricciones Tecnológicas

---

### RT-001 — Tecnología del backend

El backend de Hardwarex debe desarrollarse con las tecnologías definidas para el proyecto. Si se mantiene la implementación actual, se utilizará **Python** como lenguaje de programación y **Django** como framework web.

No se deben incorporar otros frameworks de backend sin la aprobación del equipo de desarrollo.

### RT-002 — Tecnologías del frontend

La interfaz de Hardwarex debe desarrollarse con tecnologías web compatibles con la arquitectura seleccionada, como **HTML, CSS y JavaScript**.

No se deben incorporar frameworks adicionales que generen incompatibilidades con la estructura existente.

### RT-003 — Base de datos

La información de Hardwarex debe almacenarse en una **base de datos relacional** compatible con el backend del proyecto. La base de datos debe permitir administrar usuarios, roles, equipos, fallas, mantenimientos, garantías y proveedores.

No se deben utilizar diferentes motores de bases de datos sin justificar y aprobar el cambio.

### RT-004 — Arquitectura del sistema

Hardwarex debe conservar una arquitectura organizada que permita separar la presentación, la lógica de negocio y el acceso a los datos.

No se deben mezclar indiscriminadamente las consultas a la base de datos, las validaciones y la presentación de información en un mismo componente.

### RT-005 — Gestión de usuarios y autenticación

El sistema debe contar con mecanismos de autenticación y autorización que permitan controlar el ingreso y las acciones disponibles para cada usuario.

Los permisos deben diferenciar los roles definidos en el proyecto: **administrador, técnico y usuario**.

---

## 2. Restricciones de Herramientas y Entorno

---

### RH-001 — Entorno de desarrollo

El desarrollo de Hardwarex debe realizarse en el entorno de programación definido por el equipo, utilizando herramientas compatibles con las tecnologías seleccionadas.

Cualquier modificación en la configuración del entorno debe documentarse para facilitar la instalación y ejecución del proyecto.

### RH-002 — Control de versiones

El código fuente y la documentación del proyecto deben mantenerse en el repositorio de **GitHub** correspondiente a Hardwarex.

Los cambios deben realizarse mediante Git, utilizando mensajes de confirmación claros que permitan identificar las modificaciones realizadas.

### RH-003 — Organización del código

Los archivos del proyecto deben organizarse en carpetas según su función, separando los componentes de la aplicación, las plantillas, los archivos estáticos, las configuraciones y la documentación.

No se deben guardar archivos temporales, duplicados o innecesarios dentro del repositorio.

### RH-004 — Herramientas de desarrollo

Las herramientas utilizadas para programar, probar y documentar Hardwarex deben ser compatibles con las tecnologías seleccionadas para el proyecto.

### RH-005 — Gestión de dependencias

Las librerías y paquetes utilizados por Hardwarex deben registrarse en los archivos de configuración correspondientes para permitir que otros integrantes del equipo instalen las dependencias necesarias.

---

## 3. Restricciones de Diseño Visual

---

### RD-001 — Identidad visual

La interfaz de Hardwarex debe conservar una apariencia coherente con la identidad visual definida para el proyecto, utilizando principalmente tonos azules y colores complementarios que faciliten la lectura.

### RD-002 — Diseño adaptable

Las páginas deben permitir la consulta y gestión de la información desde diferentes tamaños de pantalla, especialmente computadores y dispositivos móviles.

### RD-003 — Consistencia de la interfaz

Los botones, formularios, mensajes de confirmación, alertas y elementos de navegación deben mantener estilos y comportamientos consistentes en los diferentes módulos.

### RD-004 — Facilidad de uso

La plataforma debe presentar nombres claros para las opciones y acciones disponibles, de manera que el administrador, el técnico y el usuario puedan identificar fácilmente las funciones correspondientes a su rol.

### RD-005 — Validación visual de acciones

Las operaciones importantes, como registrar equipos, reportar fallas, asignar mantenimientos y modificar estados, deben mostrar mensajes que informen si la acción se realizó correctamente o si ocurrió un error.

---

## 4. Restricciones de Idioma

---

### RI-001 — Nombres del código fuente

Los nombres de variables, funciones, clases, métodos y archivos de código deben seguir una convención uniforme de nomenclatura.

### RI-002 — Documentación en español

Los documentos de requisitos, historias de usuario, manuales y demás entregables académicos de Hardwarex deben redactarse en español.

### RI-003 — Interfaz en español

Los textos visibles para los usuarios, incluidos los menús, formularios, botones, mensajes de error y notificaciones, deben presentarse en español.

---

## 5. Restricciones Organizacionales

---

### RO-001 — Proyecto educativo del SENA

Hardwarex se desarrolla como parte del proceso formativo del SENA. Su construcción debe cumplir los objetivos de aprendizaje y los entregables establecidos para el proyecto.

### RO-002 — Alcance del proyecto

La implementación debe centrarse en las funcionalidades definidas para la gestión de equipos tecnológicos, usuarios, reportes de fallas, solicitudes de mantenimiento, garantías y proveedores.

### RO-003 — Trabajo colaborativo

Los integrantes del equipo deben mantener comunicación sobre los cambios realizados en el código, los requisitos y la documentación.

### RO-004 — Control de cambios

Las modificaciones a los requisitos, las funcionalidades o la estructura del proyecto deben registrarse y revisarse para determinar su impacto en los demás componentes.

### RO-005 — Entorno de ejecución

Durante la etapa de desarrollo y formación, Hardwarex debe poder ejecutarse en el entorno local configurado por el equipo.

### RO-006 — Pruebas del sistema

Las funcionalidades implementadas deben someterse a pruebas para verificar que cumplen los requisitos establecidos.

---

## 6. Restricciones de Seguridad

---

### RS-001 — Protección de credenciales

Las contraseñas deben almacenarse utilizando los mecanismos seguros de hashing que ofrece el framework de autenticación seleccionado.

### RS-002 — Protección de información sensible

Las claves secretas, contraseñas de bases de datos y demás credenciales deben mantenerse fuera del código fuente y del repositorio público.

### RS-003 — Validación de datos

Los datos ingresados en los formularios deben validarse antes de ser procesados o almacenados.

### RS-004 — Control de acceso por roles

Cada usuario debe acceder únicamente a las funciones y a la información que le correspondan según sus permisos.

### RS-005 — Protección contra intentos fallidos

El sistema debe implementar controles para limitar los intentos fallidos de inicio de sesión, de acuerdo con el requisito establecido de bloqueo después de tres intentos.

### RS-006 — Protección de la base de datos

Las operaciones de consulta, creación, modificación y eliminación deben realizarse mediante los mecanismos seguros proporcionados por las tecnologías utilizadas.

### RS-007 — Copias de seguridad

La información almacenada debe contar con un procedimiento de respaldo acorde con los recursos disponibles para el proyecto.

### RS-008 — Manejo de errores

Los mensajes de error que se muestran al usuario no deben revelar contraseñas, credenciales, claves secretas ni detalles sensibles de la configuración.

### RS-009 — Protección de la información de los equipos

Los datos técnicos, las fallas reportadas, el historial de mantenimientos y la información de las garantías deben estar disponibles únicamente para los usuarios autorizados.
