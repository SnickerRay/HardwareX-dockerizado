
# RF-016 — Registro de equipos

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-016 |
| **Nombre** | Registro de equipos |
| **Módulo** | Gestión de equipos |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema Hardwarex debe permitir al administrador registrar los equipos tecnológicos de la organización, almacenando sus datos principales para facilitar su identificación y control.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Nombre del equipo | Texto | Sí | No puede estar vacío. |
| Tipo de equipo | Texto | Sí | Debe corresponder a una categoría válida. |
| Marca | Texto | Sí | Longitud permitida. |
| Modelo | Texto | Sí | Longitud permitida. |
| Número de serie | Texto | Sí | No debe estar duplicado. |
| Ubicación | Texto | Sí | Debe indicar dónde se encuentra el equipo. |

---

## Proceso

1. El administrador ingresa al módulo de equipos.
2. Selecciona la opción de registrar equipo.
3. Completa los datos solicitados.
4. El sistema valida los campos.
5. Comprueba que el número de serie no esté registrado.
6. Almacena la información del equipo.
7. Muestra la confirmación del registro.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Equipo registrado | 201 | Equipo creado correctamente. |
| Número de serie duplicado | 409 | El equipo ya se encuentra registrado. |
| Datos inválidos | 422 | Errores en los campos del formulario. |
| Sin autorización | 403 | No tiene permisos para registrar equipos. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/equipment` | Sí | Registra un nuevo equipo tecnológico. |

---

## Reglas de negocio

- **RN-001:** Solo el administrador puede registrar equipos.
- **RN-002:** Cada equipo debe tener un identificador único.
- **RN-003:** El número de serie no debe repetirse.
- **RN-004:** Los datos obligatorios deben completarse.
