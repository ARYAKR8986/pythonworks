listofdict = [{"V":"S001"},{"V":"S002"},{"VI":"SOO1"},{"VI":"SOO5"},{"VII":"SOO5"},{"V":"S009"},{"VIII":"S007"}]
setof_uvalues = set()
for i in listofdict:
    for value in i.values():
        setof_uvalues.add(value)
print(setof_uvalues)

#another method

listofdict = [{"V":"S001"},{"V":"S002"},{"VI":"SOO1"},{"VI":"SOO5"},{"VII":"SOO5"},{"V":"S009"},{"VIII":"S007"}]
dict = []
for i in listofdict:
    dict.extend(list(i.values()))
dict = set(dict)
print(dict)