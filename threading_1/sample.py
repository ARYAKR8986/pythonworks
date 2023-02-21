# from time import sleep
#def task():
#     #block for a moment
#     sleep(3)
#     #display a message
#     print('this is from another thread')
# task()


# from threading_1 import Thread
# def task():
#     #create a thread
#     thread = Thread(target=task)
#     #next we can create an instance of the threading_1 . Thread class and specify
#     #our function name as the "target" argument in the constuctor.
# Thread.start()


#a custom function that blocks for a moment

def task(sleep_time,message):
    #block for a moment
    sleep(sleep_time)
    #display a message
    print(message)

#create a thread
thread = Thread(target=task, args=(1.5, 'new mwssage from another thread'))




    #by using threading_1

