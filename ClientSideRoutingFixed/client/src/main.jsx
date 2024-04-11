import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import 'vite/modulepreload-polyfill'
import  { createHashRouter, RouterProvider } from "react-router-dom";
import { Page1 } from './Page1.jsx'
import { Page2 } from './Page2.jsx'
import { Page3 } from './Page3.jsx'

const router = createHashRouter([
  {
    path: "/",
    element: <App />,
    children: [{
      path: "/",
      element: <Page1 />,
    }, {
      path: "/page2",
      element: <Page2  />,
    }, {
      path: "/page3",
      element: <Page3 />
    }]
  }
]);


ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
