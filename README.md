# Sistema de Domótica para el Hogar

Este sistema de domótica permite la gestión y automatización de diferentes dispositivos en el hogar. A continuación, se describen las entidades principales y sus atributos:

## Entidades y Atributos

### ✅ Usuario

Representa a los usuarios del sistema.

* **id\_usuario (PK)**: Identificador único del usuario (clave primaria).
* **nombre**: Nombre completo del usuario.
* **correo**: Dirección de correo electrónico del usuario.
* **rol**: Rol del usuario dentro del sistema (ej: `admin`, `invitado`).

### ✅ Dispositivo

Representa los dispositivos inteligentes conectados al sistema.

* **id\_dispositivo (PK)**: Identificador único del dispositivo (clave primaria).
* **nombre**: Nombre descriptivo del dispositivo (ej: "Luz del salón", "Sensor de temperatura cocina").
* **tipo**: Tipo de dispositivo (ej: `luz`, `sensor`, `cámara`, `termostato`).
* **estado**: Estado actual del dispositivo (`ON`, `OFF`).
* **ubicacion** (opcional): Ubicación física del dispositivo (ej: `habitación`, `exterior`, `cocina`).

### ✅ Automatizacion

Representa las reglas de automatización definidas por los usuarios.

* **id\_automatizacion (PK)**: Identificador único de la automatización (clave primaria).
* **nombre**: Nombre descriptivo de la automatización (ej: "Encender luces al detectar movimiento").
* **condicion**: Condición que dispara la automatización (ej: "detección de movimiento", "temperatura > 25°C").
* **accion**: Acción a realizar cuando se cumple la condición (ej: "encender luz", "enviar notificación").
* **id\_dispositivo (FK → Dispositivo)**: Identificador del dispositivo al que se aplica la acción.
* **id\_usuario (FK → Usuario)**: Identificador del usuario que creó la automatización (clave foránea que referencia a la tabla `Usuario`).

## Relaciones

* La tabla `Automatizacion` tiene una relación de clave foránea con la tabla `Dispositivo` a través del atributo `id_dispositivo`. Esto indica a qué dispositivo se aplica la acción de la automatización.
* La tabla `Automatizacion` también tiene una relación de clave foránea con la tabla `Usuario` a través del atributo `id_usuario`. Esto indica qué usuario creó la regla de automatización.

## Posibles Extensiones Futuras

* Implementación de una interfaz de usuario para la gestión de usuarios, dispositivos y automatizaciones.
* Soporte para una mayor variedad de tipos de dispositivos.
* Adición de más tipos de condiciones y acciones para las automatizaciones.
* Registro de eventos y actividades del sistema.

¡Espero que este README te sea de utilidad! ¿Hay algo más en lo que pueda ayudarte?
