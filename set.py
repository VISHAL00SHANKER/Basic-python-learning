'''collection of unordered items 
-> immutable
->removes duplicates
->no fix index
'''

Days = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday'}
print(Days)
print(type(Days), '\n') 
for i in Days:
   print(i)

print('\n')
Months = set([ "jan",  'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
for i in Months:
    print(i)
