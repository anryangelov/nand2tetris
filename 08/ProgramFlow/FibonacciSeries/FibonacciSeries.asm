
@256
D=A
@SP
M=D
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
    
// pop pointer 1           
    @SP
    A=M-1
    D=M
    
    @4
    M=D
    
    @SP
    M=M-1
    
// push constant 0
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop that 0              
    @0
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

// push constant 1
    @1
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop that 1              
    @1
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

// push argument 0
    @0
    D=A
    @ARG
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push constant 2
    @2
    D=A

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
    
// pop argument 0          
    @0
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

// label MAIN_LOOP_START
(MAIN_LOOP_START)

// push argument 0
    @0
    D=A
    @ARG
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// if-goto COMPUTE_ELEMENT 
    @SP
    AM=M-1
    D=M
    @COMPUTE_ELEMENT
    D;JNE

// goto END_PROGRAM        
    @END_PROGRAM
    0;JMP

// label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)

// push that 0
    @0
    D=A
    @THAT
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push that 1
    @1
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

// push pointer 1
    @4  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// push constant 1
    @1
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

    D=M+D

    

    @SP
    AM=M-1  // reposition SP and save in register as well
    A=A-1   // get address where to save result
    M=D  // save result in stack on position of first operand
    
// pop pointer 1           
    @SP
    A=M-1
    D=M
    
    @4
    M=D
    
    @SP
    M=M-1
    
// push argument 0
    @0
    D=A
    @ARG
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push constant 1
    @1
    D=A

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
    
// pop argument 0          
    @0
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

// goto MAIN_LOOP_START
    @MAIN_LOOP_START
    0;JMP

// label END_PROGRAM
(END_PROGRAM)

(INFINITE_LOOP)
   @INFINITE_LOOP
   0;JMP
