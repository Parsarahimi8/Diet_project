import React, {
  createContext,
  useCallback,
  useState,
  type ReactNode,
} from "react";

type UserProgressContext = {
  token: string;
  progress: string;
  progressData: Record<string, unknown> | null;
  setAccessToken: (accessToken: string) => void;
  setProgress: (mode: string, data?: Record<string, unknown>) => void;
};

const UserProgressContext = createContext<UserProgressContext>({
  token: "",
  progress: "" /* register || login || reset-password */,
  progressData: {},
  setAccessToken: () => {},
  setProgress: () => {},
});

export const UserProgressContextProvider: React.FC<{ children: ReactNode }> = (
  props
) => {
  const [token, setToken] = useState(localStorage.getItem("accessToken") || "");
  const [userProgress, setUserProgress] = useState("");
  const [userProgressData, setUserProgressData] = useState<Record<
    string,
    unknown
  > | null>(null);

  const setAccessToken = (accessToken: string) => {
    setToken(accessToken);
  };

  const setProgress = useCallback(
    (mode: string, data?: Record<string, unknown>) => {
      setUserProgress(mode);
      setUserProgressData(data ?? null);
    },
    []
  );

  const contextValue = {
    token,
    progress: userProgress,
    progressData: userProgressData,
    setAccessToken,
    setProgress,
  };

  return (
    <UserProgressContext.Provider value={contextValue}>
      {props.children}
    </UserProgressContext.Provider>
  );
};

export default UserProgressContext;
