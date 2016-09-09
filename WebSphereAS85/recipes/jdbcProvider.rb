 execute 'jdbc-provider' do
  command "/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -f /Softwares/manageJ.py #{node['WebSphereAS85']['jdbcName']} #{node['WebSphereAS85']['scope']} #{node['WebSphereAS85']['cellName']} #{node['WebSphereAS85']['nodeOrClusterName']} #{node['WebSphereAS85']['serverName']}"
#  cwd "#{node['WebSphereAS85']['wasuserhome']}"
  action :run
 end
