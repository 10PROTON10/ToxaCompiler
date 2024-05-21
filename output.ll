; ModuleID = "my_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = bitcast [5 x i8]* @"fmt_str" to i8*
  %"c" = alloca float
  store float 0x4097f399a0000000, float* %"c"
  br label %"loop_condition"
loop_condition:
  %".5" = load float, float* %"c"
  %".6" = fcmp ogt float %".5", 0x4090220000000000
  br i1 %".6", label %"loop_body", label %"after_loop"
loop_body:
  %".8" = load float, float* %"c"
  %".9" = fpext float %".8" to double
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".2", double %".9")
  %".11" = load float, float* %"c"
  %".12" = fsub float %".11", 0x407424ccc0000000
  store float %".12", float* %"c"
  br label %"loop_condition"
after_loop:
  ret void
}

@"fmt_str" = global [5 x i8] c"%.3f\0a"
declare i32 @"printf"(i8* %".1", ...)
