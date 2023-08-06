# TecRMI Seamless login APP

TecRMI Seamless catalog login URL generation

## Installation

```
pip install carooline-tecrmi-seamless
```

## Configuration

Create a `.tecrmi.env` file in your `~/` or Home folder with global TecRMI credentials:

```
TECRMI_WEBCAT_URL = "https://web.tecalliance.net"
TECRMI_WEBCAT_WSDL = 'https://webservice.tecalliance.services/webcat30/v1/services/WebCat30WS.soapEndpoint?wsdl'
TECRMI_CATALOG = "rmi-iazduih-2"
TECRMI_USERNAME = "username"
TECRMI_PASSWORD = "password"
TECRMI_DEFAULT_TTL = 31536000
TECRMI_LANG = "fr"
```

This is not mandatory, you can also pass each arguments directly to the command line.

## Usage

Command should be installed 

```
wich carooline-tecrmi-seamless
````

### Help

```
carooline-tecrmi-seamless
```

### Generate API Key
```
carooline-tecrmi-seamless get-api-key 
```

### Get Seamless link
```
carooline-tecrmi-seamless get-api-key 
```