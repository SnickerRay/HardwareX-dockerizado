
# RF-030 — Administración de proveedores

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-030 |
| **Nombre** | Administración de proveedores |
| **Módulo** | Gestión de proveedores |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir registrar, consultar, editar y eliminar o desactivar la información de los proveedores relacionados con los equipos tecnológicos y sus garantías.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Nombre del proveedor | Texto | Sí | No puede estar vacío. |
| Identificación | Texto | Sí | Debe ser válida y no estar duplicada. |
| Teléfono | Texto | No | Debe tener un formato válido. |
| Correo electrónico | Correo | No | Debe tener un formato válido. |
| Dirección | Texto | No | Longitud permitida. |
| Acción | Texto | Sí | Registrar, consultar, editar o eliminar. |

---

## Proceso

1. El administrador ingresa al módulo de proveedores.
2. Selecciona la operación que desea realizar.
3. Si va a registrar, completa los datos solicitados.
4. Si va a consultar, selecciona un proveedor existente.
5. Si va a editar, modifica los datos necesarios.
6. Si va a eliminar, el sistema verifica las relaciones existentes.
7. Valida y guarda la información.
8. Muestra el resultado de la operación.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Proveedor registrado | 201 | Proveedor creado correctamente. |
| Consulta exitosa | 200 | Información del proveedor. |
| Proveedor actualizado | 200 | Datos modificados correctamente. |
| Proveedor eliminado | 200 | Proveedor eliminado o desactivado. |
| Proveedor duplicado | 409 | El proveedor ya está registrado. |
| Datos inválidos | 422 | Errores de validación. |
| Sin autorización | 403 | No tiene permisos para administrar proveedores. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/providers` | Sí | Consulta los proveedores. |
| GET | `/api/v1/providers/{id}` | Sí | Consulta un proveedor específico. |
| POST | `/api/v1/providers` | Sí | Registra un proveedor. |
| PUT | `/api/v1/providers/{id}` | Sí | Actualiza los datos del proveedor. |
| DELETE | `/api/v1/providers/{id}` | Sí | Elimina o desactiva un proveedor. |

---

## Reglas de negocio

- **RN-001:** Solo los usuarios autorizados pueden administrar proveedores.
- **RN-002:** El nombre del proveedor es obligatorio.
- **RN-003:** La identificación no debe estar duplicada.
- **RN-004:** No se deben perder las relaciones históricas con equipos y garantías.
