'''
Author - PRABHAKAR KUMAR
Roll   - IRM2017008
Date   - 7th Feb, 2020
'''

# The generated data is for age which is taken
# to lie between 0 to 100.

import random
import matplotlib.pyplot as plt

# For 15 sets
set_index=[]
set_sum=[]
set_mean=[]
set_var=[]
for i in range(15):
    print("For Set ",i,"\n\n");
    total_sum=0
    global_list=[]
    global_data=[]
    for j in range(10):
        local_list=[]
        local_sum=0
        for k in range(20):
            num=random.randint(0,100)
            local_sum=local_sum+num
            local_list.append(num)
        global_data.append({})
        global_data[j]["sum"]=local_sum
        mean=local_sum/20
        global_data[j]["mean"]=mean
        var=0
        for k in range(20):
            var=var+(local_list[k]-mean)**2
        var=var/19
        global_data[j]["variance"]=var
        global_list.append(local_list)
        total_sum=total_sum+local_sum
        
        print("For ",j,"th class - ")
        print("Total Sum = ",local_sum)
        print("Mean = ",mean)
        print("Variance = ",var,"\n")
        
    total_mean=total_sum/200
    total_var=0
    for j in range(10):
        for k in range(20):
            total_var=total_var+(global_list[j][k]-total_mean)**2
    total_var=total_var/199
    print("For ",i,"th Set - ")
    print("Total Sum = ",total_sum)
    print("Total Mean = ",total_mean)
    print("Total Variance = ",total_var,"\n\n")
    set_index.append(i+1)
    set_sum.append(total_sum)
    set_mean.append(total_mean)
    set_var.append(total_var)
    
plt.plot(set_index,set_sum,label="Total Sum Per Set")
plt.plot(set_index,set_mean,label="Total Mean Per Set")
plt.plot(set_index,set_var,label="Total Variance Per Set")
plt.legend()
plt.show()            
            