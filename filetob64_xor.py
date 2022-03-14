import base64
import sys
from io import BytesIO
xor_key = 0x42

bio = BytesIO()
bio.write(b'ascdf')
bio.getvalue()


def encode(infile, key, outfile, chunk_size=8192):
    chunk_size -= chunk_size % 3
    with open(infile, 'rb') as fin, open(outfile, 'wb') as fout:
        while True:
            bin_data = bytearray(fin.read(chunk_size))
            if not bin_data:
                break
            for i in range(len(bin_data)):
                bin_data[i] ^= key
            # print 'bin %s data len: %d' % (type(bin_data), len(bin_data))
            b64_data = base64.b64encode(bin_data)
            # print 'b64 %s data len: %d' % (type(b64_data), len(b64_data))
            fout.write(b64_data)


def decode(infile, key, outfile, chunk_size=8192):
    chunk_size -= chunk_size % 4
    with open(infile, 'rb') as fin, open(outfile, 'wb') as fout:
        while True:
            b64_data = bytearray(fin.read(chunk_size))
            if not b64_data:
                break
            # print 'bin %s data len: %d' % (type(bin_data), len(bin_data))
            bin_data = bytearray(base64.b64decode(b64_data))
            for i in range(len(bin_data)):
                bin_data[i] ^= key
            # print 'b64 %s data len: %d' % (type(b64_data), len(b64_data))
            fout.write(bin_data)
    pass

if __name__ == '__main__':

    mode = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]
    if len(sys.argv) < 4:
        print('param error')
    if mode == 'encode':
        encode(infile, xor_key, outfile)
    elif mode == 'decode':
        decode(infile, xor_key, outfile)
    else:
        print('invalid mode')

    pass
