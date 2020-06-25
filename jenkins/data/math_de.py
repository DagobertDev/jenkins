""" German math data for training and evaluatiopn
    -: Word is not necessary for understanding the question,
    OPER: Mathematical Operator,
    NUM: Number
"""

TRAIN_DATA = [
    (
        "Was ist 1 + 2",
        {
            "heads": [1, 1, 2, 2, 3],
            "deps": ["-", "-", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Hallo Jenkins berechne 1 + 2 - 23",
        {
            "heads": [1, 2, 2, 3, 3, 4, 5, 6],
            "deps": ["-", "-", "-", "NUM", "OPER", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Kannst du 563 + 21 berechnen",
        {
            "heads": [1, 5, 2, 3, 4, 2],
            "deps": ["-", "-", "NUM", "OPER", "NUM", "-"],
        },
    ),
    (
        "Addiere die Zahlen 20 und 98",
        {
            "heads": [0, 2, 3, 0, 3, 0],
            "deps": ["OPER", "-", "-", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Addiere 20 und 98 und 36 und 86 und 13",
        {
            "heads": [0, 0, 1, 0, 3, 0, 5, 0, 7, 0],
            "deps": ["OPER", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Zähle 236 und 26 zusammen",
        {
            "heads": [0, 1, 1, 1, 0],
            "deps": ["-", "NUM", "LIST", "NUM", "-"],
        },
    ),
    (
        "Jenkins zähle 236 und 26 und 75 und 54 zusammen",
        {
            "heads": [0, 1, 1, 2, 1, 4, 1, 6, 1, 9],
            "deps": ["-", "OPER", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM", "-"],
        },
    ),
    (
        "Nenne die Summe von 15 und 49",
        {
            "heads": [0, 2, 2, 3, 2, 4, 2],
            "deps": ["-", "-", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),

    (
        "Was ist die Summe von 243 und 53 und 86",
        {
            "heads": [0, 1, 3, 3, 5, 3, 5, 3, 7, 3],
            "deps": ["-", "-", "-", "OPER", "CON", "NUM", "LIST", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Addiere die Summe von 56 und 64 zu der Summe von 62 und 75",
        {
            "heads": [9, 2, 0, 4, 2, 4, 2, 9, 9, 9, 11, 9, 11, 9],
            "deps": ["OPER", "-", "OPER", "CON", "NUM", "LIST", "NUM",
                     "CON", "-", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Was ist 1 - 2",
        {
            "heads": [0, 1, 2, 2, 3],
            "deps": ["-", "-", "NUM", "OPER", "NUM"],
        },
    ),
    (
        "Ziehe 99 von 100 ab",
        {
            "heads": [3, 0, 3, 3, 0],
            "deps": ["OPER", "NUM", "CON", "NUM", "-"],
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
            "heads": [8, 2, 0, 4, 2, 4, 2, 8, 8],
            "deps": ["OPER", "-", "OPER", "CON", "NUM", "LIST", "NUM", "CON", "NUM"],
        },
    ),
    (
        "Ziehe die Summe aus 643 und 764 von 743 ab",
        {
            "heads": [8, 2, 0, 4, 2, 4, 2, 8, 8, 0],
            "deps": ["OPER", "-", "OPER", "CON", "NUM", "LIST", "NUM", "CON", "NUM", "-"],
        },
    ),
    (
        "Addiere 50 zur Summe von 653 und 64",
        {
            "heads": [3, 0, 3, 3, 5, 3, 5, 3],
            "deps": ["OPER", "NUM", "CON", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Hey Jenkins addiere 5 zur Zahl 32",
        {
            "heads": [1, 2, 6, 2, 6, 6, 6],
            "deps": ["-", "-", "OPER", "NUM", "CON", "-", "NUM"],
        },
    ),
    (
        "Berechne die Summe der Zahlen 6 und 7",
        {
            "heads": [2, 2, 2, 4, 5, 2, 5, 2],
            "deps": ["-", "-", "OPER", "-", "-", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Hey Jenkins gebe mir das Ergebnis von 3 + 5 aus",
        {
            "heads": [1, 2, 3, 3, 5, 5, 7, 7, 7, 8, 10],
            "deps": ["-", "-", "-", "-", "-", "-", "CON", "NUM", "OPER", "NUM", "-"],
        },
    ),
]
