# Python Program to depict multiple inheritance 
# when method is overridden in both classes 

class A: 
	def m(self): 
		print("In class A") 
		
class B(A): 
	def m(self): 
		print("In class B") 

class C(A): 
	def m(self): 
		print("In class C") 
		
class D(B, C): 
	pass
	
obj = D() 
obj.m() 
