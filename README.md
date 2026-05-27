AWS | Serverless | Lambda | API Gateway | Flask

AppTiempo2 — Serverless Weather App (AWS)
AppTiempo2 es la evolución cloud de la aplicación AppTiempo original.
Esta versión migra una aplicación Flask monolítica a una arquitectura serverless en AWS utilizando AWS Lambda y API Gateway.

Descripción
AppTiempo2 permite consultar el clima actual de cualquier ciudad mediante la API de OpenWeatherMap, a través de una interfaz web simple construida con Flask.
✅ Migración de app local → cloud
✅ Arquitectura serverless
✅ Despliegue sin servidores (AWS Lambda)
✅ Exposición HTTP mediante API Gateway

Arquitectura
La aplicación sigue el siguiente flujo:
Cliente (browser)
↓
API Gateway (REST API)
↓
AWS Lambda
↓
Flask (awsgi adapter)
↓
OpenWeather API

Decisiones técnicas importantes
Durante la migración se resolvieron varios desafíos reales:

Uso de aws-wsgi (awsgi) para adaptar Flask a Lambda
Configuración de ProxyFix para manejar headers detrás de API Gateway
Correcciones de routing entre Flask y API Gateway
Manejo de variables de entorno para API Key
Debug de errores típicos como:

KeyError: httpMethod
Internal Server Error


Migración de HTTP API → REST API por compatibilidad con WSGI


Nota importante sobre API Gateway
Se utiliza REST API (API Gateway v1) en lugar de HTTP API porque:

REST API usa payload format 1.0
Incluye httpMethod, requerido por awsgi
HTTP API (v2.0) no es completamente compatible con WSGI adapters


📂 Estructura del proyecto
AppTiempo2/
├── app.py                # Aplicación Flask adaptada a Lambda
├── templates/            # HTML (Jinja2)
├── lambda_package/       # Paquete listo para deploy
│   ├── app.py
│   ├── templates/
│   ├── flask/
│   ├── requests/
│   ├── awsgi/
│   └── app.zip
├── requirements.txt
├── README.md


Tecnologías utilizadas

Python 3
Flask
AWS Lambda
API Gateway (REST API)
OpenWeatherMap API
awsgi (WSGI adapter)
🔐 Variables de entorno
La aplicación utiliza una variable de entorno para la API Key:
API_KEY=TU_API_KEY

Debe configurarse en AWS Lambda.

📦 Despliegue en AWS (resumen)

Crear función Lambda (Python)
Subir paquete .zip con dependencias
Configurar handler:

app.lambda_handler


Configurar variable de entorno API_KEY
Crear trigger con API Gateway (REST API)
Obtener URL pública


🌐 Uso
Acceder a la URL proporcionada por API Gateway:
https://xxxx.execute-api.amazonaws.com/prod/

Ingresar una ciudad y visualizar:

Temperatura
Descripción del clima
Humedad
Velocidad del viento


📈 Evolución respecto a AppTiempo (v1)
Característicav1 (Local)v2 (Serverless)HostingLocalhostAWS LambdaEscalabilidadManualAutomáticaInfraestructuraServidorServerlessDeploymentManualCloud

🚧 Mejoras futuras

API REST (JSON) sin frontend HTML
Integración con DynamoDB (cache)
Manejo de errores más robusto
Internacionalización (idioma/unidades)
CI/CD con GitHub Actions


💡 Sobre este proyecto
Este proyecto fue creado como práctica de migración a cloud y arquitectura serverless, enfrentando problemas reales de integración entre servicios AWS y frameworks tradicionales.

👨‍💻 Autor
Juan Gabriel Bregonzi
Proyecto orientado a aprendizaje y preparación para certificaciones AWS 
