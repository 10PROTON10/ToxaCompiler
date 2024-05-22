; ModuleID = "my_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = bitcast [4 x i8]* @"fmt_str_int" to i8*
  %".3" = bitcast [4 x i8]* @"fmt_str_float" to i8*
  %"c" = alloca i32
  store i32 8, i32* %"c"
  %".5" = load i32, i32* %"c"
  %".6" = icmp sgt i32 %".5", 10
  br i1 %".6", label %"if_body", label %"else_body"
if_body:
  %".8" = load i32, i32* %"c"
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".2", i32 %".8")
  br label %"after_if_else"
else_body:
  %"b" = alloca float
  store float 0x404a266660000000, float* %"b"
  %".12" = load float, float* %"b"
  %".13" = fpext float %".12" to double
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".3", double %".13")
  br label %"after_if_else"
after_if_else:
  ret void
}

@"fmt_str_int" = global [4 x i8] c"%d\00a"
@"fmt_str_float" = global [4 x i8] c"%f\00a"
declare i32 @"printf"(i8* %".1", ...)
