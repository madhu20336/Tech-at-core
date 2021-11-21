from datetime import datetime
print("0900 1700")
employe = int(input("Enter the number of employe: "))
array=[]
for i in range(employe):
    
    submission_time=str(input("enter date(yyyy-mm-dd hh:mm:ss): "))
    id=int(input("enter the id:"))
    print(submission_time,"EMP0"+str(id))
    meetingstarttime = str(input("enter date(yyyy-mm-dd hh:mm :"))
    durationofmeeting=str(input("Enter the duration of the time (hh:mm): "))
    duration=datetime.strptime(durationofmeeting,"%H:%M")
    my_date=datetime.strptime(meetingstarttime, "%Y-%m-%d %H:%M")
    # final_time=(int("%s"%(my_date.hour))+int("%s"%(duration.hour)))+(int("%s"%(my_date.minute))+int("%s"%(duration.minute)))
    final_time=(int("%s"%(my_date.hour))+int("%s"%(duration.hour)))
    final_min=(int("%s"%(my_date.minute))+int("%s"%(duration.minute)))
    if (final_time>=9 and final_time<=17) and (final_min>=00 and final_min<=59):
        array.append(meetingstarttime)
        # array.append(final_time)
        # array.append(final_min)
        
        print(array)
        if meetingstarttime in array :
            print("no over lap")
        else:
            print("over lap")
   
        
    else:
        print("out of office time")
    
