import { Link } from "react-router-dom"

export const Page1 = () => {
  return <h1>I am on page 1 <Link to="/page2">Go to page 2</Link></h1>
}