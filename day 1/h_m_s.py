total_seconds=int(input("enter the total seconds:"))
hours=total_seconds/3600
minutes=(total_seconds%3600)/60
seconds=(total_seconds%3600)%60
print("the time is : ",int(hours),"hour:",int(minutes),"minutes:",int(seconds),"seconds")