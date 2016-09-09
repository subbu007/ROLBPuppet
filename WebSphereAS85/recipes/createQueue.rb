# Recipe for craetion of JMS provider
$cmd = ""
$queueProvName = ""
$extICF = ""
$extPURL = ""
$scope = ""
$cellName = ""
$nodeOrClusterName = ""
$serverName = ""
$desc = ""
$classPath = ""
$nativepath = ""



queue_config_data = data_bag('queue-config')
queue_config_data.each do |identifier|
        queue_data = data_bag_item('queue-config', identifier)
        $jmsProviderName = queue_data['jmsProviderName']
        $queueProvName = queue_data['queueName']
        $jndiName = queue_data['jndiName']
        $scope = queue_data['scope']
        $cellName = queue_data['cellName']
        $nodeOrClusterName = queue_data['nodeOrClusterName']
        $serverName = queue_data['serverName']
        $desc = queue_data['desc']
        $classPath = queue_data['classPath']
        $nativepath = queue_data['nativepath']
 end

        if "#$scope" == "cell"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageQueue.py \'#$queueProvName\' #$scope \'#$cellName\' jmsProviderName \'#$jmsProviderName\' jndiName \'#$jndiName\' description \'#$desc\'"
        elsif "#$scope" == "node" or "#$scope" == "cluster"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageQueue.py \'#$queueProvName\' #$scope  \'#$cellName\' \'#$nodeOrClusterName\' jmsProviderName \'#$jmsProviderName\' jndiName \'#$jndiName\' description \'#$desc\'"
        elsif "#$scope" == "server"
        $cmd = "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /home/vagrant/config-data/WAS/manageQueue.py \'#$queueProvName\' #$scope \'#$cellName\' \'#$nodeOrClusterName\' \'#$serverName\' jmsProviderName \'#$jmsProviderName\' jndiName \'#$jndiName\' description \'#$desc\'"
        end

execute "#$queueProvName" do
        command "#$cmd"
        action :run
end


#git "/var/www/code_repo/temp4" do
#  repository "https://github.com/subbu007/ROLBPuppet.git"
#  revision node['last_version']
#  action :sync
#  notifies :create,"file[/var/www/code_repo/temp4/temp4.yaml]"
#end

#file "/var/www/code_repo/temp4/temp4.yaml" do
#   content IO.read('/var/www/code_repo/temp4/queueCentos.yaml')
#   mode "0644"   
#   notifies :run,"execute[#$queueProvName]", :immediately
#end 