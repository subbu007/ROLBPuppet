# Recipe for craetion of JMS provider
$cmd = ""
$jmsProvName = ""
$extICF = ""
$extPURL = ""
$scope = ""
$cellName = ""
$nodeOrClusterName = ""
$serverName = ""
$desc = ""
$classPath = ""
$nativepath = ""



jms_config_data = data_bag('jms-config')
jms_config_data.each do |identifier|
        jms_data = data_bag_item('jms-config', identifier)
        $jmsProvName = jms_data['jmsName']
        $extICF = jms_data['extICF']
        $extPURL = jms_data['extPURL']
        $scope = jms_data['scope']
        $cellName = jms_data['cellName']
        $nodeOrClusterName = jms_data['nodeOrClusterName']
        $serverName = jms_data['serverName']
        $desc = jms_data['desc']
        $classPath = jms_data['classPath']
        $nativepath = jms_data['nativepath']
 end

        if "#$scope" == "cell"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJMS.py \'#$jmsProvName\' #$scope \'#$cellName\' externalInitialContextFactory \'#$extICF\' externalProviderURL \'#$extPURL\' description \'#$desc\' classpath \'#$classPath\' nativepath \'#$nativepath\'"
        elsif "#$scope" == "node" or "#$scope" == "cluster"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJMS.py \'#$jmsProvName\' #$scope  \'#$cellName\' \'#$nodeOrClusterName\' externalInitialContextFactory \'#$extICF\' externalProviderURL \'#$extPURL\' description \'#$desc\' classpath \'#$classPath\' nativepath \'#$nativepath\'"
        elsif "#$scope" == "server"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageJMS.py \'#$jmsProvName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' \'#$serverName\' externalInitialContextFactory \'#$extICF\' externalProviderURL \'#$extPURL\' description \'#$desc\' classpath \'#$classPath\' nativepath \'#$nativepath\'"
        end

execute "#$jmsProvName" do
        command "#$cmd"
        action :run
end


#git "/var/www/code_repo/temp3" do
#  repository "https://github.com/subbu007/ROLBPuppet.git"
#  revision node['last_version']
#  action :sync
#  notifies :create,"file[/var/www/code_repo/temp3/temp3.yaml]"
#end

#file "/var/www/code_repo/temp3/temp3.yaml" do
#   content IO.read('/var/www/code_repo/temp3/jmsCentos.yaml')
#   mode "0644"   
#   notifies :run,"execute[#$jmsProvName]", :immediately
#end   
