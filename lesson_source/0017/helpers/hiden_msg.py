import random

def get_random_sign():
    return random.choice("!@#$%^&*()_+{}|:<>?][]\;',./")

def create_hiden_string():
    alist = []
    for let in "I love Python":
        for _ in range(1000):
            alist.append(get_random_sign())
        alist.append(let)
    return "".join(alist)
