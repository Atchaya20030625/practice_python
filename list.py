if __name__ == '__main__':
    N = int(input())
    my_list=[]
    for i in range(N):
        command=input().split()
        action= command[0]
        if action=='append':
            my_list.append(int(command[1]))
        elif action=='insert':
            index = int(command[1])
            element = int(command[2])
            my_list.insert(index,element)
        elif action=="remove":
            value=int(command[1])
            my_list.remove(value)
        elif action=="sort":
            my_list.sort()
        elif action=="pop":
            my_list.pop()
        elif action=="reverse":
            my_list.reverse()
        elif action=='print':
            print(my_list)
