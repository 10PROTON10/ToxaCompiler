; ModuleID = "my_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = bitcast [4 x i8]* @"fmt_str_int" to i8*
  %".3" = bitcast [4 x i8]* @"fmt_str_float" to i8*
  %".4" = mul i32 2, 2
  %".5" = add i32 2, %".4"
  %".6" = add i32 %".5", 2
  %"c" = alloca i32
  store i32 %".6", i32* %"c"
  %"g" = alloca float
  store float 0x4041c00000000000, float* %"g"
  %".9" = load i32, i32* %"c"
  %".10" = sitofp i32 %".9" to float
  %".11" = fcmp ogt float %".10", 0x4025000000000000
  br i1 %".11", label %"if_body", label %"else_body"
if_body:
  %".13" = load i32, i32* %"c"
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".13")
  br label %"after_if_else"
else_body:
  %"b" = alloca float
  store float 0x40249999a0000000, float* %"b"
  %".17" = load float, float* %"b"
  %".18" = fpext float %".17" to double
  %".19" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".18")
  br label %"after_if_else"
after_if_else:
  ret void
}

@"fmt_str_int" = global [4 x i8] c"%d\0a\00"
@"fmt_str_float" = global [4 x i8] c"%f\0a\00"
declare i32 @"printf"(i8* %".1", ...)
