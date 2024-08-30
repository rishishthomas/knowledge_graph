import React from 'react';
import Chatbot from './Chatbot';
import './App.css'; // Import the stylesheet

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Knowledge Graph</h1>
      </header>
        <br></br>
      <main>
        <Chatbot />
      </main>
    </div>
  );
}

export default App;
