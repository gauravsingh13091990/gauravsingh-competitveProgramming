import random


def rand7():
    return random.randint(1, 7)


def rand5():
    
    while True:
        x = rand7()
        if x < 6:
            return x


for m in range(20):
    results = [0] * 5
        results[rand5() - 1] += 1

    print(results)