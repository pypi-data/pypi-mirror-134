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

Show version:
```
carooline-tecrmi-seamless --version
```

### Help

To see the different options and commands available:

```
carooline-tecrmi-seamless --help
```

Should output 
```shell
Usage: carooline-tecrmi-seamless [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version                   Show the application's version and exit.
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  get-api-key  Get Api Key
  get-link     Get API Key and generate TecRMI seamless deeplink for...
```

### Generate API Key
```
carooline-tecrmi-seamless get-api-key 
```

This will output your APIKey in the shell.

### Get Seamless link

#### Basic command to get a link

```
carooline-tecrmi-seamless get-link 
```

#### Get RMI webapp link directly on vehicle with KType:

Giving a *car* id (KType):

```
carooline-tecrmi-seamless get-link --type-id=9465
```

Giving a *truck* id (NType):

```
carooline-tecrmi-seamless get-link --vehicle-type=trucks --type-id=13290
```

#### Options
```shell
Options:
  --catalog TEXT                  [env var: TECRMI_CATALOG; default:
                                  TecrmiCatalog]
  --username TEXT                 [env var: TECRMI_USERNAME; default:
                                  TecrmiUsername]
  --password TEXT                 [env var: TECRMI_PASSWORD; default:
                                  TecrmiPassword]
  --default-ttl INTEGER           Living duration of the generated TecRMI API
                                  Key  [env var: TECRMI_DEFAULT_TTL; default:
                                  31536000]
  --wsdl TEXT                     [env var: TECRMI_WEBCAT_WSDL; default: https
                                  ://webservice.tecalliance.services/webcat30/
                                  v1/services/WebCat30WS.soapEndpoint?wsdl]
  --lang TEXT                     [env var: TECRMI_LANG; default: fr]
  --url TEXT                      [env var: TECRMI_WEBCAT_URL; default:
                                  https://web.tecalliance.net]
  --module [rmi|parts|home]       [default: TecRMIModule.rmi]
  --vehicle-type [cars|trucks]    [default: VehicleType.cars]
  --type-id TEXT                  KType or NType (Without the 100 prefix)
  --display [modules|components]  [default: Display.modules]
  --siv TEXT                      SIV search is subject to the access rights
                                  of the credentials
  --vin TEXT                      VIN search is subject to the access rights
                                  of the credentials
  --help                          Show this message and exit.
```