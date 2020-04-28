from bot import get_response
import random

def test_bot(tests, times=100):

    correct = 0

    test = []
    response = []

    for key, value in tests.items():
        test.append(key)
        response.append(value)

    total = len(test)

    print(f'Test running for {times} times')
    for i in range(times):
        for j in range(total):
            val = random.choice(list(tests.items()))
            if str(get_response(val[0])) == val[1]:
                correct += 1
    print('Test finished')

    return correct, total * times