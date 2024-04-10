import cookie from "cookie";
import { useRef, useState } from "react";

class Api {
  async makeRequest(url, method, body) {
    const {csrftoken} = cookie.parse(document.cookie);
    const options = {
      method,
      credentials: "same-origin", // include cookies
      headers: {
        "Content-Type": "application/json",
        "X-CSRFTOKEN": csrftoken // prevent CSRF attacks
      },
    }
    if (body) {
      options.body = JSON.stringify(body)
    }
    const res = await fetch(url, options);
    return res.json();
  }

  get(url) {
    return this.makeRequest(url, "get");
  }

  post(url, body={}) {
    return this.makeRequest(url, "post", body);
  }

  put(url, body={}) {
    return this.makeRequest(url, "put", body);
  }

  del(url) {
    return this.makeRequest(url, "delete");
  }
}

const api = new Api()

export const useApi = () => {
  return api;
}