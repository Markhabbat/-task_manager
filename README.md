# Task manager - Система управления задачами


Установка
```commandline
docker compose -p task_manager -f docker-compose.yml up --build
```

API
```djangourlpath
http://localhost:8000/swagger/
```


Пример запроса
```bash
curl -X 'GET' \
  'http://localhost:8000/employees/users/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer <token>'
```
