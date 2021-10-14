from typing import Union
from requests import Session
from judge.submissions import submit, Status, check_status, get_details
from utils.reader import read, readWith
from search.multitonic import intervals
from time import sleep

TASK = 'somma'

def try_interval(s: Session, analyze: int, gs: list) -> int:
    id = submit(s, TASK, readWith('tasks/somma/somma.cpp',
        ANALYZE=analyze,
        F_L_1=gs[0][0], F_H_1=gs[0][1],
        F_L_2=gs[1][0], F_H_2=gs[1][1],
        F_L_3=gs[2][0], F_H_3=gs[2][1],
        F_L_4=gs[3][0], F_H_4=gs[3][1],
        F_L_5=gs[4][0], F_H_5=gs[4][1]))
    return id

def try_element(s: Session, analyze: int, element: int) -> int:
    id = submit(s, TASK, readWith('tasks/somma/somma_verify.cpp',
        ANALYZE=analyze, ELEMENT=element))
    return id
    
def wait_result(s: Session, id: int, frequency: float=0.5) -> Status:
    st = Status.COMPILING
    while (st != Status.COMPILATION_FAILED) and (st != Status.EVALUATED):
        sleep(frequency)
        st, _ = check_status(s, TASK, id)
        print(st)
    return st

def parse_result(s: Session, id: int, test: int, gs: list) -> list: 
    res = get_details(s, TASK, id)
    result = res[test - 1]
    # print(result)

    if result == 'Execution failed because the return code was nonzero':
        return gs[0]
    if result == 'Execution killed (could be triggered by violating memory limits)':
        return gs[1]
    if result == 'Output isn&#39;t correct':
        return gs[2]
    if result == 'Execution timed out':
        return gs[3]
    if result == 'Output is correct':
        return gs[4]

def process_interval(s: Session, analyze: int, test: int, gs: list) -> list:
    id = try_interval(s, analyze, gs)
    st = wait_result(s, id, 1) # REMOVE 1
    assert st == Status.EVALUATED, 'Qualcosa è andato storto nella verifica'
    res = parse_result(s, id, test, gs)
    return res

def extract_element(s: Session, analyze: int, test: int) -> int:
    print('Extract element {} of test {}'.format(analyze, test))
    min = -2000000 # -1000000
    max =  2000000 # 1000000

    while min != max:
        print('min:', min, 'max:', max)
        gs = intervals(min, max, 5)
        new_gs = process_interval(s, analyze, test, gs)
        min = new_gs[0]
        max = new_gs[1]

    print(min)
    return min

def verify_element(s: Session, analyze: int, test: int, hypotesys: int) -> bool:
    print('Testing element {} of test {} for value {}'.format(analyze, test, hypotesys))
    id = try_element(s, analyze, hypotesys)
    wait_result(s, id)
    vals = [True, False, False, False, False]
    res = parse_result(s, id, test, vals)
    # assert res, 'Verification failed'
    if res:
        print('Verified!')
    else:
        print('Verification failed')
    return res

def extract_test(s: Session, test: int) -> list:
    res = []
    for i in range(2):
        el = extract_element(s, i + 1, test)
        res.append(el)
        verify_element(s, i + 1, test, el)
    return res

def extract_all(s: Session) -> list:
    res = []
    for i in range(10): ## TODO: fix
        res.append(extract_test(s, i + 1))
    return res