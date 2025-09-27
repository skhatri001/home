import spidev

bus = 0						#Select SPI bus 0
device_cs = 0				#CS pin. Select 0 or 1, depending on the connection to the RPi
spi = spidev.SpiDev()		# Enable SPI
spi.open(bus, device_cs)	#Open connection to the device
spi.max_speed_hz = 500000
spi.mode = 0


#Send a byte
data_tx = [0x76]
spi.xfer2(data_tx)

#Send and receive a byte
data_tx = [0x00]
data_rx = spi.xfer2(data_tx)


#Send and receive bytes
data_tx = [0x24, 0x33, 0x18]
data_rx = spi.xfer2(data_tx)
if (data_rx[0] == 0x11):
	print('Received')
