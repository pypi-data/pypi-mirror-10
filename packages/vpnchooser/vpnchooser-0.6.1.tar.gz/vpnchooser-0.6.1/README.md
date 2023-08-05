# VPNChooser #

The vpnchooser is a web application which can be used as a graphical
user interface to move devices from one ip rule table to another.

These can be used to reroute clients to different gateways, hence the
name "vpnchooser".

## Setup ##

The system builds on top of a linux router utilizing the ip rule system.
It has been tested with the "[dd-wrt](http://www.dd-wrt.com/site/index)"
router system though should work fine with every linux router which has
ssh access.

First you need to define an own ip rule definition and send the traffic
on the router to an other gateway (which usually should be sending the
traffic through an vpn).

```
ip route add default via {gateway} dev {device} table 10
```

### Via Docker ###

For this it is necessary to checkout the full repository at
[Github](https://github.com/cbrand/vpnchooser).

If you want to test the setup I would recommend docker.

Ensure you have [docker](https://www.docker.com/) and
[docker-compose](https://docs.docker.com/compose/) installed.

Copy the "example.cfg" and put it with the username, the password
and the retrieved host key as "docker.cfg".

To fill in the data you require the ssh host key of the user. You can
usually get these with one of the following commands on the server/router:

```
ssh-keygen -l -f /etc/ssh/ssh_host_rsa_key.pub
ssh-keygen -l -f /etc/ssh/ssh_host_dsa_key.pub
ssh-keygen -l -f /etc/ssh/ssh_host_key.pub
```

As a alternative you can follow the normal installation instructions
and use the configuration generating utility provided by the console
script, which is packed in the package.

```
vpnchooser generate_config --docker {path_to_config_file}
```

This will ask for the necessary configuration options (host of the router,
username, password) and extracts the ssh host key from the host. Finally
it stores it to the file passed as a command line parameter.

After that you can start the necessary docker instances with the following
command.

```
docker-compose up
```

This builds and downloads all necessary system components and starts the
necessary system components.
After that you should be able to access the application through port 5000.
The default username is "admin" and the password is "admin".


### Without Docker ###

To run the system without docker you need to at least provide a Redis
server which can be used to synchronize the redis backend. An optional
database can also be provided. However a default sqlite database can
also be utilized.

If you have provided the necessary software you can install the application.
I recommend doing this in an
[virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

You can now install the vpnchooser via
```
easy_install vpnchooser
```

After this you can generate a configuration file with the "vpnchooser" command.

```
vpnchooser generate_config {path_to_config_file}
```

This will guide you through the process of configuring the data. After
the file is generated you should set it as the configuration file and
then can start the server.

```
export FLASK_CONFIG_FILE={path_to_config_file}
vpnchooser runserver
```

In a different terminal start the celery process to synchronize the
current state with the router.

```
export FLASK_CONFIG_FILE={path_to_config_file}
vpnchooser runcelery
```

## Development Environment ##

To compile the frontend you do need node.js and npm.

Go to the "src/vpnchooser/static" folder and type

```
npm install
grunt dev
```

This will compile the frontend.

## License ##

The code is available with the [MIT](http://opensource.org/licenses/MIT)
license.

## TODO ##

The application is still in development. If you want to contribute
here are some topics which would be nice to have:

- SSH Private Keys for authentication with the router
- Better documentation
    * On Boarding
    * Code
- Unit Tests

I will gladly review and merge pull requests given to this project.
