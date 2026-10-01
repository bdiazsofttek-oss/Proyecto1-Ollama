# Proyecto1-Ollama

API sencilla con FastAPI que envia preguntas a un modelo local mediante Ollama.

## Requisitos

- Python 3.10 o posterior.
- [Ollama](https://ollama.com/) instalado y en ejecucion.
- El modelo `llama3.2:3b` descargado en Ollama.

## Instalacion

Desde la carpeta del proyecto, crea y activa un entorno virtual e instala las dependencias:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Descarga el modelo si todavia no esta instalado:

```powershell
ollama pull llama3.2:3b
```

## Ejecutar la API

Inicia el servidor desde la carpeta del proyecto:

```powershell
uvicorn api:app --reload
```

La API queda disponible en `http://127.0.0.1:8000`. La documentacion interactiva esta en `http://127.0.0.1:8000/docs`.

## Consultar el modelo

Envia una solicitud `POST` a `/ask` con un objeto JSON que incluya `prompt`:

```json
{
  "prompt": "Que es una API REST?"
}
```

La respuesta tiene esta forma:

```json
{
  "response": "..."
}
```

Tambien puedes probar esta operacion desde `/docs`: abre `POST /ask`, pulsa **Try it out**, escribe el JSON y pulsa **Execute**.

## Archivos principales

- `api.py`: define la aplicacion FastAPI y el endpoint `/ask`, que consulta Ollama.
- `main.py`: ejemplo independiente de una consulta a Ollama desde la terminal.
- `requirements.txt`: dependencias de Python.

## Notas

Ollama debe estar funcionando localmente y el modelo configurado en `api.py` debe estar disponible. El endpoint realiza la consulta al modelo de forma sincronica.
