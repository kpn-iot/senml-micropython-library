from senml_pack import SenmlPack
from senml_record import SenmlRecord
import utime as time


pack = SenmlPack("device_name")

while True:
    with SenmlRecord("test", value="working") as rec:           # use a with statement to automatically remove the item from the list when it goes out of scope
        pack.append(rec)
        print(pack.to_json())
    time.sleep(1)

