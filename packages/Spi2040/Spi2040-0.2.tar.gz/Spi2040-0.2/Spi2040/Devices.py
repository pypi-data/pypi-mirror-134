from machine import SPI, Pin


class SpiDevice:
    def __init__(self, sck, copi, cipo, cs, jd):
        self.cs = Pin(cs, mode=Pin.OUT, value=1)
        self.js = Pin(jd, mode=Pin.IN)
        self.spi = SPI(0,
                       baudrate=10000000,
                       polarity=0,
                       phase=1,
                       bits=8,
                       firstbit=SPI.MSB,
                       sck=Pin(sck),
                       mosi=Pin(copi),
                       miso=Pin(cipo))

    def Send(self, bitstream):
        msg = bytearray()
        for i in range(7):
            msg.append(0x01)
        msg.extend(bitstream)
        self.cs(0)
        self.spi.write(msg)
        self.cs(1)

    def Receive(self):
        msg = bytearray()
        for i in range(8):
            msg.append(0x02)

        self.cs(0)
        self.spi.write(msg)
        data = self.spi.read(256)
        self.cs(1)
        return data
