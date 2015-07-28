# dlabstest

## Development environment
1. Install [Virtualbox](https://www.virtualbox.org)
2. Install [Vagrant](https://www.vagrantup.com/)
3. Run following commands:

``` bash
git clone SOMEREPO
cd dlabstest
vagrant up
```

This will setup development environment. Default box settings are:
``` yaml
# settings.yml
hostname: dlabstest.dev
ip: 192.0.0.123
memory: 4092
cpus: 4
```
To override settings create a file named `settings.local.yml` and provide your custom configuration.

