"""
Passos para usar o pytest no Django
1. instalar pytest-django via pip
2. criar documento chamado pytest.ini (ou tox.ini) no diretório do projeto (o que tem o arquivo manage.py)
3. preencher o pytest.ini com 
    [pytest]
    DJANGO_SETTINGS_MODULE = project_name.settings
    python_files = tests.py test_*.py *_tests.py
4. criar os testes
    4.1 importar pytest no arquivo de teste
    4.2 adicionar linha `pytestmark = pytest.mark.django_db` no arquivo de teste
5. rodar `pytest -q arquivo_test.py` no terminal
"""
import pytest
from core.models import Pessoa

# O teste abaixo não testa nenhum modelo ou função do aplicativo. Funciona
def teste():
    a = 1
    b = 1
    assert a == b

# Essa linha é importante para o acesso ao banco de dados
pytestmark = pytest.mark.django_db

# O teste abaixo também funciona
def teste1():
    pessoa1 = Pessoa.objects.create(idade='25')
    pessoa2 = Pessoa.objects.create(idade='20')
    # tipo_idade_pessoa1 = type(pessoa1.idade)
    # tipo_idade_pessoa2 = type(pessoa2.idade)
    assert pessoa1 == pessoa2

# O teste abaixo não funciona
# @pytest.mark.django_db
# class TestClassPessoa:
#     pessoa1 = Pessoa.objects.create(idade=25)
#     pessoa2 = Pessoa.objects.create(idade=20)
#     tipo_idade_pessoa1 = type(pessoa1.idade)
#     tipo_idade_pessoa2 = type(pessoa2.idade)
#     def teste2(self):
#         assert self.tipo_idade_pessoa1 == self.tipo_idade_pessoa2

