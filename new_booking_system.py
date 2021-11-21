from datetime import *
print("0900 1730")
loop=int(input("Enter the number of employess:"))
first=[]
duration_list=[]
dic={}
for i in range(loop):
    my_string = str(input('Enter date(yyyy/mm/dd hh:mm:ss) :'))
    start=int(input("Enter the starting time of the meeting "))
    duration=int(input("Enter the duration of the meeting in hours "))
    my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M:%S")
    x=datetime(int("%s"%(my_date.year)),int("%s"%(my_date.month)),int("%s"%(my_date.day)),int("%s"%(my_date.hour)),int("%s"%(my_date.minute)),int("%s"%(my_date.second)))
    first.append(x)
    dic[x]={start:start+duration}
    # first.append((("%s"%(my_date.year)),("%s"%(my_date.month)),("%s"%(my_date.day)),("%s"%(my_date.hour)),("%s"%(my_date.minute)),("%s"%(my_date.second))))
    # first.append(int("%s"%(my_date.hour)))
    # id = int(input("enter the id"))
    # start=int(input("Enter the starting time of the meeting"))
    # duration=int(input("Enter the duration of the meeting"))
    # my_date = datetime.strptime(my_string, "%Y-%m-%d %H:%M:%S")
    # print("%s"%(my_date.hour))
    # if (int("%s"%(my_date.hour))>=9 and int("%s"%(my_date.minute))>=0) and (int(("%s"%(my_date.hour)))<=17 and int("%s"%(my_date.minute))<=30):
    #     continue
    # else:
    #     print("wrong")
# duplicates=[i for i in first if first.count(i)>1]
key_list=list(dic.keys())
for i in range(len(key_list)):
    for k in range(len(key_list)-i-1):
        if key_list[k]>key_list[k+1]:
            temp=key_list[k]
            key_list[k]=key_list[k+1]
            key_list[k+1]=temp
final={}
for i in key_list:
    for k in dic:
        if i==k :
            final[i]=dic[k]
print(final)
# val_list=final.values()
# slots=[]
# for i in range(len(val_list)):
#     if i==0:
#         slots.append(val_list[i])
#     else:
#         if val_list[i][0]>slots[i-1][1] or val_list[i][1]<slots[i-1][0]:
#             slots.append(val_list[i])
#         else:
#             print("Overlap")

