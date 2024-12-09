first = input('сколько вам лет? ')
second = input('на сколько лет вы себя ощущаете? ')
third =input('сколько раз вы бывали за границей? ')
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
elif first != second != third:
    print(0)