const TextareaBox: React.FC<{
  label?: string;
  classes?: string;
  placeHolder: string;
  row: number;
}> = (props) => {
  return (
    <>
      {props.label && (
        <label className="xs:text-xs sm:text-sm mr-1 text-right font-lalezar text-colorHeaderTitle">
          {props.label}
        </label>
      )}
      <textarea
        className={`w-full ${props.classes} border-2 rounded-xl font-noto outline-none w-full p-[0.7rem] text-[16px] border-green-300 group focus-within:border-green-400`}
        placeholder={props.placeHolder}
        rows={props.row}
      ></textarea>
    </>
  );
};

export default TextareaBox;
