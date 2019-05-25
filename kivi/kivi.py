from time import time
import inspect

class Kivi(object):

	def __init__(self, description):
		self.description = description

	def __enter__(self):
		self.frame = inspect.currentframe().f_back
		self.old_locals = self.frame.f_locals.copy()
		self.start = time()

	def __exit__(self, type, value, traceback):
		self.frame = inspect.currentframe().f_back
		self.new_locals = self.frame.f_locals.copy()
		self.created_locals = set(self.new_locals) - set(self.old_locals)
		self.end = time()

		print(f"{self.description}")
		print(f"Time:{self.end - self.start}")
		for local in self.created_locals:
			print(f"Size of {local} is {self.new_locals[local].__sizeof__()}")
