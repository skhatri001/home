#from smbus2 import SMBus, i2c_msg
import smbus
bus = smbus.SMBus(1) # bus number
device_address = 0x40 # After checking i2cdetect -y -1
current_address = 0x01 # Current register address
voltage_address = 0x02 # Voltage register address
power_address = 0x03 # Power register address

bus.write_byte_data(0x40,0x00,0x6127)

#msg = i2c_msg.write(0x00,[0x61,0x27])
#data = i2c_msg.write(0x8B,[])# Reading bus voltage 10001011
#print(f"Data read: {data}")
#msg2 = i2c_msg.read(0x8B,1)
#bus.i2c_rdwr(msg2)
#data = list(msg2)
#print(data)
#bus.i2c_rdwr(msg2)
#print(msg)



