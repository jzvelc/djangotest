require "yaml"
require "rbconfig"

begin
  config = YAML.load_file("Vagrantfile.local")
rescue
  config = YAML.load_file("Vagrantfile.yml")
end

Vagrant.configure(2) do |vagrant|
  # SSH settings
  vagrant.ssh.shell = "bash -c 'BASH_ENV=/etc/profile exec bash'"
  vagrant.ssh.forward_agent = true

  # VM settings
  vagrant.vm.box = "ubuntu/trusty64"
  vagrant.vm.hostname = config["hostname"]
  vagrant.vm.network "private_network", ip: config["ip"]

  # Synced folders
  vagrant.vm.synced_folder ".", "/vagrant", disabled: true
  vagrant.vm.synced_folder ".", "/vagrant"

  # Virtualbox provider settings
  vagrant.vm.provider :virtualbox do |vb|
    vb.memory = config["memory"]
    vb.cpus = config["cpus"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on", "--name", config["hostname"]]
  end

  # Provisioning
  vagrant.vm.provision "shell" do |sh|
    sh.path = ".bin/install.sh"
    sh.privileged = true
  end
  vagrant.vm.provision "shell" do |sh|
    sh.path = ".bin/provision.sh"
    sh.args = "/vagrant"
    sh.privileged = false
  end
end

