def testfilter(x):
    for y in filter((lambda z: z>5), x):
        print(y)

test = range(1, 11)
testfilter(test)
