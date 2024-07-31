backstack=[]
forwardstack=[]
runningstack=[]
def search():
    i=input("enter a word for search: ")
    if len(runningstack)>=1:
        backstack.append(runningstack.pop())
    runningstack.append(i)
def back():
    c=backstack.pop()
    print(c)
    forwardstack.append(c)
def forward():
    c = forwardstack.pop()
    backstack.append(c)
    print(c)
oper="search"
while True:
    oper=input("what you need to do?")
    if oper=="search":
        search()
    elif oper=="exit":
        break
    elif oper=="forward":
        forward()
    elif oper=="break":
        back()
