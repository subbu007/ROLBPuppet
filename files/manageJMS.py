import sys
import py_compile
from time import sleep

def createJMS(scopeId, jmsName, extICF, extPURL):
    new1 = AdminConfig.create('JMSProvider', scopeId, [['name',jmsName],['externalInitialContextFactory',extICF],['externalProviderURL',extPURL]])
    print "Saving the new JMSProvider : "+ new1
    AdminConfig.save()

def modifyJMS(jmsId, jmsName):
    tuple = myDict.items()
    length = len(tuple)
    count =0
    attrs = []
    while(count<length):
        attrs.append(list(tuple[count]))
        count +=1
    AdminConfig.modify(jmsId, attrs)
    print "Saving the configuration with modifications in JMSProvider : "+jmsName
    AdminConfig.save()

def manageJ(jmsName,  scope, cellName, nodeOrClusterName=None, serverName=None):

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp
   
#----------------------------------------------------------------
#            -- Modify existing JMS provider --
#----------------------------------------------------------------
   print "Manage JMSProvider object named " + jmsName
   jmsId = ""
   scopeId = ""
   extICF = "Put the external initial context factory here"
   extPURL = "Put the external provider URL here"
   

   allKeys = myDict.keys()
   for key in allKeys :
   	if key == "externalInitialContextFactory" :
        	extICF = myDict[key]
    	else :
        	extICF = extICF
        if key == "externalProviderURL" :
            extPURL = myDict[key]
        else :
            extPURL = extPURL

   if scope == 'cell':
      	jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/JMSProvider:" + jmsName)
      	if jmsId.find(jmsName) == -1:
		scopeId =  AdminConfig.getid("/Cell:"+ cellName)
 		createJMS(scopeId, jmsName, extICF, extPURL)
                #After succesfull creation of JMS Provide updating the remaining values
                jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/JMSProvider:" + jmsName) 
                modifyJMS(jmsId, jmsName)
	else :
            modifyJMS(jmsId, jmsName)
        
   elif scope == 'node':
	jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsName)
      	if jmsId.find(jmsName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName)
                createJMS(scopeId, jmsName, extICF, extPURL)
                #After succesfull creation of JMS Provide updating the remaining values
                jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JMSProvider:" + jmsName)
                modifyJMS(jmsId, jmsName)
	else :
                modifyJMS(jmsId, jmsName)

   elif scope == 'cluster':
      	jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JMSProvider:" + jmsName)
	if jmsId.find(jmsName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName)
                createJMS(scopeId, jmsName, extICF, extPURL)
                #After succesfull creation of JMS Provide updating the remaining values
                jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JMSProvider:" + jmsName)
                modifyJMS(jmsId, jmsName)
        else :
                modifyJMS(jmsId, jmsName)

   elif scope == 'server':
      	jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JMSProvider:" + jmsName)
	if jmsId.find(jmsName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName)
                createJMS(scopeId, jmsName, extICF, extPURL)
                #After succesfull creation of JMS Provide updating the remaining values
                jmsId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JMSProvider:" + jmsName)
                modifyJMS(jmsId, jmsName)
        else :
                modifyJMS(jmsId, jmsName)

   return 
#--------------------------------------------------------
#       -- Main 
#--------------------------------------------------------

if (len(sys.argv) < 3) :
   print "This script requires atleast 3  parameters : JdbcProvName, Scope, Cellname, and optionally, nodename, servername, clustername, param1, param1value, param2 param2value /n Scope values : cell node server cluster"
   print "e.g.: modifyJ MyJdbcProvider server cell01 node01 server01 description 'my new description' classpath '/bin/newclasspath'" 
else:   
	jmsName = sys.argv[0]
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

	manageJ(jmsName, scope, cellName, nodeOrClusterName, serverName)
