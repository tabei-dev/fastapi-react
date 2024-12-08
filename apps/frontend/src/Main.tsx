// import { StrictMode } from 'react'
// import { createRoot } from 'react-dom/client'
// import './index.css'
// import App from './App.tsx'

// createRoot(document.getElementById('root')!).render(
//   <StrictMode>
//     <App />
//   </StrictMode>,
// )
import React, { useEffect, useState } from 'react';

const Main = () => {
  const [data, setData] = useState(null);

  // useEffect(() => {
  //   fetch('http://localhost:8000/api/data')
  //     .then(response => response.json())
  //     .then(data => setData(data));
  // }, []);

  return (
    <div>
      <h1>Hello from Vite!</h1>
      {data && <p>{data.data}</p>}
    </div>
  );
};
export default Main;
