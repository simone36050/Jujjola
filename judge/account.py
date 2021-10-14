from requests import Session


BASE_URL = 'https://judge.science.unitn.it/'


def new_session() -> Session:
    return Session()


def get_csrf(s: Session) -> str:
    r = s.get(BASE_URL)
    token = r.text.split('<input type="hidden" name="_xsrf" value="')[1].split('"')[0]
    return token

def make_login(s: Session, csrf: str, username: str, password: str):
    r = s.post(BASE_URL + 'login', data={
        '_xsrf': csrf,
        'username': username,
        'password': password
    })
    assert r.status_code == 200, 'Invalid credentials'
    
def login(s: Session, username: str, password: str):
    csrf = get_csrf(s)
    make_login(s, csrf, username, password)


