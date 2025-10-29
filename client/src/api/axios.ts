import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
});

api.interceptors.request.use((config) => {
  return config;
});

api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
