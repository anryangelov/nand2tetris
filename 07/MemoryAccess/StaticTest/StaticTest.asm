
@256
D=A
@SP
M=D
// push constant 111
    @111
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 333
    @333
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 888
    @888
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop static 8
    @SP
    A=M-1
    D=M
    @StaticTest.8
    M=D
    @SP
    M=M-1
    
// pop static 3
    @SP
    A=M-1
    D=M
    @StaticTest.3
    M=D
    @SP
    M=M-1
    
// pop static 1
    @SP
    A=M-1
    D=M
    @StaticTest.1
    M=D
    @SP
    M=M-1
    
// push static 3
    @StaticTest.3
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
// push static 1
    @StaticTest.1
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    
// sub
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// push static 8
    @StaticTest.8
    D=M
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

    D=M+D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
