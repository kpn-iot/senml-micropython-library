from kpn_senml import *
import utime as time
import ubinascii
import cbor_decoder

pack = SenmlPack("device_name")

while True:
    with SenmlRecord("test", value=10) as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope, generate a value for the record
        pack.add(rec)
        cbor_val = pack.to_cbor()
        print(cbor_val)
        print(ubinascii.hexlify(cbor_val))
        print(cbor_decoder.loads(cbor_val))                                          # convert to string again so we can print it.
    time.sleep(1)

