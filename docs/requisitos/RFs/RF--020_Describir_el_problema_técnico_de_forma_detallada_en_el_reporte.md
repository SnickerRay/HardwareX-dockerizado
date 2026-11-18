
# RF-020 — Descripción detallada de fallas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-020 |
| **Nombre** | Descripción detallada de fallas |
| **Módulo** | Gestión de fallas |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que el usuario describa detalladamente el problema técnico que presenta un equipo al momento de registrar una falla, facilitando su identificación y posterior atención por parte del personal técnico.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del reporte | ID | Sí | Debe existir. |
| Descripción del problema | Texto | Sí | Debe contener información sobre la falla. |
| Evidencia | Archivo | No | Si se implementa, debe cumplir los formatos y tamaños permitidos. |

---

## Proceso

1. El usuario selecciona un equipo.
2. Ingresa al formulario de reporte de fallas.
3. Describe los síntomas o problemas que presenta el equipo.
4. Agrega información adicional si es necesario.
5. El sistema valida la descripción.
6. Relaciona la información con el reporte correspondiente.
7. Almacena los datos para su posterior consulta.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Descripción registrada | 201 | Información técnica almacenada correctamente. |
| Reporte inexistente | 404 | No se encontró el reporte. |
| Descripción vacía | 422 | Debe ingresar una descripción del problema. |
| Datos inválidos | 422 | Información incorrecta. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/fault-reports` | Sí | Registra la descripción de una falla. |
| PATCH | `/api/v1/fault-reports/{id}` | Sí | Actualiza la descripción de un reporte autorizado. |

---

## Reglas de negocio

- **RN-001:** Cada descripción debe estar relacionada con un reporte de falla.
- **RN-002:** La descripción es obligatoria.
- **RN-003:** Solo los usuarios autorizados pueden modificar el reporte.
- **RN-004:** La información debe conservarse para facilitar el diagnóstico técnico.
