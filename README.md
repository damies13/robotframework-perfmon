# robotframework-perfmon

Robot Framework wrapper for pyperfmon, provides a simple way to collect windows performance monitor (perfmon) counter statistics from a windows machine, usually the AUT servers.

Simple example usage:
```robotframework
*** Settings ***
Library		PerfmonLibrary

*** Variables ***
${AUTServer} 	MyAUTServer

*** Test Cases ***
Check Memory
	${mempct}= 	Get Counter 	Memory\\% Committed Bytes In Use 	${AUTServer}
	Should Be True 	${mempct} < 80

Check CPU
	${cputotpct}= 	Get Counter 	Processor\\_Total\\% Processor Time 	${AUTServer}
	Should Be True 	${cputotpct} < 80

```

|Keyword|Description|
|---|---|
| Connect To ||
| Get Counter ||
| Get Objects ||
| Get Counters ||
