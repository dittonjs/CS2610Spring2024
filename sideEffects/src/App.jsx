import { useState, useEffect } from 'react'
import { KeyLogger } from './KeyLogger';

function App() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [atDetected, setAtDetected] = useState(false);

  const [passwordMessage, setPasswordMessage] = useState("");
  const [lengthDetected, setLengthDetected] = useState(false);

  useEffect(() => {
    if (atDetected && !email.includes("@")) {
      setErrorMessage("Email must have @ symbol")
    } else if (email.includes("@")){
      setAtDetected(true);
      setErrorMessage("");
    }
  }, [email]);

  useEffect(() => {
    if (lengthDetected && password.length < 8) {
      setPasswordMessage("Password must be 8 chars")
    } else if (password.length >= 8){
      setLengthDetected(true);
      setPasswordMessage("");
    }
  }, [password]);

  return (
    <>
      <form>
        <div>Email</div>
        <input value={email} onChange={e => setEmail(e.target.value)} />
        <div>{errorMessage}</div>
        <div>Password</div>
        <input value={password} type="password" onChange={e => setPassword(e.target.value)} />
        <div>{passwordMessage}</div>
      </form>
      <KeyLogger />
    </>
  )
}

export default App
