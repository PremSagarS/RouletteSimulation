from bets import *
import random
import time

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
    testBet["LOWHIGH"]["LOW"] = 10
    testBet["STRAIGHTUP"]["ONE"] = 10
    testBet["STREET"]["THREE"] = 10
    testBet["EVENODD"]["ODD"] = 10
    testBet["COLOURS"]["RED"] = 10
    testBet["CORNER"]["FIVE"] = 10
    testBet["SPLIT"]["TWENTY ONE"] = 10
    freq = {}
    
    for i in range(10000):
        retVal = spin(testBet)
        if retVal not in freq: freq[retVal] = 0
        freq[retVal] += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    print(freq)