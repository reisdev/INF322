# INF322

Repositório para o trabalho final de INF322.

## Utilização

### Instalação

Para instalar a aplicação da API, execute os seguinte passos:

- Acesse a pasta:

```bash
$ cd api
```

- Crie um ambiente virtual com o python e execute a ativação

```bash
$ python -m venv .env
$ .env\Scripts\activate
```

- Instale os pacotes necessários

```bash
$ pip install -r requirements.txt
```
### Configuração

Para configurar a aplicação, é necessário editar o arquivo `settings.py`, contido na pasta `/api`.

Altere as informações da base de dados para a sua configuração local.

O formato é o seguinte:

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'HOST': 'localhost',
        'PORT': '1521',
        'NAME': 'pulga',
        'USER': 'SYSMAN',
        'PASSWORD': '' # Your password here
    }
}

```


## Links úteis

[Oracle DB + Python](https://www.oracle.com/technetwork/articles/dsl/python-091105.html)

[Django](https://docs.djangoproject.com/en/2.2/)