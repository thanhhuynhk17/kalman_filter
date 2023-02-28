
from bleak import BleakScanner
import asyncio
import time
import numpy as np
from kalman import tracker_1st_order, predict_rssi

from constant import FNAME, BEACON, TIME_OUT
# init filter
tracker = tracker_1st_order(R=4**2, P=10**2, Q=0.1**2, X0=np.array([[-60,0]]))

def filter_device(device, advertising_data):
    if device.name==BEACON:
        tracker.predict()
        tracker.update(device.rssi)
        rssi_filter = tracker.x[0][0]
        # store data
        with open(FNAME,'a') as my_file:
            my_file.write(f'{device.rssi}, {rssi_filter}')
            my_file.write("\n")
        return True
    return False

async def scan_ble():
    count = 0
    while True:
        try:
            if(count==500):
                break
            device = await BleakScanner.find_device_by_filter(filter_device, timeout=TIME_OUT)
            count = count + 1
            print(device.name, device.rssi)
            # await asyncio.sleep(time_out)
        except AttributeError as err:
            count = count - 1
            print(f'{BEACON} not found!', count)
def main():
    with open(FNAME,'w') as my_file: # clear old data
        pass

    loop = asyncio.get_event_loop()
    try:
        print('looping...')
        asyncio.ensure_future(scan_ble())
        loop.run_forever()
    except KeyboardInterrupt:
        print('Interrupted')
        loop.stop()
    finally:
        print("Closing Loop")
        loop.close()

if __name__ == "__main__":
    main()