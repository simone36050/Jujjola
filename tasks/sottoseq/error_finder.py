from requests import Session
from judge.submissions import submit, get_details
from utils.reader import read
from utils.judge import wait_result

TASK = 'sottoseq'

def test(s: Session):
    # send submission
    id = submit(s, TASK, read('tasks/sottoseq/error_finder.cpp'))

    # wait result
    wait_result(s, id, TASK)

    # get details
    dets = get_details(s, TASK, id)
    for i in range(10):
        print('Case #{}: {}'.format(i + 1, parse_result(dets[i])))

def parse_result(result: str) -> str:
    if result == 'Execution failed because the return code was nonzero':
        return 'N'
    if result == 'Execution timed out':
        return 'A'
    return 'O'
