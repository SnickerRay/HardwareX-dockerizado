
# RF-035 — Vinculación de garantías con proveedores

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-035 |
| **Nombre** | Vinculación de garantías con proveedores |
| **Módulo** | Gestión de garantías y proveedores |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir relacionar cada garantía registrada con su proveedor correspondiente, para identificar la empresa responsable de respaldar la garantía del equipo tecnológico.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID de garantía | ID | Sí | Debe existir. |
| ID del proveedor | ID | Sí | Debe corresponder a un proveedor registrado. |

---

## Proceso

1. El administrador ingresa al módulo de garantías.
2. Selecciona la garantía que desea vincular.
3. Consulta los proveedores registrados.
4. Selecciona el proveedor correspondiente.
5. El sistema verifica que ambos registros existan.
6. Guarda la relación.
7. Muestra el proveedor asociado a la garantía.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Vinculación exitosa | 200 | Proveedor asociado correctamente. |
| Garantía inexistente | 404 | No se encontró la garantía. |
| Proveedor inexistente | 404 | No se encontró el proveedor. |
| Relación duplicada | 409 | La garantía ya está vinculada a ese proveedor. |
| Datos inválidos | 422 | Información incorrecta. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/warranties/{id}/provider` | Sí | Vincula una garantía con un proveedor. |
| GET | `/api/v1/warranties/{id}` | Sí | Consulta la información de la garantía y su proveedor. |

---

## Reglas de negocio

- **RN-001:** La garantía debe estar registrada.
- **RN-002:** El proveedor debe existir en Hardwarex.
- **RN-003:** No se deben generar asociaciones duplicadas.
- **RN-004:** Solo los usuarios autorizados pueden modificar estas relaciones.
