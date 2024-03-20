import { useState } from "react"



function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [rememberLogin, setRememberLogin] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  function validateEmail() {
    return email.includes("@");
  }

  function login(e) {
    e.preventDefault();
    setErrorMessage("");
    if (!validateEmail(email)) {
      setErrorMessage("Email must must be valid!");
      return;
    }
    if (password.length < 8) {
      setErrorMessage("Password length must be greater than 8");
      return;
    }

    console.log(`Login request successful with email ${email} and password ${password}`);
  }

  return (
    <>
      <form onSubmit={login}>
        <div>
          <div>Email</div>
          <input type="text" value={email} onChange={e => setEmail(e.target.value)}/>
        </div>
        <div>
          <div>Password</div>
          <input type="password" value={password} onChange={e => setPassword(e.target.value)}/>
        </div>
        <div>
          <div>Remember login</div>
          <input type="checkbox" checked={rememberLogin} onChange={e => setRememberLogin(e.target.checked)} />
        </div>
        <button>Login</button>
        <div>{errorMessage}</div>
      </form>
    </>
  )
}

export default App
