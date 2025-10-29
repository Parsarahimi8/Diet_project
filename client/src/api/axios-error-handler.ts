import type { AxiosError } from "axios";

export default function handleAxiosError(error: unknown) {
  const err = error as AxiosError<{
    email?: string[];
    non_field_errors?: string[];
    error?: string[];
    message?: string;
    code?: string;
  }>;
  if (err.code === "ERR_NETWORK") {
    return { success: false, message: "خطای شبکه" };
  }
  if (err.status === 404) {
    if (err.response?.data?.error?.includes("User not found")) {
      return {
        success: false,
        message: "کاربری با ایمیل وارد شده، وجود ندارد",
      };
    }
  }
  if (err.status === 400) {
    if (err.response?.data?.email?.some((e) => e.includes("already exists"))) {
      return {
        success: false,
        message:
          "ایمیل وارد شده قبلاً ثبت شده است. لطفاً ایمیل دیگری را وارد کنید",
      };
    }
    if (
      err.response?.data?.non_field_errors?.some((e) =>
        e.includes("Invalid credentials")
      )
    ) {
      return {
        success: false,
        message: "آدرس ایمیل یا رمزعبور شما اشتباه است",
      };
    }
    if (err.response?.data?.error?.includes("Invalid or expired OTP")) {
      return {
        success: false,
        message: "کد امنیتی اشتباه یا منقضی شده است",
      };
    }
  }
  return { success: false, message: "خطای شناخته نشده" };
}
