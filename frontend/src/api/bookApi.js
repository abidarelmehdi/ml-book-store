import { baseUrl } from "./baseUrl";
import axios from "./axiosApi";

export function getBooks(querySTring = "") {
  return axios
    .get(baseUrl + "books/" + querySTring)
    .catch((err) => console.log(err));
}

export function getBookbyId(id) {
  return axios.get(`${baseUrl}books/${id}`).catch((err) => console.log(err));
}

export function rateBook(isbn, rate) {
  return axios
    .post(`${baseUrl}books/rating`, { isbn, rate })
    .catch((err) => console.log(err));
}

export function unrateBook(isbn) {
  return axios
    .delete(`${baseUrl}books/rating`, { data: { isbn } })
    .catch((err) => console.log(err));
}

export function getUserRatedBooks() {
  return axios
    .get(`${baseUrl}books/user/ratings`)
    .catch((err) => console.log(err));
}

export function UserBookRating(isbn) {
  return axios
    .get(`${baseUrl}books/rating/${isbn}`)
    .catch((err) => console.log(err));
}

export function getUserPreferenceBooks() {
  return axios
    .get(`${baseUrl}books/recommend/content-based`, { timeout: 60000 })
    .catch((err) => console.log(err));
}

export function getCoSinSimilarBooks(isbn) {
  return axios
    .get(`${baseUrl}books/recommend/content-based/${isbn}`)
    .catch((err) => console.log(err));
}
