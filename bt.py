class BT(object):

  def __init__(self, val):
    self.val = val
    self.r = None
    self.l = None

  def __str__(self):
    return (self.l.__str__() + '<-' if self.l != None else '') + \
            self.val.__str__() + ('->' + self.r.__str__() if self.r != None else '')

  def insert(self, node):
    #insert LEFT
    if self.val > node.val:

      if self.l == None:
        self.l = node
      else:
        self.l.insert(node)

    #insert RIGHT
    else:

      if self.r == None:
        self.r = node
      else:
        self.r.insert(node)

def main():

    import random
    val = sorted(random.sample(xrange(10000), 10))
    #val = ['h','b','c','d','e','f', 'i']

    mid = len(val)/2   
    btreeRoot = BT(val[mid])
    del val[mid]

    print 'root', btreeRoot

    for i in val:
      btreeRoot.insert(BT(i))
      print 'inserted %s:' % i, btreeRoot

main()
