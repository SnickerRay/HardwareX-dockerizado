
# RF-033 — Alertas de garantías próximas a vencer

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-033 |
| **Nombre** | Alertas de garantías próximas a vencer |
| **Módulo** | Gestión de garantías y notificaciones |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe generar alertas cuando las garantías de los equipos tecnológicos estén próximas a vencer, permitiendo que el administrador conozca con anticipación cuáles requieren seguimiento.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID de garantía | ID | Sí | Debe existir. |
| Fecha de vencimiento | Fecha | Sí | Debe ser válida. |
| Días de anticipación | Número entero | Sí | Debe ser un valor igual o superior a cero. |

---

## Proceso

1. El sistema consulta las garantías registradas.
2. Obtiene sus fechas de vencimiento.
3. Compara las fechas con la fecha actual.
4. Identifica las garantías próximas a vencer.
5. Genera una alerta para los usuarios autorizados.
6. Guarda el registro de la alerta.
7. Permite consultar las garantías identificadas.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Garantías próximas a vencer | 200 | Listado de garantías identificadas. |
| Sin garantías próximas a vencer | 200 | No existen garantías próximas a vencer. |
| Error de consulta | 500 | No fue posible consultar las garantías. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| GET | `/api/v1/warranties/expiring` | Sí | Consulta las garantías próximas a vencer. |
| GET | `/api/v1/notifications` | Sí | Consulta las alertas generadas. |

---

## Reglas de negocio

- **RN-001:** Las alertas deben generarse según el periodo de anticipación configurado.
- **RN-002:** Solo deben considerarse las garantías registradas.
- **RN-003:** No deben generarse alertas duplicadas innecesariamente.
- **RN-004:** Las fechas deben compararse con la fecha actual.
