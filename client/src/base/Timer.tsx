import React, { memo, useEffect, useState } from "react";
import { formatTime } from "../utils/public";
import Button from "./Button";

const Timer: React.FC<{ initialTime: number | null; onFinish: () => void }> =
  memo((props) => {
    const [timeLeft, setTimeLeft] = useState(props.initialTime || 0);

    useEffect(() => {
      const onFinish = () => {
        props.onFinish();
      };

      const expiryTime = localStorage.getItem("otpTimer");
      if (expiryTime) {
        const remaining = Math.max(
          0,
          Math.floor((Number(expiryTime) - Date.now()) / 1000)
        );
        if (remaining === 0) {
          localStorage.removeItem("otpTimer");
          setTimeLeft(0);
          onFinish();
          return;
        } else {
          setTimeLeft(remaining);
        }
      }

      if (timeLeft < 0) return;
      const timer = setInterval(() => {
        setTimeLeft((prev) => prev - 1);
      }, 1000);

      return () => clearInterval(timer);
    }, [props, timeLeft]);

    return (
      <>
        {timeLeft > 0 ? (
          <Button
            classes="btn !text-[16px] !rounded-md !px-4 !py-2"
            title={formatTime(timeLeft)}
            disable
          ></Button>
        ) : null}
      </>
    );
  });

export default Timer;
