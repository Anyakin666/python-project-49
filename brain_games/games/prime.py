import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def get_question_and_answer():
    n = random.randint(1, 100)
    def is_prime_fast(n):
        if n <= 1: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True
    return str(n), str(is_prime_fast(n))