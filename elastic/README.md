# Elastic Stack

This is the ELK / Elastic stack implementation for this project, which uses the Elastic / Logstash / Kibana technologies together to ingest and analyse data with a HTTP web interface.

## Installation

Install the following applications onto your system:

* VirtualBox ([version 6.1.32](https://www.virtualbox.org/wiki/Downloads))
* Vagrant ([version 2.2.19](https://www.vagrantup.com/downloads))

TODO: rest of instructions

## Usage

Run the following commands:
```
cd vagrant
vagrant up
vagrant ssh
```
Note: The default password is 'vagrant'.

You can access Kibana via localhost:
```
http://localhost:5601
```

When finished, run the following command:
```
vagrant halt
```
