# App Sorveteria

Projeto Django para aplicação de sorveteria.

O repositório base foi baixado de [opencodigos/DjangoProjetoConfiguracao at DjangoProjetoConfiguracaoCompleta](https://github.com/opencodigos/DjangoProjetoConfiguracao/tree/DjangoProjetoConfiguracaoCompleta) e está sendo usado como ponto de partida para o primeiro commit.

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

## O que já foi implementado

Atualmente a aplicação já possui:

- Estrutura Django configurada com projeto `core` e app `myapp`
- Banco de dados SQLite configurado para desenvolvimento
- Página inicial disponível na rota `/`
- Template base com Bootstrap e carregamento de arquivos estáticos
- Context processor global com a variável `social`, exibida na página inicial
- Django Admin habilitado na rota `/admin/`
- Modelos `Embalagem` e `TipoSabor` criados, migrados e registrados no admin

### Modelos disponíveis no admin

#### Embalagem

Representa os recipientes vendidos pela sorveteria, com os campos:

- `tipo`
- `capacidade_maxima_bolas`
- `ativo`
- `preco`

#### TipoSabor

Representa os tipos de sabor cadastrados no sistema, com os campos:

- `tipo`
- `ativo`
- `preco`

## Executar o projeto

Com o ambiente configurado e as dependências instaladas:

```bash
python manage.py migrate
python manage.py runserver
```

Depois, acesse:

- Aplicação: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Criar um superusuário admin

Para acessar o Django Admin com permissões administrativas, crie um superusuário com o comando:

```bash
python manage.py createsuperuser
```

O Django solicitará os dados abaixo:

- `Username`
- `Email address`
- `Password`
- `Password (again)`

Depois de criar o usuário:

1. Inicie o servidor com `python manage.py runserver`
2. Acesse `http://127.0.0.1:8000/admin/`
3. Faça login com o usuário e senha informados no `createsuperuser`

## Fluxo atual de uso

Neste momento, o projeto permite:

1. Executar a aplicação localmente
2. Acessar a página inicial
3. Entrar no painel administrativo
4. Cadastrar, editar e remover registros de `Embalagem` e `TipoSabor` pelo admin
