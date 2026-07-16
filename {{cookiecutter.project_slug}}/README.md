# Fast API Starter Kit

<div align="center">
    <img src="readme_resources/README.png" alt="AWS Utils" width="200"/>
</div>

## Overview:
Fast API starter kit
- Simple CRUD operations
- Type-safe API endpoints
- Create, read and retrieve items by their ID.


## Usage:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

## Language:
- Python


## Instructions to run the project:
- Install these 2 dependencies fastapi and uvicorn using pip
- To run the fastapi server, use the following command:
```bash
uvicorn fast-api.app:app --reload
```
- To run the endpoint with root to see hello world, use the following command:
```bash
curl http://127.0.0.1:8000/
```
- To run a post request to create an item, use the following command:
```bash
curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d '{"text": "Sample item", "is_done": false}'
```
- To get the full list of items, use the following command:
```bash
curl http://127.0.0.1:8000/items
```
- To list an item by its ID, use the following command:
```bash
curl http://127.0.0.1:8000/items/{item_id}
```
- To update an item by its ID, use the following command:
```bash
curl -X PUT "http://127.0.0.1:8000/items/{item_id}" -H "Content-Type: application/json" -d '{"text": "Updated item", "is_done": true}'
```
- To delete an item by its ID, use the following command:
```bash
curl -X DELETE "http://127.0.0.1:8000/items/{item_id}"
```
- Swagger UI is available at http://127.0.0.1:8000/docs
- Redoc is available at http://127.0.0.1:8000/redoc


## Project Structure:
```
{{cookiecutter.project_slug}}/
      ├── fast-api/
      │     └── app.py  # Main application file for Fast API
      │
      │
      ├──readme_resources
      │     └── README.png    # Picture for the Read me file
      │
      ├── .gitignore  # Git ignore file to exclude unnecessary files from version control
      └── README.md   # README file for project documentation

```