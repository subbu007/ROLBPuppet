import sys
import py_compile
from time import sleep

def createQueue(scopeId, queueName, jndiName):
    new1 = AdminConfig.create('WASQueue', scopeId, [['name',queueName],['jndiName',jndiName]])
    print "Saving the new WASQueue : "+ new1
    AdminConfig.save()

def modifyQueue(queueId, queueName):
    del myDict["jmsProviderName"]
    tuple = myDict.items()
    length = len(tuple)
    count = 0
    attrs = []
    while(count<length):
        attrs.append(list(tuple[count]))
        count +=1
    AdminConfig.modify(queueId, attrs)
    print "Saving the configuration with modifications in WASQueue : " + queueName
    AdminConfig.save()

def manageQueue(queueName, scope, cellName, nodeOrClusterName=None, serverName=None):

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp
   
#----------------------------------------------------------------
#            -- Modify existing Queue provider --
#----------------------------------------------------------------
   print "Manage WASQueue object named " + queueName
   queueId = ""
   scopeId = ""
   jndiName = "Argument_passed_incorrectly"
   

   allKeys = myDict.keys()
   for key in allKeys :
   	if key == "jndiName" :
        	jndiName = myDict[key]
    	else :
        	jndiName = jndiName
        if key == "jmsProviderName" :
          jmsProviderName = myDict[key]

   if scope == 'cell':
      	queueId =  AdminConfig.getid("/Cell:"+ cellName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
      	if queueId.find(queueName) == -1:
		scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/JMSProvider:" + jmsProviderName)
 		createQueue(scopeId, queueName, jndiName)
                #After succesfull creation of Queue Provide updating the remaining values
                queueId =  AdminConfig.getid("/Cell:"+ cellName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName) 
                modifyQueue(queueId, queueName)
	else :
            modifyQueue(queueId, queueName)
        
   elif scope == 'node':
	queueId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
      	if queueId.find(queueName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsProviderName)
                createQueue(scopeId, queueName, extICF, extPURL)
                #After succesfull creation of Queue Provide updating the remaining values
                queueId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
                modifyQueue(queueId, queueName)
	else :
                modifyQueue(queueId, queueName)

   elif scope == 'cluster':
      	queueId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
	if queueId.find(queueName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsProviderName)
                createQueue(scopeId, queueName, extICF, extPURL)
                #After succesfull creation of Queue Provide updating the remaining values
                queueId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
                modifyQueue(queueId, queueName)
        else :
                modifyQueue(queueId, queueName)

   elif scope == 'server':
      	queueId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
	if queueId.find(queueName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JMSProvider:" + jmsProviderName)
                createQueue(scopeId, queueName, extICF, extPURL)
                #After succesfull creation of Queue Provide updating the remaining values
                queueId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JMSProvider:" + jmsProviderName + "/WASQueue:" + queueName)
                modifyQueue(queueId, queueName)
        else :
                modifyQueue(queueId, queueName)

   return 
#--------------------------------------------------------
#       -- Main 
#--------------------------------------------------------

if (len(sys.argv) < 3) :
   print "This script requires atleast 3  parameters : JdbcProvName, Scope, Cellname, and optionally, nodename, servername, clustername, param1, param1value, param2 param2value /n Scope values : cell node server cluster"
   print "e.g.: modifyJ MyJdbcProvider server cell01 node01 server01 description 'my new description' classpath '/bin/newclasspath'" 
else:   
	queueName = sys.argv[0]
     	scope = sys.argv[1]
     	length = len(sys.argv)

	if scope == 'cell':
     		cellName = sys.argv[2]
     		nodeOrClusterName = ""
     		serverName = ""
        	count = 3
        	myDict = {};
        	while (count < length):
        		myDict [sys.argv[count]] = sys.argv[count+1]
                	count += 2 	
     	elif scope == 'node':
     		cellName = sys.argv[2]
     		nodeOrClusterName = sys.argv[3]
     		serverName = ""
        	count = 4
        	myDict = {};
        	while (count < length):
                	myDict [sys.argv[count]] = sys.argv[count+1]
                	count += 2
     	elif scope == 'cluster':
     		cellName = sys.argv[2]
     		nodeOrClusterName = sys.argv[3]
     		serverName = ""
        	count = 4
        	myDict = {};
        	while (count < length):
               		myDict [sys.argv[count]] = sys.argv[count+1]
                	count += 2
     	elif scope == 'server':
     		cellName = sys.argv[2]
     		nodeOrClusterName = sys.argv[3]
     		serverName = sys.argv[4]
     		count = 5
        	myDict = {};
        	while (count < length):
                	myDict [sys.argv[count]] = sys.argv[count+1]
                	count += 2

	manageQueue(queueName, scope, cellName, nodeOrClusterName, serverName)
