# reproducers

- Creating a custom pypi repo on CLI

Add the necessary firewall rules
```
# firewall-cmd --add-port=8080/tcp
# firewall-cmd --reload
```

Create a custom venv and install the necessary modules
```
# /usr/libexec/platform-python -m venv piprepo
# source piprepo/bin/activate
# pip install pypiserver
```

Download some sample packages to a directory
```
# mkdir packages ; cd packages
# wget [url]pythonpackage.tar.gz
# cd -
```

Run the pypi repo with the necessary options
```
# pypi-server -i 10.1.164.207 -p 8080 packages
```