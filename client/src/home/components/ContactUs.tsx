import Button from "../../base/Button";
import EmailBox from "../../base/EmailBox";
import TextareaBox from "../../base/TextareaBox";

const ContactUs = () => {
  return (
    <div
      id="contact-us"
      className="container flex flex-col items-center gap-6 justify-center mx-auto mt-28 xs:px-4 md:px-1 lg:px-4 xl:px-20"
    >
      <h3 className="after:mx-auto after:content-[''] after:block after:w-1/2 after:h-1 after:bg-gradient-to-l after:from-green-500 after:to-green-300 after:mt-2">
        ارتباط با ما
      </h3>
      <p className="text-center">
        سوال یا پیشنهادی دارید؟ با ارسال یک نامه جادویی، ما را با خبر کنید.
      </p>
      <div className="xs:w-full md:w-1/2 xl:w-6/12 2xl:w-5/12 space-y-4">
        <EmailBox
          classes="bg-green-50 border-green-300 group focus-within:border-green-400"
          placeHolder="ایمیل شما"
        />
        <TextareaBox
          classes="bg-green-50 border-green-300"
          placeHolder="پیام شما"
          row={8}
        />
      </div>
      <Button classes="btn btn-gradient px-6" title="ارسال پیام" />
    </div>
  );
};

export default ContactUs;
