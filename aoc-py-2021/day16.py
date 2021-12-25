from functools import reduce
packet = open('day16.txt').read()

## part 1
def hex_to_bin(hexstr): return bin(int(hexstr,16))[2:].zfill(len(hexstr)*4)
def bin_to_int(binstr): return int(binstr,2)

def parse_literal(binp):
  # print('lit',binp)
  contents = binp[6:]
  res = []
  for i in range(0,len(contents),5):
    keep_going,*bit4 = contents[i:i+5]
    if keep_going == '0':
      res.extend(bit4)
      break
    res.extend(bit4)
  num = bin_to_int("".join(res))
  bits_processed = len(res) + len(res) // 4
  # trailing zeroes after final literal nibble
  rest_packets = contents[bits_processed:]
  return parse(rest_packets)

def parse(binp):
  # print('bin={}|nbits={}|npkts={}'.format(binp,bits,npackets))
  if len(binp) < 6 or all(b == '0' for b in binp):
    return 0
  v, typeid = bin_to_int(binp[0:3]), bin_to_int(binp[3:6])
  # print('version',v,'typeid',typeid,binp)
  if typeid == 4:
    # identify end of literal packet by the block of 5 starting w/ '0'
    return v + parse_literal(binp)
  else:
    tlv,totalbits,totalsubp = binp[6], binp[7:22], binp[7:18]
    if tlv == '0':
      bitlen = bin_to_int(totalbits)
      # print('b',bitlen)
      packets, rest = binp[22:bitlen+22], binp[bitlen+22:]
      #parse while not all bits read
      return v + parse(packets) + parse(rest)
    elif tlv == '1':
      npackets = bin_to_int(totalsubp)
      # print('n',npackets)
      packets = binp[18:]
      # parse while not all subp read
      return v + parse(packets)
    else:
      raise ValueError('unknown tlv={}'.format(tlv))

def parse_packet(packet): 
  binary_packet = hex_to_bin(packet)
  return parse(binary_packet)

print(parse_packet(packet))

## part 2
def parse_literal(binp):
  contents = binp[6:]
  res = []
  for i in range(0,len(contents),5):
    keep_going,*bit4 = contents[i:i+5]
    if keep_going == '0':
      res.extend(bit4)
      break
    res.extend(bit4)
  num = bin_to_int("".join(res))
  bits_processed = len(res) + len(res) // 4 + 6 # header
  return num,bits_processed

def parse(binp):
  if len(binp) < 6 or all(b == '0' for b in binp):
    return [None,None]
  _, typeid = bin_to_int(binp[0:3]), bin_to_int(binp[3:6])
  if typeid == 4:
    return parse_literal(binp)
  else:
    tlv,totalbits,totalsubp = binp[6], binp[7:22], binp[7:18]
    def prod(*args): return reduce(lambda a,b: a*b,args)
    def  sum(*args): return reduce(lambda a,b: a+b,args)
    oper = {0:sum,1:prod,2:lambda *a:min(a),3:lambda *a: max(a),
            5:lambda a,b:  1 if a > b else 0,
            6:lambda a,b:  1 if a < b else 0,
            7:lambda a,b:  1 if a == b else 0}

    op = oper[typeid]

    if tlv == '0':
      subps = []
      total_bits = bits_remaining = bin_to_int(totalbits)
      packets = binp[22:]
      while bits_remaining:
        lit,processed = parse(packets)
        bits_remaining -= processed
        packets = packets[processed:]
        subps.append(lit)
      return op(*(s for s in subps if s is not None)),total_bits + 22
    else:
      subps = []
      npackets = bin_to_int(totalsubp)
      packets = binp[18:]
      bits_processed = 18
      while len(subps) < npackets:
        lit, processed = parse(packets)
        packets = packets[processed:]
        bits_processed += processed
        subps.append(lit)
      return op(*(s for s in subps if s is not None)),bits_processed
 
def parse_packet(packet): 
  binary_packet = hex_to_bin(packet)
  num,bits_processed = parse(binary_packet)
  return num

print(parse_packet(packet))