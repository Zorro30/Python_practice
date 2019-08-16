"""
Defanging IP Address 1.1.1.1 to 1[.]1[.]1[.]1 
"""

def string_replace(ip_str):
    return ip_str.replace('.','[.]')

print(string_replace("1.1.1.1"))