def is_palindrome_int(x: int) -> bool:
    return _is_palindrome(x)

def _is_palindrome_bruteforce(x):
    if x < 0 or (x != 0 and x % 10 == 0) :
        return False
    revers = 0
    digits = x
    while digits > 0:
        revers = revers * 10 + digits % 10
        digits = digits // 10
    print(f'compared: {x}|{revers}')
    return x == revers

def _is_palindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    revers = 0
    while x > revers:
        revers = revers * 10 + x % 10
        x //= 10
    return x == revers or x == revers // 10 # handle odd cases

