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

# Get All Services
client.GetServices()

# Get Prices
client.GetPrices()

# Get Servers
client.GetServers()

# Get Service License
data = client.GetServiceLicense('xxxxxxxxxx')
data.license
data.service_id


# Change Service License
data = client.ChangeLicense('xxxxxxxxxx')
data.license
data.service_id


# Buy Service
data = client.BuyService('xxxxxxxxxx',1,50,1)
data.license
data.service_id


client = UnknownVPN.ManageServices("xxxxxxxxxxxxx")

# Get Info
data = client.GetInfo()
data.createdTime
data.enabled
data.expired
#...

# Get Links
data = client.GetLinks()
data.nimbaha
data.direct

# Change Protocol
client.ChangeProtocol("vless")

# Change Connection Type
client.ChangeConnectionType("ws")

# Change Link
uuid = client.ChangeLink()

# Get Connections
ips = client.GetConnections()

# Change Location
result = client.ChangeLocation("j5aRq3")
