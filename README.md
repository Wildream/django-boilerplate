#7ninjas Django Boilerplate

This project serves as a baseline for real-world Django-based applications.

## What's inside the box?
 * [Django](https://github.com/django/django)/[Django REST framework](https://github.com/tomchristie/django-rest-framework)
 * [Redis](https://github.com/antirez/redis)
 * [PostgreSQL](https://github.com/postgres/postgres)
 * [Gunicorn](https://github.com/benoitc/gunicorn) WSGI HTTP Server
 * [nginx](https://nginx.org/)
 * [Tornado](https://github.com/tornadoweb/tornado) for handling websockets and more
 * [Celery](https://github.com/celery/celery) Distributed Task Queue 
 * [Circus](https://github.com/circus-tent/circus) - ZeroMQ-powered Proccess manager

## Getting started
### How to run the project locally:
 1. Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
 2. Install [Vagrant](https://www.vagrantup.com/downloads.html).
 3. Install [Ansible (version 2.0.2)](http://docs.ansible.com/ansible/intro_installation.html).
 4. Run `sudo ansible-galaxy install -r ./ansible/requirements.yml` from project root directory. This will install all required dependencies for Ansible to build the project.

 ***
 **Warning!** Better to rename your project name from `boilerplate` to something more dedicated. And use this project name instead `boilerplate` for commands and paths in further steps.
 ***

 5. Run `sudo -- sh -c "echo '192.168.38.66 boilerplate.local flower.boilerplate.local api.boilerplate.local docs.boilerplate.local ws.boilerplate.local' >> /etc/hosts"` for simple accessing to Vagrant machine in your browser (optional).
 6. Run `vagrant up` from root project directory for start the Vagrant machine. At first time machine will be automatically provisioned.
 7. Configure PyCharm (in case you use PyCharm, optional):
     - Configure Python interpreter: File > Settings > Project Interpreter > Add Remote > Vagrant > Python interpreter path: `/home/vagrant/boilerplate/venv/bin/python` > OK
     - Enable Django support: File > Settings > Languages & Frameworks > Django > Enable Django support; Django project root: `{project_dir}`; Settings: `boilerplate/settings.py`
     - Set up run/debug configurations: Run > Edit configurations… > Add new configuration > Django server > Name: Development Server; Host: 0.0.0.0; Port: 8000; Run browser: http://boilerplate.local:8000/; Path mapping: `Local path - path to project on host system : Remote path - path to project on vagrant machine`
     - Configuring database: Database > Add > Data Source > PostgreSQL > Download Driver > Host: `localhost`; Port: `5433`; Database: `boilerplate`; User: `boilerplate`; Password: `{password}` > Configure SSH > Check use SSH tunnel; Proxy host: `127.0.0.1`; Port: `2222`; Proxy user: `vagrant`; Auth type: Key pair; Private key file: `./.vagrant/machines/default/virtualbox/private_key` > OK > Test Connection > OK

***

#####_Notice!_ This boilerplate uses Ansible Valut to encrypt sensitive parts of the configuration. Always encrypt your sensitive variables when working on real projects.
Files `host_vars/staging/vault.yml` and `host_vars/staging/vault.yml` are encrypted by default (Default password is `7ninjas`).
These files are used to store sensitive data, such as database credentials, deployment keys, certificates etc.
Before deploying to public servers, you must:
 
 1. Decrypt necessary files by executing `ansible-vault decrypt host_vars/staging/vault.yml host_vars/production/vault.yml` in `ansible` directory. Use the default password. 
 2. Edit configuration in those files as needed.
    If it's the first time you touch those files, you _MUST_ change the following:
     - database name, user and password;
     - Django secret key (http://www.miniwebtool.com/django-secret-key-generator/);
    Passwords should be strong enough, it's better to use generated ones: (http://passwordsgenerator.net/).
 3. Encrypt files again with your _NEW AND SECURE_ password using command `ansible-vault encrypt host_vars/staging/vault.yml host_vars/production/vault.yml`.
 4. Create file `vault_pass.txt` in ansible root directory and write your password to it.
 5. Enjoy deployment :)
***

### How to deploy the project to remote server(s)
 1. Edit respective files in a `host_vars` directory, as well as inventory files. This repo includes default configuration samples for production and staging environments.
 2. Execute `./deploy <inventory name> <tags>` command in the project's root directory, where <inventory name> is the name of your inventory (e.g. "staging" or "production"), and <tags> are optional tags that will execute only the tasks that were marked by this tag (e.g. "provision" tag, which will skip installing most part of the setup and only update the code from a repo and restart services). 
 3. Enjoy deployment :)

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
