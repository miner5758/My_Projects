def unit_converter(go):  
  if first_unit == 'cm' or first_unit == 'Cm' or first_unit == 'CM' and first_unit != second_unit:
      cm_conversion('go')
  
  
def cm_conversion(go):
    if second_unit == 'm' or second_unit == 'M':
        New_first_number = first_number/100
    per_conversion(New_first_number)



def per_conversion(N):
    if per == 'Hour' or per == 'hour' and per != second_per:
        if second_per == 'min' or second_per == 'Min' or second_per == 'Minute' or second_per == 'minute':
            new_per_number = 60
            final_stage(N,new_per_number)
    else:
        final_stage(N,1)
    
def final_stage(New_firstNum,new_per_number):
    New_firstNum = float(New_firstNum/new_per_number)
    print(str(New_firstNum)+second_unit,'per',second_per)


first_number = float(input('first value(example:7):'))
first_unit = input('what unit is your number in?(example:cm):')
per = input('per(example:hour):')
second_unit = input('unit you want to convert to:')
second_per = input('what do to convert {} too?'.format(per))
unit_converter('go')
