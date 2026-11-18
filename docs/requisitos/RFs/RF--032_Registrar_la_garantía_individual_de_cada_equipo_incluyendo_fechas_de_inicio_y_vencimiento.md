
# RF-032 — Registro de garantías de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-032 |
| **Nombre** | Registro de garantías de equipos |
| **Módulo** | Gestión de garantías |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

Hardwarex debe permitir registrar la garantía individual de cada equipo tecnológico, almacenando las fechas de inicio y vencimiento para facilitar el control de su vigencia.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe corresponder a un equipo registrado. |
| Fecha de inicio | Fecha | Sí | Debe ser válida. |
| Fecha de vencimiento | Fecha | Sí | Debe ser igual o posterior a la fecha de inicio. |
| ID del proveedor | ID | No | Debe corresponder a un proveedor registrado. |
| Condiciones de garantía | Texto | No | Longitud permitida. |

---

## Proceso

1. El administrador ingresa al módulo de garantías.
2. Selecciona el equipo al que desea registrar una garantía.
3. Ingresa las fechas de inicio y vencimiento.
4. Selecciona el proveedor correspondiente si aplica.
5. El sistema valida la información.
6. Guarda la garantía relacionada con el equipo.
7. Muestra la confirmación del registro.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Garantía registrada | 201 | Garantía creada correctamente. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Fechas inválidas | 422 | Las fechas ingresadas no son válidas. |
| Datos incompletos | 422 | Faltan campos obligatorios. |
| Sin autorización | 403 | No tiene permisos para registrar garantías. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/warranties` | Sí | Registra una garantía para un equipo. |
| GET | `/api/v1/equipment/{id}/warranties` | Sí | Consulta las garantías del equipo. |

---

## Reglas de negocio

- **RN-001:** Toda garantía debe estar relacionada con un equipo existente.
- **RN-002:** Las fechas de inicio y vencimiento son obligatorias.
- **RN-003:** La fecha de vencimiento no puede ser anterior a la de inicio.
- **RN-004:** La información debe conservarse para futuras consultas.
