# Cloud Insight API

This is an example project which shows how to access the [Cloud Insight API](https://console.cloudinsight.alertlogic.com/api/) using Python.

## Overview
The [Cloud Insight API](https://console.cloudinsight.alertlogic.com/api/) is a REST API which provides many services related to the Cloud Insight system.
The data transmission protocol is JSON objects. The API receives and sends answers as JSON objects and HTTP errors or confirmation as HTTP status code.
The [CloudInsightAPI class](cloudInsightAPI.py)  provides an interface and some example methods to access the [Cloud Insight API](https://console.cloudinsight.alertlogic.com/api/). All the objects accessed by the [CloudInsightAPI class](cloudInsightAPI.py) will have the JSON response converted to generic Python objects ([Bunch](https://github.com/dsc/bunch)) which can have their properties accessed by obj.property syntax instead of dictionary syntax. The print of the objects will return a JSON formatted string to facilitate the visualization of the object data.
The requests are made using the [Requests](http://docs.python-requests.org/en/latest/) library and will raise [requests.exceptions.RequestException](http://docs.python-requests.org/en/latest/api/#requests.exceptions.RequestException) when some request fails according to the status code error.

The [program.py](program.py) provide an example of a command line script implementation of the [CloudInsightAPI class](cloudInsightAPI.py)

## Methods

### CloudInsightAPI()
The CloudInsightAPI instance will hold the API URL, the user information, the access token used in that session, a dictionary of the user credentials and a dictionary of enviroments.

```python
class CloudInsightAPI:
	def __init__(self):
		self._BASE_URL = "https://api.cloudinsight.alertlogic.com"
		self.credentials = dict()
		self.sources = dict()
		self.user = None
		self.token = ""
```

### login(username, password)
**@param** _username_ (string)  
The user name to log into the system  
**@param** _password_ (string)  
The user password  
**@return** _(boolean)_
Whether the login succeed

### validate(credential) _@staticmethod_
**@param** _credential_ (object)  
The object which contains the credential information  
**@return** _boolean_  
Whether the given credential information is valid  

### createCredential(type, name, dict_cred_data)
 **@param** _type_ (string)  
 The type of the credential  
 **@param** _name_ (string)  
 The name of the credential  
 **@param** _dict_cred_data_ (dictionary)  
 The dictionary which contains the key and values according to the credential configuration needed  
 **@return** _(object)_  
 The created credential  
 
### listCredentials(filters="")
**@param** filters (string)  
The filters to apply in the API credential search according to the [CloudInsightAPI filters objects](https://console.cloudinsight.alertlogic.com/api/sources/#api-_footer)  
**@return** (dictionary)  
This method saves locally in the instance a dictionary of the search results where the UUID of each item is the key and the credential object itself is the value. It also returns that dictionary

### getCredential(credential_id)
**@param** _credential_id_ (string)  
The UUID of the credential  
**@return** _(object)_  
The found credential object or raise a 404 exception if any object was found.  

### deleteCredential(credential_id)
**@param** _credential_id_ (string)  
The UUID of the credential  
**@return** _(void)_ 
This removes the credential from system and from the instance dictionary as well  

### createSource(name, collection_type, credential, scope, discover, scan):
**@param** _name_ (string)  
The name of the source  
**@param** _collection_type_ (string)  
The collection type of the source  
**@param** _credential_ (object)  
The credential object which will be added to the source  
**@param** _scope_ (dictionary)  
The scope with the path of the sources to be included or excluded from the environment  
**@param** _discover_ (boolean)  
Whether the system system should discover the environment  
**@param** _scan_ (boolean)  
Whether the system should scan the sources  
**@return** _(object)_  
The created source   

### listSources(filters="")
**@param** _filters_ (string)  
The filters to apply in the API credential search according to the [CloudInsightAPI filter objects](https://console.cloudinsight.alertlogic.com/api/sources/#api-_footer)  
**@return** _(dictionary)_  
This method saves locally in the instance a dictionary of the search results where the UUID of each item is the key and the source object itself is the value. It also returns that dictionary

### getSource(source_id)
**@param** _source_id_ (string)  
The UUID of the source  
**@return** _(object)_  
The found source object or raise a 404 exception if any object was found.  

### deleteSource(source_id)
**@param** _source_id_ (string)  
The UUID of the source  
**@return** _(void)_  
This removes the source from system and from the instance dictionary as well  