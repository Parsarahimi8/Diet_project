import { createPortal } from "react-dom";
import { Bounce, ToastContainer } from "react-toastify";

const HotToaster = () => {
  return createPortal(
    <ToastContainer
      position="top-center"
      autoClose={2000}
      hideProgressBar
      newestOnTop={false}
      closeOnClick={false}
      rtl={true}
      pauseOnFocusLoss
      draggable
      pauseOnHover
      theme="colored"
      transition={Bounce}
    />,
    document.getElementById("toast") as HTMLElement
  );
};

export default HotToaster;
