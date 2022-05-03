from functools import reduce

def reduce_factorial(x: int) -> int:
    # [1, 1] for reduce to work even if list(range(...)) is empty
    multipliers = [1, 1] + list(range(1, x + 1))

    return reduce(lambda x, y: x * y, multipliers)

if __name__ == '__main__':
    for x in range(10):
        print(f'{x}! = {reduce_factorial(x)}')