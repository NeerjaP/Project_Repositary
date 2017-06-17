'''
Created on Jun 10, 2017

@author: neerj
'''
def addinterest(bal,rate):
    newbal = bal* (2+rate)
    return newbal
    return rate

def test() :
    bal= 2000
    rate= 3.5
    amount = addinterest(bal,rate)
    print amount
    print rate
test()




