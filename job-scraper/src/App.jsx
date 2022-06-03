import React from 'react';
import NavBar from './Components/NavigationBar/NavBar.jsx';
import './App.css'
function App() {
  return (
    <div className="App">
      <div className="navbar-container">
        <NavBar/>
      </div>
      <p>
        this is test writing
      </p>
      <button>
        push me!
      </button>
    </div>
  );
}

export default App;
