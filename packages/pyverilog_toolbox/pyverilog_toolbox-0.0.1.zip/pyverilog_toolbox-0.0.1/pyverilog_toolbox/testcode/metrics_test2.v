module TOP(CLK, RST, IN, IN2);
  input CLK, RST, IN, IN2;
  reg reg2;

  always @(posedge CLK or negedge RST) begin
    if(RST) begin
      reg2 <= 1'b0;
    end else if(IN2) begin
      reg2 <= IN;
    end else if(IN2) begin
      if(IN2) begin
        reg2 <= IN;
      end
    end else begin
      if(IN2) begin
        case(IN2)
          1'b0: reg2 <= IN;
          1'b1: reg2 <= IN;
        endcase
      end
    end
  end


endmodule

