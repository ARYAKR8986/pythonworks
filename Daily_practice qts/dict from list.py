def dict1(keys,values):
    return {keys[i]:values[i] for i in range(len(keys))}
movie = ['RDB','wanted','DDLG','sholay','war']
actor = ['Amir','Salman','SRK','Amitabh','Hrithik']
print('dictionary:',str(dict1(movie,actor)))