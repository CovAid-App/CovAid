from bot import get_response


def test_bot(tests, times=100):

    correct = 0

    test = []
    response = []

    total = len(test)
    for key, value in tests.items():
        test.append(key)
        response.append(value)

    for i in range(times):
        for j in range(len(test)):
            if str(get_response(test[i])) == response[i]:
                correct += 1

    return correct, total