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
            "heads": [3, 2, 3, 3, 3, 4],
            "deps": ["OPER", "NONE", "NONE", "NUM", "LIST", "NUM"],
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
            "heads": [0, 0, 1, 0, 4],
            "deps": ["OPER", "NUM", "LIST", "NUM", "NONE"],
        },
    ),
    (
        "Jenkins zähle 236 und 26 und 75 und 54 zusammen",
        {
            "heads": [0, 1, 1, 2, 1, 4, 1, 6, 1, 9],
            "deps": ["NONE", "OPER", "NUM", "LIST", "NUM", "LIST", "NUM", "LIST", "NUM", "NONE"],
        },
    ),
    (
        "Nenne die Summe von 15 und 49",
        {
            "heads": [0, 2, 2, 3, 2, 4, 2],
            "deps": ["NONE", "NONE", "OPER", "CON", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Was ist die Summe von 243 und 53 und 86",
        {
            "heads": [0, 1, 3, 3, 5, 3, 5, 3, 7, 3],
            "deps": ["NONE", "NONE", "NONE", "OPER", "CON", "NUM", "LIST", "NUM", "LIST", "NUM"],
        },
    ),
    (
        "Addiere die Summe von 56 und 64 zu der Summe von 62 und 75",
        {
            "heads": [9, 2, 0, 4, 2, 4, 2, 9, 9, 9, 11, 9, 11, 9],
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
        "Subtrahiere 64 von 12",
        {
            "heads": [3, 0, 3, 3],
            "deps": ["OPER", "NUM", "CON", "NUM"],
        },
    ),
    (
        "Ziehe 99 von 100 ab",
        {
            "heads": [3, 0, 3, 3, 0],
            "deps": ["OPER", "NUM", "CON", "NUM", "NONE"],
        },
    ),
    (
        "Subtrahiere die Summe aus 643 und 764 von 743",
        {
            "heads": [8, 2, 0, 4, 2, 4, 2, 4, 8],
            "deps": ["OPER", "NONE", "OPER", "CON", "NUM", "LIST", "NUM", "CON", "NUM"],
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
            "deps": ["NONE", "NONE", "OPER", "NUM", "CON", "NONE", "NUM"],
        },
    ),
    (
        "Berechne die Summe der Zahlen 6 und 7",
        {
            "heads": [2, 2, 2, 4, 5, 2, 5, 2],
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
    # Multiplication Data-Set
    (
        'Hey Jenkins rechne 2 x 20',
        {
            'heads': [1, 1, 2, 3, 3, 4, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'Multipliziere 5 mit 7',
        {
            'heads': [1, 1, 3, 0, ],
            'deps': ['OPER', 'NUM', 'CON', 'NUM'],
        },
    ),
    (
        'Hey Jenkins berechne 5 x 8 x 6',
        {
            'heads': [1, 2, 2, 3, 3, 4, 5, 6, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'Berechne das Produkt von 3 und 4',
        {
            'heads': [0, 2, 2, 4, 2, 4, 2, ],
            'deps': ['NONE', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Multipliziere 5 mit 4 mit 3 mit 2 mit 7',
        {
            'heads': [0, 0, 1, 0, 3, 0, 5, 0, 7, 0, ],
            'deps': ['OPER', 'NUM', 'LIST', 'NUM', 'LIST', 'NUM', 'LIST', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        '3 x 5 x 6 x 11 x 6',
        {
            'heads': [0, 0, 1, 2, 3, 4, 5, 6, 7, ],
            'deps': ['NUM', 'OPER', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'Multipliziere das Produkt aus 5 und 7 mit dem Produkt aus 11 und 9',
        {
            'heads': [9, 2, 0, 4, 2, 4, 2, 9, 9, 9, 11, 9, 11, 9, ],
            'deps': ['OPER', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM', 'CON', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Multipliziere 5 mit dem Produkt aus 9 und 9',
        {
            'heads': [4, 0, 3, 3, 4, 6, 4, 6, 4, ],
            'deps': ['OPER', 'NUM', 'CON', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Hey Jenkins gebe mir das Ergbenis von 24 x 12 aus',
        {
            'heads': [1, 2, 3, 3, 5, 5, 7, 7, 7, 8, 10, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'CON', 'NUM', 'OPER', 'NUM', 'NONE'],
        },
    ),
    (
        'Was ist 3 mal 5',
        {
            'heads': [0, 1, 2, 2, 3, ],
            'deps': ['NONE', 'NONE', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        '98 mal die Summe aus 12 und 65',
        {
            'heads': [0, 0, 3, 1, 5, 3, 5, 3, ],
            'deps': ['NUM', 'OPER', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        '34 mal Produkt von 2 und 9',
        {
            'heads': [0, 0, 1, 4, 2, 4, 2, ],
            'deps': ['NUM', 'OPER', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Was ist 34 mal Summe von 2 und 9',
        {
            'heads': [0, 1, 2, 2, 3, 6, 4, 6, 4, ],
            'deps': ['NONE', 'NONE', 'NUM', 'OPER', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Jenkins was ist 7 mal die Summe von 3 und 5',
        {
            'heads': [0, 1, 2, 3, 3, 6, 4, 8, 6, 8, 6, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NUM', 'OPER', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM', ],
        },
    ),
    # Division Data-Set
    (
        'Hey Jenkins rechne 20 durch 5',
        {
            'heads': [1, 1, 2, 3, 3, 4, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'berechne 36 / 6',
        {
            'heads': [0, 1, 1, 2, ],
            'deps': ['NONE', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'Hey Jenkins rechne 20 / 5 / 2',
        {
            'heads': [1, 2, 2, 3, 3, 4, 5, 6, ],
            'deps': ['NONE', 'NONE', 'NONE', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'bilde den Quotienten aus 20 und 5',
        {
            'heads': [1, 2, 2, 4, 2, 4, 2, ],
            'deps': ['NONE', 'NONE', 'OPER', 'CON', 'NUM', 'LIST', 'NUM'],
        },
    ),
    (
        'Hey Jenkins dividiere 20 durch 5',
        {
            'heads': [1, 2, 3, 3, 5, 2, ],
            'deps': ['NONE', 'NONE', 'OPER', 'NUM', 'CON', 'NUM'],
        },
    ),
    (
        '100 / 2 / 5 / 2 / 5',
        {
            'heads': [0, 0, 1, 2, 3, 4, 5, 6, 7, ],
            'deps': ['NUM', 'OPER', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM'],
        },
    ), (
        '100 durch 5 durch 2 durch 5',
        {
            'heads': [0, 0, 1, 2, 3, 4, 5, ],
            'deps': ['NUM', 'OPER', 'NUM', 'OPER', 'NUM', 'OPER', 'NUM'],
        },
    ),
    (
        'Hey Jenkins gebe mit das Ergebnis von 42 / 6 aus',
        {
            'heads': [1, 2, 3, 3, 5, 5, 7, 7, 7, 8, 10,],
            'deps': ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'CON', 'NUM', 'OPER', 'NUM', 'NONE'],
        },
    ),
    (
        'Hey Jenkins gebe mir das Ergebnis von 81 durch 9 aus',
        {
            'heads': [1, 2, 3, 3, 5, 5, 7, 7, 7, 8, 10],
            'deps': ['NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'NONE', 'CON', 'NUM', 'OPER', 'NUM', 'NONE'],
        },
    ),
]
