roman = "MCMXCIV"

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
    while i <= (len(roman)-1):
        if i < len(roman)-1 and ((roman[i] == "I" and roman[i+1] in ["V","X"]) or
            (roman[i] == "X" and roman[i+1] in ["L","C"])  or
            (roman[i] == "C" and roman[i+1] in ["D","M"])) :
            result.append(roman[i:j])
            i+=2
            j+=2
        else:
            result.append(roman[i])
            i+=1
            j+=1        
        
    for i in range(len(result)):
        a = romanList.get(result[i][0])
        if len(result[i]) == 1 and i == len(result) - 1:
            result[i] = a
            break
        elif len(result[i]) == 1:
            result[i] = a
            continue
        b = romanList.get(result[i][1])
        if a >= b:
            result[i] = a + b
        else:
            result[i] = b - a
            
    total = 0
    for i in range(len(result)):
        if total >= result[i]:
            total = total + result[i]
        else:
            total = result[i] - total
    return total


print(convertRomanToInteger(roman))