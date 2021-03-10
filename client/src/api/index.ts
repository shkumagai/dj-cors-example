import axios from "axios"

export const apiClient = axios.create({
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  baseURL: "/api",
})
