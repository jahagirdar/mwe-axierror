
VERILOG_SOURCES+=./tb_top.v
TOPLEVEL=tb_top
MODULE=test_module
default:
	$(MAKE) sim

include $(shell cocotb-config --makefiles)/Makefile.sim
