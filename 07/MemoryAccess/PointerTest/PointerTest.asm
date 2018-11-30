
@256
D=A
@SP
M=D
// push constant 3030
    @3030
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop pointer 0
    @SP
    A=M-1
    D=M
    
    @3
    M=D
    
    @SP
    M=M-1
    
// push constant 3040
    @3040
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop pointer 1
    @SP
    A=M-1
    D=M
    
    @4
    M=D
    
    @SP
    M=M-1
    
// push constant 32
    @32
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop this 2
    @2
    D=A
    @THIS
    D=D+M  // pointer to value
    
    @R13
    M=D

    @SP
    A=M-1  // address (pointer) of value
    D=M  // real value

    @R13
    A=M  // register D contain new address
    M=D

    @SP
    M=M-1

// push constant 46
    @46
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop that 6
    @6
    D=A
    @THAT
    D=D+M  // pointer to value
    
    @R13
    M=D

    @SP
    A=M-1  // address (pointer) of value
    D=M  // real value

    @R13
    A=M  // register D contain new address
    M=D

    @SP
    M=M-1

// push pointer 0
    @3  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// push pointer 1
    @4  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
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
    
// push this 2
    @2
    D=A
    @THIS
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
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
    
// push that 6
    @6
    D=A
    @THAT
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
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
