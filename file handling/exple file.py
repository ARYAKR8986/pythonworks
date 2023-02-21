# f = open('test1','r')
# for i in f:
#     print(i)
# f.close()

# f = open('test1','a')
# f.write('python is a oop')
# f.close()
#
# f = open('test1','r')
# for i in f:
#     print(i)
# f.close()

# f = open('test1','w')
# f.write('python is a oop')
# f.close()
#
# f = open('test1','r')
# for i in f:
#     print(i)
# f.close()
# f = open('test1','r')
# f.seek(8)
# print(f.readline())
# f.close()

# f = open('test1','r')
# f.readline()
# pos = f.tell()
# f.close()
# print('position is',pos)

# '''program to read a file line by line and store in list'''
#
# def file_read(fna):
#     with open(fna) as f:
#         output_list = f.readlines()
#         print(output_list)
# file_read('test1')
#
# from shutil import copyfile
# copyfile('test1','test2') #syntax - (file to be copied , file to copy)

str = 'cat rat mat cat pat rat cat sat cat sat'
print(str)
lst = str.split()
dict1 = {}
for i in lst:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)