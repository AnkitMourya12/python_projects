def convert24(str1):
    if str1[-2:]=='AM' and str1[:2]=='12':  # if 12 AM then convert into 00:minute:seconds
        return '00'+str1[2:]
    elif str1[-2:]=='AM':
        return str1[0:]
    elif str1[-2:]=='PM' and str1[:2]=='12':
        return str1[0:]
    else:
        return str(int(str1[:2])+12)+str1[2:11]

print()
print()
print("********************************************************************************************************************************************************************")
print()
print()
print()

print("                                                          SMALL PROJECT CONVERT 12 HOURS INTO 24 HOURS FORMATE")
st=input("                                                              enter the time in format of hh:mm:ss AM/PM:")
print()
print("                                                                     Output is:",convert24(st),"          ")
print()
print()
print()
print("********************************************************************************************************************************************************************")
