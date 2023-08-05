## 10^(3*i) dict
thousands = {
    1:  'thousand',
    2:  'million',
    3:  'billion',
    4:  'trillion',
    5:  'quadrillion',
    6: 'quintillion',
}

x_tys = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

tens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

digits = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}


def intToWords(number: int) -> str:
    # each scale is a 10^3 advancement on the number string
    outputString: str = ""
    and_bol = False
    scale = 0
    num_left = number
    while num_left > 0:
        curr_right = num_left % 1000
        num_left = num_left // 1000
        if scale > 0:
            if and_bol:
                outputString = " " + thousands[scale] + outputString
            else:
                if curr_right != 0:
                    outputString = " " + thousands[scale] + outputString

        if curr_right > 0:
            ##check if has 1-99 part
            curr_right_xx = curr_right % 100
            if curr_right_xx > 0:
                # after i check under 1000 ill add support for the list
                if curr_right_xx < 10:
                    outputString = digits[curr_right_xx] + outputString

                if 10 <= curr_right_xx < 20:
                    outputString = tens[curr_right_xx] + outputString

                if 20 <= curr_right_xx < 100:
                    optional_digit = curr_right_xx % 10
                    if optional_digit != 0:
                        outputString = " " + digits[optional_digit] + outputString
                    outputString = x_tys[curr_right_xx//10] + outputString
                # logic for hundreds
                if curr_right // 100 > 0:
                    outputString = digits[curr_right // 100] + " hundred and " + outputString
            else:
                if curr_right // 100 > 0:
                    outputString = digits[curr_right // 100] + " hundred" + outputString


            # by british english we add and after numbers bigger than 1000 if they are smaller than 100
            if num_left > 0:
                if curr_right < 100:
                    outputString = " and " + outputString
                    and_bol = True
                else:
                    if not and_bol:
                        outputString = " and " + outputString
                        and_bol = True
                    else:
                        outputString = ", " + outputString
        scale += 1

    return outputString.capitalize()+"."


def intConverter(number: int) -> str:
    if number == 0:
        return "Zero."
    if number < 0:
        return "Negative " + intToWords(-1 * number)
    else:
        return intToWords(number)


if __name__ == "__main__":
    val = input("Enter a number to convert to string: ")
    print(intConverter(int(val)))
