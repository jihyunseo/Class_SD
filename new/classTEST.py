#1
class First:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=x*2
     
frst=First(4)
print('First class result',frst.x,',',frst.y);
frst=First(7)
print('First class result',frst.x,',',frst.y);

#2
class Second:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=2+x/2
     
Snd=Second(2)
print('Second class result',Snd.x,',',Snd.y);
Snd=Second(7)
print('Second class result',Snd.x,',',Snd.y);

#3
class Third:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=2*x+2
        
Trd=Third(3)
print('Third class result',Trd.x,',',Trd.y);
Trd=Third(7)
print('Third class result',Trd.x,',',Trd.y);

#3-1
class Third2:
    def __init__(self, x=0,y=0,z=0):
        self.x=x
        self.y=x+2
        self.z=x+y
        
        
Trd2=Third2(3,5)
print('Third2 class result',Trd2.x,',',Trd2.y,',',Trd2.z);
Trd2=Third2(7,9)
print('Third2 class result',Trd2.x,',',Trd2.y,',',Trd2.z);

#4
class Fourth:
    def __init__(self, x=0,y=0,z=0):
        self.x=x
        self.y=x+2
        self.z=x+y
        
Fth=Fourth(3,5)
print('Fourth class result',Fth.x,',',Fth.y,',',Fth.z);
Fth=Fourth(7,9)
print('Fourth class result',Fth.x,',',Fth.y,',',Fth.z);

