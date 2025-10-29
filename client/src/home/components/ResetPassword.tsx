import { useContext, useEffect, useState } from "react";
import Modal, { type ModalContentConfig } from "../../base/Modal";
import UserProgressContext from "../../store/userProgressContext";
import {
  Form,
  useActionData,
  useNavigate,
  useNavigation,
  useSearchParams,
} from "react-router-dom";
import EmailBox from "../../base/EmailBox";
import NumberBox from "../../base/NumberBox";
import Button from "../../base/Button";
import PasswordBox from "../../base/PasswordBox";
import { toast } from "react-toastify";
import Timer from "../../base/Timer";

const resetPasswordModalConfig: ModalContentConfig = {
  imageUrl: "/images/login-image.png",
  headline: "تغییر رمز عبور",
  title: "ببینم بلدی یه رمزی بذاری که فراموش نکنی :)",
  footerText: "رمزعبور یادت اومد؟",
  footerActionText: "ورود",
};

const ResetPassword = () => {
  const navigate = useNavigate();
  const navigation = useNavigation();
  const { progress, setProgress } = useContext(UserProgressContext);
  const [searchParams] = useSearchParams();
  const [timer, setTimer] = useState(
    localStorage.getItem("otpTimer") ? true : false
  );
  const res = useActionData();
  const isSubmitting = navigation.state === "submitting";
  useEffect(() => {
    if (searchParams.get("mode") === "reset-password") {
      if (!!res && !!res.success) {
        if (res.mode === "forgot-password") {
          setTimer(true);
          const expireTime = Date.now() + 2 * 60 * 1000;
          localStorage.setItem("otpTimer", expireTime.toString());
          toast.success("کد امنیتی به ایمیل شما ارسال شد");
        } else if (res.mode === "reset-password") {
          setProgress("login");
          navigate("?mode=login");
          toast.success("رمزعبور شما با موفقیت تغییر پیدا کرد");
        }
      } else if (!!res && !res.success) {
        toast.error(res.message);
      }
    }
  }, [res, progress, setProgress, navigate, searchParams]);

  function onFinishTime() {
    setTimer(false);
  }
  return (
    <Modal
      open={progress === "reset-password"}
      onClose={
        progress === "reset-password" ? () => setProgress("") : undefined
      }
      config={{
        ...resetPasswordModalConfig,
        onFooterActionTextClick: () => setProgress("login"),
      }}
    >
      <Form method="post" className="flex flex-col gap-3 my-4 w-full">
        <EmailBox placeHolder="ایمیل" name="email" />
        <PasswordBox placeHolder="رمز عبور جدید" name="new-password" />
        <PasswordBox placeHolder="تکرار رمز عبور جدید" name="re-new-password" />
        <div className="flex flex-row items-center w-full gap-2">
          <div className="flex-grow">
            <NumberBox placeHolder="کد امنیتی" name="otp" />
          </div>
          {!timer && (
            <Button
              name="sendOtp"
              value="sendOtp"
              classes="btn !text-[12px] !rounded-md !px-4 !py-3"
              title="ارسال کد"
              disable={isSubmitting}
            />
          )}
          {timer && <Timer initialTime={120} onFinish={onFinishTime} />}
        </div>
        <Button
          classes="btn btn-gradient !rounded-md mx-1 mt-2"
          title={`${
            !!timer && isSubmitting ? "در حال تغییر رمزعبور..." : "ثبت"
          }`}
          disable={isSubmitting}
        />
      </Form>
    </Modal>
  );
};

export default ResetPassword;
