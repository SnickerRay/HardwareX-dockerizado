
# RF-019 — Reporte de fallas de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-019 |
| **Nombre** | Reporte de fallas de equipos |
| **Módulo** | Gestión de fallas |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir que los usuarios reporten fallas de los equipos tecnológicos registrados en Hardwarex, para que el personal encargado pueda revisar y gestionar los problemas presentados.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe corresponder a un equipo registrado. |
| Descripción de la falla | Texto | Sí | No puede estar vacía. |
| Usuario reportante | ID | Sí | Debe corresponder al usuario autenticado. |
| Fecha del reporte | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El usuario ingresa al módulo de equipos.
2. Selecciona el equipo que presenta la falla.
3. Selecciona la opción de reportar falla.
4. Describe el problema presentado.
5. El sistema valida los datos.
6. Registra el reporte en la base de datos.
7. Asigna un identificador al reporte.
8. Muestra la confirmación del registro.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Falla registrada | 201 | Reporte creado correctamente. |
| Equipo inexistente | 404 | No se encontró el equipo seleccionado. |
| Datos incompletos | 422 | Se debe completar la descripción de la falla. |
| Sin autenticación | 401 | Debe iniciar sesión para reportar una falla. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/fault-reports` | Sí | Registra una nueva falla de un equipo. |

---

## Reglas de negocio

- **RN-001:** El equipo debe estar registrado en Hardwarex.
- **RN-002:** El usuario debe estar autenticado.
- **RN-003:** La descripción de la falla es obligatoria.
- **RN-004:** Cada reporte debe conservar la fecha y el usuario que lo realizó.
