### Проект: Микросервисное приложение на Django

**Описание:**  
Этот проект представляет собой микросервисное приложение, построенное на базе Django и Django REST Framework с использованием JWT-аутентификации и PostgreSQL в качестве основной базы данных. Архитектура основана на четырех микросервисах для управления пользователями, документами, медицинскими данными и расписанием.

**Основные технологии:**
- **Django, Django REST Framework (DRF)** для построения REST API
- **JWT** для безопасной аутентификации пользователей
- **PostgreSQL** для хранения данных
- **gRPC** для межсервисного взаимодействия

**Микросервисы:**
- **auth_service** — сервис аутентификации и управления пользователями
- **doc_service** — сервис для работы с документами
- **health_service** — сервис для хранения и управления медицинскими данными
- **schedule_service** — сервис управления расписанием

### Основное задание

- **Account URL**: [http://localhost:8081/ui-swagger](http://localhost:8081/ui-swagger)
- **Hospital URL**: [http://localhost:8082/ui-swagger](http://localhost:8082/ui-swagger)
- **Timetable URL**: [http://localhost:8083/ui-swagger](http://localhost:8083/ui-swagger)
- **Document URL**: [http://localhost:8084/ui-swagger](http://localhost:8084/ui-swagger)

### Дополнительное задание

- **ElasticSearch URL**: [http://localhost:9200/](http://localhost:9200/)
- **Kibana URL**: [http://localhost:5601/app/kibana](http://localhost:5601/app/kibana)

### Запуск приложения

Для запуска всех микросервисов используйте команду:
```bash
docker-compose up -d --build
```

**Примечание:** Убедитесь, что все зависимости установлены, а Docker настроен правильно для корректного запуска и взаимодействия сервисов.