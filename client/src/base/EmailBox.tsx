import { FaEnvelope } from "react-icons/fa6";

const EmailBox: React.FC<{
  label?: string;
  hasIcon?: boolean;
  classes?: string;
  placeHolder: string;
  name: string;
}> = (props) => {
  return (
    <div className="flex flex-col items-center">
      {props.label && (
        <label className="xs:text-xs sm:text-sm font-lalezar self-start mr-1 text-colorHeaderTitle">
          {props.label}
        </label>
      )}
      <div
        className={`${props.classes} flex flex-row items-center w-full justify-between rounded-xl border-2 py-3 px-2 border-gray-300 group focus-within:border-gray-400`}
      >
        {props.hasIcon && (
          <span>
            <FaEnvelope className="opacity-60" />
          </span>
        )}
        <input
          type="email"
          placeholder={props.placeHolder}
          className={`flex-1 w-full px-2 rounded-s-xl font-noto outline-none text-[16px]`}
          name={props.name}
        />
      </div>
    </div>
  );
};

export default EmailBox;
