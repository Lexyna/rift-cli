
roman_map = [
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
    (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9,"IX"), (5, "V"), (4, "IV"),
    (1, "I")]

def number_to_roman(number: int) -> str:
    roman = ""

    while number > 0:
        for i, r in roman_map:
            while number >= i:
                roman += r
                number -= i

    return roman


def format_number(number: int) -> str:
    if number < 100000:
        return str(number)

    tier = 0
    while number > 1000:
        tier += 3
        number /= 1000

    return f"{number:.0f}e{tier}"