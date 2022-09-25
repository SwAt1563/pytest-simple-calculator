import functools
import re


def add(user_input):
    input_length = len(user_input)

    if input_length == 0:
        return 0

    try:
        delimiter = '[,\n]'
        negative_numbers = []

        if re.match(r"^//", user_input):
            delimiters = re.search('//(.*?)\n', user_input).group(1)
            # [2][1].*
            if not delimiters or not re.match(r".*\[.+\].*", delimiters):
                raise AttributeError

            user_input = user_input.split(f"//{delimiters}\n")[1]
            if len(user_input) == 0:
                return 0

            delimiters = list(map(lambda x: x[1:-1], re.findall(r'\[.*?\]', delimiters)))

            for i in range(len(delimiters)):
                delimiters[i] = "".join(list(map(lambda c: f'\{c}' if re.match(r'[^a-zA-Z0-9]', c) else c,
                                                 delimiters[i])))

            delimiter = "|".join(delimiters)

        numbers = list(map(lambda x:
                           int(x) if x.isdigit() else negative_numbers.append(str(int(x))),
                           re.split(delimiter, user_input)))

        if negative_numbers:  # not empty
            raise Exception(f"negatives not allowed: {','.join(negative_numbers)}")
        return functools.reduce(lambda a, b: a + b, list(map(lambda x: x if x <= 1000 else 0, numbers)))

    except ValueError:
        raise ValueError
    except AttributeError:
        raise AttributeError  # when can't match the change of the delimiter in line 16

