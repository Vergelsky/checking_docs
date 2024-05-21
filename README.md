# checking_docs
### Простой сервис для ручной проверки предоставляемых документов

## Порядок установки:
###### (подразумевается что у вас уже установлен python, git, и docker)
- клонируем репозиторий:<br>
git clone https://github.com/Vergelsky/checking_docs.git<br>

- создаём виртуальное окружение:<br>
python -m venv .venv
- устанавливаем зависимости:<br>
pip install -r requirements.txt
- из файла env_example создаём файл с переменными окружения .env:<br>
copy env_expample .env<br>
и заполняем его своими значениями
- запускаем докер:<br>
docker-compose up --build

## Использование сервиса <br>
- CRUD пользователей:
  - создание: POST /users/<br>
    {<br>
    "email": "test@gmail.com",<br>
    "is_moderator": true, # необязательный<br> 
    "password": "test"<br>
    }
  - список: GET /users/<br>
  - один: POST /users/1/<br>
  - изменение: PATCH /users/1/<br>
  - удаление: DELETE /users/1/<br>
- CRUD документов:
  - создание: POST /doc-check/  # через form-data<br> 
  - список: GET /doc-check/<br>
  - один: POST /doc-check/1/<br>
  - изменение: PATCH /doc-check/1/<br>
  - удаление: DELETE /doc-check/1/<br>

В момент создания документа первому попавшемуся пользователю с полем is_moderator=True
отправляется письмо. Если такого нет, письмо уходит на почту указанную в переменной окружения DEFAULT_MODERATOR_EMAIL.
<br>После этого модератор через API изменяет status документа на "2_rej" или "3_conf" в случае отклонения или
подтверждения документа соответственно. Или назначает статус документу через админ-панель. В этот момент пользователю
отправляется уведомление о результате проверки через celery.'

Используемые технологии:
- Python
- PostgreSQL
- Git
- Django
- Django REST framework
- Celery
- Redis
- Docker
- unittest