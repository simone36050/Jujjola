from requests import Session
from judge.submissions import Status, check_status
from time import sleep


def wait_result(s: Session, id: int, task: str, frequency: float=0.5) -> Status:
    st = Status.COMPILING
    while (st != Status.COMPILATION_FAILED) and (st != Status.EVALUATED):
        sleep(frequency)
        st, _ = check_status(s, task, id)
        print(st)
    return st
