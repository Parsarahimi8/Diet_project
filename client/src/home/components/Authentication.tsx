import { useContext } from "react";
import Login from "./Login";
import Register from "./Register";
import ResetPassword from "./ResetPassword";
import UserProgressContext from "../../store/userProgressContext";

const Authentication = () => {
  const { progress } = useContext(UserProgressContext);

  if (progress === "register") return <Register />;
  if (progress === "login") return <Login />;
  if (progress === "reset-password") return <ResetPassword />;

  return null;
};

export default Authentication;
