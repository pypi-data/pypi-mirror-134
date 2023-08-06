# PreHEAT Open Python Package

This is the open Python package to consume Neogrids REST API.
For a quick introduction, see `demo.ipynb`.

# Installation

## Installation with pip (mostly for Linux)
Recommended: stable version (master branch):

    pip install git+https://gitlab.com/neogrid-technologies-public/preheat-open-python.git@master

Development version (Development branch - not recommended for most users):
    
    pip install git+https://gitlab.com/neogrid-technologies-public/preheat-open-python.git@Development

## Alternative installation

On Windows machines, you might experience that your system is not finding Git, so that the above command fails. In this case, you can install the toolbox manually following the steps below:

1- Download the code from this [link](https://gitlab.com/neogrid-technologies-public/preheat-open-python/-/archive/master/preheat-open-python-master.zip)

2- Unzip the file

3- Execute the following command in your Python command (replacing the path below by the path of the folder in which you unzipped the file):
> pip install [path to the unzipped folder containing the setup.py file]/.

(e.g. if you extracted the files in *C:/Users/my_user/code/*, then run: *pip install C:/Users/my_user/code/.*)


# Configuring the toolbox
First, make sure that you have created an API key for your user. This can be done on your [user profile page](https://app.neogrid.dk/icebear/#!/app/user/profile) in the PreHEAT App.

Now, you can store the API key in a configuration file. This user configuration file should be created in the following places:

| OS      | User level (recommended)                  | Machine level                  |  
|---------|-------------------------------------------|--------------------------------|
| Windows | C:/Users/[your user]/.preheat/config.json | (unsupported)                  |
| Linux   | ~/.preheat/config.json                    | /etc[/opt]/preheat/config.json |

The configuration files are read in the following priority order (using the first available):

1- User level

2- Machine level (Linux only): */etc/opt/preheat/config.json*

3- Machine level (Linux only): */etc/preheat/config.json*

And then add the following content in this file (adjusting with your API key):


```
{
  "PREHEAT_API_KEY": "YOUR_API_KEY_HERE"
}
```

Alternatively, you can also just import it explicitly in your code using the following command in your code 
(this is however not recommended, as you risk compromising your API key when sharing your code with others) :

```
from preheat_open import set_api_key

set_api_key("YOUR_API_KEY_HERE")
```


# Contributions

We encourage pull requests if you have developed new interesting features.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
