PROJECT_NAME = "boilerplate"
PROJECT_DIR = "/home/vagrant/#{PROJECT_NAME}/src/api"

Vagrant.require_version ">= 1.8.1"
Vagrant.configure(2) do |config|

  config.vm.hostname = PROJECT_NAME
  config.vm.box = "ubuntu/trusty64"

  config.vm.network :private_network, ip: "192.168.38.66"
  config.vm.synced_folder ".", PROJECT_DIR

  config.vm.provider :virtualbox do |vb|
    vb.name = PROJECT_NAME
    vb.memory = "2048"
    vb.cpus = 2
    vb.gui = false
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "ansible/site.yml"
    ansible.inventory_path = "ansible/vagrant.ini"
    ansible.host_key_checking = false
    ansible.limit = "*"
  end
end