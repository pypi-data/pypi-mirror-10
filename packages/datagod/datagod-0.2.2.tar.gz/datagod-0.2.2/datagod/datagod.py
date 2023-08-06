__author__ = 'gaoce'

from typevar import *
from reporter import *
from graphtype import GraphType

class DataGodBuilder(object):
	"""Data God Factory"""
	def __init__(self):
		self.type = -1
		self.lowRange = 0
		self.highRange = 10
		self.step = 1
		self.swing = 0.1

	def draw(self):
		self.typeVar.draw()

	def getInstance(self, type, termsLst):
		self.typeVar = PolynomialType(termsLst)
		return self.typeVar

	def setLowRange(self, lowRange):
		self.lowRange = lowRange
		return self

	def setHighRange(self, highRange):
		self.highRange = highRange
		return self

	def setType(self, type):
		self.type = type
		return self

	def setStep(self, step):
		self.step = step
		return self

	def setTermList(self, termsLst):
		self.termsLst = termsLst
		return self

	def setSwing(self, swing):
		self.swing = swing
		return self

	# for log
	def setLogTerm(self, term):
		self.term = term
		return self

	def setBase(self, base):
		self.base = base
		return self

	def setIntercept(self, intercept):
		self.intercept = intercept
		return self

	def build(self):
		# to do
		if (self.type == GraphType.getDefaultType()):
			print Reporter.FAIL + "Error: " + Reporter.ENDC + "Type nondetermined"
			self.typeVar = TypeBase()
			return self.typeVar
		elif (self.type == GraphType.getPolynomialType()):
			self.typeVar = PolynomialType(self.termsLst, lowRange = self.lowRange, highRange = self.highRange, step = self.step, swing = self.swing)
			return self.typeVar
		elif (self.type == GraphType.getLogType()):
			self.typeVar = LogType(self.term, self.base, self.intercept, lowRange = self.lowRange, highRange = self.highRange, step = self.step, swing = self.swing)
			return self.typeVar