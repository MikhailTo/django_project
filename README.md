# django_project
### Project for learning the Django...
[Добрый, добрый Django с Сергеем Балакиревым](https://stepik.org/course/183363/syllabus)

1. new project with wsl

2. install venv:
sudo apt install python3-venv

3. create venv:
python3 -m venv venv
source venv/bin/activate

4. to choose python interpreter 
exist venv

5. mark venv directory as excluded

6. install pip 
sudo apt install -y python3-pip 

7. install django
pip install django

7.5 freeze requirements.txt
pip freeze > requirements.txt

8. create project django
python3 -m django startproject django_project

9. runserver
python3 manage.py runserver

10. create gitignore
https://www.toptal.com/developers/gitignore

11. edit git config
git config --global user.name "MikhailTo"
git config --global user.email "toshkin.mikhail@yandex.ru"

12. git init ***

13. git commit and push

14. python manage.py migrate

15. install plugin database navigator
and download drives in db

16. create superuser
python3 manage.py createsuperuser

manage.py:
Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

startapp:
init - пайтон пакет
admin - что отображать в админке
apps - содержит конфиг
models - модели
tests - тесты
views - запросы
migrations - 
