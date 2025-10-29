import { FaBolt, FaClock } from "react-icons/fa6";
import { motion } from "framer-motion";

const AboutProject = () => {
  return (
    <div
      id="about-project"
      className="container flex xs:flex-col md:flex-row items-center gap-6 justify-center mx-auto mt-28 xs:px-4 md:px-1 lg:px-4 xl:px-20"
    >
      <div className="xs:w-full md:w-[55%] flex flex-col gap-6 h-auto">
        <h3 className="after:content-[''] after:block xs:after:w-2/6 md:after:w-2/6 lg:after:w-2/12 xl:after:w-1/6 after:h-1 after:bg-gradient-to-l after:from-green-500 after:to-green-300 after:mt-2">
          درباره ماجراجویی ما
        </h3>
        <p className="text-pretty">
          این پروژه یک سفر جادویی برای ارتقای آگاهی در مورد تاثیرات رژیم غذایی
          بر سلامتی فرد و محیط زیست است. ما با ارائه ابزارهای کاربردی و
          داده‌‌های علمی در قالبی فانتزی، به شما کمک می‌کنیم تا انتخاب‌های غذایی
          هوشمندانه‌تر و پایدارتری داشته باشید.
        </p>
        <div className="flex flex-row gap-4">
          <div className="flex flex-row items-center gap-4 w-full bg-green-50 p-2 py-4 rounded-3xl shadow-xl">
            <FaBolt className="xs:hidden sm:block text-green-100 bg-emerald-200 sm:w-16 h-auto rounded-full p-3 self-start" />
            <div className="space-y-2 self-start">
              <h6>قدرت‌بخشی</h6>
              <p>به شما قدرت می‌دهیم تا کنترل سلامتی خود را در دست بگیرید.</p>
            </div>
          </div>
          <div className="flex flex-row items-center gap-4 w-full bg-green-50 p-2 py-4 rounded-3xl shadow-xl">
            <FaClock className="xs:hidden sm:block text-green-100 bg-emerald-200 sm:w-14 h-auto rounded-full p-3 self-start" />
            <div className="space-y-2 self-start">
              <h6>آگاهی‌بخشی</h6>
              <p>تاثیرات انتخاب‌هایتان بر زمین را شفاف می‌کنیم.</p>
            </div>
          </div>
        </div>
      </div>
      <div className="xs:w-full md:w-[45%] h-auto">
        <motion.img
          animate={{ scale: [1, 1.05, 1] }}
          transition={{ duration: 10, repeat: Infinity, ease: "easeInOut" }}
          src="/images/about-project.jpg"
          alt="about-project"
          className="sm:w-full sm:h-[300px] xl:w-4/5 xl:h-[350px] object-cover rounded-3xl mr-auto p-3 will-change-transform"
        />
      </div>
    </div>
  );
};

export default AboutProject;
