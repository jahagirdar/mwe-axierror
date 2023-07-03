import cocotb
import os
from cocotbext.axi import AxiBus, AxiSlave, MemoryRegion
from cocotb.handle import Force, Release
from cocotb.triggers import Timer, Lock, RisingEdge, Event
from cocotb_bus.drivers import BusDriver
from cocotb_coverage.coverage import CoverPoint, CoverCross, coverage_db
import random


def match_rd_sb(actual, rd_sb):
    cocotb.log.info("match_rd_sb called")
    expected = rd_sb.pop(0)
    assert hex(actual) == hex(
        expected), "Error: Read Data did not match data from axi"


@cocotb.test()
async def test_hyperbu(dut):
    cocotb.log.info("Hyperbus test env")
    sb = []
    rd_sb = []
    mmio = MMIO(rd_sb)
    axi_slave = AxiSlave(AxiBus.from_prefix(dut, ""), clock=dut.clk,
                         reset=dut.rst_n, target=mmio, reset_active_level=False)
    # dut.o_csn0.value=Force(0)
    await Timer(1, "us")


class MMIO:
    def __init__(self, rd_sb):
        self.rd_sb = rd_sb
        self.ev_axi = Event()

    def sb_match(self, address, length, data, isWrite):
        self.ev_axi.set({'address': address, 'length': length,
                        'data': data, 'isWrite': isWrite})

    async def read(self, address, length):
        cocotb.log.info(f"Reading {address}, {length}")
        rv = random.randint(0, 0xffffffff)
        self.sb_match(address, length, rv, False)
        self.rd_sb.append(rv)
        cocotb.log.info(f"rdsb is now {self.rd_sb}")
        return rv.to_bytes(4, "little")

    async def write(self, address, data):
        self.sb_match(address, 4, data, True)
        cocotb.log.info(f"Writing {address} {data}")
        pass
