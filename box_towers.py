"""
Box Towers

In the not so distant future, Box has commissioned you to design the new Box Worldwide Headquarters - The Box Towers. The design principal is a series of boxes (what else?),  one on top of each other. Each department in Box will be located in a different box.

Now each department has decided they have different needs in terms of the height, width and length (depth) of their box. For structural integrity reasons, you must also not place a box that has a larger footprint on top of a box with a smaller footprint i.e a box can be kept on the top of another box only if the Length of the upper box is not more than the Length of box below and the same for Width. You may rotate the boxes as necessary to make any of the face as base i.e 3D rotation is allowed.

Given the set of boxes, come up with the tallest building possible while satisfying the above constraints. It may not be possible to use all the boxes.

Input Format:

1st line contains the number of boxes , N.

Then follow N lines describing the configuration of each of the N boxes. Each of these lines contain three integers (length, width and height of the box)

Output Format:

Output a single line which is the height of the tallest possible building that can be formed with some of the boxes given and satisfying the constraints.
"""
from sys import stdin as sin
import operator

class BOX:
   height = 0
   boxes = list()
   stackkeys = set()
   l =0

   def __init__(self, i):
      self.l = i

   def stackBoxes(self, i, hgt=0,k =0):
      bx = self.boxes[i]
      top = self.boxes[k]
      if len(self.stackkeys) == 0 or (
         bx['l'] <= top['l'] and bx['w'] <= top['w']):
         hgt+=bx['h']
         self.stackkeys.add(bx['k'])
         if hgt > self.height:
             self.height = hgt
         if len(self.stackkeys)< self.l:
             for j in range(i+1,len(self.boxes)):
                 if self.boxes[j]['k'] not in self.stackkeys:
                     self.stackBoxes(j,hgt,i)
             
         self.stackkeys.remove(bx['k'])
         hgt-=bx['h']

   def addbox(self, b):
      if b['w'] > b['l']:
         t=b['w']
         b['w']=b['l']
         b['l'] = t
      b['a'] = b['w'] * b['l']
      self.boxes.append(b)

      if b['w'] == b['l'] and b['l']==b['h']: #one instance
         return
      elif b['w'] == b['l']:#two instances w=l
         bo = {'w':b['h'],'l':b['l'],'h':b['w'],'k':b['k']}
         if bo['w'] > bo['l']:
            bo['w'] = bo['l']
            bo['l'] = b['h']
         bo['a'] = bo['w'] * bo['l']
         self.boxes.append(bo)
      elif b['l']==b['h']:#two instances l=h
         bo = {'w':b['h'],'l':b['l'],'h':b['w'],'k':b['k']}
         bo['a'] = bo['w'] * bo['l']
         self.boxes.append(bo)
      elif b['w']==b['h']: #two instances w=h
         bo = {'w':b['w'],'l':b['h'],'h':b['l'],'k':b['k']}
         bo['a'] = bo['w'] * bo['l']
         self.boxes.append(bo)
      else:#three instances
         bo = {'w':b['l'],'l':b['h'],'h':b['w'],'k':b['k']}
         if bo['w'] > bo['l']:
            bo['w'] = bo['l']
            bo['l'] = b['l']
         bo['a'] = bo['w'] * bo['l']
         self.boxes.append(bo)

         bo = {'w':b['w'],'l':b['h'],'h':b['l'],'k':b['k']}
         if bo['w'] > bo['l']:
            bo['w'] = bo['l']
            bo['l'] = b['w']
         bo['a'] = bo['w'] * bo['l']  
         self.boxes.append(bo)

   def process(self):
      self.boxes = sorted(self.boxes, key=operator.itemgetter('a'),
                          reverse=True)
      for i in range(len(self.boxes)):
         self.stackBoxes(i)
      print(self.height)
        
def main():
   l=int(sin.readline())
   B = BOX(l)
   for i in range(l):
      line = sin.readline().rstrip().split(" ")
      B.addbox({'l':int(line[0]),'w':int(line[1]),'h':int(line[2]), 'k':i})
   B.process()
    
main()
