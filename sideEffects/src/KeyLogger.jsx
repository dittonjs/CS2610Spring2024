import { useEffect, useState } from "react"

export const KeyLogger =  () => {
  const [keys, setKeys] = useState("");


  // useEffect(() => {
  //   const keydown = (e) => {
  //     if (e.repeat) return;
  //     setKeys(keys + e.key);
  //   }
  //   window.addEventListener("keydown", keydown);

  //   const keyup = (e) => {
  //     setKeys(keys.replace(e.key, ""))
  //   }
  //   window.addEventListener("keyup", keyup);

  //   return () => {
  //     window.removeEventListener("keydown", keydown);
  //     window.removeEventListener("keyup", keyup);
  //   }
  // }, [keys])

  useEffect(() => {
    const keydown = (e) => {
      if (e.repeat) return;
      setKeys(oldKeys => oldKeys + e.key);
    }
    window.addEventListener("keydown", keydown);

    const keyup = (e) => {
      setKeys(oldKeys => oldKeys.replace(e.key, ""))
    }
    window.addEventListener("keyup", keyup);
  }, [])

  return (
    <h1>
      {keys}
    </h1>
  )
}