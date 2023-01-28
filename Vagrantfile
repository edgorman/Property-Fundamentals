
Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.define "PropertyFundamentalsVM"
    config.vm.hostname = "dev-vm"
    
    config.vm.provider :virtualbox do |vb|
      vb.memory = 8192
      vb.cpus = 2
      vb.name = "PropertyFundamentalsVM"
      vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/.", "1"]
    end
    
    config.vm.synced_folder ".", "/home/vagrant/PropertyFundamentals"
    config.vm.provision "shell", path: "scripts/setup.sh", privileged: true
    config.vm.provision "shell", reboot: true
  end
