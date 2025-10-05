#from smbus2 import SMBus, i2c_msg
import smbus
import time
from smbus2 import SMBus
I2C_BUS = 1 # bus number
device_address = 0x40 # After checking i2cdetect -y -1
current_address = 0x01 # Current register address
voltage_address = 0x02 # Voltage register address
power_address = 0x03 # Power register address
current_LSB_A = 1.25e-3 # 1.25mA per LSB
voltage_LSB_V = 1.25e-3 # 1.25mV per LSB
#bus.write_word_data(0x40,0x00,0x2761)

def read_be16_signed(bus,addr,reg):
    #Read a 16-bit word and swap byte order (SMBus returns LSB first)
    raw = bus.read_word_data(addr,reg)
    raw = ((raw&0xFF)<<8) | (raw>>8) #swap
    #Convert to signed 16-bit
    if raw & 0x8000:
        raw -=1<<16
    return raw

with SMBus(I2C_BUS) as bus:
    bus.write_word_data(device_address,0x00,0x0766)
    raw_counts = read_be16_signed(bus,device_address,current_address)
    current_A = raw_counts*current_LSB_A
    v_raw = bus.read_word_data(device_address,voltage_address)
    v_raw = ((v_raw & 0xFF) << 8) | (v_raw >> 8)
    voltage_v = v_raw * voltage_LSB_V
    print(f"Raw counts: {raw_counts}, Current: {current_A:.4f} A")
    print(f"Raw counts: {v_raw}, Voltage: {voltage_v:.2f} V")

#data = bus.read_byte_data(device_address,voltage_address)
#print(f"Data read: {data}")
#msg = i2c_msg.write(0x00,[0x61,0x27])
#data = i2c_msg.write(0x8B,[])# Reading bus voltage 10001011
#print(f"Data read: {data}")
#msg2 = i2c_msg.read(0x8B,1)
#bus.i2c_rdwr(msg2)
#data = list(msg2)
#print(data)
#bus.i2c_rdwr(msg2)
#print(msg)



