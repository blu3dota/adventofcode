import os
import math

VERSION_LENGTH = 3 # length in bits
TYPE_ID_LENGTH = 3 # length in bits
LENGTH_TYPEID_LENGTH = 1 # length in bits
GROUP_LEN = 5 # length in bits

TYPE_ID_LITERAL = 4

LENGTH_TYPEID_TOTAL_IN_BITS = 0
LENGTH_TYPEID_TOTAL_IN_BITS_LEN = 15

LENGTH_TYPEID_NUMBER_OF_PACKETS = 1
LENGTH_TYPEID_NUMBER_OF_PACKETS_LEN = 11

class Packet:
    def __init__(self, version, typeid):
        self.version = version
        self.typeid = typeid

    def __str__(self):
        return f"Packet(version: {self.version}, typeid: {self.typeid})"

class LiteralPacket(Packet):
    def __init__(self, version, typeid, groups):
        Packet.__init__(self, version, typeid)
        self.groups = groups

        print(f"Read LiteralPacket(Version:{self.version} TypeID:{self.typeid} Value: {self.value()})")

    def __str__(self):
        return f"Packet(version: {self.version}, typeid: {self.typeid}(literal), groups: {self.groups}, value: {self.value()})"

    def value(self):
        binary_value = ""
        for group in self.groups:
            binary_value += group[1:]
        return int(binary_value, 2)

class OperatorPacket(Packet):
    def __init__(self, version, typeid, lengthtypeid, length, sub_packets):
        Packet.__init__(self, version, typeid)
        self.sub_packets = sub_packets
        self.lengthtypeid = lengthtypeid
        self.length = length

        print(f"Read OperatorPacket(Version:{self.version} TypeID:{self.typeid} LengthTypeID: {self.lengthtypeid} Length: {int(self.length, 2)} SubPackets: {len(sub_packets) if sub_packets is not None else 0})")

class Context:
    def __init__(self):
        self.pointer = 0

def main():
    filepath = os.path.join(os.getcwd(), "sample.txt")
    with open(filepath) as file:
        for line in file.read().splitlines():
            packet = parse(hex_to_bin(line))
            print(packet)
    print(version_sum)

def hex_to_bin(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)

def read_version(data, context):
    pos = context.pointer
    context.pointer += VERSION_LENGTH
    return data[pos:pos+VERSION_LENGTH]

def read_typeid(data, context):
    pos = context.pointer
    context.pointer += TYPE_ID_LENGTH
    return data[pos:pos+TYPE_ID_LENGTH]

def read_length_typeid(data, context):
    pos = context.pointer
    context.pointer += LENGTH_TYPEID_LENGTH
    return data[pos:pos+LENGTH_TYPEID_LENGTH]

def read_length(data, type, context):
    pos = context.pointer
    if int(type) == LENGTH_TYPEID_TOTAL_IN_BITS:
        context.pointer += LENGTH_TYPEID_TOTAL_IN_BITS_LEN
        return data[pos:pos+LENGTH_TYPEID_TOTAL_IN_BITS_LEN]
    elif int(type) == LENGTH_TYPEID_NUMBER_OF_PACKETS:
        context.pointer += LENGTH_TYPEID_NUMBER_OF_PACKETS_LEN
        return data[pos:pos+LENGTH_TYPEID_NUMBER_OF_PACKETS_LEN]
    else:
        print("Unknown length_typeid: ", type)

def read_groups(data, context):
    groups = []
    start = context.pointer
    while True:
        groups.append(data[start:start + GROUP_LEN])
        start += GROUP_LEN
        if groups[-1][0] == "0":
            break
    context.pointer = start
    return groups

def read_subpackets(data, context, length_typeid, length):
    packets = []
    remaining_length = length
    if int(length_typeid) == LENGTH_TYPEID_TOTAL_IN_BITS:
        while remaining_length > 0:
            read_context, read_packet = parse(data, context.pointer)
            packets.append(read_packet)
            read_bits = read_context.pointer - context.pointer
            remaining_length -= read_bits
            context.pointer += read_bits
        return packets
    elif int(length_typeid) == LENGTH_TYPEID_NUMBER_OF_PACKETS:
        while remaining_length > 0:
            read_context, read_packet = parse(data, context.pointer)
            packets.append(read_packet)
            read_bits = read_context.pointer - context.pointer
            remaining_length -= 1
            context.pointer += read_bits
        return packets

version_sum = 0

def parse(packet_binary, offset=0):
    global version_sum
    print(f"Parsing Packet(Offset{offset}) {packet_binary[offset:]}")
    context = Context()
    context.pointer = offset
    version = read_version(packet_binary, context)
    version_sum += int(version, 2)
    typeid = read_typeid(packet_binary, context)

    if int(typeid, 2) == TYPE_ID_LITERAL:
        groups = read_groups(packet_binary, context)
        return (context, LiteralPacket(version, typeid, groups))

    else:
        length_typeid = read_length_typeid(packet_binary, context)
        length = read_length(packet_binary, length_typeid, context)
        subpackets = read_subpackets(packet_binary, context, length_typeid, int(length, 2))
        return (context, OperatorPacket(version, typeid, length_typeid, length, subpackets))

if __name__ == "__main__":
    main()