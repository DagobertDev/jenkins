import matcher


class Number:
    value: int
    operator = None

    def __init__(self, value, operator=None):
        self.value = value
        self.operator = operator

    def get_value(self):
        return self.value

    def to_string(self) -> str:
        if self.operator is None:
            return str(self.get_value())
        return self.operator.to_string(self.value)


class Operator:
    number: Number
    sign: str

    def __init__(self, number, sign: str):
        self.number = number
        self.sign = sign

    def to_string(self, apply_to: str) -> str:
        return apply_to + self.sign + self.number.to_string()


class Addition(Operator):
    def __init__(self, number):
        super().__init__(number, "+")


class Subtraction(Operator):
    def __init__(self, number):
        super().__init__(number, "-")


class Multiplication(Operator):
    def __init__(self, number):
        super().__init__(number, "*")


class Division(Operator):
    def __init__(self, number):
        super().__init__(number, "/")


class ProxyNumber(Number):
    number: Number
    operator: Operator = None

    def __init__(self, number, operator=None):
        self.number = number
        self.operator = operator

    def set_value(self, v):
        self.number.value = v

    def get_value(self):
        return self.number.value

    value = property(get_value, set_value)

    def to_string(self) -> str:
        if self.operator is None:
            return "(" + str(self.number.to_string()) + ")"
        return self.operator.to_string("(" + self.number.to_string() + ")")


switch_term = {
    matcher.Term.NUMBER: Number,
    matcher.Term.ADDITION: Addition,
    matcher.Term.SUBSTRACTION: Subtraction,
    matcher.Term.MULTIPLICATION: Multiplication,
    matcher.Term.DIVISION: Division,
}


def generate_term(token):
    _type: int = token._.operator
    children = []
    number_children = []
    operator_children = []

    for c in token.children:
        if c._.operator != matcher.Term.NONE:
            term = generate_term(c)
            children.append(term)

            if isinstance(term, Number):
                number_children.append(term)
            else:
                operator_children.append(term)

    if len(children) == 0:
        assert _type == matcher.Term.NUMBER
        return Number(token.text)

    if len(children) == 1:
        if _type is matcher.Term.NUMBER:
            if isinstance(children[0], Operator):
                return Number(token.text, children[0])
            else:
                return Number(token.text, Addition(children[0]))

        else:
            return switch_term[_type](children[0])

    if _type == matcher.Term.NUMBER:
        number_children.reverse()
        previous = number_children.pop(0)

        for number in number_children:
            number.operator = Addition(previous)
            previous = number

        for operator in operator_children:
            previous = ProxyNumber(previous, operator)
        return ProxyNumber(previous)

    number_children.reverse()
    previous = number_children.pop(0)

    for number in number_children:
        number.operator = switch_term[_type](previous)
        previous = number

    for operator in operator_children:
        previous = ProxyNumber(previous, operator)
    return ProxyNumber(previous)
