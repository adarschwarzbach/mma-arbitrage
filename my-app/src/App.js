import React from "react";
import './App.css';
import axios from "axios";
import ReactDOM from 'react-dom';


const baseURL = "http://localhost:5000/data";

// class Input extends ReactDOM{

// } 



function Data() {
  const [post, setPost] = React.useState(null);
  React.useEffect(() => {
    axios.get(baseURL).then((response) => {
      setPost(response.data);
    });
  }, []);
  if (!post) return null;
  const ret = (
    <div>
    </div>)
  let hold =''
  for(let i = 0;i<post.fights.length; i++){
    hold = <div>
    {post.fights[i][0]} vs {post.fights[i][1]}: 
    <br></br>
    <br></br>Odds Shark: {post.oddsShark[i][0]} {post.oddsShark[i][1]}
    <br></br>Bovada: {post.bovada[i][0]} {post.bovada[i][1]}
    <br></br>Bet Online: {post.betOnline[i][0]} {post.betOnline[i][1]}
    <br></br>Every Game Sportsbook: {post.everyGameSportsbook[i][0]} {post.everyGameSportsbook[i][1]}
    <br></br>Sports Betting: {post.sportsBetting[i][0]} {post.sportsBetting[i][1]}
    <br></br>Bet Us: {post.betUs[i][0]} {post.betUs[i][1]}
    </div>
  }
  return hold;
}
   
export default Data;





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
