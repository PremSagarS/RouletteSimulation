ZERO = 0
ZEROZERO = 37

ODDS = {
    "COLOURS": 2,
    "LOWHIGH": 2,
    "EVENODD": 2,
    "DOZENS": 3,
    "FIVEBET": 7,
    "STREET": 12,
    "CORNER": 9,
    "COLUMN": 3,
    "SIXBET": 6,
    "SPLIT": 18,
    "STRAIGHTUP": 36, 
}

BETCOUNTSRANGES = {
    "COLOURS": (0,1),
    "LOWHIGH": (0,1),
    "EVENODD": (0,1),
    "DOZENS": (0,2),
    "FIVEBET": (0,1),
    "STREET": (0,11),
    "CORNER": (0,21),
    "COLUMN": (0,2),
    "SIXBET": (0,11),
    "SPLIT": (0,56),
    "STRAIGHTUP": (0, 35)
}

COLOURS = { "RED": [9, 30, 7, 32, 5, 34, 3, 36, 1, 27, 25, 12, 19, 18, 21, 16, 22 ,14],
          "BLACK": [28, 26, 11, 20, 17, 22, 15, 24, 13, 10, 29, 8, 31, 6, 33, 4, 35, 2] }

LOWHIGH = {"LOW": [i for i in range(1,19)],
           "HIGH": [i for i in range(19, 37)]}

DOZENS = {"FIRST": [i for i in range(1,13)],
          "SECOND": [i for i in range(13, 25)],
          "THIRD": [i for i in range(25, 37)]
          }

EVENODD = {
    "ODD": [ i for i in range(1,37) if i%2==1 ],
    "EVEN": [ i for i in range(2,37) if i%2==0 ],
    }

FIVEBET = {"WIN": [ZERO, ZEROZERO, 1, 2, 3]}

STREET = {
    "ONE": [i for i in range(1,4)],
    "TWO": [i for i in range(4,7)],
    "THREE": [i for i in range(7,10)],
    "FOUR": [i for i in range(10,13)],
    "FIVE": [i for i in range(13,16)],
    "SIX": [i for i in range(16,19)],
    "SEVEN": [i for i in range(19,22)],
    "EIGHT": [i for i in range(22,25)],
    "NINE": [i for i in range(25,28)],
    "TEN": [i for i in range(28,31)],
    "ELEVEN": [i for i in range(31,34)],
    "TWELVE": [i for i in range(34,37)],
    }

CORNER = {
    "ONE": [1, 2, 4, 5],
    "TWO": [2, 3, 5, 6],
    "THREE": [4, 5, 7, 8],
    "FOUR": [5, 6, 8, 9],
    "FIVE": [7, 8, 10, 11],
    "SIX": [8, 9, 11, 12],
    "SEVEN": [10, 11, 13, 14],
    "EIGHT": [11, 12, 14, 15],
    "NINE": [13, 14, 16, 17],
    "TEN": [16, 17, 19, 20],
    "ELEVEN": [17, 18, 20, 21],
    "TWELVE": [14, 15, 17, 18],
    "THIRTEEN": [19, 20, 22, 23],
    "FOURTEEN": [20, 21, 23, 24],
    "FIFTEEN": [22, 23, 25, 26],
    "SIXTEEN": [23, 24, 26, 27],
    "SEVENTEEN": [25, 26, 28, 29],
    "EIGHTEEN": [26, 27, 29, 30],
    "NINETEEN": [28, 29, 31, 32],
    "TWENTY": [29, 30, 32, 33],
    "TWENTY ONE": [31, 32, 34, 35],
    "TWENTY TWO": [32, 33, 35, 36],
}

COLUMN = {
    "FIRST": [i for i in range(1, 37) if i % 3 == 1],
    "SECOND": [i for i in range(2, 37) if i % 3 == 2],
    "THIRD": [i for i in range(3, 37) if i % 3 == 0]
}

SIXBET = {
    "ONE": [i for i in range(1, 7)],
    "TWO": [i for i in range(4, 10)],
    "THREE": [i for i in range(7, 13)],
    "FOUR": [i for i in range(10, 16)],
    "FIVE": [i for i in range(13, 19)],
    "SIX": [i for i in range(16, 22)],
    "SEVEN": [i for i in range(19, 25)],
    "EIGHT": [i for i in range(22, 28)],
    "NINE": [i for i in range(25, 31)],
    "TEN": [i for i in range(28, 34)],
    "ELEVEN": [i for i in range(31, 37)],
}

