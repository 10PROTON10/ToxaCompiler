; ModuleID = "my_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = bitcast [3 x i8]* @"fmt_str" to i8*
  %"c" = alloca i32
  store i32 5, i32* %"c"
  br label %"loop_condition"
loop_condition:
  %".5" = load i32, i32* %"c"
  %".6" = icmp slt i32 %".5", 6
  br i1 %".6", label %"loop_body", label %"after_loop"
loop_body:
  %".8" = load i32, i32* %"c"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".8")
  br label %"loop_condition"
after_loop:
  ret void
}

@"fmt_str" = global [3 x i8] c"%d\0a"
declare i32 @"printf"(i8* %".1", ...)
