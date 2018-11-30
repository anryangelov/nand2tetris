
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
    
// pop local 0
    @0
    D=A
    @LCL
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

// push constant 21
    @21
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 22
    @22
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop argument 2
    @2
    D=A
    @ARG
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

// pop argument 1
    @1
    D=A
    @ARG
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

// push constant 36
    @36
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop this 6
    @6
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

// push constant 42
    @42
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 45
    @45
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop that 5
    @5
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

// pop that 2
    @2
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

// push constant 510
    @510
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop temp 6
    @SP
    A=M-1
    D=M
    
    @11
    M=D
    
    @SP
    M=M-1
    
// push local 0
    @0
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push that 5
    @5
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
    
// push argument 1
    @1
    D=A
    @ARG
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
    
// push this 6
    @6
    D=A
    @THIS
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push this 6
    @6
    D=A
    @THIS
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
    
// push temp 6
    @11  // THAT or THIS
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
    
(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
