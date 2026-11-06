
# RF-009 — Almacenamiento de información de usuarios

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-009 |
| **Nombre** | Almacenamiento de información de usuarios |
| **Módulo** | Gestión de usuarios |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe almacenar la información de cada usuario registrado, permitiendo conservar sus datos personales, credenciales protegidas, rol y estado de la cuenta para el funcionamiento de Hardwarex.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Nombre completo | Texto | Sí | Entre 2 y 255 caracteres. |
| Correo electrónico | Correo | Sí | Debe ser único y válido. |
| Contraseña protegida | Hash | Sí | Debe almacenarse mediante un algoritmo seguro. |
| Rol | Texto o ID | Sí | Debe corresponder a un rol existente. |
| Estado | Booleano | Sí | Debe aceptar valores válidos. |

---

## Proceso

1. El sistema recibe los datos del usuario.
2. Verifica que los campos obligatorios estén completos.
3. Comprueba que el correo no esté duplicado.
4. Protege la contraseña mediante hash.
5. Almacena la información en la base de datos.
6. Relaciona el usuario con el rol correspondiente.
7. Confirma el almacenamiento de la información.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Información almacenada | 201 | Usuario guardado correctamente. |
| Correo duplicado | 409 | El correo ya se encuentra registrado. |
| Datos inválidos | 422 | Error en los datos enviados. |
| Error de almacenamiento | 500 | No fue posible guardar la información. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/users` | Sí | Registra la información de un usuario autorizado. |
| GET | `/api/v1/users/{id}` | Sí | Consulta los datos de un usuario. |

---

## Reglas de negocio

- **RN-001:** Cada usuario debe tener un identificador único.
- **RN-002:** El correo electrónico debe ser único.
- **RN-003:** La contraseña debe almacenarse mediante hash.
- **RN-004:** Solo los usuarios autorizados pueden consultar información administrativa de otras cuentas.
