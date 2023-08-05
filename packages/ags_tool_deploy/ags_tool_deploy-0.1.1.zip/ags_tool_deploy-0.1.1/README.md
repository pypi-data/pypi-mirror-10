## Overview ##

This tool provides a command-line interface for packaging and publishing python toolboxes to ArcGIS Server (10.2.x).


## Installation ##

To install the latest stable version:

```
pip install python-ags
```


Latest changes:
```
pip install https://bitbucket.org/databasin/ags_tool_deploy/get/develop.zip#egg=ags_tool_deploy
```

*Installing manually:*

Download the latest changes from the [develop branch](https://bitbucket.org/databasin/ags_tool_deploy/get/develop.zip), extract, 
and execute 

```
python setup.py install
```

This will install the script to your local python packages folder as 

```
ags_tool_deploy/deploy.py
```

Consider adding this folder to your PATH.


## Usage ##
This tool is intended to be run from within a console.

For information on usage, simply run 

```
python deploy.py --help
```

The commands below allow you to include Mercurial repository information.  This does not bundle the full repository,
but instead includes the link to the source repository and current branch, so that you can run 

```
hg pull --update
```

on the server to pull down the full repository.



### Packaging ###
Use the ```package``` command to bundle your python toolbox into a service definition (*.sd) file.

```
Usage: deploy.py package [OPTIONS] <toolbox_path> <service_name> <outfile_name>

Package a python toolbox into a service definition file (*.sd). Local
python modules this toolbox references are included automatically.
Requires 7Zip to be installed and on the system PATH.

WARNING: this will overwrite the file <outfile_name> if it already exists.

  Aguments:
  <toolbox_path>:         Filename of python toolbox (*.pyt) to deploy
  <service_name>:         Name of service, including folder(s).  Example: SomeFolder/MyTool
  <outfile>:              Name of the service definition file to create

Options:
  --files <files>                 Wildcard patterns of additional files to
                                  include (relative to toolbox).  Example:
                                  *.csv,some_data.*
  --hg                            Include Mercurial (hg) repository 
                                  information?                                  
  --sync                          Execute tool synchronously instead of
                                  asynchronously (default)
  --messages [None|Info|Error|Warning]
                                  Level of messaging for service
  --help                          Show this message and exit.
```  
  

### Publishing ###
Use the ```publish``` command to deploy your python toolbox to an ArcGIS server.

```
Usage: deploy.py publish [OPTIONS] <toolbox_path> <service_name> <server:port> <user>

Publish a python toolbox to an ArcGIS server. Local python modules this
toolbox references are included automatically. Requires 7Zip to be
installed and on the system PATH.

  Aguments:
  <toolbox_path>:         Filename of python toolbox (*.pyt) to deploy
  <service_name>:         Name of service, including folder(s).  Example: SomeFolder/MyTool
  <server:port>:               Hostname and port number of ArcGIS server
  <user>:                 ArcGIS server administrator user name

Options:
  --password <password>           ArcGIS administrator password.  You will be
                                  prompted for this if you do not provide it
  --files <files>                 Wildcard patterns of additional files to
                                  include (relative to toolbox).  Example:
                                  *.csv,some_data.*
  --hg                            Include Mercurial (hg) repository 
                                  information?                                  
  --sync                          Execute tool synchronously instead of
                                  asynchronously (default)
  --messages [None|Info|Error|Warning]
                                  Level of messaging for service
  --overwrite                     Delete and replace the service, if it
                                  already exists?
  --help                          Show this message and exit.

```





## Requirements: ##

* lxml
* click
* ags  (from: https://bitbucket.org/databasin/python-ags)
* 7Zip: must be installed manually from [7Zip website](http://www.7-zip.org/)


## Assumptions ##
* only Python 2.7 is supported
* only tested on Windows
* only ArcGIS 10.2.x is supported



## License ##
See LICENSE file.