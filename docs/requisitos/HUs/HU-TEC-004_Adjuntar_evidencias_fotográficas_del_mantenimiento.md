
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
| **RF asociados** | Pendiente de definir |

---

## Historia

Como técnico, necesito adjuntar evidencias fotográficas del mantenimiento, con la finalidad de dejar soporte visual del trabajo realizado sobre los equipos tecnológicos de Hardwarex.

---

## Criterios de aceptación

**Pendientes de validación:** los siguientes criterios describen el comportamiento esperado de esta funcionalidad, pero requieren la definición y aprobación de un requisito funcional específico antes de considerarse establecidos.

### CA-TEC-004.1 — Carga de imágenes

- **Dado que** el mantenimiento se encuentra en proceso.
- **Cuando** el técnico adjunte una imagen como evidencia del trabajo realizado.
- **Entonces** el sistema debería guardar la evidencia y relacionarla con el mantenimiento correspondiente.

### CA-TEC-004.2 — Validación de formato

- **Dado que** el archivo seleccionado no corresponde a un formato de imagen permitido.
- **Cuando** el técnico intente subir el archivo.
- **Entonces** el sistema debería mostrar un mensaje indicando que el formato no es válido.

### CA-TEC-004.3 — Visualización de evidencias

- **Dado que** existen evidencias fotográficas registradas.
- **Cuando** el técnico consulte la información del mantenimiento.
- **Entonces** el sistema debería permitir visualizar las imágenes almacenadas.

### CA-TEC-004.4 — Eliminación de archivos incorrectos

- **Dado que** el técnico necesita eliminar una evidencia fotográfica incorrecta.
- **Cuando** seleccione el archivo y confirme su eliminación.
- **Entonces** el sistema debería permitir eliminar la evidencia.

---

## Observación

Esta historia no tiene un requisito funcional asociado actualmente. Si se mantiene la funcionalidad de adjuntar evidencias fotográficas dentro del alcance del proyecto, será necesario definir y aprobar un requisito funcional específico que establezca sus condiciones.
