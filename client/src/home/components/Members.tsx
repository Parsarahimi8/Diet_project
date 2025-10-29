import { Autoplay, Pagination } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import "swiper/css/pagination";

const Members = () => {
  return (
    <>
      <div id="members" className="container mx-auto flex justify-center mt-28">
        <h3 className="after:mx-auto after:content-[''] after:block after:w-1/2 after:h-1 after:bg-gradient-to-l after:from-green-500 after:to-green-300 after:mt-2">
          نگهبانان این سرزمین
        </h3>
      </div>

      <div className="w-full max-w-5xl mx-auto mt-8 px-4 h-[300px] flex">
        <Swiper
          modules={[Pagination, Autoplay]}
          spaceBetween={30}
          slidesPerView={1}
          pagination={{
            clickable: true,
          }}
          autoplay={{
            delay: 2500,
            disableOnInteraction: false,
          }}
          loop
          breakpoints={{
            340: { slidesPerView: 1 },
            414: { slidesPerView: 2 },
            768: { slidesPerView: 3 },
          }}
          className="rounded-2xl"
        >
          <SwiperSlide>
            <div className="flex flex-col gap-2 items-center">
              <img
                src="/images/members/user-one.jpg"
                alt="user-one"
                className="w-40 h-40 rounded-full object-cover border-4 border-green-300"
              />
              <div className="flex-1 text-center">
                <h5>سپهر جوان</h5>
                <p className="text-xs">تحلیلگر اسرار</p>
              </div>
            </div>
          </SwiperSlide>
          <SwiperSlide>
            <div className="flex flex-col gap-2 items-center">
              <img
                src="/images/members/user-two.jpg"
                alt="user-two"
                className="w-40 h-40 rounded-full object-cover border-4 border-green-300"
              />
              <div className="flex-1 text-center">
                <h5>مینا راد</h5>
                <p className="text-xs">طراح رویاها</p>
              </div>
            </div>
          </SwiperSlide>
          <SwiperSlide>
            <div className="flex flex-col gap-2 items-center">
              <img
                src="/images/members/user-three.jpg"
                alt="user-three"
                className="w-40 h-40 rounded-full object-cover border-4 border-green-300"
              />
              <div className="flex-1 text-center">
                <h5>آرش کاوه</h5>
                <p className="text-xs">جادوگر کد</p>
              </div>
            </div>
          </SwiperSlide>
          <SwiperSlide>
            <div className="flex flex-col gap-2 items-center">
              <img
                src="/images/members/user-one.jpg"
                alt="user-one"
                className="w-40 h-40 rounded-full object-cover border-4 border-green-300"
              />
              <div className="flex-1 text-center">
                <h5>سپهر جوان</h5>
                <p className="text-xs">تحلیلگر اسرار</p>
              </div>
            </div>
          </SwiperSlide>
        </Swiper>
      </div>
    </>
  );
};

export default Members;
