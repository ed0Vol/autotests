import pytest
import sender_send_request


@pytest.fixture(scope='session')
def get_token():
    sender_send_request.post_new_user()
    res = sender_send_request.auth()
    if res.ok:
        return res.json()['token']
    else:
        return ''


@pytest.mark.parametrize('name', [
    pytest.param('купить молоко', id='valid name'),
    pytest.param('w', id='min length'),
    pytest.param('qwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiopqwertyuiop', id='max length')
])
def test_valid_todo_name(get_token, name):
    res = sender_send_request.post_todo(get_token, name)
    assert res.status_code == 201
    assert res.json()['description'] == name
