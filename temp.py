from math import sqrt

message: str = (
    'Добро пожаловать в самую '
    'лучшую программу для вычисления квадратного корня из заданного числа'
)


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Calculate sqrt root."""
    if your_number <= 0:
        return 'root = 0'
    square_root = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет: {square_root}')


print(message)
calc(25.5)