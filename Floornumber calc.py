def computepay(Hours, Rate):
    if Hours <= 40 :
        calc = Hours * Rate
    elif Hours > 40 :
        calc = ((Hours - 40) * 15) + 400
    return calc

dave = computepay(50,10)
print('The salary for Dave this month is ', dave)