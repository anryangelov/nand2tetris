
@256
D=A
@SP
M=D
// push constant 7
    @7
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 8
    @8
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// add
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    AD=M+D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
