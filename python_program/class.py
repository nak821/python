
"""
class TestClass:

	#constructor start
	def __init__(self):
		print("In constructor")
		#rettun 5 #constructor can't return anything
		#constructor End
	def testFunction1(self):
		print("In test function")

	def testFunction2(self):
		print("in test Function2")

obj = TestClass()
obj.testFunction1()
obj.testFunction2()
"""

#pivate and public

class TestClass1(object):
	"""docstring for TestClass1"""

	def __init__(self, arg):
		self.arg = arg

	def __privateMethod(self):
		return "increased by 1 : "

	def publicMethod(self):
		self.arg += 1
		msg = self.__privateMethod()
		#print(msg)
		print(msg + str(self.arg))

obj1 = TestClass1(24)

obj1.publicMethod()
#access private method
print obj1._TestClass1__privateMethod()
