import { useEffect, useState } from 'react'
import cookie from "cookie";


function App() {

  const [file, setFile] = useState(null);
  const [files, setFiles] = useState([]);
  const [count, setCount] = useState(0);

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

  async function loadFiles() {
    const res = await fetch("/files/", {
      credentials: "same-origin", // include cookies!
    });
    const {files} = await res.json();
    setFiles(files);
  }

  useEffect(() => {
    loadFiles();
  }, []);

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
        <button onClick={() => setCount(count+1)}>{count}</button>
      </nav>
      <div>
        <input type="file" onChange={selectFile}></input>
        <button onClick={uploadImage}>Upload File</button>
      </div>
      <div>
        {files.map(f => (
          <div key={f.id}>
            <a href={`/files/${f.id}/`}>{f.name}</a>
          </div>
        ))}
      </div>
    </>
  )
}

export default App;
