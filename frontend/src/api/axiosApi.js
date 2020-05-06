import axios from "axios";
import { baseUrl } from "./baseUrl";

export default axios.create({
  baseURL: baseUrl,
  timeout: 5000,
  headers: {
    Authorization: "JWT " + localStorage.getItem("access_token"),
    "Content-Type": "application/json",
    accept: "application/json",
  },
});
