
@256
D=A
@SP
M=D
// push constant 10
    @10
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 11
    @11
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 12
    @12
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 12
    @12
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// eq
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE0
    D;JEQ
    D=0
    @FALSE0
    0;JMP
(TRUE0)
    D=-1
(FALSE0)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// eq
    @SP
    A=M-1 // address of second operand
    D=M  // value of second operand

    A=A-1  // address of first operand

    D=M-D

    
    @TRUE1
    D;JEQ
    D=0
    @FALSE1
    0;JMP
(TRUE1)
    D=-1
(FALSE1)


    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
