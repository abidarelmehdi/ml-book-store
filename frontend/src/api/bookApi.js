import { baseUrl } from "./baseUrl";
import axios from "axios";

export function getBooks() {
  return axios.get(baseUrl + "books/").catch((err) => console.log(err));
}
