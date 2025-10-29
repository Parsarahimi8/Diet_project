import { redirect } from "react-router-dom";

export function getAccessToken() {
  return localStorage.getItem("accessToken");
}

export function calcTokenDuration() {
  const expirationDate = localStorage.getItem("expiration");
  if (!expirationDate) return;

  const expiration = new Date(expirationDate);
  const currentTime = new Date();

  return expiration.getTime() - currentTime.getTime();
}

export function checkTokenExpiration() {
  const duration = calcTokenDuration() || -1;
  if (!!duration && duration > 0) {
    return duration;
  } else {
    return "EXPIRED";
  }
}

export default function logout() {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("expiration");
  return redirect("/");
}
