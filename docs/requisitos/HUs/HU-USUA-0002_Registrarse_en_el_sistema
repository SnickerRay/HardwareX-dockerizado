
# HU-USUA-0002 — Registrarse en el sistema

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-USUA-0002 |
| **Título** | Registrarse en el sistema |
| **Módulo** | Registro de usuarios |
| **Prioridad** | Alta |
| **Estado** | Por validar |
| **RF asociados** | RF-003, RF-004 |

---

## Historia

Como usuario, necesito registrarme en el sistema, con la finalidad de crear una cuenta que me permita ingresar a la aplicación Hardwarex y utilizar sus funcionalidades.

---

## Criterios de aceptación

### CA-USUA-0002.1 — Datos completos

- **Dado que** todos los campos obligatorios del formulario de registro están completos y contienen información válida.
- **Cuando** el usuario envíe los datos.
- **Entonces** el sistema debe crear una cuenta nueva y mostrar un mensaje indicando que el registro fue realizado correctamente.

### CA-USUA-0002.2 — Correo repetido

- **Dado que** el correo electrónico ingresado ya se encuentra registrado en Hardwarex.
- **Cuando** el usuario intente registrarse nuevamente con ese correo.
- **Entonces** el sistema debe mostrar un mensaje de error indicando que el correo electrónico ya está registrado.

### CA-USUA-0002.3 — Contraseña vacía

- **Dado que** el campo de contraseña se encuentra vacío.
- **Cuando** el usuario envíe el formulario de registro.
- **Entonces** el sistema no debe permitir completar el registro y debe solicitar que se diligencien los campos obligatorios.

### CA-USUA-0002.4 — Registro exitoso

- **Dado que** el usuario ha ingresado correctamente todos los datos solicitados.
- **Cuando** envíe el formulario de registro.
- **Entonces** el sistema debe guardar la cuenta y mostrar una confirmación del registro realizado.
