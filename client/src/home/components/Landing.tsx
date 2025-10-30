import { useContext } from "react";
import Button from "../../base/Button";
import UserProgressContext from "../../store/userProgressContext";

const Landing = () => {
  const { setProgress } = useContext(UserProgressContext);
  return (
    <div className="relative xs:h-[calc(100dvh-68px)] sm:h-[calc(100dvh-82.8px)] md:h-[calc(100dvh-88px)] bg-gradient-to-br from-green-50 to-emerald-100">
      <img
        src="/images/landing-image.jpg"
        alt="landing-image"
        className="absolute inset-0 w-full h-full object-cover opacity-20 z-0"
      />

      <div className="relative z-10 flex flex-col items-center justify-center h-full text-center">
        <h1 className="font-bold xs:mb-5 md:mb-16 text-pretty bg-clip-text text-transparent bg-gradient-to-r from-fromGradientTitle to-toGradientTitle">
          کشف کن رژیم غذایی تو چه تاثیری روی سلامتی و زمین دارد
        </h1>
        <h6 className="xs:mb-10 xs:px-5 md:mb-16 text-pretty font-noto">
          با ابزار جادویی ما، به سادگی تاثیر انتخاب های غذایی خود را بر سلامتی
          شخصی و سیاره‌ی زمین مشاهده و بهینه کنید.
        </h6>
        <Button
          classes="btn btn-gradient px-8"
          title="ماجراجویی رو شروع کن"
          onClick={() => setProgress("login")}
          motion
        />
      </div>
    </div>
  );
};

export default Landing;
