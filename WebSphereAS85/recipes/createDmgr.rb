
Chef::Log.info("This VM has IP address #{node["ipaddress"]} and hostname: #{node["hostname"]};  WAS binary bath is #{node['WebSphereAS85']['was85-installpath']}/bin")
Chef::Log.info("Dmgr Path is #{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']} ")


execute 'bash' do
  environment 'LANG' => "en_US.UTF-8", 'LANGUAGE' => "en_US.UTF-8", 'LC_ALL' => "en_US.UTF-8"
  command "unlink sh; ln -s /bin/bash sh; env > /tmp/chefenv2"
  cwd "/bin"
  action :run
end

execute 'createDmgr' do
  path = "#{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']}"
  path = path.strip
  not_if do FileTest.directory?(path) end
  environment 'LANG' => "en_US.UTF-8", 'LANGUAGE' => "en_US.UTF-8", 'LC_ALL' => "en_US.UTF-8"
  command "#{node['WebSphereAS85']['was85-binpath']}/manageprofiles.sh -create -profileName #{node['WebSphereAS85']['was85-dmgrname']} -profilePath #{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']} -templatePath #{node['WebSphereAS85']['was85-installpath']}/profileTemplates/management -nodeName #{node['WebSphereAS85']['was85-dmgrname']}Node -cellName #{node["hostname"]}Cell -hostname #{node["hostname"]} -adminUserName wasuser -adminPassword wasuser -enableAdminSecurity true"
  cwd "#{node['WebSphereAS85']['was85-binpath']}"
  action :run
end

template "#{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']}/properties/soap.client.props" do
  source 'soap-client-props.erb'
  owner 'root'
  group 'root'
  mode '0644'
end

execute 'hosts' do
  command "echo '127.0.0.1       #{node["hostname"]}  localhost' >> /etc/hosts  "
  cwd "/etc"
  action :run
end

execute 'startDmgr' do
  path = "#{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']}/logs/dmgr/dmgr.pid"
  path = path.strip
  not_if do FileTest.file?(path) end
  environment 'LANG' => "en_US.UTF-8", 'LANGUAGE' => "en_US.UTF-8", 'LC_ALL' => "en_US.UTF-8"
  command "#{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']}/bin/startManager.sh"
  cwd "#{node['WebSphereAS85']['was85-installpath']}/profiles/#{node['WebSphereAS85']['was85-dmgrname']}/bin"
  action :run
end