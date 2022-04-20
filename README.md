# robotframework-perfmon

.. image:: https://img.shields.io/pypi/v/robotframework-perfmon.svg
    :target: https://pypi.python.org/pypi/robotframework-perfmon/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/robotframework-perfmon.svg
    :target: https://pypi.python.org/pypi/robotframework-perfmon/
    :alt: Number of PyPI downloads


Robot Framework wrapper for pyperfmon, provides a simple way to collect windows performance monitor (perfmon) counter statistics from a windows machine, usually the AUT servers.

- [Installation](#installation)
- [Example Usage](#example-usage)
- [Keyword Documentation](#keyword-documentation)

## Installation

```
pip install robotframework-perfmon
```

## Example Usage
Simple example usage:
```robotframework
*** Settings ***
Library		PerfmonLibrary

*** Variables ***
${AUTServer} 	MyAUTServer

*** Test Cases ***
Check Memory
	${mempct}= 	Get Counter 	Memory\\% Committed Bytes In Use 	${AUTServer}
	Should Be True 	${mempct[1]} < 80

Check CPU
	${cputotpct}= 	Get Counter 	Processor\\_Total\\% Processor Time 	${AUTServer}
	Should Be True 	${cputotpct[1]} < 80

```

## Keyword Documentation
|Keyword|Description|
|---|---|
| Connect To | Establishes a connection to a remote windows machine. <br> The most likely reasons for  using this keyword are: <br> - You need to use different credentials to connect to the remote windows machine <br> - You want to avoid the connection time overhead on reading the first performance counter <br> All arguments are optional with the default values used if omitted <br> - `hostname` the windows machine to connect to. Default: localhost <br> - `username` the windows user to connect with, when specifying a domain you will need to escape the \\ as \\\\. Default: current logged in user. <br> - `password` the password for the specified windows user. If username no specified password is not used. Default: None <br> example usage: <br> ``` Connect To	hostname 	domnain\\username 	password ``` <br> ``` Connect To 	hostname ``` <br> It is suggested to use this keyword in [Suite setup](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#toc-entry-260) |
| Get Counter | Get the performance monitor counter's value, the value is returned as a tuple of `('counterpath', value)` <br> `counterpath` argument is required, `hostname` argument is optional with the default value used if omitted <br> - `counterpath` the path to the windows performance counter, can be in either format <br> &nbsp; &nbsp; &nbsp; `<object>\\<counter>` or <br> &nbsp; &nbsp; &nbsp; `<object>\\<instance>\\<counter>` <br> - `hostname` the windows machine to connect to. Default: localhost |
| Get Objects | Get a list of available performance monitor counter objects <br> All arguments are optional with the default values used if omitted <br> - `hostname` the windows machine to connect to. Default: localhost |
| Get Counters | Get a list of available performance monitor counters for specified object <br> `object` argument is required, `hostname` argument is optional with the default value used if omitted <br> - `object` the object to get a list of windows performance counters for. <br> - `hostname` the windows machine to connect to. Default: localhost |
