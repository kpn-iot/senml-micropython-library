from kpn_senml import *
import utime as time


pack = SenmlPack("device_name")
temp = SenmlRecord(SenmlNames.KPN_SENML_TEMPERATURE, unit=SenmlUnits.SENML_UNIT_DEGREES_CELSIUS, value=23.5)
door_pos = SenmlRecord("doorPos", update_time=20, value=True)
int_val = SenmlRecord("int_val", sum=100)

pack.add(temp)
pack.add(door_pos)
pack.add(int_val)

pack.base_time = time.time()
pack.base_value = 5
pack.base_sum = 50
time.sleep(2)
temp.time = time.time()    



print(pack.to_json())
