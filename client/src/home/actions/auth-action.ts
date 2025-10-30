import { type ActionFunctionArgs } from "react-router-dom";
import api from "../../api/axios";
import handleAxiosError from "../../api/axios-error-handler";
import isEmpty, { isNotEqual } from "../../utils/validation";
import User from "../../models/user.model";

export async function action({ request }: ActionFunctionArgs) {
  const model = new User();
  const url = new URL(request.url);
  const data = await request.formData();
  const entries = Object.fromEntries(data.entries()) as Record<string, any>;

  model.mode = url.searchParams.get("mode") ?? "";
  model.firstName = entries.firstName;
  model.lastName = entries.lastName;
  model.email = entries.email;
  model.password = entries.password;
  model.newPassword = entries["new-password"];
  model.otp = entries.otp;

  if (
    model.mode !== "register" &&
    model.mode !== "login" &&
    model.mode !== "forget-password" &&
    model.mode !== "reset-password"
  ) {
    return {
      success: false,
      message: "در حال حاضر امکان احراز هویت برای کاربر فراهم نیست",
    };
  }

  if (model.mode === "register") {
    if (isEmpty(model.firstName)) {
      return { success: false, message: "لطفا نام خود را وارد کنید" };
    }
    if (isEmpty(model.lastName)) {
      return { success: false, message: "لطفا نام‌خانوادگی خود را وارد کنید" };
    }
    if (isEmpty(model.email)) {
      return { success: false, message: "لطفا ایمیل خود را وارد کنید" };
    }
    if (isEmpty(model.password)) {
      return { success: false, message: "لطفا رمزعبور خود را وارد کنید" };
    }
    if (isEmpty(entries["re-password"])) {
      return { success: false, message: "لطفا تکرار رمزعبور خود را وارد کنید" };
    }
    if (isNotEqual(model.password, entries["re-password"])) {
      return { success: false, message: "رمزعبور و تکرار آن باید یکسان باشد" };
    }
  }

  if (model.mode === "login") {
    if (isEmpty(model.email)) {
      return { success: false, message: "لطفا ایمیل خود را وارد کنید" };
    }
    if (isEmpty(model.password)) {
      return { success: false, message: "لطفا رمزعبور خود را وارد کنید" };
    }
  }

  if (model.mode === "reset-password") {
    if (data.get("sendOtp") === "sendOtp") {
      model.mode = "forgot-password";
      if (isEmpty(model.email)) {
        return { success: false, message: "لطفا آدرس ایمیل را وارد کنید" };
      }
    } else {
      model.mode = "reset-password";
      if (
        isEmpty(model.email) ||
        isEmpty(model.newPassword) ||
        isEmpty(entries["re-new-password"]) ||
        isEmpty(model.otp)
      ) {
        return {
          success: false,
          message: "لطفا تمام مقادیر ورودی را وارد کنید",
        };
      }
      if (isNotEqual(model.newPassword, entries["re-new-password"])) {
        return {
          success: false,
          message: "مقدار رمزعبور و تکرار آن باید یکسان باشد",
        };
      }
      if (model.otp.toString().length > 6) {
        return {
          success: false,
          message: "کد امنیتی نمیتواند بیشتر از شش رقم باشد",
        };
      }
    }
  }

  try {
    if (
      model.mode === "login" ||
      model.mode === "register" ||
      model.mode === "forgot-password"
    ) {
      const response = await api.post(
        `/auth/${model.mode}/`,
        model.toServer(),
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      if (model.mode === "login") {
        const expiration = new Date();
        expiration.setMinutes(expiration.getMinutes() + 5);
        localStorage.setItem("accessToken", response.data.access);
        localStorage.setItem("expiration", expiration.toString());
      }

      return {
        mode: model.mode,
        success: response.status === 201 || response.status === 200,
        data: response.data || null,
      };
    }

    if (model.mode === "reset-password") {
      const verifyOtpResponse = await api.post(
        `/auth/verify-otp/`,
        { email: model.email, otp: model.otp },
        {
          headers: { "Content-Type": "application/json" },
          withCredentials: true,
        }
      );
      if (verifyOtpResponse.status === 200) {
        const resetPasswordResponse = await api.post(
          `/auth/reset-password/`,
          model.toServer(),
          {
            headers: { "Content-Type": "application/json" },
            withCredentials: true,
          }
        );

        return {
          mode: model.mode,
          success: resetPasswordResponse.status === 200,
        };
      }
    }
  } catch (error) {
    return handleAxiosError(error);
  }
}
