# - UnknownVPN Python3 Module

![alt](https://raw.githubusercontent.com/ConfusedCharacter/UnknownVPN/main/pic.png)

Simple Library for [UnknownVPN](https://t.me/Unknown_Vpn) [Robot](https://t.me/Unknownvpnbot) API documentation.
* You can check Example.py on github to see examples.

# installation
```bash
$ pip3 install UnknownVPN
```

# Upgrade 
```bash
$ pip3 install UnknownVPN --upgrade
```
or

```bash
$ pip3 install UnknownVPN==1.0.3
```

# Usage

```python3
import UnknownVPN

client = UnknownVPN.UserAccount("xxxxxxxxxxxxxxxxxxxxx")

# Get Api Version
client.ApiVersion()

# Get Account info 
data = client.AccountInfo()
data.balance
data.userid
data.services_count
data.username
```

### Created By [ConfusedCharacter](https://github.com/ConfusedCharacter)
### Good Luck!
