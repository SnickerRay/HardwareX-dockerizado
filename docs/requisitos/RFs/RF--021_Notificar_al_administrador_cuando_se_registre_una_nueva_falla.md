
# RF-021 — Notificación de nuevas fallas al administrador

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-021 |
| **Nombre** | Notificación de nuevas fallas al administrador |
| **Módulo** | Notificaciones y gestión de fallas |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe generar una notificación para el administrador cuando un usuario registre una nueva falla en un equipo tecnológico, permitiendo conocer oportunamente los problemas reportados.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del reporte | ID | Sí | Debe corresponder a una falla registrada. |
| ID del administrador | ID | Sí | Debe corresponder a un administrador activo. |
| Fecha de registro | Fecha/hora | Sí | Generada por el sistema. |

---

## Proceso

1. El usuario registra una nueva falla.
2. El sistema almacena el reporte.
3. Identifica a los administradores autorizados.
4. Genera una notificación relacionada con la falla.
5. La notificación queda disponible en el medio implementado.
6. El sistema conserva el registro de la notificación.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Notificación generada | 201 | Notificación creada correctamente. |
| Falla no encontrada | 404 | No existe el reporte asociado. |
| Destinatario inválido | 422 | No se encontró un administrador válido. |
| Error de notificación | 500 | No fue posible generar la notificación. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/notifications` | Sí | Genera una notificación para el administrador. |
| GET | `/api/v1/notifications` | Sí | Consulta las notificaciones disponibles. |

---

## Reglas de negocio

- **RN-001:** La notificación debe generarse después de registrar correctamente la falla.
- **RN-002:** El destinatario debe tener el rol de administrador.
- **RN-003:** La notificación debe estar relacionada con el reporte correspondiente.
- **RN-004:** El reporte debe conservarse aunque ocurra un error al generar la notificación.
