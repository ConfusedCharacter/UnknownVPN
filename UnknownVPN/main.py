#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =================================================== 
# UnknownVPN Library v1.0.2
#
# Telegram Channel: Unknown_Vpn.t.me
#                                                     
# Github: https://github.com/ConfusedCharacter/UnknownVPN/
#                                                     
# Documentation: https://documenter.getpostman.com/view/25344905/2s8ZDSdR3q#6ad6d4a1-ba9c-4169-a8d1-5a31e9ea6a95
#
# Website: https://UnknownVpn.org
#
# =================================================== 


import requests
import UnknownVPN.config as config
from UnknownVPN.structs import AccountDetails,GetServiceLicense,ChangeLicense,BuyService,GetInfo,GetLinks


class UserAccount:
    def __init__(self,X_API_KEY : str) -> None:
        """
        Getting X-API-KEY For Requests
        X-API-KEY need to access UnknownVPN API you can get it on UnknownVpnBot.t.me
        """
        self.X_API_KEY = X_API_KEY
        self.session = requests.session()
        self.session.headers.update(
            {
                "X-API-KEY" : self.X_API_KEY
            })

    def ApiVersion(self) -> object:
        """
        Getting API Version of UnknownVPN Service
        """
        response = self.session.get(config.APIVERSION_URL)
        response = response.json()
        if response['status']:
            return response['version']
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")

    def AccountInfo(self) -> AccountDetails:
        """
        Getting Account Info such as:
            - balance
            - services_count
            - userid
            - username
        """
        response = self.session.get(config.ACCOUNTINFO_URL)
        response = response.json()
        if response['status']:
            return AccountDetails(
                float(response['balance']),
                int(response['services_count']),
                int(response['userid']),
                response['username']
                )

        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")
        
    def GetServices(self) -> list:
        """
        Getting All Services:

        Output Data (list):
            [
                {
                    "id": "xxxxxxxxxxx",
                    "license": "xxxxxxxxxxx",
                    "name": "ServiceName",
                    "subscription_id": "aBcDeFgHiJkLmNoPQrStUvWxYz"
                }
            ]
        """

        response = self.session.get(config.GETSERVICES_URL)
        response = response.json()
        if response['status']:
            return response['services']
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")

    def GetPrices(self)  -> list:
        """
        Get Vpn And Service Prices
            month month
            size size in GB
            user max count of connections
            price price of service in TOMAN.

        Output Data (list):
            [
                {
                "month": "1",
                "price": 57000,
                "size": "50",
                "user": "1"
                }
            ]
        """

        response = self.session.get(config.GETPRICES_URL)
        response = response.json()
        if response['status']:
            return response['prices']
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")

    def GetServers(self) -> list:
        """
        Get List of locations. server_id can be used in buy service and change location.

        Output Data (list):
            [
                {
                "enabled": false,
                "flag": "🇩🇪",
                "id": "xxxxxxxxxxx",
                "name": "xxxxxxxxxxx"
                }
            ]
        """

        response = self.session.get(config.GETSERVERS_URL)
        response = response.json()
        if response['status']:
            return response['servers']
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")
    
    def GetServiceLicense(self,service_id:str) -> GetServiceLicense:
        """
        Get service license by service_id.

        Output Data (Object):
            - license
            - service_id
        """

        response = self.session.post(config.GETSERVICELICENSE_URL,json={
            'service_id':service_id
        })
        response = response.json()
        if response['status']:
            return GetServiceLicense(response['license'],response['service_id'])
        elif not response['status'] and 'invalid' in response['message']:
            raise ValueError(response['message'] + ' sent to server.')
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")
    
    def ChangeLicense(self,service_id:str) -> ChangeLicense:
        """
        Change Service license by service_id.

        Output Data (Object):
            - license
            - service_id
        """

        response = self.session.post(config.CHANGELICENSE_URL,json={
            'service_id':service_id
        })
        response = response.json()
        if response['status']:
            return ChangeLicense(response['license'],response['service_id'])
        elif not response['status'] and 'invalid' in response['message']:
            raise ValueError(response['message'] + ' sent to server.')
        else:
            raise ValueError(response['message'] + " X-API-KEY is Invalid")

    def BuyService(self,server_id:str,service_time:int,size:int,count:int) -> BuyService:
        """
        Buy a new service. data should be json and match with /getprices list. server_id you can pick it from /getservers.

        Output Data (Object):
            - license
            - service_id
        """

        response = self.session.post(config.BUYSERVICE_URL,json={
            "server_id":server_id,
            "time":str(service_time),
            "size":str(size),
            "count":str(count)
        })
        response = response.json()
        if response['status']:
            return BuyService(response['license'],response['service_id'])
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])

    def ChangeName(self,service_id:str,name:str) -> bool:
        """
        Chanage service name by service_id

        Output Data (boolean):
            True,False
        """

        response = self.session.post(config.CHANGENAME_URL,json={
            "service_id":service_id,
            "name": name
        })
        response = response.json()
        if response['status']:
            return True
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])

