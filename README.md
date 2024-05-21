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


