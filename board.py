import random
import time

ZERO = 0
ZEROZERO = 37

ODDS = {
    "COLOURS": 2,
    "LOWHIGH": 2,
    "DOZENS": 3,
    "FIVEBET": 7
}

BETCOUNTSRANGES = {
    "COLOURS": (0,1),
    "LOWHIGH": (0,1),
    "DOZENS": (0,2),
    "FIVEBET": (0,1),
}

COLOURS = { "RED": [9, 30, 7, 32, 5, 34, 3, 36, 1, 27, 25, 12, 19, 18, 21, 16, 22 ,14],
          "BLACK": [28, 26, 11, 20, 17, 22, 15, 24, 13, 10, 29, 8, 31, 6, 33, 4, 35, 2] }
LOWHIGH = {"LOW": [i for i in range(1,19)],
           "HIGH": [i for i in range(19, 37)]}
DOZENS = {"FIRST": [i for i in range(1,13)],
          "SECOND": [i for i in range(13, 25)],
          "THIRD": [i for i in range(25, 37)]
          }
FIVEBET = {"WIN": [ZERO, ZEROZERO, 1, 2, 3]}

BETTYPES = {
    "COLOURS": COLOURS,
    "LOWHIGH": LOWHIGH,
    "DOZENS": DOZENS,
    "FIVEBET": FIVEBET,
}

def generateMinBets():
    minBet = {}
    for betType in BETTYPES:
        minBetValue = {}
        for betPossibility in BETTYPES[betType]:
            minBetValue[betPossibility] = 0
        minBet[betType] = minBetValue
    return minBet

def verify_bets(bets):
    for betType in BETTYPES:
        assert betType in bets
        for betVal in BETTYPES[betType]:
            assert betVal in bets[betType]
    
    for betType in BETTYPES:
        count = 0
        for betPossibility in bets[betType]:
            assert bets[betType][betPossibility] >= 0
            if bets[betType][betPossibility] > 0:
                count += 1
        assert BETCOUNTSRANGES[betType][0] <= count and BETCOUNTSRANGES[betType][1] >= count


def spin(bets):
    verify_bets(bets)

    choices = [i for i in range(0, 38)]
    ballLand = random.choice(choices)   

    returnVal = 0

    for betType, value in bets.items():
        for bet, amount in value.items():
            if ballLand in BETTYPES[betType][bet]:
                returnVal += amount * ODDS[betType]
    
    return returnVal

if __name__ == "__main__":
    start_time=  time.time()
    
    testBet = generateMinBets()
    testBet["FIVEBET"]["WIN"] = 10
    freq = {}
    
    for i in range(1000000):
        retVal = spin(testBet)
        if retVal not in freq: freq[retVal] = 0
        freq[retVal] += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    print(freq)