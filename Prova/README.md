# Instruções para instalação e execução
<!-- Descrever o que deve ser feito para instalar (ou baixar) a aplicação, o que precisa ser configurando (parâmetros, banco de dados e afins) e como executá-la. -->
Os requerimentos são apenas o Python(3.8+) e o Django(4.0+)

O django pode ser instalado em uma Virtual Environment através do comando:

´pip install Django´

Por questôes de simplicidade, descomentei no gitignore a venv e o db.sqlite3 (banco de dados utilizado no projeto) para utilização.

Para rodar o servidor, ´source venv/bin/activate´ depois ´python manage.py runserver´

O usuário para a parte administração é ´admin´ com senha ´admin´.