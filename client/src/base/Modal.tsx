import React, { useEffect, useRef, type ReactNode } from "react";
import { createPortal } from "react-dom";
import { FaXmark } from "react-icons/fa6";
import { animate } from "framer-motion";
import { Link, useSearchParams } from "react-router-dom";

export interface ModalContentConfig {
  imageUrl: string;
  headline: string;
  title: string;
  footerText: string;
  footerActionText: string;
  onFooterActionTextClick?: () => void;
}

interface AuthModalProps {
  open: boolean;
  onClose?: () => void;
  children?: ReactNode;
  config: ModalContentConfig;
}

const Modal: React.FC<AuthModalProps> = (props) => {
  const [searchParams] = useSearchParams();
  const isLogin = searchParams.get("mode") === "login";
  const modalRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = modalRef.current;
    if (!el) return;

    if (props.open) {
      animate(el, { opacity: [0, 1], y: [30, 0] }, { duration: 0.4 });
    } else {
      animate(el, { opacity: [1, 0], y: [0, 30] }, { duration: 0.4 });
    }
  }, [props.open]);

  if (!props.open) return null;

  return createPortal(
    <>
      <div className="fixed inset-0 bg-black/70 z-[9998] flex items-center justify-center">
        <div
          ref={modalRef}
          className="relative z-[9999] w-full xs:w-full sm:w-1/2 md:w-[40%] lg:w-[30%] xl:w-[25%] 2xl:w-[23%] bg-white rounded-md overflow-hidden"
          onClick={(e) => e.stopPropagation()}
        >
          <div className="relative flex flex-col items-center justify-center w-full h-full">
            <div className="absolute left-4 top-4 z-50 bg-gray-300 rounded-full p-2 duration-300 hover:scale-110 hover:bg-gray-200">
              <Link to="..">
                <FaXmark
                  className="text-colorHeaderTitle duration-300 hover:scale-110"
                  onClick={props.onClose}
                />
              </Link>
            </div>

            <div className="absolute w-96 h-96 bg-[#169C89] rounded-full right-0 top-0 transform translate-x-32 -translate-y-44 opacity-40"></div>

            <header className="bg-gradient-to-b from-emerald-100 to-transparent w-full px-2">
              <img
                src={props.config.imageUrl}
                alt="auth-image"
                className="relative w-64 h-auto mx-auto my-auto"
              />
              <h6 className="px-2">{props.config.headline}</h6>
              <small className="px-2 text-textDark font-semibold inline-block">
                {props.config.title}
              </small>
            </header>

            <section className="flex-1 w-full px-4">{props.children}</section>

            <footer className="bg-[#E8F3F2] flex items-center justify-center w-full py-4">
              <small className="text-textDark inline-flex items-center gap-1">
                {props.config.footerText}{" "}
                <span
                  onClick={props.config.onFooterActionTextClick}
                  className="hover:cursor-pointer font-bold duration-300 hover:underline underline-offset-4 decoration-2"
                >
                  <Link to={`?mode=${isLogin ? "register" : "login"}`}>
                    {props.config.footerActionText}
                  </Link>
                </span>
              </small>
            </footer>
          </div>
        </div>
      </div>
    </>,
    document.getElementById("modal") as HTMLElement
  );
};

export default Modal;
