
import json
#import os
#print(dir(os))


# #json
# x = '{"name":"arya","age":12}'
# print(type(x))
# #parsing json to python
# y = json.loads(x)
# print(type(y))

q={"place":"India","place2":"srilanka"}
print(type(q))
w = json.dumps(q)
print(type(w))