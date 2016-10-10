#7ninjas Django Boilerplate

##How to start:
 1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads) if not installed.
 2. Install [Vagrant](https://www.vagrantup.com/downloads.html) if not installed.
 3. Install  [Ansible (version 2.0.2)](http://docs.ansible.com/ansible/intro_installation.html) if not installed.
 4. Run `sudo ansible-galaxy install -r ./ansible/requirements.yml` from root project directory for installing Ansible role dependencies.
 ***
 **Warning!** Better to rename your project name from `boilerplate` to something more dedicated. And use this project name instead `boilerplate` for commands and paths in further steps.
 ***
 5. Run `sudo -- sh -c "echo '192.168.38.66 boilerplate.local flower.boilerplate.local api.boilerplate.local docs.boilerplate.local ws.boilerplate.local' >> /etc/hosts"` for simple accessing to Vagrant machine in your browser.
 6. Run `vagrant up` from root project directory for start the Vagrant machine. At first time machine will be automatically provisioned.
 7. Configure PyCharm (if you are using it):
     - Configuring Python interpreter: File > Settings > Project Interpreter > Add Remote > Vagrant > Python interpreter path: `/home/vagrant/boilerplate/venv/bin/python` > OK
     - Configuring Django support: File > Settings > Languages & Frameworks > Django > Enable Django support; Django project root: `{project_dir}`; Settings: `boilerplate/settings.py`
     - Configuring run/debug configurations: Run > Edit configurations… > Add new configuration > Django server > Name: Development Server; Host: 0.0.0.0; Port: 8000; Run browser: http://boilerplate.local:8000/; Path mapping: `Local path - path to project on host system : Remote path - path to project on vagrant machine`
     - Configuring database: Database > Add > Data Source > PostgreSQL > Download Driver > Host: `localhost`; Port: `5433`; Database: `boilerplate`; User: `boilerplate`; Password: `{password}` > Configure SSH > Check use SSH tunnel; Proxy host: `127.0.0.1`; Port: `2222`; Proxy user: `vagrant`; Auth type: Key pair; Private key file: `./.vagrant/machines/default/virtualbox/private_key` > OK > Test Connection > OK

***
#####_Notice!_ In this boilerplate is used Ansible Vault!
Files `host_vars/staging/vault.yml` and `host_vars/staging/vault.yml` are encrypted by default (Default password is `7ninjas`).
They're used to store sensitive data as db names, passwords, keys, secrets etc.
Before deploying to public servers as production or staging you must:
 
 1. Decrypt necessary files by command `ansible-vault decrypt host_vars/staging/vault.yml host_vars/production/vault.yml` (run it from ansible directory) using default password. 
 2. Edit configuration in those files as needed.
    Also if it's first edition of those files you _SHOULD_ edit:
     - database name, user and password;
     - django secret key (http://www.miniwebtool.com/django-secret-key-generator/);
    For passwords better to use generated (http://passwordsgenerator.net/).
 3. Encrypt files again with your _NEW AND SECURE_ password using command `ansible-vault encrypt host_vars/staging/vault.yml host_vars/production/vault.yml`.
 4. Create file `vault_pass.txt` in ansible root directory and write your password to it.
 5. Enjoy deployment :)
***

## Useful commands
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
