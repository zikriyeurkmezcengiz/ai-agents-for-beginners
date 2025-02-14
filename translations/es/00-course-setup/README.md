# Configuración del Curso

## Introducción

Esta lección cubrirá cómo ejecutar los ejemplos de código de este curso.

## Requisitos

- Una cuenta de GitHub  
- Python 3.12+

## Clonar o Hacer un Fork de este Repositorio

Para comenzar, por favor clona o haz un fork del repositorio de GitHub. Esto creará tu propia versión del material del curso para que puedas ejecutar, probar y ajustar el código a tu gusto.

Esto se puede hacer haciendo clic en el enlace para [hacer fork del repositorio](https://github.com/microsoft/ai-agents-for-beginners/fork).

Ahora deberías tener tu propia versión del curso como se muestra a continuación:

![Repositorio con Fork](../../../translated_images/forked-repo.eea246a73044cc984a1e462349e36e7336204f00785e3187b7399905feeada07.es.png)

## Recuperar tu Token de Acceso Personal (PAT) de GitHub

Actualmente, este curso utiliza el Marketplace de Modelos de GitHub para ofrecer acceso gratuito a Modelos de Lenguaje de Gran Escala (LLMs) que se usarán para crear Agentes de IA.

Para acceder a este servicio, necesitarás crear un Token de Acceso Personal de GitHub.

Esto se puede hacer yendo a la configuración de [Tokens de Acceso Personal](https://github.com/settings/personal-access-tokens) en tu cuenta de GitHub.

Selecciona la opción `Fine-grained tokens` en el lado izquierdo de tu pantalla.

Luego selecciona `Generate new token`.

![Generar Token](../../../translated_images/generate-token.361ec40abe59b84ac68d63c23e2b6854d6fad82bd4e41feb98fc0e6f030e8ef7.es.png)

Copia tu nuevo token que acabas de crear. Ahora deberás agregarlo a tu archivo `.env` incluido en este curso.

## Agregar esto a tus Variables de Entorno

Para crear tu archivo `.env`, ejecuta el siguiente comando en tu terminal:

```bash
cp .env.example .env
```

Esto copiará el archivo de ejemplo y creará un `.env` en tu directorio.

Abre ese archivo y pega el token que creaste en el campo `GITHUB_TOKEN=` del archivo .env.

## Instalar los Paquetes Requeridos

Para asegurarte de que tienes todos los paquetes de Python necesarios para ejecutar el código, ejecuta el siguiente comando en tu terminal.

Recomendamos crear un entorno virtual de Python para evitar conflictos y problemas.

```bash
pip install -r requirements.txt
```

Esto debería instalar los paquetes de Python requeridos.

¡Ahora estás listo para ejecutar el código de este curso! ¡Feliz aprendizaje sobre el mundo de los Agentes de IA!

Si tienes algún problema con esta configuración, únete a nuestro [Discord de la Comunidad de Azure AI](https://discord.gg/kzRShWzttr) o [crea un issue](https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.