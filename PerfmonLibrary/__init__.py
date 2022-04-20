from pyperfmon import pyperfmon
from robot.api.deco import keyword, library


@library
class PerfmonLibrary:
	"""robotframework-perfmon
	
	A Robot Framework wrapper for pyperfmon, provides a simple way to collect windows performance monitor (perfmon) counter statistics from a windows machine, usually the AUT servers.
	"""
	
	pm = None

	def __init__(self):
		self.pm = pyperfmon.pyperfmon()


	@keyword('Connect To')
	def connect_to(self, machine=".", username=None, password=None):
		"""Establishes a connection to a remote windows machine.
		
		The most likely reasons for using this keyword are:
		- You need to use different credentials to connect to the remote windows machine
		- You want to avoid the connection time overhead on reading the first performance counter
		
		All arguments are optional with the default values used if omitted
		- hostname the windows machine to connect to. Default: localhost
		- username the windows user to connect with, when specifying a domain you will need to escape the \ as \\. Default: current logged in user.
		- password the password for the specified windows user. If username no specified password is not used. Default: None
		
		example usage:
		Connect To hostname domnain\\username password
		Connect To hostname
		
		It is suggested to use this keyword in Suite setup
		"""
		
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
		"""Get the performance monitor counter's value, the value is returned as a tuple of ('counterpath', value)
		
		counterpath argument is required, hostname argument is optional with the default value used if omitted
		
		- counterpath the path to the windows performance counter, can be in either format
		      <object>\\<counter> or
		      <object>\\<instance>\\<counter>
		- hostname the windows machine to connect to. Default: localhost
		"""

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
		"""Get a list of available performance monitor counter objects
		
		All arguments are optional with the default values used if omitted
		- hostname the windows machine to connect to. Default: localhost
		"""

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
		"""Get a list of available performance monitor counters for specified object
		
		object argument is required, hostname argument is optional with the default value used if omitted
		- object the object to get a list of windows performance counters for.
		- hostname the windows machine to connect to. Default: localhost
		"""

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
