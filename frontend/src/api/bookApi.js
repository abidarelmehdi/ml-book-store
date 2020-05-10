import { baseUrl } from "./baseUrl";
import axios from "./axiosApi";

export function getBooks() {
  return axios.get(baseUrl + "books/").catch((err) => console.log(err));
}

export function getBookbyId(id) {
  return axios.get(`${baseUrl}books/${id}`).catch((err) => console.log(err));
}

export function getCoSinSimilarBooks(isbn) {
  return axios
    .get(`${baseUrl}books/recommend/content-based/${isbn}`)
    .catch((err) => console.log(err));
}
