import time  #import timr module
import threading

def cal_square(num): #define the cal square function
    print("calculate the square root of the given number")
    for n in num:
        time.sleep(0.3) #at each iteration it waits for 0.3 time
        print("square is :", n*n)
def cal_cube(num): #define the cal_cube function
    print("calculate the cube of the given number")
    for n in num:
        time.sleep(0.3) #at each iteration it waits for 0.3 time
        print("cube is :",n*n*n)
arr = [4,5,6,7,2] #given array or list

t1 = time.time() #get total time to execute the function
#cal_square(arr) #call cal_square() function
#cal_cube(arr)  #call cal_cube() function
th1 = threading.Thread(target=cal_square, args=(arr,))
th2 = threading.Thread(target=cal_cube, args=(arr, ))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by thread is :", time.time() - t1) #print the total time
