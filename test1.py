import serial

s_port = '/dev/ttyUSB3'
b_rate = 115200

#method for reading incoming bytes on serial
def read_serial(ser):
    buf = ''
    inp = ser.readall()
    print (inp,), inp.encode("hex") #gives me the correct bytes, each on a newline
    buf = buf + inp #accumalate the response
    return buf   

#open serial
ser = serial.Serial(
    port=s_port,
    baudrate=b_rate,
    timeout=1
)


command = '\xff\x55\x01\x06\x2a\xfe' #should come from user input
print ("TX: ", command)
ser.write(command)
rx = read_serial(ser)
print "RX: " + rx.encode("hex")

