import { baseUrl } from "./baseUrl";
import axios from "./axiosApi";

export function getBooks() {
  return axios.get(baseUrl + "books/").catch((err) => console.log(err));
}
