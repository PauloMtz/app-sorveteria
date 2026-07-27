# App Sorveteria

Projeto Django para aplicação de sorveteria.

O repositório base foi baixado de [opencodigos/DjangoProjetoConfiguracao at DjangoProjetoConfiguracaoCompleta](https://github.com/opencodigos/DjangoProjetoConfiguracao/tree/DjangoProjetoConfiguracaoCompleta).

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
- Modelos `Embalagem`, `TipoSabor`, `Sabor`, `Cobertura`, `MontaPote`, `SelSabor`, `SacolaItens` e `Pedido` criados e registrados no admin

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

#### Sabor

Representa os sabores individuais cadastrados no sistema, com os campos:

- `nome`
- `tipo` (relacionamento com `TipoSabor`)
- `ativo`

Cada `Sabor` pertence a um `TipoSabor`, permitindo classificar sabores como Tradicional, Premium, Sorbet ou Açaí.

#### Cobertura

Representa as coberturas adicionais disponíveis, com os campos:

- `nome`
- `ativo`
- `preco`

#### MontaPote

Representa a montagem de um pote de sorvete, com os campos:

- `embalagem` (relacionamento com `Embalagem`)
- `cobertura` (relacionamento muitos-para-muitos com `Cobertura`)
- `quantidade`

#### SelSabor

Representa a seleção de sabores para um pote montado, com os campos:

- `pote` (relacionamento com `MontaPote`)
- `sabor` (relacionamento com `Sabor`)
- `quantidade_bolas`

#### SacolaItens

Representa o carrinho com os potes selecionados, com os campos:

- `potes` (relacionamento muitos-para-muitos com `MontaPote`)
- `preco`

#### Pedido

Representa o fechamento do pedido do cliente, com os campos:

- `data_pedido`
- `user` (relacionamento com `User` do Django)
- `itens_da_sacola` (relacionamento um-para-um com `SacolaItens`)
- `status`
- `pago`

## Rotas da aplicação

Atualmente o projeto expõe as seguintes rotas:

- `/` - página inicial da aplicação
- `/admin/` - painel administrativo do Django

### Origem das rotas

- `core/urls.py` define a rota `/admin/` e inclui as rotas do app `myapp`
- `myapp/urls.py` define a rota `/`, apontando para a view `index`

## Executar o projeto

Com o ambiente configurado e as dependências instaladas:

1. Sempre que um novo modelo for criado ou um modelo existente for alterado, gere uma nova migration:

```bash
python manage.py makemigrations
```

2. Em seguida, aplique as migrations para criar ou atualizar as tabelas no banco de dados:

```bash
python manage.py migrate
```

3. Depois, inicie o servidor de desenvolvimento:

```bash
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
4. Cadastrar, editar e remover registros de `Embalagem`, `TipoSabor`, `Sabor`, `Cobertura`, `MontaPote`, `SelSabor`, `SacolaItens` e `Pedido` pelo admin

## Próximas etapas

Com a etapa de modelagem finalizada, os próximos passos da aplicação serão:

1. Implementar os cálculos de preço, composição e fechamento dos pedidos
2. Desenvolver a parte do site voltada ao usuário externo
