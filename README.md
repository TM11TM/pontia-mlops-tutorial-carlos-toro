# 🚀 Proyecto DevOps - Automatización de Pipelines

## Funcionamiento 

### 1 - CI: workflow **integration.yml**
- Se ejecuta en cada pr
- Clona el repositorio
- Instala dependencias
- Ejecuta los test unitarios ubicados en **unit_test/**
- Si los test fallan el job no se ejecuta


### 2 - Construcción: workflow **build.yml**
- Se ejecuta en cada pr 
- Clona el repositorio
- Instala dependencias
- Hace una descarga del Adult dataset 
- Entrena el modelo en `src/main.py` y lo guarda en model.pkl
- Ejecuta test_model.py
- guarda el modelo en MLFlow ejecutando `register_model.py`


### 3 - Despliegue: workflow **deploy.yml**
- Se ejecuta en cada pr 
- Clona el repositorio
- Define el modelo
- Construye la imagen Docker y la sube a Azure


## 🗂️ Estructura del Proyecto

```text
📁 .github/          # Workflows de GitHub Actions 
📁 data/             # Se almacena la información del modelo
📁 deployment/       # Contiene la app y el Dockerfile
📁 model_test/       # Modelos de test     
📁 models/           # Otros modelos
📁 scripts/          # Scripts auxiliares
📁 src/              # Código fuente principal
📁 unit_test/        # Test unitarios
📄 README.md         # Documentación principal
📄 requirements.txt  # Dependencias del proyecto
````


# ▶️ Uso
#### 1. Clonar el proyecto
#### 2. Desde la terminal instalamos todas las dependencias 
        `pip install - r requirements.txt`
#### 3. Ejecuta el modelo desde main.py
#### 4. Ejecuta las pruebas unitarias
#### 5. Comprobar en el navegador el correcto despliegue de la API
