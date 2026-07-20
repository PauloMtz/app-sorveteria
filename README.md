# App Sorveteria

Projeto Django base para iniciar a aplicação.

Este repositório foi baixado de [opencodigos/DjangoProjetoConfiguracao at DjangoProjetoConfiguracaoCompleta](https://github.com/opencodigos/DjangoProjetoConfiguracao/tree/DjangoProjetoConfiguracaoCompleta) e está sendo usado como ponto de partida para o primeiro commit.

## Requisitos

- Python 3 instalado
- `pip` disponível no ambiente

## Criar e ativar o ambiente virtual

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Windows CMD

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### Linux ou macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar as dependências

Com o ambiente virtual ativo, instale as dependências do projeto com:

```bash
pip install -r requirements.txt
```

## Criar ou atualizar o requirements.txt

Depois de instalar novas bibliotecas no ambiente virtual, gere ou atualize o arquivo `requirements.txt` com:

```bash
pip freeze > requirements.txt
```

## Dependências usadas neste projeto

As dependências já listadas no `requirements.txt` incluem Django e bibliotecas de apoio, como `Pillow`, `python-dotenv`, `django-cors-headers`, `django-requestlogs`, `django-session-timeout` e `djangorestframework`.

## Executar o projeto

Com o ambiente configurado e as dependências instaladas:

```bash
python manage.py migrate
python manage.py runserver
```
