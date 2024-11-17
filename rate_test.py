import requests as re


def rate_testing(iterations):
    for i in range(1, iterations + 1):
        r = re.get(f"http://127.0.0.1:5001/api/books?page={i}")
        print(i, r.status_code)
    return r.status_code


assert rate_testing(30) == 200
assert rate_testing(1) == 429
