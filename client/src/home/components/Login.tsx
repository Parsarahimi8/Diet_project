import { useContext, useEffect } from "react";
import Modal, { type ModalContentConfig } from "../../base/Modal";
import UserProgressContext from "../../store/userProgressContext";
import EmailBox from "../../base/EmailBox";
import PasswordBox from "../../base/PasswordBox";
import Button from "../../base/Button";
import {
  Form,
  Link,
  useActionData,
  useNavigate,
  useNavigation,
  useSearchParams,
} from "react-router-dom";
import { toast } from "react-toastify";

const loginModalConfig: ModalContentConfig = {
  imageUrl: "/images/login-image.png",
  headline: "خوش اومدی",
  title: "با ورودت، سفرت به دنیای سلامت و محیط‌زیست آغاز می‌شه.",
  footerText: "حساب کاربری نداری؟",
  footerActionText: "ثبت‌نام",
};

const Login = () => {
  const navigate = useNavigate();
  const navigation = useNavigation();
  const { progress, setProgress, setAccessToken } =
    useContext(UserProgressContext);
  const [searchParams] = useSearchParams();
  const res = useActionData();
  const isSubmitting = navigation.state === "submitting";
  useEffect(() => {
    if (searchParams.get("mode") === "login") {
      if (!!res && !!res.success) {
        setProgress("");
        navigate("/", { replace: true });
        setAccessToken(res.data.access);
        toast.success("خوش اومدی مربا");
      } else if (!!res && !res.success) {
        toast.error(res.message);
      }
    }
  }, [res, setProgress, navigate, setAccessToken, searchParams]);
  return (
    <Modal
      open={progress === "login"}
      onClose={progress === "login" ? () => setProgress("") : undefined}
      config={{
        ...loginModalConfig,
        onFooterActionTextClick: () => setProgress("register"),
      }}
    >
      <Form method="post" className="flex flex-col gap-3 my-4">
        <EmailBox placeHolder="ایمیل" hasIcon name="email" />
        <PasswordBox placeHolder="رمز عبور" hasIcon name="password" />
        <Link to="/?mode=reset-password">
          <small
            className="hover:cursor-pointer font-bold duration-300 hover:underline underline-offset-4 decoration-2"
            onClick={() => {
              setProgress("reset-password");
            }}
          >
            رمز عبور رو فراموش کردی؟
          </small>
        </Link>
        <Button
          classes="btn btn-gradient !rounded-md mx-1 mt-2"
          title={`${isSubmitting ? "در حال ورود..." : "ورود"}`}
          disable={isSubmitting}
        />
      </Form>
    </Modal>
  );
};

export default Login;
