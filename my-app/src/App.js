import React from "react";
import './App.css';
import axios from "axios";


const baseURL = "http://localhost:5000/data";

function App() {
  const [post, setPost] = React.useState(null);

  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;

  return (
    <div>
      <h1>{post.fights}</h1>
      <p>{post.oddsShark}</p>
      
    </div>
  );
}
   
export default App;





// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit these nuts.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div> 
//   ); 
// }

// export default App;


// import React, { useState, useEffect } from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/').then(res => res.json()).then(data => {
//       setCurrentTime(data);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
// }

// export default App;
