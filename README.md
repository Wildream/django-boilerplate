# Backend

## Installation
 - Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
 - Install [Vagrant](https://www.vagrantup.com/downloads.html)
 - Install [Ansible (version 2.0.2)](http://docs.ansible.com/ansible/intro_installation.html)
 - Run `sudo ansible-galaxy install -r ./ansible/requirements.yml`
 - Run `sudo -- sh -c "echo '192.168.38.66 boilerplate.local flower.boilerplate.local api.boilerplate.local docs.boilerplate.local ws.boilerplate.local' >> /etc/hosts"`
 
## Configuring PyCharm
 - Configuring Python interpreter: File > Settings > Project Interpreter > Add Remote > Vagrant > Python interpreter path: `/home/vagrant/boilerplate/venv/bin/python` > OK
 - Configuring Django support: File > Settings > Languages & Frameworks > Django > Enable Django support; Django project root: `{project_dir}`; Settings: `boilerplate/settings.py`
 - Configuring run/debug configurations: Run > Edit configurations… > Add new configuration > Django server > Name: Development Server; Host: 0.0.0.0; Port: 8000; Run browser: http://boilerplate.local:8000/; Path mapping: `Local path - path to project on host system : Remote path - path to project on vagrant machine`
 - Configuring database: Database > Add > Data Source > PostgreSQL > Download Driver > Host: `localhost`; Port: `5433`; Database: `boilerplate`; User: `boilerplate`; Password: `{password}` > Configure SSH > Check use SSH tunnel; Proxy host: `127.0.0.1`; Port: `2222`; Proxy user: `vagrant`; Auth type: Key pair; Private key file: `./.vagrant/machines/default/virtualbox/private_key` > OK > Test Connection > OK

## Commands
### Ansible
 - `bin/ansible-playbook -i ./ansible/{environment}.ini ./ansible/site.yml` - Deploy to {environment} servers.

### Vagrant
 - `vagrant up` - Start the virtual machine.
 - `vagrant halt` - Shutdown the virtual machine.
 - `vagrant destroy` - Destroy the virtual machine.
 - `vagrant provision` - Triggers provisioning on a running virtual machine.
 - `vagrant ssh` - Create an ssh connection with the virtual machine.
 - `vagrant reload` - Restarts vagrant machine, loads new Vagrantfile configuration.
 - `vagrant status` - Outputs status of the vagrant machine.
 - `vagrant suspend` - Suspends the machine.
 - `vagrant resume` - Resume a suspended vagrant machine.
 - `vagrant share` - Share your Vagrant environment with anyone in the world.

### SSH
 - `ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "your_email@example.com"` - Generate a new SSH key (https://help.github.com/articles/generating-ssh-keys/).
 - `cat ~/.ssh/id_rsa.pub` - Show SSH public key.
 - `cat ~/.ssh/id_rsa` - Show SSH private key.
