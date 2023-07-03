module tb_top(
// AXI4 Bus side signals
	output wire [31:0] awaddr,
	output wire [7:0] awlen,
	output wire [2:0] awsize,
	output wire [1:0] awburst,
	output wire awlock,
	output wire [3:0] awcache,
	output wire [2:0] awprot,
	output wire awvalid,
	input  wire awready,
	output reg  [63:0] wdata,
	output reg [7:0] wstrb,
	output wire wlast,
	output reg wvalid,
	input  wire wready,

	input wire [1:0] bresp,
	input wire bvalid,
	output wire bready,


	output wire [31:0] araddr,
	output wire [7:0]  arlen,
	output wire [2:0]  arsize,
	output wire [1:0]  arburst,
	output wire        arlock,
	output wire [3:0]  arcache,
	output wire [2:0]  arprot,
	output wire         arvalid,
	input  wire        arready,
	input  wire [63:0] rdata,
	input  wire [1:0]  rresp,
	input  wire        rlast,
	input  wire        rvalid,
	output wire        rready,
	// ID Signals
 //output wire [1:0] awid,
 //output wire [1:0] arid,
 //input wire [1:0] bid,
 //input wire [1:0] rid,

	input wire clk,
	input wire rst_n
);
endmodule
