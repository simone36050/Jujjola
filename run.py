from credentials import USERNAME, PASSWORD
from judge.account import new_session, login
from tasks.somma.somma import extract_all
from tasks.intervalli.error_finder import test


# login
s = new_session()
login(s, USERNAME, PASSWORD)


# somma
result = extract_all(s)
for i in range(10):
    print('Case #{}: {} + {}'.format(i + 1, result[i][0], result[i][1]))


# intervalli
test(s)