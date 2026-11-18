
# RF-017 — Almacenamiento de información de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-017 |
| **Nombre** | Almacenamiento de información técnica y operativa |
| **Módulo** | Gestión de equipos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe almacenar las características técnicas y operativas de cada equipo tecnológico registrado, permitiendo consultar información como marca, modelo, ubicación, estado y demás datos necesarios para su mantenimiento.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| ID del equipo | ID | Sí | Debe existir. |
| Marca | Texto | Sí | No puede estar vacía. |
| Modelo | Texto | Sí | No puede estar vacío. |
| Características técnicas | Texto | No | Debe contener información válida. |
| Ubicación | Texto | Sí | Debe estar registrada. |
| Estado operativo | Texto | Sí | Debe corresponder a un estado permitido. |

---

## Proceso

1. El administrador registra o actualiza un equipo.
2. Ingresa sus características técnicas y operativas.
3. El sistema valida los datos.
4. Relaciona la información con el equipo correspondiente.
5. Guarda los datos en la base de datos.
6. Permite consultar la información desde la ficha del equipo.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Información almacenada | 200 | Datos del equipo guardados correctamente. |
| Equipo inexistente | 404 | No se encontró el equipo. |
| Datos inválidos | 422 | Información incorrecta o incompleta. |
| Error de almacenamiento | 500 | No fue posible guardar la información. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| PUT | `/api/v1/equipment/{id}` | Sí | Actualiza la información técnica y operativa. |
| GET | `/api/v1/equipment/{id}` | Sí | Consulta la información del equipo. |

---

## Reglas de negocio

- **RN-001:** La información debe estar relacionada con un equipo registrado.
- **RN-002:** Los campos obligatorios deben contener datos válidos.
- **RN-003:** Solo los usuarios autorizados pueden modificar la información.
- **RN-004:** Los datos deben mantenerse actualizados.
