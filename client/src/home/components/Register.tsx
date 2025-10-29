import { useContext, useEffect } from "react";
import Modal, { type ModalContentConfig } from "../../base/Modal";
import UserProgressContext from "../../store/userProgressContext";
import PasswordBox from "../../base/PasswordBox";
import EmailBox from "../../base/EmailBox";
import TextBox from "../../base/TextBox";
import { FaUser } from "react-icons/fa6";
import Button from "../../base/Button";
import {
  Form,
  useActionData,
  useNavigate,
  useNavigation,
  useSearchParams,
} from "react-router-dom";
import { toast } from "react-toastify";

const registerModalConfig: ModalContentConfig = {
  imageUrl: "/images/register-image.png",
  headline: "ایجاد حساب کاربری",
  title: "یک حساب‌کاربری، یک قدم بزرگ برای سلامتی و سیاره.",
  footerText: "قبلا ثبت‌نام کردی؟",
  footerActionText: "وارد شو",
};

const Register = () => {
  const navigate = useNavigate();
  const navigation = useNavigation();
  const { progress, setProgress } = useContext(UserProgressContext);
  const [searchParams] = useSearchParams();
  const res = useActionData();
  const isSubmitting = navigation.state === "submitting";
  useEffect(() => {
    if (searchParams.get("mode") === "register") {
      if (!!res && !!res.success) {
        setProgress("login");
        navigate("?mode=login");
        toast.success("عملیات ثبت‌نام با موفقیت انجام شد");
      } else if (!!res && !res.success) {
        toast.error(res.message);
      }
    }
  }, [res, setProgress, navigate, searchParams]);

  return (
    <Modal
      open={progress === "register"}
      onClose={progress === "register" ? () => setProgress("") : undefined}
      config={{
        ...registerModalConfig,
        onFooterActionTextClick: () => setProgress("login"),
      }}
    >
      <Form method="post" className="flex flex-col gap-3 my-4">
        <div className="flex flex-row">
          <TextBox placeHolder="نام" icon={<FaUser />} name="firstName" />
          <TextBox
            placeHolder="نام‌خانوادگی"
            icon={<FaUser />}
            name="lastName"
          />
        </div>
        <EmailBox placeHolder="ایمیل" hasIcon name="email" />
        <PasswordBox placeHolder="رمز عبور" hasIcon name="password" />
        <PasswordBox placeHolder="تکرار رمز عبور" hasIcon name="re-password" />
        <Button
          classes="btn btn-gradient !rounded-md mx-1 mt-2"
          title={`${isSubmitting ? "در حال ثبت‌نام..." : "ثبت‌نام"}`}
          disable={isSubmitting}
        />
      </Form>
    </Modal>
  );
};

export default Register;
