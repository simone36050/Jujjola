from typing import Union
from requests import Session
from judge.account import BASE_URL
from enum import IntEnum


class Status(IntEnum):
    COMPILING = 1
    COMPILATION_FAILED = 2
    EVALUATING = 3
    UNKNOWN = 4
    EVALUATED = 5


def get_csrf(s: Session, task: str) -> str:
    r = s.get(BASE_URL + 'tasks/{}/submissions'.format(task))
    token = r.text.split('<input type="hidden" name="_xsrf" value="')[1].split('"')[0]
    return token

def send_submission(s: Session, task: str, csrf: str, program: str) -> int:
    r = s.post(BASE_URL + 'tasks/{}/submit'.format(task),
                data={ 
                    'language': 'C++11 / g++',
                    '_xsrf': csrf
                },
                files={
                    '{}.%l'.format(task): ('auto_software.cpp', program)
                })
    id = r.text.split('<tr data-submission="')[1].split('"')[0]
    return int(id)

def submit(s: Session, task: str, program: str) -> int:
    token = get_csrf(s, task)
    return send_submission(s, task, token, program)
    

def check_status(s: Session, task: str, submission_id: int) -> Union[Status, int]:
    r = s.get(BASE_URL + 'tasks/{}/submissions/{}'.format(task, submission_id))
    res = r.json()

    status = Status(res['status'])

    if status == Status.EVALUATED:
        points = res['public_score_message'].split(' / ')
        return status, int(points[0]) / int(points[1])
    else:
        return status, None


def get_details(s: Session, task: str, submission_id: int) -> dict:
    r = s.get(BASE_URL + 'tasks/{}/submissions/{}/details'.format(task, submission_id))
    
    res = []
    for case in r.text.split('<td class="idx">')[1:]:
        message = case.split('<td class="details">')[1].split('</td>')[0]
        res.append(message)
    
    return res

