roman = "IXIX"

romanList = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def convertRomanToInteger(roman):
    total = 0
    prev_val = 0
    for number in reversed(roman):
        val = romanList[number]
        if val < prev_val:
            total -= val
        else:
            total += val
        prev_val = val
    return total

print(convertRomanToInteger(roman))
            