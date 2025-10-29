import { toPersianDigits } from "../../utils/public";

const RoadMap = () => {
  return (
    <>
      <div
        id="road-map"
        className="container flex flex-col items-center gap-6 justify-center mx-auto mt-28 xs:px-4 md:px-1 lg:px-4 xl:px-20"
      >
        <h3 className="after:mx-auto after:content-[''] after:block after:w-1/2 after:h-1 after:bg-gradient-to-l after:from-green-500 after:to-green-300 after:mt-2">
          نقشه راه جادویی
        </h3>
        <div className="text-center space-y-2">
          <p>
            این ابزار جادویی به شما کمک می‌کند تا تاثیر رژیم غذایی خود را در
            چهار مرحله ساده و شگفت‌انگیز کشف کنید.
          </p>
          <p>
            هر مرحله شما را به درک عمیق‌تری از ارتباط بین غذا، سلامتی و
            سیاره‌مان می‌رساند.
          </p>
        </div>
      </div>
      <ul className="grid xs:grid-cols-1 sm:grid-cols-2 md:grid-cols-2 lg:grid-cols-4 items-center gap-4 xs:px-5 md:px-12 mt-16">
        <li className="flex flex-col gap-4 items-center w-full h-full bg-green-50 rounded-3xl shadow-xl py-4 px-6">
          <img
            src="/images/add-food.jpg"
            alt="add-food"
            className="w-1/2 h-auto"
          />
          <h5 className="text-nowrap">{`${toPersianDigits(1)}.ثبت غذاها`}</h5>
          <p className="text-xs text-center md:px-4">
            ماجراجویی با ثبت وعده‌های غذایی روزانه در دفترچه جادویی ما آغاز
            می‌شود. با هر ورودی، یک دانه در باغچه سلامتی خود می‌کارید.
          </p>
        </li>
        <li className="flex flex-col gap-4 items-center w-full h-full bg-green-50 rounded-3xl shadow-xl py-4 px-6">
          <img
            src="/images/healthy-road.jpg"
            alt="healthy-road"
            className="w-1/2 h-auto"
          />
          <h5 className="text-nowrap">{`${toPersianDigits(
            2
          )}.ردیابی سلامت`}</h5>
          <p className="text-xs text-center md:px-4">
            معجون‌های سلامتی خود را با دنبال کردن شاخص‌های کلیدی بسازید. شاهد
            رشد و شکوفایی باغچه خود با انتخاب‌های سالم‌تر باشید.
          </p>
        </li>
        <li className="flex flex-col gap-4 items-center w-full h-full bg-green-50 rounded-3xl shadow-xl py-4 px-6">
          <img
            src="/images/usefull.jpg"
            alt="usefull"
            className="w-1/2 h-auto"
          />
          <h5 className="text-nowrap">{`${toPersianDigits(
            3
          )}.تحلیل تاثیرات`}</h5>
          <p className="text-xs text-center md:px-4">
            ردپای جادویی رژیم خود بر روی زمین مشاهده کنید. با استفاده از گوی
            بلورین ما، تاثیر هر غذا بر سیاره را ببینید.
          </p>
        </li>
        <li className="flex flex-col gap-4 items-center w-full h-full bg-green-50 rounded-3xl shadow-xl py-4 px-6">
          <img
            src="/images/smart-offers.jpg"
            alt="smart-offers"
            className="w-1/2 h-auto"
          />
          <h5 className="text-nowrap">{`${toPersianDigits(
            4
          )}.پیشنهادات هوشمند`}</h5>
          <p className="text-xs text-center md:px-4">
            توصیه‌های هوشمندانه از مرشدان ما برای بهبود رژیم دریافت کنید.
            راهنمایی‌های شخصی‌سازی شده برای یک زندگی سالم‌تر و سیاره‌ای سرسبزتر.
          </p>
        </li>
      </ul>
    </>
  );
};

export default RoadMap;
