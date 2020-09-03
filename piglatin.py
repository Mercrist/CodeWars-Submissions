def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000}
    output = 0
    roman = list(roman)
    for i in range(len(roman)): 
        if i != len(roman)-1 and numerals[roman[i]] < numerals[roman[i+1]]:
            output -= numerals[roman[i]]
        else:
            output += numerals[roman[i]]
    return output