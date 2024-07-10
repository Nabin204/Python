import time 
start = time.time()
sum=0
for i in range(1,pow(10,5)+1):
    sum += i
print(f"The sum of numbers form 1 to 100000 is : ",sum)
end = time.time()
print("Start : ",start)
print("End : ",end)
print("Execution time : ",(end-start)*pow(10,3) ,"ms.")