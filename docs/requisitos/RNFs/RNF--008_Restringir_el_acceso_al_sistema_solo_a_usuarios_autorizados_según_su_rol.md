
# RNF-008 — Restricción de acceso según roles

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-008 |
| **Nombre** | Restricción de acceso según roles |
| **Categoría** | Seguridad y control de acceso |
| **Prioridad** | Crítica |
| **Estado** | Por validar |

---

## Requisitos

### RNF-008.1 — Control de permisos

Hardwarex debe controlar el acceso a sus funcionalidades de acuerdo con el rol asignado a cada usuario.

### RNF-008.2 — Rol administrador

El administrador debe tener acceso a las funciones de gestión de usuarios, equipos, proveedores, garantías, mantenimientos y reportes.

### RNF-008.3 — Rol técnico

El técnico debe acceder a las funciones relacionadas con la consulta de equipos, solicitudes asignadas y gestión de mantenimientos.

### RNF-008.4 — Rol usuario

El usuario debe poder consultar los equipos autorizados y registrar reportes de fallas y solicitudes de mantenimiento.

### RNF-008.5 — Restricción de funcionalidades

El sistema debe impedir que un usuario acceda a funciones que no correspondan a los permisos de su rol, incluso si intenta ingresar directamente mediante una URL o solicitud a la API.
