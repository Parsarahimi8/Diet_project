import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./App.css";
import Home from "./home/components/Home";
import Index from "./home/Index";
import { UserProgressContextProvider } from "./store/userProgressContext";
import { action as authAction } from "./home/actions/auth-action";
import HotToaster from "./base/Toaster";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Index />,
      action: authAction,
      children: [{ index: true, element: <Home /> }],
    },
  ]);
  return (
    <>
      <UserProgressContextProvider>
        <RouterProvider router={router} />
      </UserProgressContextProvider>
      <HotToaster />
    </>
  );
}

export default App;
