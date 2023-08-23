# Version 1.0.0

I just learned the Version naming, So just Let's talk about it first. There are many kinds of way to represent a person of a system but the most used one is X.Y.Z

1. **X** : The major version
2. **Y** : The minor version
3. **Z**  : The patch version 

Alright so now we know about the version system let's talk about our first problem on this GitHub depository

>[!NOTE]
> All the questions I will use will be from [leetCode website](https://leetcode.com/)

Hopefully I will learn a lot of things :+1:

## Roman to Integer
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

|**Symbol**|**Value**|
|--|--|
|I|1|
|V|5|
|X|10|
|L|50|
|C|100|
|D|500|
|M|1000|

For example, 2 is written as `II` in Roman numeral, just two ones added together. 12 is written as XII, which is simply `X + II`. The number 27 is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

### Combination rules

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9. 
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90. 
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.    

**Example 1:**<br>
    **Input**: s = "III"<br>
    **Output**: 3<br>
    **Explanation**: III = 3.

**Example 2:**<br>
    **Input**: s = "MCMXCIV"<br>
    **Output**: 1994<br>
    **Explanation**: M = 1000, CM = 900, XC = 90 and IV = 4.

# Solution
## Approach

The Simplest thing is within the example when we have<br>
let's say <br>
- `III` = `I` + `I` + `I` <br>
- `IV`  = `I` + `V`<br>
- `CMIV`  = `CM` + `IV`

The simplest solution i came up with was using an array<br>
```python
result = []
```
Break the coming string of **Roman numbers** down into pairs of two and put it in the array

```python
roman = "IXIV"

result = ["IX","IV"]
```
which I achieved using this logic
```python
j = 0
i = 0
while i <= (len(roman)-1):
    i+=2
    result.append(roman[j:i])
    j+=2
```

Then we can work with pairs of two or one to do the calculation:<br>
* if first value is big and second is small, we add them
* if first value is small and second is big, we Subtract them

visually it will look like this
```python
result = ["IX","IV"]
# IX = I(1)X(X) = 10 - 1 = 9
# IV = I(1)V(5) = 5 - 1  = 4
# After Calculation our updated array will look like
result = [9,4]
```
The simple solution is a bit complicated for this one it took me a while to figure out how will I convert and put values as well
```python
for i in range(len(result)):
    a = romanList.get(result[i][0])
    ```
    If the length is one it means we are at the end 
    of the array where we have only one pair of one 
    letter like "I" here: result = ["IX","IV", "I"]
    ```
    if len(result[i]) == 1
        result[i] = a
        break
    b = romanList.get(result[i][1])
    if a >= b:
        result[i] = a + b
    else:
        result[i] = b - a
```
Then we just need to do the rest of the calculation to get to the answerthe logic will be same if a is bigger than or equal to b we add otherwise we subtract<br>
In our case:
```python
total = 0
result = [9,4]
total = 9 + 4
total = 13
```
And it could be done by
```python
for i in range(len(result)):
    if total >= result[i]:
        total = total + result[i]
    else:
        total = result[i] - total
return total
```
## Mistakes
At this point I thought I have the answer but with this logic if we are trying to convert this roman number `MCMXCIV`, I thought it would result in `MC` + `MX` + `CI` + `V` <br><br>
Which was wrong because I didn't read the question properly<br>
It was supposed to look like this: `M` + `CM` + `XC` + `IV` <br><br>

This happened because of I didn't follow the rule of [Combination rules](#combination-rules)

Alright can apply these rules in our combining statement in Wile loop
```python
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
```

since now we can have a pair of one in the middle or in the front of our array Instead of at the end, we have to change the logic forward calculation as well
```python
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
```
## Efficiency
Alright this solution is a completely working now but as you can see we are using three *Three Loops* for three logics. I already knew the solution was not efficient but I just want to make The code work since it is like my 4th leetCode question the solution I have right now, will run with the time complexity of **O(n<sup>3</sup>)** Which is actually quite slow, now let's try to improve the Solution

# Version 1.0.0

The first big improvement we can do is just by joining two septate logics together in one loop, Currently we use:<br>
* One loop for creating pairs
* Second loop for Calculation of those pairs

So every time we make a pair of two Values let's lay `IV` We pass the same array into another function so that the calculation can be done on only the value which is at the end of the array. And here's that function

```python
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
```

Now we can use this function every time we create a pair right away we can do the calculation

```python
 result = [] 
    j = 2
    i = 0
    while i <= (len(roman)-1):
        if i < len(roman)-1 and ((roman[i] == "I" and roman[i+1] in ["V","X"]) or
            (roman[i] == "X" and roman[i+1] in ["L","C"])  or
            (roman[i] == "C" and roman[i+1] in ["D","M"])) :
            result.append(roman[i:j])
            Calculation(result, romanList)
            i+=2
            j+=2
        else:
            result.append(roman[i])
            Calculation(result, romanList)
            i+=1
            j+=1
```

But still we need to calculate the actual value For that we again need to loop through the array with the same logic

## Efficiency

Hello as our code uses only two loops now the time complexity would decrease to **O(n<sup>2</sup>)** Which is still bad but better than last time let's see if we can make it with **O(n)** In version three

