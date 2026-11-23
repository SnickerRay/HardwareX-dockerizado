
# HU-USUA-0001 — Iniciar sesión

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-USUA-0001 |
| **Título** | Iniciar sesión |
| **Módulo** | Autenticación |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-001, RF-002 |

---

## Historia

Como usuario, necesito iniciar sesión, con la finalidad de poder ingresar a la aplicación Hardwarex y utilizar las funcionalidades disponibles según los permisos de mi cuenta.

---

## Criterios de aceptación

### CA-USUA-0001.1 — Inicio de sesión correcto

- **Dado que** el usuario se encuentra registrado y tiene una cuenta habilitada.
- **Cuando** ingrese su correo electrónico y contraseña correctos.
- **Entonces** el sistema debe validar las credenciales y permitir el acceso a Hardwarex.

### CA-USUA-0001.2 — Contraseña incorrecta

- **Dado que** el usuario existe en el sistema, pero ingresa una contraseña incorrecta.
- **Cuando** intente iniciar sesión.
- **Entonces** el sistema debe mostrar un mensaje de error y no permitir el acceso.

### CA-USUA-0001.3 — Usuario no registrado

- **Dado que** el correo electrónico ingresado no corresponde a un usuario registrado.
- **Cuando** intente iniciar sesión.
- **Entonces** el sistema debe mostrar un mensaje informando que las credenciales no son válidas y no permitir el acceso.
