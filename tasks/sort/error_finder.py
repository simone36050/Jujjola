from requests import Session
from judge.submissions import submit, get_details
from utils.reader import read
from utils.judge import wait_result

TASK = 'sort'

def test(s: Session):
    # send submission
    id = submit(s, TASK, read('tasks/{}/error_finder.cpp'.format(TASK)))

    # wait result
    wait_result(s, id, TASK, frequency=1)

    # get details
    dets = get_details(s, TASK, id)
    for i in range(10):
        print('Case #{}: {}'.format(i + 1, parse_result(dets[i])))

def parse_result(result: str) -> str:
    if result == 'Execution timed out':
        return 'N out of bounds'
    return 'Ok'
