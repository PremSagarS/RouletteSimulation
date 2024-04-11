data = {
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

replacement_keys = list(range(1, 33))


replaced_data = {replacement_keys[i]: value for i,
                 (_, value) in enumerate(data.items())}

for key, value in replaced_data.items():
    print(key, ":", value, ",")
