str = input()
cntLow, cntUpp = 0, 0;
for char in str:
    if char.islower() == True: cntLow+=1;
    elif char.isupper() == True: cntUpp+=1;
if cntLow >= cntUpp: print(str.lower())
else: print(str.upper())