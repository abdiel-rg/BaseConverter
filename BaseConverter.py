from functools import reduce
from multipledispatch import dispatch

equivalences = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def dec_to_base(num: int, to_base: int) -> str:
    valid_base(to_base)
    result = []
    while num > 0:
        calc = num % to_base
        result.append(equivalences[calc] or calc)
        num = int(num / to_base)
    return "".join(result.__reversed__())


def base_to_dec(num: str, from_base: int) -> int:
    valid_base(from_base)
    string_list = map(lambda x: equivalences.find(x), num)
    return reduce(
                    lambda acc, curr: acc + curr[1] * from_base ** (len(num) - curr[0] - 1),
                    enumerate(string_list),
                    0
                )


def valid_base(*bases: int):
    for base in bases:
        if base < 2 or base > len(equivalences):
            raise IndexError(f"Base must be higher or equal to 2 and lower or equal to {len(equivalences)}")

@dispatch(int, int)
def converter(num: int, to_base: int) -> str:
    return dec_to_base(num, to_base)


@dispatch(str, int, int)
def converter(num: str, from_base: int, to_base: int) -> str:
    return dec_to_base(base_to_dec(num, from_base), to_base)

print(
    # dec_to_base(2500, 16),
    # base_to_dec("9C4", 16),
    # converter("9C4", 10, 16),
    converter(1500, 36),
    converter("111111101", 2, 10),
    sep="\n"
    )
