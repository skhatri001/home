from smbus2 import SMBus, i2c_msg

bus = SMBus(1) # bus number
current_address = 0x01 # Current register address
voltage_address = 0x02 # Voltage register address
power_address = 0x03 # Power register address

msg = i2c_msg.write(0x00,[0x61,0x27])
#msg2 = i2c_msg.read(0x00,3)
#bus.i2c_rdwr(msg2)
#print(msg)


