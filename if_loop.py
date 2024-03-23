is_male = True
if is_male:
    print('you are a male')
else:
    print('you are not a male')

is_male = False
is_tall= False
if is_male or is_tall:      #or=one or both is true
    print('you are a male or tall or both')
else:
    print('you neither male not tall')

is_male = True
is_tall= True
if is_male and is_tall:      #and=when both is true
    print('you are a tall male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male) and is_tall:
    print('you are not a male but tall')
else:
    print('you are either not male or not tall')