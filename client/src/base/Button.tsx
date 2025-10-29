import { motion } from "framer-motion";
import type React from "react";

const Button: React.FC<{
  classes: string;
  isGradient?: boolean;
  title: string;
  name?: string;
  value?: string;
  disable?: boolean;
  motion?: boolean;
  onClick?: () => void;
}> = (props) => {
  return (
    <>
      {props.motion && (
        <motion.button
          animate={{
            scale: [1, 1.03, 1],
            boxShadow: [
              "0 0 0 0 rgba(134, 239, 172, 0.7)",
              "0 0 0 20px rgba(134, 239, 172, 0)",
              "0 0 0 0 rgba(134, 239, 172, 0.7)",
            ],
          }}
          transition={{ duration: 2.5, ease: "easeInOut", repeat: Infinity }}
          className={`${props.classes} xs:text-[14px] sm:text-xs md:text-sm lg:text-base leading-none duration-300 py-2 outline-none`}
          onClick={props.onClick}
        >
          {props.title}
        </motion.button>
      )}

      {!props.motion && (
        <button
          className={`${props.classes} xs:text-[14px] sm:text-xs md:text-sm lg:text-base leading-none duration-300 py-2 outline-none`}
          onClick={props.onClick}
          disabled={props.disable}
          name={props.name}
          value={props.value}
        >
          {props.title}
        </button>
      )}
    </>
  );
};

export default Button;
