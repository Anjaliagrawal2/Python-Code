class car:
     def __init__(self,name='',model=''):
          print("Object Created")
          self.name=name
          self.model=model
     def start(self,name):
          print("Car Started:",name)
     def __del__(self):
          print(self.__class__.__name__,"destroyed")
          

c1=car('swift','lxi')
print(isinstance(c1,car),c1.name,c1.model)
c1.start(c1.name)
c2=car('Alto')
c2.start(c2.name)
del c1
del c2
