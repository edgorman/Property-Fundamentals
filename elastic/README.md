# Elastic Stack

This is the ELK / Elastic stack implementation for this project, which uses the Elastic / Logstash / Kibana technologies together to ingest and analyse data with a HTTP web interface.

## Installation

Install the following applications onto your system:

* VirtualBox ([version 6.1.32](https://www.virtualbox.org/wiki/Downloads))
* Vagrant ([version 2.2.19](https://www.vagrantup.com/downloads))

Verify this has installed correctly by running:
```
vagrant -v
```

Run the following commands to set up the box (this may take ~10 minutes):
```
cd vagrant
vagrant up
```

Once complete, test you can SSH into the box by running (default password is 'vagrant'):
```
vagrant ssh
```

## Usage

Run the following commands to bring the box up:
```
cd vagrant
vagrant up
```

You can access the Kibana dashboard via the webpage:
```
http://localhost:5601
```

When finished, run the following command to close the box:
```
vagrant halt
```
