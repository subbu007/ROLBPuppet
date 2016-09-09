import sys
import py_compile
from time import sleep

def createJdbcDataSource(scopeId, JdbcDataSourceName):
    new1 = AdminConfig.create('DataSource', scopeId, [['name',JdbcDataSourceName]])
    print "Saving the new WASJdbcDataSource : "+ new1
    AdminConfig.save()

def modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName):
    del myDict["JDBCProviderName"]
    tuple = myDict.items()
    length = len(tuple)
    count = 0
    attrs = []
    while(count<length):
        attrs.append(list(tuple[count]))
        count +=1
    AdminConfig.modify(JdbcDataSourceId, attrs)
    print "Saving the configuration with modifications in WASJdbcDataSource : " + JdbcDataSourceName
    AdminConfig.save()

def manageJdbcDataSource(JdbcDataSourceName, scope, cellName, nodeOrClusterName=None, serverName=None):

#--------------------------------------------------------------
# set up globals
#--------------------------------------------------------------
   global AdminConfig
   global AdminControl
   global AdminApp
   
#----------------------------------------------------------------
#            -- Modify existing JdbcDataSource provider --
#----------------------------------------------------------------
   print "Manage WASJdbcDataSource object named " + JdbcDataSourceName
   JdbcDataSourceId = ""
   scopeId = ""
   
   allKeys = myDict.keys()
   for key in allKeys :
   	  if key == "JDBCProviderName" :
           JDBCProviderName = myDict[key]

   if scope == 'cell':
      	JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName)
      	if JdbcDataSourceId.find(JdbcDataSourceName) == -1:
		scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/JDBCProvider:" + JDBCProviderName)
 		createJdbcDataSource(scopeId, JdbcDataSourceName)
                #After succesfull creation of JdbcDataSource Provide updating the remaining values
                JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName) 
                modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)
	else :
            modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)
        
   elif scope == 'node':
	JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName +"/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName)
        if JdbcDataSourceId.find(JdbcDataSourceName) == -1:
    		scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/JDBCProvider:" + JDBCProviderName)
    		createJdbcDataSource(scopeId, JdbcDataSourceName)
                #After succesfull creation of JdbcDataSource Provide updating the remaining values
                JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:" + nodeOrClusterName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName) 
                modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)
  	else :
            modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)

   elif scope == 'cluster':
	JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:"+ nodeOrClusterName +"/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName)
        if JdbcDataSourceId.find(JdbcDataSourceName) == -1:
    		scopeId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:"+ nodeOrClusterName + "/JDBCProvider:" + JDBCProviderName)
    		createJdbcDataSource(scopeId, JdbcDataSourceName)
                #After succesfull creation of JdbcDataSource Provide updating the remaining values
                JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/ServerCluster:" + nodeOrClusterName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName) 
                modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)
  	else :
            modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)

   elif scope == 'server':
      	JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName)
        if JdbcDataSourceId.find(JdbcDataSourceName) == -1:
    		scopeId =  AdminConfig.getid("/Cell:"+ cellName +"/Node:"+ nodeOrClusterName + "/Server:" + serverName + "/JDBCProvider:" + JDBCProviderName)
    		createJdbcDataSource(scopeId, JdbcDataSourceName)
                #After succesfull creation of JdbcDataSource Provide updating the remaining values
      		JdbcDataSourceId =  AdminConfig.getid("/Cell:"+ cellName + "/Node:" + nodeOrClusterName + "/Server:" + serverName + "/JDBCProvider:" + JDBCProviderName + "/DataSource:" + JdbcDataSourceName) 
                modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)
  	else :
            modifyJdbcDataSource(JdbcDataSourceId, JdbcDataSourceName)

   return 
#--------------------------------------------------------
#       -- Main 
#--------------------------------------------------------

if (len(sys.argv) < 3) :
   print "This script requires atleast 3  parameters : JdbcProvName, Scope, Cellname, and optionally, nodename, servername, clustername, param1, param1value, param2 param2value /n Scope values : cell node server cluster"
   print "e.g.: modifyJ MyJDBCDataSource server cell01 node01 server01 description 'my new description' classpath '/bin/newclasspath'" 
else:   
	JdbcDataSourceName = sys.argv[0]
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

	manageJdbcDataSource(JdbcDataSourceName, scope, cellName, nodeOrClusterName, serverName)
