from pyperfmon import pyperfmon
from robot.api.deco import keyword, library


@library
class PerfmonLibrary:

	pm = None

	def __init__(self):
		self.pm = pyperfmon.pyperfmon()


	@keyword('Connect To')
	def connect_to(self, machine=".", username=None, password=None):
		try:
			ctn = self.pm.connect(machine, username, password)
			return ctn
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(machine)
			if username is not None:
				emsg += " with user {} and password {}".format(username, password)
			raise AssertionError(emsg)

	@keyword('Get Counter')
	def get_counter(self, counterpath=None, machinealias="localhost"):
		try:
			ctr = self.pm.getCounter(counterpath, machinealias)
			if ctr[1] == 'ERR: Not Found.':
				raise AssertionError("Counter {} was not found on host {}".format(counterpath, machinealias))
			return ctr
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(machinealias)
			raise AssertionError(emsg)

	@keyword('Get Objects')
	def get_objects(self, machinealias="localhost"):
		try:
			objs = self.pm.getCounterObjects(machinealias)
			if len(objs) <1:
				raise AssertionError("No Objects found on host {}".format(machinealias))
			return objs
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(machinealias)
			raise AssertionError(emsg)

	@keyword('Get Counters')
	def get_counters(self, objectname=None, machinealias="localhost"):
		try:
			ctrs = self.pm.getCounters(objectname, machinealias)
			if len(ctrs) <1:
				raise AssertionError("No Counters found for Object {} on host {}".format(objectname, machinealias))
			return ctrs
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(machinealias)
			raise AssertionError(emsg)
