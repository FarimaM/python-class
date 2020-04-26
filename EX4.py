"chandomin rooze separi shode az saal"
d = int(input('rooz: '))
m = int(input('mah:  '))
y = int(input('sal: '))
days=[31,28,31,30,31,30,31,31,31,30,31,30]
days_passed = 0
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
   days[1] = 29
for months in days[:m-1]:
    days_passed += months
    days_passed += d
print(days_passed)
