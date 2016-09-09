require 'chef/knife'

class Chef
  class Knife
    class DataBagFromYaml < Knife
      deps do
        require 'chef/knife/data_bag_from_file'
        Chef::Knife::DataBagFromFile.load_deps
        require 'yaml'
        require 'tempfile'
      end

      banner "knife data bag from yaml BAG FILE (options)"
      category "data bag"

      def run
        databag_from_file = Chef::Knife::DataBagFromFile.new
        data_bag, item_path = name_args[0], name_args[1]
        data = YAML::load_file(
          databag_from_file.loader.find_file("data_bags", data_bag, item_path))
        tmpf = Tempfile.new([data_bag, '.json'])
        tmpf.puts Chef::JSONCompat.to_json(data)
        tmpf.close
        databag_from_file.config = config
        databag_from_file.name_args = [ data_bag, tmpf.path ]
        databag_from_file.run
      end
    end
  end
end