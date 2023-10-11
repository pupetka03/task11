def parser(numbers: str) -> list:
    return list(map(int, numbers.split()))


def is_arithmetic_sequence(numbers: list) -> bool:
    difference = numbers[1] - numbers[0]
    for num in range(1, len(numbers)-1):
        return True


def is_geometric_sequence(numbers: list) -> bool:
    ...


def next_arithmetic_item(numbers: list) -> int:
    difference = numbers[1] - numbers[0]
    next_item = numbers[-1] + difference
    return next_item


def next_geometric_item(numbers: list) -> int:
    ...


def get_next_item(numbers: list):
    if len(numbers) > 2:
        if is_arithmetic_sequence(numbers):
            return next_arithmetic_item(numbers)

        if is_geometric_sequence(numbers):
            return next_geometric_item(numbers)

    return None


if __name__ == '__main__':
    numbers = input('numbers>>>')
    numbers = parser(numbers.replace(","," "))
    print(get_next_item(numbers))
