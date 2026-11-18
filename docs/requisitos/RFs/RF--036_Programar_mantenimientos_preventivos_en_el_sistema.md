
# RF-036 — Programación de mantenimientos preventivos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-036 |
| **Nombre** | Programación de mantenimientos preventivos |
| **Módulo** | Planificación de mantenimientos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir programar mantenimientos preventivos para los equipos tecnológicos, estableciendo fechas y actividades que permitan conservar su buen funcionamiento y evitar posibles fallas.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe corresponder a un equipo registrado. |
| Fecha programada | Fecha/hora | Sí | Debe ser válida. |
| Actividad de mantenimiento | Texto | Sí | No puede estar vacía. |
| Responsable | ID | No | Debe corresponder a un usuario autorizado. |

---

## Proceso

1. El administrador ingresa al módulo de mantenimientos.
2. Selecciona la opción de programar mantenimiento preventivo.
3. Selecciona el equipo correspondiente.
4. Ingresa la fecha y las actividades que se realizarán.
5. Asigna un responsable si corresponde.
6. El sistema valida la información.
7. Guarda la programación en la base de datos.
8. Muestra la confirmación del mantenimiento programado.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Programación exitosa | 201 | Mantenimiento preventivo programado. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Fecha inválida | 422 | La fecha ingresada no es válida. |
| Datos incompletos | 422 | Faltan datos obligatorios. |
| Sin autorización | 403 | No tiene permisos para programar mantenimientos. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/preventive-maintenance` | Sí | Registra un mantenimiento preventivo. |
| GET | `/api/v1/preventive-maintenance` | Sí | Consulta los mantenimientos programados. |

---

## Reglas de negocio

- **RN-001:** El equipo debe estar registrado en Hardwarex.
- **RN-002:** La fecha programada debe ser válida.
- **RN-003:** Cada mantenimiento debe tener una actividad definida.
- **RN-004:** La programación debe conservar la información del responsable cuando se asigne.
