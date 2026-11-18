# RF-004 — Registro de datos personales del usuario

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | RF-004 |
| **Nombre** | Registro de datos personales del usuario |
| **Módulo** | Gestión de usuarios |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **Fecha** | Noviembre 2026 |

---

## Descripción

El sistema debe permitir registrar los datos personales de cada usuario durante la creación de su cuenta, almacenando la información necesaria para identificarlo dentro de Hardwarex.

---

## Entradas

| Campo | Tipo | Obligatorio | Validaciones |
|:---|:---|:---:|:---|
| Nombre completo | Texto | Sí | Mínimo 2 caracteres. |
| Correo electrónico | Correo | Sí | Formato válido y sin duplicados. |
| Contraseña | Texto protegido | Sí | Debe cumplir la política de seguridad. |
| Rol | Texto o ID | Sí | Debe corresponder a un rol permitido. |

---

## Proceso

1. El usuario ingresa al formulario de registro.
2. Completa los campos con sus datos personales.
3. El sistema verifica que la información esté completa.
4. Comprueba que el correo electrónico no exista previamente.
5. Valida el rol que se asignará a la cuenta.
6. Guarda los datos en la base de datos.
7. Muestra la confirmación del registro.

---

## Salidas

| Escenario | Código HTTP | Respuesta |
|:---|:---:|:---|
| Datos registrados | 201 | Información personal almacenada correctamente. |
| Correo duplicado | 409 | El correo ya pertenece a otro usuario. |
| Datos incompletos | 422 | Se indican los campos que deben completarse. |

---

## Endpoints asociados

| Método | Ruta | Auth requerida | Descripción |
|:---:|:---|:---:|:---|
| POST | `/api/v1/auth/register` | No | Registra los datos personales del usuario. |

---

## Reglas de negocio

- **RN-001:** Los datos personales deben corresponder al usuario registrado.
- **RN-002:** El correo electrónico no puede repetirse.
- **RN-003:** La información debe almacenarse de manera segura.
- **RN-004:** Solo se deben solicitar los datos necesarios para el funcionamiento de Hardwarex.
