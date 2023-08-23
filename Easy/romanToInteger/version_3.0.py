roman = "MCIV"

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
    result = [] 
    j = 2
    i = 0
    total = 0

    while i <= (len(roman)-1):
        if i < len(roman)-1 and ((roman[i] == "I" and roman[i+1] in ["V","X"]) or
            (roman[i] == "X" and roman[i+1] in ["L","C"])  or
            (roman[i] == "C" and roman[i+1] in ["D","M"])) :
            result.append(roman[i:j])
            Calculation(result, romanList)
            total = CalculationOfTotal(total, result[len(result) - 1])
            i+=2
            j+=2
        else:
            result.append(roman[i])
            Calculation(result, romanList)
            total = CalculationOfTotal(total, result[len(result) - 1])
            i+=1
            j+=1
            
    return total       

def CalculationOfTotal(total, lastVal):
    if total >= lastVal:
        total = total + lastVal
    else:
        total = lastVal - total
    return total       
            
def Calculation(result, romanList):
    a = romanList.get(result[len(result) - 1][0])
    if len(result[len(result) - 1]) == 1:
        result[len(result) - 1] = a
        return result
    b = romanList.get(result[len(result) - 1][1])
    if a >= b:
        result[len(result) - 1] = a + b
    else:
        result[len(result) - 1] = b - a
    return result

print(convertRomanToInteger(roman))