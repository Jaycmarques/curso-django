import pytest
from django.urls import reverse
from model_bakery import baker
from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client, db):
    return client.get(reverse('login'))


def test_login_page(resp):
    assert resp.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('modulos:indice')


@pytest.fixture
def resp_home(client, db):
    return client.get(reverse('base:home'))


def test_botao_login(resp_home):
    assert_contains(resp_home, 'Login')


def test_link_login(resp_home):
    assert_contains(resp_home, reverse('login'))


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:home'))


def test_botao_login_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, 'Login')


def test_link_login_indisponivel(resp_home_com_usuario_logado):
    assert_not_contains(resp_home_com_usuario_logado, reverse('login'))


def test_botao_logout(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Logout')


def test_nome_usuario(resp_home_com_usuario_logado, usuario_logado):
    assert_contains(resp_home_com_usuario_logado, usuario_logado.first_name)


def test_link_logout(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))
