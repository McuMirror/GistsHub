import re

# Each line is 3 bytes of input and the observed 1-byte checksum
data="""\
10100001 10010011 01100011  => 01110111
10100001 10010011 01100100  => 01110001
10100001 10010011 01100101  => 01110000
10100001 10010011 01100110  => 01110010
10100001 10010011 01100111  => 01110011
10100001 10010011 01101000  => 01111001
10100001 10010011 01101001  => 01111000
10100001 10010011 01101010  => 01111010
10100001 10010011 01101011  => 01111011
10100001 10010011 01101100  => 01111110
10100001 10010011 01101101  => 01111111
10100001 10010011 01101110  => 01111100
10100001 10010011 01101111  => 01111101
10100001 10010011 01110001  => 01100100
10100001 10010011 01110010  => 01100110
10100001 10010011 01110011  => 01100111
10100001 10010011 01110100  => 01100001
10100001 10010011 01110101  => 01100000
10100001 10010011 01110111  => 01100011
10100001 10010011 01110111  => 01100011
10100001 10010011 01111000  => 01101001
10100001 10010011 01101000  => 01111001
10100001 00010011 01101000  => 11111001
10100001 00010011 01101100  => 11111110
10100001 10010011 01101100  => 01111110
10100001 10010100 01111110  => 01101011
10100001 10000010 01101100  => 01100000
10100001 10000001 01101100  => 01100011
10100001 10010011 01101100  => 01111110
10100001 10010000 01101100  => 01111100
10100001 10011000 01101100  => 01110100
10100001 10001000 01101100  => 01101100
10100001 10010000 01101100  => 01111100
10100001 10011000 01101100  => 01110100
10100010 00000010 11111111  => 01111110"""

# Reverse bits in 8-bit value
def bitreverse(x):
  return int('{:08b}'.format(x)[::-1], 2)

for line in data.split('\n'):
  # Create inbytes (byte values) and checksum (bit string) from input line
  inbits, checksum = line.split('  => ')
  inbytes = [int(x, 2) for x in inbits.split(' ')]

  # Compute the result checksum byte
  inbytes = map(bitreverse, inbytes)
  xorpart = (inbytes[0] ^ inbytes[1] ^ inbytes[2] ^ 0x4) & 0xf
  sumpart = (inbytes[0] >> 4) + (inbytes[1] >> 4) + (inbytes[2] >> 4) + (inbytes[2] & 1) + ((inbytes[1] >> 3) & 1) + 1
  sumpart = (-sumpart) & 0xf
  result = bitreverse((sumpart << 4) | xorpart)

  # Check the result and print
  if checksum != '{:08b}'.format(result): print '** ERROR **',
  print line, '{:08b}'.format(result)
