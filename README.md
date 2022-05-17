# openvpn-auth-handler

ensure python3 is installed

requests python package is required for calling the api
```bash
pip3 install requests
```
api should return json 
```{'success': 1}``` 
upon successfull authentication
so that we can return the proper exit code

Download or clone this repository
and add this line to your openvpn server config
usually `/etc/openvpn/server.conf`
```
script-security 2
duplicate-cn
username-as-common-name
auth-user-pass-verify ./openvpn-auth-handler/auth.py via-file
```

restart openvpn
```
systemctl restart openvpn
```
