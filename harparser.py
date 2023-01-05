#!/usr/bin/env python3
import json
import urllib.parse
import base64
from lxml import etree
from pathlib import Path
import sys

"""Verify if required files and folders exist"""
def preliminary_checks():
    """Verify if the input file exists"""
    if len(sys.argv) != 2:
        print(f"No parameters provided. \nusage: harparser.py haranalysis.har")
        sys.exit(1)
    if sys.argv[1]:
        if (not Path(sys.argv[1]).is_file()):
            print(f"Unable to open find \{sys.argv[1]}' file on the current directory")
            sys.exit(1)

def harFileRead(inputFile):
    with open(sys.argv[1], 'r') as f:
        dataJson = json.load(f)
        dataEntries = dataJson['log']['entries']
    return dataEntries

def processHarData(harData):
    for info in harData:
        if not "/saml" in info['request']['url']:
            continue
        
        if "POST" in info['request']['method']:
            if 'postData' in info['request'].keys():
                SResponse_out = info['request']['postData']['text']
                print(f"""SAML Response: \n{SResponse_out}\n""")
                deflated_text = str(urllib.parse.unquote_plus(SResponse_out))
                spl_word = "&"
                deflated_text_cleanup = str([SAMLResponse for SAMLResponse in deflated_text.split(spl_word, 1) if "SAMLResponse" in SAMLResponse and "RelayState" not in SAMLResponse]).replace('SAMLResponse=', '')
                root = etree.fromstring(base64.b64decode(deflated_text_cleanup))
                print(etree.tostring(root, pretty_print=True).decode())
                continue
            
        if "GET" in info['request']['method']:
            for item in info['request']['queryString']:
                if "SAMLRequest" in item['name']:
                    SRequest_out = item['value']
                    print(f"""SAMLRequest: \n{SRequest_out}\n""")
            if "RelayState" in item['name']:
                    SRequest_out = item['value']
                    print(f"""RelayState: \n{SRequest_out}\n""")


if __name__ == "__main__":
    preliminary_checks()
    harData = harFileRead(sys.argv[1])
    processHarData(harData)