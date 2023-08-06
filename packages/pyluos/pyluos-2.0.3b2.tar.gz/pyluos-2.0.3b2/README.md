<a href="https://luos.io"><img src="https://uploads-ssl.webflow.com/601a78a2b5d030260a40b7ad/602f8d74abdf72db7f5e3ed9_Luos_Logo_animation_Black.gif" alt="Luos logo" title="Luos" align="right" height="60" /></a>

[![Build Status](https://travis-ci.org/pollen-robotics/pyluos.svg?branch=master)](https://travis-ci.org/pollen-robotics/pyluos)
[![](http://certified.luos.io)](https://luos.io)
[![](https://img.shields.io/github/license/Luos-io/Pyluos)](https://github.com/Luos-io/Pyluos/blob/master/LICENSE)
[![](https://img.shields.io/reddit/subreddit-subscribers/Luos?style=social)](https://www.reddit.com/r/Luos)

# Pyluos

Pyluos lets you easily connect, interact and program your [luos](https://www.luos.io) based devices.

The API was designed to be as simple as possible and let you focus on **bringing life to your ideas!**

Read the complete [documentation of Pyluos](https://docs.luos.io/pages/tools/pyluos.html).

## Install Pyluos

#### From pypi (master branch stable):
```bash
pip install pyluos
```

#### From pypi (master branch pre-release):
```bash
pip install --pre pyluos
```

#### Or clone from git:
```
git clone https://github.com/Luos-io/pyluos
```

#### Compatibility

Pyluos is a pure-python library and works with Python >= 2.7 or 3.4 and later.

## Quickstart

Pyluos API was designed to be as simple as possible so you can directly focus on the application you want to make!

### Connecting

Connecting to your device is really easy. It actually takes only two lines of code.

#### On WiFi

```python
from pyluos import Device

device = Device('my_robot_hostname.local')
```

#### On serial

```python
from pyluos import Device

device = Device('my_serial_port')
```

The `my_serial_port` will look something like COM3 on a Windows device, or /dev/ttyUSB on a Mac or Linux device.

## Finding a gate

If you don't know the name of a gate, you can easily find it using the ```pyluos-usb-gate``` and ```pyluos-wifi-gate``` command line utilities. They should be automatically installed when you install Pyluos, and available in your path. From the terminal, you can run:

```pyluos-wifi-gate discover```

This will show the name of the WiFi gate connected on the same WiFi. This uses the Zeroconf protocol.

*Make sure to use either the IP or the hostname.local for WiFi gates.*

Similarly, to find the name of the USB gate connected to your machine you can run:
```pyluos-usb-gate discover```

You can then uses the found name to connect to it via Pyluos:

```python
from pyluos import Device
device = Device('/dev/cu.usbmodem2964691')
```
## The most for the community​
Most of the embedded developments are made from scratch. By using Luos, you will be able to capitalize on the development you, your company, or the Luos community already did. The re-usability of features encapsulated in Luos services will fasten the time your products reach the market and reassure the robustness and the universality of your applications.

* → Join the [Luos Slack Community](http://bit.ly/JoinLuosSlack)
* → Join the [Luos Discord Community](http://bit.ly/JoinLuosDiscord)
* → Join the [Luos Reddit Community](http://bit.ly/JoinLuosReddit)
* → Join the [Luos Forum](http://bit.ly/JoinLuosForum)

Need dedicated help with your project? Check out [Luos' support packages](https://www.luos.io/support).

## Contributing

Pyluos is developed by [Luos](https://www.luos.io) with the support of [Pollen Robotics](http://pollen-robotics.com/).

Pyluos still needs lots of usage and testing to help it become more useful and reliable. If you are actively using Pyluos, and have suggestion or comments, please let us know!

Do not hesitate to share your experience with Pyluos and meet other Luos users on our [forum](https://community.luos.io)!

## License

Pyluos is licensed under the [MIT license](./LICENSE).

## Don't hesitate to read [our documentation](https://docs.luos.io), or to post your questions/issues on the [Luos' subreddit](https://www.reddit.com/r/Luos/). :books:


[![](https://img.shields.io/reddit/subreddit-subscribers/Luos?style=social)](https://www.reddit.com/r/Luos)
[![](https://img.shields.io/badge/Luos-Documentation-34A3B4)](https://docs.luos.io)
[![](https://img.shields.io/badge/LinkedIn-Follow%20us-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/company/luos)
