def task1():
    n = int(input())
    array = []
    for i in range(1, n+1):
        array.append(i)
        if i % 5 == 0:
                array[i-1] = "buzz"
        if i % 3 == 0:
            array[i-1] = "fizz"
            if i % 5 == 0:
                array[i-1] = "fizzbuzz"

    print(" ".join(map(str, array)))
task1
def task2():
    userinput = input("")
    words = userinput.split()
    words.reverse()
    for i in range(len(words)):
        if words[i].isdigit():
            words[i] = int(words[i])*-1
    print(words)    
task2