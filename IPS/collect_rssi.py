import rssi
import time
import sys

count = 0
#interface = 'wlp3s0'
interface = 'wlan0'
addrs = {
    '00:11:32:9D:2B:30':0,
    '00:11:32:AD:8E:B7':1,
    '00:11:32:9D:30:3A':2,
    '00:11:32:AD:8C:82':3,
    '00:11:32:9D:2B:31':4,
    '00:11:32:AD:8E:B8':5,
    '00:11:32:9D:30:3B':6,
    '00:11:32:AD:8C:83':7,
}

ssid = ['ntuiot_402']

if __name__ == '__main__':

    try:
        x = sys.argv[1]
        y = sys.argv[2]
        print(f"Reading args, x={x}, y={y}...")
    except:
        print("Error: You must specify x and y")

    myrssi = rssi.RSSI_Scan(interface)
    
    filename = 'rssi'+x+'_'+y+'.csv'
    fp = open(filename,'w')

    while count < 10:
        ap_infos = myrssi.getAPinfo(ssid)
        data = ["","","","","","","",""]

        for ap in ap_infos:
            data[addrs[ap['mac']]] = str(ap['signal'])
    
        out = ",".join(data) + "\n" 
        
        if not "" in data:
            count += 1
            print(out)
            fp.write(out)

        time.sleep(1)