SPLIT = {
    'ONE': [1, 2],
    'TWO': [1, 4], 
    'THREE': [2, 3],
    'FOUR': [2, 5],
    'FIVE': [3, 6],
    'SIX': [4, 5], 
    'SEVEN': [4, 7], 
    'EIGHT': [5, 6], 
    'NINE': [5, 8], 
    'TEN': [6, 9], 
    'ELEVEN': [7, 8], 
    'TWELVE': [7, 10], 
    'THIRTEEN': [8, 9], 
    'FOURTEEN': [8, 11], 
    'FIFTEEN': [9, 12], 
    'SIXTEEN': [10, 11], 
    'SEVENTEEN': [10, 13], 
    'EIGHTEEN': [11, 12], 
    'NINETEEN': [11, 14], 
    'TWENTY': [12, 15], 
    'TWENTY ONE': [13, 14], 
    'TWENTY TWO': [13, 16], 
    'TWENTY THREE': [14, 15], 
    'TWENTY FOUR': [14, 17], 
    'TWENTY FIVE': [15, 18], 
    'TWENTY SIX': [16, 17], 
    'TWENTY SEVEN': [16, 19], 
    'TWENTY EIGHT': [17, 18], 
    'TWENTY NINE': [17, 20], 
    'THIRTY': [18, 21], 
    'THIRTY ONE': [19, 20], 
    'THIRTY TWO': [19, 22], 
    'THIRTY THREE': [20, 21], 
    'THIRTY FOUR': [20, 23], 
    'THIRTY FIVE': [21, 24], 
    'THIRTY SIX': [22, 23], 
    'THIRTY SEVEN': [22, 25], 
    'THIRTY EIGHT': [23, 24], 
    'THIRTY NINE': [23, 26], 
    'FORTY': [24, 27], 
    'FORTY ONE': [25, 26], 
    'FORTY TWO': [25, 28], 
    'FORTY THREE': [26, 27], 
    'FORTY FOUR': [26, 29], 
    'FORTY FIVE': [27, 30], 
    'FORTY SIX': [28, 29], 
    'FORTY SEVEN': [28, 31], 
    'FORTY EIGHT': [29, 30], 
    'FORTY NINE': [29, 32], 
    'FIFTY': [30, 33], 
    'FIFTY ONE': [31, 32], 
    'FIFTY TWO': [31, 34], 
    'FIFTY THREE': [32, 33], 
    'FIFTY FOUR': [32, 35], 
    'FIFTY FIVE': [33, 36], 
    'FIFTY SIX': [34, 35], 
    'FIFTY SEVEN': [35, 36]
    }

STRAIGHTUP = {
    'ONE': [1],
    'TWO': [2],
    'THREE': [3],
    'FOUR': [4],
    'FIVE': [5],
    'SIX': [6],
    'SEVEN': [7],
    'EIGHT': [8],
    'NINE': [9],
    'TEN': [10],
    'ELEVEN': [11],
    'TWELVE': [12],
    'THIRTEEN': [13],
    'FOURTEEN': [14],
    'FIFTEEN': [15],
    'SIXTEEN': [16],
    'SEVENTEEN': [17],
    'EIGHTEEN': [18],
    'NINETEEN': [19],
    'TWENTY': [20],
    'TWENTY ONE': [21],
    'TWENTY TWO': [22],
    'TWENTY THREE': [23],
    'TWENTY FOUR': [24],
    'TWENTY FIVE': [25],
    'TWENTY SIX': [26],
    'TWENTY SEVEN': [27],
    'TWENTY EIGHT': [28],
    'TWENTY NINE': [29],
    'THIRTY': [30],
    'THIRTY ONE': [31],
    'THIRTY TWO': [32],
    'THIRTY THREE': [33],
    'THIRTY FOUR': [34],
    'THIRTY FIVE': [35],
    'THIRTY SIX': [36],
}

BETTYPES = {
    "COLOURS": COLOURS,
    "LOWHIGH": LOWHIGH,
    "DOZENS": DOZENS,
    "FIVEBET": FIVEBET,
    "STREET": STREET,
    "CORNER": CORNER,
    "COLUMN": COLUMN,
    "SIXBET": SIXBET,
    "EVENODD": EVENODD,
    "SPLIT": SPLIT,
    "STRAIGHTUP": STRAIGHTUP
}