
# RF-040 — Registro de observaciones técnicas

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-040 |
| **Nombre** | Registro de observaciones técnicas |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir registrar observaciones técnicas sobre los mantenimientos preventivos realizados a los equipos tecnológicos, almacenando información sobre las revisiones, procedimientos y actividades ejecutadas por el responsable.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del mantenimiento | ID | Sí | Debe corresponder a un mantenimiento registrado. |
| Observaciones técnicas | Texto | Sí | No puede estar vacío. |
| Responsable | ID | Sí | Debe corresponder a un usuario autorizado. |
| Fecha de registro | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El responsable ingresa al módulo de mantenimientos.
2. Selecciona el mantenimiento preventivo correspondiente.
3. Ingresa las observaciones técnicas de las actividades realizadas.
4. El sistema verifica que el mantenimiento exista.
5. Valida que el usuario tenga permisos para registrar información.
6. Guarda las observaciones en la base de datos.
7. Relaciona las observaciones con el mantenimiento.
8. Permite consultar la información posteriormente.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Observaciones registradas | 201 | Información técnica guardada correctamente. |
| Mantenimiento inexistente | 404 | No se encontró el mantenimiento. |
| Observaciones vacías | 422 | Debe ingresar las observaciones técnicas. |
| Sin autorización | 403 | No tiene permisos para registrar observaciones. |
| Error de almacenamiento | 500 | No fue posible guardar la información. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/preventive-maintenance/{id}/observations` | Sí | Registra observaciones técnicas. |
| GET | `/api/v1/preventive-maintenance/{id}/observations` | Sí | Consulta las observaciones del mantenimiento. |

---

## Reglas de negocio

- **RN-001:** Las observaciones deben estar relacionadas con un mantenimiento existente.
- **RN-002:** La descripción técnica es obligatoria.
- **RN-003:** Solo los usuarios autorizados pueden registrar observaciones.
- **RN-004:** Cada observación debe conservar la fecha y el responsable.
- **RN-005:** La información debe permanecer disponible para futuras consultas.
