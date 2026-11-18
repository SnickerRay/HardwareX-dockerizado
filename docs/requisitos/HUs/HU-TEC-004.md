
# HU-TEC-004 — Adjuntar evidencias fotográficas del mantenimiento

---

## Identificación

| Campo | Valor |
|:---|:---|
| **ID** | HU-TEC-004 |
| **Título** | Adjuntar evidencias fotográficas del mantenimiento |
| **Módulo** | Gestión de mantenimientos |
| **Prioridad** | Media |
| **Estado** | Por validar |
| **RF asociados** | RF-040 (relación complementaria) |

---

## Historia

Como técnico, necesito adjuntar evidencias fotográficas del mantenimiento, con la finalidad de dejar soporte visual del trabajo realizado sobre los equipos tecnológicos de Hardwarex.

---

## Criterios de aceptación

### CA-TEC-004.1 — Carga de imágenes

- **Dado que** el mantenimiento se encuentra en proceso.
- **Cuando** el técnico adjunte una imagen como evidencia del trabajo realizado.
- **Entonces** el sistema debe guardar la evidencia correctamente y relacionarla con el mantenimiento correspondiente.

### CA-TEC-004.2 — Validación de formato

- **Dado que** el archivo seleccionado no corresponde a un formato de imagen permitido.
- **Cuando** el técnico intente subir el archivo.
- **Entonces** el sistema debe mostrar un mensaje indicando que el formato no es válido.

### CA-TEC-004.3 — Visualización de evidencias

- **Dado que** existen evidencias fotográficas registradas.
- **Cuando** el técnico consulte la información del mantenimiento.
- **Entonces** el sistema debe mostrar las imágenes almacenadas.

### CA-TEC-004.4 — Eliminación de archivos incorrectos

- **Dado que** el técnico necesita eliminar una evidencia fotográfica incorrecta.
- **Cuando** seleccione el archivo y confirme su eliminación.
- **Entonces** el sistema debe eliminar el archivo correctamente.
