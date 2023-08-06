## py-linux-ports
Check Linux System Port's Status

[![Build Status](https://app.travis-ci.com/sujitmandal/py-linux-ports.svg?branch=master)](https://app.travis-ci.com/sujitmandal/py-linux-ports) ![GitHub license](https://img.shields.io/github/license/sujitmandal/py-linux-ports) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-linux-ports) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/py-linux-ports) ![PyPI](https://img.shields.io/pypi/v/py-linux-ports)


[![Downloads](https://pepy.tech/badge/py-linux-ports)](https://pepy.tech/project/py-linux-ports)



## Package Installation  : 
```
pip install py-linux-ports
```
[Package Link](https://pypi.org/project/py-linux-ports/)


## Py-Linux-Port's: 
```python
import json
from PyLinuxPorts.PyLinuxPorts import portScan 

IpAddress = "192.168.43.133"
PortNumber = 65000

result  = portScan(IpAddress, PortNumber)

print(json.dumps(result, indent=4))

with open('result.json', 'w') as i:
    json.dump(result, i)
```

## License:
MIT Licensed

## Author:
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)