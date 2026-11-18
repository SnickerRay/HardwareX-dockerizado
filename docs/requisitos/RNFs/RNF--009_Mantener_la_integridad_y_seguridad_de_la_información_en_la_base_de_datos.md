
# RNF-009 — Integridad y seguridad de la base de datos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RNF-009 |
| **Nombre** | Integridad y seguridad de la base de datos |
| **Categoría** | Seguridad de la información |
| **Prioridad** | Crítica |
| **Estado** | Por validar |

---

## Requisitos

### RNF-009.1 — Integridad de los registros

La base de datos de Hardwarex debe mantener la información de usuarios, equipos, mantenimientos, garantías y proveedores sin alteraciones incorrectas.

### RNF-009.2 — Validación de datos

El sistema debe validar la información antes de almacenarla, evitando registros incompletos, duplicados o incorrectos.

### RNF-009.3 — Relaciones entre registros

La base de datos debe utilizar llaves primarias y foráneas para mantener correctamente las relaciones entre sus tablas.

### RNF-009.4 — Protección contra modificaciones no autorizadas

Solamente los usuarios y procesos autorizados deben poder modificar o eliminar información de la base de datos.

### RNF-009.5 — Consistencia de la información

Las operaciones de registro, actualización y eliminación deben mantener la consistencia de los datos almacenados.
