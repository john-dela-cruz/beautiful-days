def reverseNum(num):
    revNum = 0

    while(num > 0):
        remainder = num % 10
        revNum = (revNum * 10) + remainder
        num = num // 10

    return revNum

def getDiff(num):
    revNum = reverseNum(num)

    if(revNum > num):
        diff = revNum - num
    
    else:
        diff = num - revNum
    
    return diff

def getBeautifulDay(diff, beautifulNum):
    remainder = diff % beautifulNum

    if(remainder == 0):
        return True
    else:
        return False

def getNumOfBDays(firstDay, lastDay, beautifulNum):
    numOfBdays = 0

    for i in range(firstDay, lastDay + 1):
        diff = getDiff(i)
        if(getBeautifulDay(diff,beautifulNum) is True):
            numOfBdays = numOfBdays + 1
    
    return numOfBdays

        


firstDay = int(input('Enter the first day: '))
lastDay = int(input('Enter the last day: '))
beautifulNum = int(input('Enter the Beautiful Number: '))

beautifulDays = getNumOfBDays(firstDay,lastDay,beautifulNum)
print('The number of Beautiful Days is', beautifulDays)