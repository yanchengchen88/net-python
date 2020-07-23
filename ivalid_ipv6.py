# net-python

#ipv6效验

def valid_ipv6(ip):
 
    ip_split = ip.split(":")
    #用冒号分段
    
    if ip.count(':') < 2 or ip.count(':') > 7:
        return"这不是IPV6地址1"
    #排除小于2和多与7‘：’
    
    elif ip.count('::') > 1 or ':::' in ip:
        return'IPV6地址格式错误2'
    #排除‘：：：’    
    
    elif ip.count("::") == 0 and ip.count(":") != 8:
         return'ipv6地址长度不够3'
    elif ip_split[0] == "" and ip_split[1] != "":
         return'ipv6地址不对4'
    elif ip_split[-1] == "" and ip_split[-2] !="":
         return'ipv6地址不对5'
    #排除地址长度
    
    else:
         
         try:
             str2dec = [int(value,16) for value in ip_split if value != '']
         except valueError:
              return"这不是16进制6"
         #排除16进制
         
         if any(value > 65535 for value in str2dec):
               return'这不是IPV6地址7'
         elif any(value < 0 for value in str2dec):
               return"这不是一个IPv6地址8"
         
         else:
              return'这是ipv6地址'
         
