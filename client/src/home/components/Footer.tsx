import { FaInstagram, FaTelegram, FaXTwitter } from "react-icons/fa6";
import { toPersianDigits } from "../../utils/public";

const Footer = () => {
  return (
    <div className="container flex flex-col items-center gap-6 justify-center mx-auto mt-28 xs:px-4 md:px-1 lg:px-4 xl:px-20">
      <div className="flex flex-row gap-6 text-base text-textDark">
        <FaXTwitter className="hover:text-primary" />
        <FaInstagram className="hover:text-primary" />
        <FaTelegram className="hover:text-primary" />
      </div>
      <p className="text-center text-xs mb-12">
        &copy;
        {` ${toPersianDigits(
          2025
        )} تمامی حقوق این وب‌سایت متعلق به "الگوی حساس به آب و محیط‌زیست" می‌باشد`}
      </p>
    </div>
  );
};

export default Footer;
