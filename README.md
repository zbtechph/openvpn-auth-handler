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
