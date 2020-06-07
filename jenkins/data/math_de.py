""" German math data for training and evaluatiopn
    NONE: Word is not necessary for understanding the question,
    OPER: Mathematical Operator,
    NUM: Number
"""

TRAIN_DATA = [
    (
        "Was ist 1 + 2",
        {
            "heads": [1, 1, 2, 2, 3],
            "deps": ["NONE", "NONE", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Hallo Jenkins berechne 1 + 2 - 23",
        {
            "heads": [1, 2, 2, 3, 3, 4, 5, 6],
            "deps": ["NONE", "NONE", "NONE", "NUM", "OPER", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Kannst du 563 + 21 berechnen",
        {
            "heads": [0, 5, 2, 3, 4, 2],
            "deps": ["NONE", "NONE", "NUM", "OPER", "NUM", "NONE"],
        },
    ),
    (
        "Addiere die Zahlen 20 und 98",
        {
            "heads": [0, 2, 3, 0, 3, 4],
            "deps": ["OPER", "NONE", "NONE", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Addiere 20 und 98 und 36 und 86 und 13",
        {
            "heads": [0, 0, 1, 2, 3, 4, 5, 6, 7, 8],
            "deps": ["OPER", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Zähle 236 und 26 zusammen",
        {
            "heads": [0, 0, 1, 2, 4],
            "deps": ["OPER", "NUM", "LIST", "NUM", "NONE"],
        },
    ),
    (
        "Jenkins zähle 236 und 26 und 75 und 54 zusammen",
        {
            "heads": [0, 1, 1, 2, 3, 4, 5, 6, 7, 9],
            "deps": ["NONE", "OPER", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM", "NONE"],
        },
    ),
    (
        "Nenne die Summe von 15 und 49",
        {
            "heads": [0, 2, 2, 3, 2, 4, 5],
            "deps": ["NONE", "NONE", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),

    (
        "Was ist die Summe von 243 und 53 und 86",
        {
            "heads": [0, 1, 3, 3, 5, 3, 5, 6, 7, 8],
            "deps": ["NONE", "NONE", "NONE", "OPER", "CON", "NUM", "LIST", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Addiere die Summe von 56 und 64 zu der Summe von 62 und 75",
        {
            "heads": [9, 2, 0, 4, 2, 4, 5, 9, 9, 9, 11, 9, 11, 12],
            "deps": ["OPER", "NONE", "OPER", "CON", "NUM", "LIST", "NUM",
                     "CON", "NONE", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Was ist 1 - 2",
        {
            "heads": [0, 1, 2, 2, 3],
            "deps": ["NONE", "NONE", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Subtrahiere 99 von 100",
        {
            "heads": [3, 0, 3, 3],
            "deps": ["OPER", "NUM", "CON", "NUM"],
        },
    ),
    (
        "Subtrahiere die Summe aus 643 und 764 von 743",
        {
            "heads": [8, 2, 0, 4, 2, 4, 5, 8, 8],
            "deps": ["OPER", "NONE", "OPER", "CON", "NUM", "LIST", "NUM", "CON", "NUM"],
        },
    ),
    (
        "Addiere 50 zur Summe von 653 und 64",
        {
            "heads": [3, 0, 3, 3, 5, 3, 5, 6],
            "deps": ["OPER", "NUM", "CON", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Hey Jenkins addiere 5 zur Zahl 32",
        {
            "heads": [1, 2, 6, 2, 6, 6, 6],
            "deps": ["NONE", "NONE", "OPER", "NUM", "CON", "NONE", "NUM"],
        },
    ),
    (
        "Berechne die Summe der Zahlen 6 und 7",
        {
            "heads": [2, 2, 2, 4, 5, 2, 5, 6],
            "deps": ["NONE", "NONE", "OPER", "NONE", "NONE", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Hey Jenkins gebe mir das Ergebnis von 3 + 5 aus",
        {
            "heads": [1, 2, 3, 3, 5, 5, 7, 7, 7, 8, 10],
            "deps": ["NONE", "NONE", "NONE", "NONE", "NONE", "NONE", "CON", "NUM", "OPER", "NUM", "NONE"],
        },
    ),
]