def verbose(number):

    units = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    scales = ['', 'Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion', 'Septillion', 'Octillion', 'Nonillion',  'Decillion',  'Undecillion',  'Duodecillion',  'Tredecillion', 'Quattuordecillion', 'Quindecillion', 'Sexdecillion',  'Septendecillion',  'Octodecillion', 'Novemdecillion',  'Vigintillion']

    words = []

    if number < 0:
        words.append('This Program Can\'t Verbose The Number Less Than 0, Try Again!')

    elif number == 0:
        words.append('Zero')

    else:
        numStr = '%d' % number # convert number to string
        numStrLen = len(numStr) # length of number
        groups = (numStrLen + 2) // 3 # group number. for example, 100 = group 1, 1000 = group 2, 1000000 = group 3
        numStr = numStr.zfill(groups * 3) # add zero to str by group size

        for i in range(0, groups * 3, 3):

            h = int(numStr[i]) # 1st unit of 3 by group
            t = int(numStr[i+1]) # 2nd unit of 3 by group
            u = int(numStr[i+2]) # 3rd unit of 3 by group
            g = int(groups - (i / 3 + 1)) # number of this group

            if h >= 1:
                words.append(units[h])
                words.append('Hundred')
            
            if t > 1:
                words.append(tens[t])
                if u >= 1:
                    words.append(units[u])

            elif t == 1:
                if u >= 1:
                    words.append(teens[u])
                else:
                    words.append(tens[t])
            else:
                if u >= 1:
                    words.append(units[u])
            
            if g >= 1 and (h + t + u) > 0:
                words.append(scales[g])

    return words

def list_to_string(words_list):
    return ' '.join(words_list)
    
def decorate_output(text):
    print('==============================')
    print(text)
    print('==============================')

decorate_output(list_to_string(verbose(int(input('Input your number : ')))))