# To-Do List - DRF API

Essa API fornece uma maneira de criar, ler, atualizar e deletar tarefas. As tarefas podem ter: Título, Descrição e um Status (Completada ou Não).

Essa API foi desenvolvida como parte do meu TCC para o curso de Técnico em Informático do Colégio Politécnico - UFSM utilizando Django-Rest-Framework.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma sugestão, por favor, abra uma issue ou crie um pull request.

## Instalando e Rodando

Clone o projeto e navegue até o diretório dele

```bash
  git clone https://github.com/KaduKessler/ToDo-DRF.git
  cd ToDo-DRF
```

Crie um ambiente virtual (virtualenv)

```bash
  python -m venv venv
```

Ative o virtualenv

```bash
  Windows: .\venv\Scripts\activate
  Linux: source venv/bin/activate
```

Instale as dependências:

```bash
  pip install -r requirements.txt
```

## Rodando

Migre o banco de dados:

```bash
  python manage.py makemigrations Task
```

```bash
  python manage.py migrate
```

Crie um superusuário (Administrador):

```bash
  python manage.py createsuperuser
```

Inicie o servidor:

```bash
  python manage.py runserver
```
