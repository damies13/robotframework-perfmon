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
	def get_counter(self, counterpath=None, hostname="localhost"):
		try:
			ctr = self.pm.getCounter(counterpath, hostname)
			if ctr[1] == 'ERR: Not Found.':
				raise AssertionError("Counter {} was not found on host {}".format(counterpath, hostname))
			return ctr
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(hostname)
			raise AssertionError(emsg)

	@keyword('Get Objects')
	def get_objects(self, hostname="localhost"):
		try:
			objs = self.pm.getCounterObjects(hostname)
			if len(objs) <1:
				raise AssertionError("No Objects found on host {}".format(hostname))
			return objs
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(hostname)
			raise AssertionError(emsg)

	@keyword('Get Counters')
	def get_counters(self, objectname=None, hostname="localhost"):
		try:
			ctrs = self.pm.getCounters(objectname, hostname)
			if len(ctrs) <1:
				raise AssertionError("No Counters found for Object {} on host {}".format(objectname, hostname))
			return ctrs
		except AssertionError as e:
			raise AssertionError(e)
		except Exception as e:
			print(e)
			emsg = "Unable to connect to host {}".format(hostname)
			raise AssertionError(emsg)
