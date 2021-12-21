# reproducers

- running a local proxy for testing purposes

Download the binaries for linux from mitmproxy.org
https://mitmproxy.org/downloads/
```
# wget https://snapshots.mitmproxy.org/7.0.4/mitmproxy-7.0.4-linux.tar.gz
# tar xf mitmproxy-7.0.4-linux.tar.gz
```

Configure a parser for the proxy or use the example config parse_headers.py
```
def response(flow):
    print("")
    print("="*50)
    #print("FOR: " + flow.request.url)
    print(flow.request.method + " " + flow.request.path + " " + flow.request.http_version)

    print("-"*50 + "request headers:")
    for k, v in flow.request.headers.items():
        print("%-20s: %s" % (k.upper(), v))

    print("-"*50 + "response headers:")
    for k, v in flow.response.headers.items():
        print("%-20s: %s" % (k.upper(), v))
```

Run the proxy on the CLI as follows:
```
# ./mitmdump -q -v -s parse_headers.py
```

On the terminal which requires the proxy, export the proxy variables:
```
# export https_proxy=localhost:8080 ; export http_proxy=localhost:8080 ; export HTTPS_PROXY=localhost:8080 ; export HTTP_PROXY=localhost:8080
```