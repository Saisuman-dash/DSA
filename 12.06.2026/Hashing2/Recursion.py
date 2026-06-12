# Recursion is a function calling itself . if we will not put a stopping condition this will give us a stack overflow error 
# Stack overflow comes in c c++ and java but in python the function will get called 987 times and then it will give us a RecursionError: maximum recursion depth exceeded in comparison
str = int(input("Enter starting number :"))
end = int(input("Enter ending number :"))
def func(i,n):
    if i > n:       #Stopping condn
        return
    print(i)        #Job
    func(i+1,n)     #Head recursion

func(str,end)
