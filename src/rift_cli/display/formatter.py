def format_number(number: int) -> str:
    if number < 100000:
        return str(number)

    tier = 0
    while number > 1000:
        tier += 3
        number /= 1000

    return f"{number:.0f}e{tier}"