tasx = open('tasks.txt', 'a')
tasxdel = open('tasks.txt', 'w')
tasks = ['the tasks:', ]
tasx.readable()

def addtask():
    while tasks[-1] != 'qf' and tasks[-1] != 'cra':
        del tasks[:1]
        a = tasks.append(input('add task: ').lower())
    if tasks[-1] == 'cra':
        tasxdel.write(a)
#if tasks[-1] == 'qf':
    #    del tasks[-1]
    tasx.write(str(tasks))


addtask()
