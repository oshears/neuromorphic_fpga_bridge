import os
import mmap


mem_file = os.open("/dev/mem", os.O_SYNC | os.O_RDWR)
neuromorphic_bridge_axi_base_addr = 0x43C00000
neuromorphic_bridge_axi_addr_size = 0x10000
neuromorphic_bridge_registers = mmap.mmap(mem_file, neuromorphic_bridge_axi_addr_size, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, 0, neuromorphic_bridge_axi_base_addr) 

CHAR_SEL_REG = 0
NET_OUT_REG = 4
DBG_REG = 8

# Char Select Register
for i in range(16):
    neuromorphic_bridge_registers[CHAR_SEL_REG] = i
    print(neuromorphic_bridge_registers[CHAR_SEL_REG])
    print(f"Character Select Register: {neuromorphic_bridge_registers[CHAR_SEL_REG]}")

# Network Output Register
print(f"Network Output Register: {neuromorphic_bridge_registers[NET_OUT_REG]}")

# Debug Register
for i in range(16):
    neuromorphic_bridge_registers[DBG_REG] = i
    print(neuromorphic_bridge_registers[DBG_REG])
    print(f"Debug Register: {neuromorphic_bridge_registers[DBG_REG]}")