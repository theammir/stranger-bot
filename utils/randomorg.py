import requests as rq

import random

def integer(*args):
    if (len(args) == 1):
        min = 0
        max = args[0]
    elif (len(args) == 2):
        min = args[0]
        max = args[1]
    else:
        raise ValueError('Improper arguments has been passed.')
    response = rq.get(f'https://www.random.org/integers/?num=1&min={min}&max={max}&col=1&base=10&format=plain&rnd=new')
    if (response.ok):
        return int(response.text)
    else:
        print(rq.exceptions.RequestException('Something went wrong. Request code: ' + str(response.status_code)))
        return random.randint(min, max)

def element(array: list):
    if (len(array) == 0):
        return
    else:
        response = rq.get(f'https://www.random.org/integers/?num=1&min=0&max={len(array) - 1}&col=1&base=10&format=plain&rnd=new')
        if (response.ok):
            return array[int(response.text)]
        else:
            print(rq.exceptions.RequestException('Something went wrong. Request code: ' + str(response.status_code)))
            return random.choice(array)
