## py-linux-ports
Check Linux System Port's Status



## Py-Linux-Port's: 
```
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