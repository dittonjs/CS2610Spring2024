import {useState} from "react";
import {WelcomeMessage} from "./components/WelcomeMessage";

function App() {
  const [count, setCount] = useState(0);
  console.log("I get called!")

  function increment() {
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
    setCount(oldCount => oldCount + 1);
  }

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increment}>Increment</button>
    </div>
  );
}

export default App
