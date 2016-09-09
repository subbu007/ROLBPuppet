# Recipe for craetion of JDBC provider
$cmd = ""
$jdbcProvName = ""
$scope = ""
$cellName = ""
$nodeOrClusterName = ""
$serverName = ""
$desc = ""
$implmenType = ""
$classPath = ""
$nativepath = ""
$dbtype = ""
$jdbcProviderType = ""
$statementCacheSize = 10


was_config_data = data_bag('was-config')
was_config_data.each do |identifier|
        jdbc_data = data_bag_item('was-config', identifier)
        $jdbcProvName = jdbc_data['jdbcName']
        $scope = jdbc_data['scope']
        $cellName = jdbc_data['cellName']
        $nodeOrClusterName = jdbc_data['nodeOrClusterName']
        $serverName = jdbc_data['serverName']
        $desc = jdbc_data['desc']
        $implmenType = jdbc_data['implmenType']
        $classPath = jdbc_data['classPath']
        $nativepath = jdbc_data['nativepath']
        $dbtype = jdbc_data['dbtype']
        $jdbcProviderType = jdbc_data['jdbcProviderType']
 end

        if "#$scope" == "cell"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJ.py \'#$jdbcProvName\' #$scope \'#$cellName\' description \'#$desc\' implementationClassName #$implmenType classpath \'#$classPath\' nativepath \'#$nativepath\'"
        elsif "#$scope" == "node" or "#$scope" == "cluster"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJ.py \'#$jdbcProvName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' databaseType \'#$dbtype\' providerType \'#$jdbcProviderType\' description \'#$desc\' implementationClassName #$implmenType classpath \'#$classPath\' nativepath \'#$nativepath\'"
        elsif "#$scope" == "server"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJ.py \'#$jdbcProvName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' \'#$serverName\' databaseType \'#$dbtype\' providerType \'#$jdbcProviderType\' description \'#$desc\' implementationClassName #$implmenType classpath \'#$classPath\' nativepath \'#$nativepath\'"
        end

execute "#$jdbcProvName" do
        command "#$cmd"
        action :run
end


#git "/var/www/code_repo/temp" do
#  repository "https://github.com/subbu007/ROLBPuppet.git"
#  revision node['last_version']
#  action :sync
#  notifies :create,"file[/var/www/code_repo/temp/temp.yaml]"
#end

#file "/var/www/code_repo/temp/temp.yaml" do
#   content IO.read('/var/www/code_repo/temp/JdbcCentos.yaml')
#   mode "0644"   
#   notifies :run,"execute[#$jdbcProvName]", :immediately
#end     
