# Recipe for craetion of JDBC provider
$cmd = ""
$scope = ""
$cellName = ""
$nodeOrClusterName = ""
$serverName = ""
$JDBCProviderName = ""
$JdbcDataSourceName = ""
$category = ""
$datasourceHelperClassname = ""
$jndiName = ""
$desc = ""


ds_config_data = data_bag('ds-config')
ds_config_data.each do |identifier|
        ds_data = data_bag_item('ds-config', identifier)
        $scope = ds_data['scope']
        $cellName = ds_data['cellName']
        $nodeOrClusterName = ds_data['nodeOrClusterName']
        $serverName = ds_data['serverName']
        $JDBCProviderName = ds_data['JDBCProviderName']
        $JdbcDataSourceName = ds_data['JdbcDataSourceName']
        $category = ds_data['category']
        $datasourceHelperClassname = ds_data['datasourceHelperClassname']
        $jndiName = ds_data['jndiName']
        $desc = ds_data['desc']   
 end

        if "#$scope" == "cell"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJdbcDataSource.py \'#$JdbcDataSourceName\' #$scope \'#$cellName\' JDBCProviderName \'#$JDBCProviderName\' description \'#$desc\' category \'#$category\' datasourceHelperClassname \'#$datasourceHelperClassname\' jndiName \'#$jndiName\'"
        elsif "#$scope" == "node" or "#$scope" == "cluster"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJdbcDataSource.py \'#$JdbcDataSourceName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' JDBCProviderName \'#$JDBCProviderName\' description \'#$desc\' category \'#$category\' datasourceHelperClassname \'#$datasourceHelperClassname\' jndiName \'#$jndiName\'"
        elsif "#$scope" == "server"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJdbcDataSource.py \'#$JdbcDataSourceName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' \'#$serverName\' JDBCProviderName \'#$JDBCProviderName\' description \'#$desc\' category \'#$category\' datasourceHelperClassname \'#$datasourceHelperClassname\' jndiName \'#$jndiName\'"
        end

execute "#$JdbcDataSourceName" do
        command "#$cmd"
        action :run
end


#git "/var/www/code_repo/temp2" do
#  repository "https://github.com/subbu007/ROLBPuppet.git"
#  revision node['last_version']
#  action :sync
#  notifies :create,"file[/var/www/code_repo/temp2/temp2.yaml]", :immediately
#end

#file "/var/www/code_repo/temp2/temp2.yaml" do
#   content IO.read('/var/www/code_repo/temp2/dsCentos.yaml')
#   mode "0644"   
#   notifies :run,"execute[#$JdbcDataSourceName]", :immediately
#end  
