import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import cookie from "cookie";
import './App.css'

function App() {

  const [file, setFile] = useState(null);

  async function logout() {
    const res = await fetch("/registration/logout/", {
      credentials: "same-origin", // include cookies!
    });

    if (res.ok) {
      // navigate away from the single page app!
      window.location = "/registration/sign_in/";
    } else {
      // handle logout failed!
    }
  }

  function selectFile(e) {
    console.log(e.target.value);
    setFile(e.target.files[0])
  }

  async function  uploadImage() {
    const {csrftoken} = cookie.parse(document.cookie);
    const formData = new FormData();
    formData.append("my_file", file);
    formData.append("csrfmiddlewaretoken", csrftoken);
    const res = await fetch("/uploads/", {
      method: "post",
      credentials: "include",
      body: formData
    });
  }

  return (
    <>
      <nav>
        <button onClick={logout}>Logout</button>
      </nav>
      <div>
        <input type="file" onChange={selectFile}></input>
        <button onClick={uploadImage}>Upload File</button>
      </div>
    </>
  )
}

export default App;
