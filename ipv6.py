# net-python

from valid_ipv6 import valid_ipv6


ips = [ 
        "1111:2222::3333",
        "111:::22",
		"gh:22::3",
		"1:2:3",
		"1:2:3:4:5:6:7:8:9",
		"1:2:3:4:5:6:7:8",
        "jlk::kdjf",
        "::123",
        "1:2:3::",
		"129.168.1.1"
        ]
     
for ip in ips:
  print(valid_ipv6(ip))