class ManageServices:

    def __init__(self,service_license : str) -> None:
        """
        Getting Service Lincense For Requests
        Service Lincense To Make chenges on services you can get with UserAccount Class
        """
        self.service_license = service_license
        self.session = requests.session()
        self.session.headers.update(
            {
                "Authorization" : self.service_license
            })
    
    def GetInfo(self) -> GetInfo:
        """
        You can manage your services using license .
        If your license is wrong you will receive response like this :
        
            message : "Unauthorized"
        
        Note: /getinfo and /getlinks have a limit 60 request per minute and /getconnections have a limit 240 request per minute.

        Output Data (Object):
             - response
            - enabled
            - expired
            - expiryTime
            - free
            - id
            - license
            - name
            - plan
            - price
            - protocol
            - remain_size
            - server_id
            - server_name
            - size
            - subscription_id
            - type
            - used_size
            - users_count
            - banned
        """
        response = self.session.get(config.GETINFO_URL)
        response = response.json()
        if response['status']:
            response = response['service']
            return GetInfo( createdTime = response['createdTime'],
                            enabled = response['enabled'],
                            expired = response['expired'],
                            expiryTime = response['expiryTime'],
                            free = response['free'],
                            id = response['id'],
                            license = response['license'],
                            name = response['name'],
                            plan = response['plan'],
                            price = response['price'],
                            protocol = response['protocol'],
                            remain_size = response['remain_size'],
                            server_id = response['server_id'],
                            server_name = response['server_name'],
                            size = response['size'],
                            subscription_id = response['subscription_id'],
                            type = response['type'],
                            used_size = response['used_size'],
                            users_count = response['users_count'],
                            banned = response['banned']
            )
        else:
            raise ValueError(response['message'] + " LICENSE is Invalid")
    
    def GetLinks(self) -> GetLinks:
        """
        Get connections links.

        Output Data (Object):
            - direct
            - nimbaha
        """
        response = self.session.get(config.GETLINKS_URL)
        response = response.json()
        if response['status']:
            return GetLinks(
                response['direct'],
                response['nimbaha']
             )
        elif not response['status'] and response['message'] == 'maintenance':
            raise Exception("This part is under maintenance. please try again")
        else:
            raise ValueError(response['message'] + " LICENSE is Invalid")
    
    def ChangeProtocol(self,protocol) -> bool:
        """
        Change Protocol of service. protocol can "vmess" or "vless".

        Output Data (boolean):
            True, False
        """
        response = self.session.post(config.CHANGEPROTOCOL_URL,json={
            'protocol':protocol
        })
        response = response.json()
        if response['status']:
            return True
        elif len(response) == 1:
            return response['status']
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])
    
    def ChangeConnectionType(self,connection_type) -> bool:
        """
        Change Connection type of service. type can "tcp" or "ws".

        Output Data (boolean):
            True, False
        """
        response = self.session.post(config.CHANGECONNECTIONTYPE_URL,json={
            'type':connection_type
        })
        response = response.json()
        if response['status']:
            return True
        elif len(response) == 1:
            return response['status']
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])
    
    def ChangeLink(self) -> str:
        """
        Change Connection Link of service.

        Output Data (string):
            "uuid" or raise error
        """
        response = self.session.get(config.CHANGELINK_URL)
        response = response.json()
        if response['status']:
            return response['uuid']
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])
    
    def GetConnections(self) -> list:
        """
        Get connection ips.

        Output Data (list):
            [
                1.1.1.1,
                1.1.1.2
            ]
        """
        response = self.session.get(config.GETCONNECTIONS_URL)
        response = response.json()
        if response['status']:
            return response['connections']
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])
    
    def ChangeLocation(self,server_id:str) -> bool:
        """
        Change location of service.

        Output Data (boolean):
            True, False
        """
        response = self.session.post(config.CHANGELOCATION_URL,json={
            "server_id":server_id
        })
        response = response.json()
        if response['status']:
            return True
        elif not response['status'] and "invalid" in response['message']:
            raise ValueError(response['message'] + " sent to server.")
        else:
            raise Exception(response['message'])