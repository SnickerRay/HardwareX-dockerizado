
# RF-031 — Asociación de proveedores a equipos y garantías

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-031 |
| **Nombre** | Asociación de proveedores a equipos y garantías |
| **Módulo** | Gestión de proveedores y garantías |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir relacionar los proveedores registrados con los equipos tecnológicos o las garantías correspondientes, facilitando la consulta de la información comercial y de respaldo de cada equipo.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del proveedor | ID | Sí | Debe existir. |
| ID del equipo | ID | Sí | Debe estar registrado. |
| ID de la garantía | ID | No | Debe existir si se especifica. |

---

## Proceso

1. El administrador ingresa al módulo de proveedores.
2. Selecciona el proveedor que desea asociar.
3. Busca el equipo o la garantía correspondiente.
4. Selecciona el registro que desea relacionar.
5. El sistema verifica que ambos registros existan.
6. Guarda la asociación.
7. Muestra los datos relacionados.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Asociación exitosa | 201 | Proveedor relacionado correctamente. |
| Proveedor inexistente | 404 | No se encontró el proveedor. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Asociación duplicada | 409 | La relación ya existe. |
| Datos inválidos | 422 | Información incorrecta. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/equipment/{id}/provider` | Sí | Relaciona un proveedor con un equipo. |
| POST | `/api/v1/warranties/{id}/provider` | Sí | Relaciona un proveedor con una garantía. |

---

## Reglas de negocio

- **RN-001:** El proveedor debe estar registrado.
- **RN-002:** El equipo o la garantía deben existir.
- **RN-003:** No se deben crear asociaciones duplicadas.
- **RN-004:** Los usuarios deben tener permisos para realizar la asociación.
