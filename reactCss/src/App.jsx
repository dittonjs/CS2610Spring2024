import { useEffect, useState } from 'react';
import styles from './App.module.css'

function App() {
  console.log(styles);
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);
  const [goingRight, setGoingRight] = useState(true);
  useEffect(() => {
    function updateX() {
      setGoingRight(goingRight => {
        setX(x => {
          if (goingRight && x < 200) {
            return x + 1;
          } else if (!goingRight && x > 0) {
            return x - 1;
          }
        })
        return goingRight;
      })
      window.requestAnimationFrame(updateX);
    }

    window.requestAnimationFrame(updateX)
  }, [])

  useEffect(() => {
    if (x > 200) {
      setGoingRight(false);
      setX(199);
    } else if (x < 0) {
      setGoingRight(true);
      setX(1);
    }
  }, [x])

  return (
    <div>
      <div style={{
        position: "absolute",
        backgroundColor: "red",
        width: "100px",
        height: "100px",
        top: `${y}px`,
        left: `${x}px`,
        // transition: "all .3s ease"
      }}/>
    </div>
  )
}

export default App
