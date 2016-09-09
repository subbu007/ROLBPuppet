import sys
import py_compile
from time import sleep

def createJDBC(scopeId, jdbcName, implClassName):
    new1 = AdminConfig.create('JDBCProvider', scopeId, [['name',jdbcName],['implementationClassName',implClassName]])
    print "Saving the new JDBCProvider : "+jdbcName
    AdminConfig.save()

def modifyJDBC(jdbcId, jdbcName):
    tuple = myDict.items()
    length = len(tuple)
    count =0
    attrs = []
    while(count<length):
        attrs.append(list(tuple[count]))
        count +=1
    AdminConfig.modify(jdbcId, attrs)
    print "Saving the configuration with modifications in JDBCProvider : "+jdbcName
    AdminConfig.save()

def manageJ(jdbcName,  scope, cellName, nodeOrClusterName=None, serverName=None):

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp
   
#----------------------------------------------------------------
#            -- Modify existing JBDC provider --
#----------------------------------------------------------------
   print "Manage JDBCProvider object named " + jdbcName
   jdbcId = ""
   scopeId = ""
   implClassName = "com.ibm.db2.jcc.DB2ConnectionPoolDataSource"
   allKeys = myDict.keys()
   for key in allKeys :
   	if key == "implementationClassName" :
        	implClassName = myDict[key]
    	else :
        	implClassName = implClassName

   if scope == 'cell':
      	jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/JDBCProvider:" + jdbcName)
      	if jdbcId.find(jdbcName) == -1:
		scopeId =  AdminConfig.getid("/Cell:"+ cellName)
 		createJDBC(scopeId, jdbcName, implClassName)
                #After succesfull creation of JDBC Provide updating the remaining values
                jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/JDBCProvider:" + jdbcName) 
                modifyJDBC(jdbcId, jdbcName)
	else :
            modifyJDBC(jdbcId, jdbcName)
        
   elif scope == 'node':
	jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JDBCProvider:" + jdbcName)
      	if jdbcId.find(jdbcName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName)
                createJDBC(scopeId, jdbcName, implClassName)
                #After succesfull creation of JDBC Provide updating the remaining values
                jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JDBCProvider:" + jdbcName)
                modifyJDBC(jdbcId, jdbcName)
	else :
                modifyJDBC(jdbcId, jdbcName)

   elif scope == 'cluster':
      	jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JDBCProvider:" + jdbcName)
	if jdbcId.find(jdbcName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName)
                createJDBC(scopeId, jdbcName, implClassName)
                #After succesfull creation of JDBC Provide updating the remaining values
                jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JDBCProvider:" + jdbcName)
                modifyJDBC(jdbcId, jdbcName)
        else :
                modifyJDBC(jdbcId, jdbcName)

   elif scope == 'server':
      	jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JDBCProvider:" + jdbcName)
	if jdbcId.find(jdbcName) == -1:
                scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName)
                createJDBC(scopeId, jdbcName, implClassName)
                #After succesfull creation of JDBC Provide updating the remaining values
                jdbcId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JDBCProvider:" + jdbcName)
                modifyJDBC(jdbcId, jdbcName)
        else :
                modifyJDBC(jdbcId, jdbcName)

   return 
#--------------------------------------------------------
#       -- Main 
#--------------------------------------------------------

if (len(sys.argv) < 3) :
   print "This script requires atleast 3  parameters : JdbcProvName, Scope, Cellname, and optionally, nodename, servername, clustername, param1, param1value, param2 param2value /n Scope values : cell node server cluster"
   print "e.g.: modifyJ MyJdbcProvider server cell01 node01 server01 description 'my new description' classpath '/bin/newclasspath'" 
else:   
	jdbcName = sys.argv[0]
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

	manageJ(jdbcName, scope, cellName, nodeOrClusterName, serverName)
