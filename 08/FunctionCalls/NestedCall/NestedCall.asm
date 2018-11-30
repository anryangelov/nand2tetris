
@256
D=A
@SP
M=D
@Sys.init
0;JMP
// function Sys.init 0
(Sys.init)

// push constant 4000	
    @4000
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
    
// push constant 5000
    @5000
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
    
// call Sys.main 0
// save return address

    @return_Sys.main0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @5
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Sys.main
    0;JMP

(return_Sys.main0)

// pop temp 1
    @SP
    A=M-1
    D=M
    
    @6
    M=D
    
    @SP
    M=M-1
    
// label LOOP
(LOOP)

// goto LOOP
    @LOOP
    0;JMP

// function Sys.main 5
(Sys.main)

    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
    @0
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// push constant 4001
    @4001
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
    
// push constant 5001
    @5001
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
    
// push constant 200
    @200
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop local 1
    @1
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

// push constant 40
    @40
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop local 2
    @2
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

// push constant 6
    @6
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// pop local 3
    @3
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

// push constant 123
    @123
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// call Sys.add12 1
// save return address

    @return_Sys.add121
    D=A

    @SP
    A=M
    M=D

    @SP
    M=M+1
    
// save LCL

    @LCL  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save ARG

    @ARG  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THIS

    @THIS  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
// save THAT

    @THAT  // THAT or THIS
    D=M
    
    @SP
    A=M
    M=D  // copy pointer value in the stack
    
    @SP
    M=M+1 // move stack pointer
    
    // reposition ARG
    @SP
    D=M
    @6
    D=D-A
    @ARG
    M=D
    // reposition LCL
    @SP
    D=M
    @LCL
    M=D
    
    @Sys.add12
    0;JMP

(return_Sys.add121)

// pop temp 0
    @SP
    A=M-1
    D=M
    
    @5
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
    
// push local 1
    @1
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push local 2
    @2
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push local 3
    @3
    D=A
    @LCL
    A=D+M  // pointer to value
    D=M  // real value
    
    @SP
    A=M
    M=D  // copy value in stack
    
    @SP
    M=M+1 // move stack pointer
    
// push local 4
    @4
    D=A
    @LCL
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
    
// return
    // R13 (temp var) = LCL
    @LCL
    D=M
    @R13
    M=D
    // R14 (temp var) = retAddr
    @5
    A=D-A
    D=M
    @R14
    M=D
    // reposition return value for caller
    @SP
    A=M-1
    D=M
    @ARG
    A=M
    M=D
    // restore the caller's SP
    @ARG
    D=M+1
    @SP
    M=D
    // restore the caller's THAT
    @R13
    AM=M-1
    D=M
    @THAT
    M=D
    // restore the caller's THIS
    @R13
    AM=M-1
    D=M
    @THIS
    M=D
    // restore the caller's ARG
    @R13
    AM=M-1
    D=M
    @ARG
    M=D
    // restore the caller's LCL
    @R13
    AM=M-1
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;JMP
    
// function Sys.add12 0
(Sys.add12)

// push constant 4002
    @4002
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
    
// push constant 5002
    @5002
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
    
// push constant 12
    @12
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
    
// return
    // R13 (temp var) = LCL
    @LCL
    D=M
    @R13
    M=D
    // R14 (temp var) = retAddr
    @5
    A=D-A
    D=M
    @R14
    M=D
    // reposition return value for caller
    @SP
    A=M-1
    D=M
    @ARG
    A=M
    M=D
    // restore the caller's SP
    @ARG
    D=M+1
    @SP
    M=D
    // restore the caller's THAT
    @R13
    AM=M-1
    D=M
    @THAT
    M=D
    // restore the caller's THIS
    @R13
    AM=M-1
    D=M
    @THIS
    M=D
    // restore the caller's ARG
    @R13
    AM=M-1
    D=M
    @ARG
    M=D
    // restore the caller's LCL
    @R13
    AM=M-1
    D=M
    @LCL
    M=D
    @R14
    A=M
    0;JMP
    