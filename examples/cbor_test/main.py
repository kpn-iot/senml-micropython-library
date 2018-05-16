# _  __  ____    _   _ 
# | |/ / |  _ \  | \ | |
# | ' /  | |_) | |  \| |
# | . \  |  __/  | |\  |
# |_|\_\ |_|     |_| \_|
# 
# (c) 2018 KPN
# License: MIT license.
# Author: Jan Bogaerts
# 
# cbor example

import cbor_encoder 
import cbor_decoder
import ubinascii

input = [{"bn":"urn:dev:ow:10e2073a01080063","u":"Cel","t":1.276020076e+09,"v":23.5},{"u":"Cel","t":1.276020091e+09,"v":23.6}]

data = cbor_encoder.dumps(input)
print(data)
print(ubinascii.hexlify(data))
text = cbor_decoder.loads(data)
print(text)