*** Settings ***
Library		PerfmonLibrary

*** Variables ***
# ${AUTServer} 	MyAUTServer
${AUTServer} 	localhost

*** Test Cases ***
Check Memory
	${mempct}= 	Get Counter 	Memory\\% Committed Bytes In Use 	${AUTServer}
	Should Be True 	${mempct[1]} < 80

Check CPU
	${cputotpct}= 	Get Counter 	Processor\\_Total\\% Processor Time 	${AUTServer}
	Should Be True 	${cputotpct[1]} < 80

Objects
    ${objs}=    Get Objects	    ${AUTServer}

Counters

    ${cntrs}=   Get Counters        Processor    ${AUTServer}

    
