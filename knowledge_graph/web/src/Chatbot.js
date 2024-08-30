import React, { useState } from 'react';
import axios from 'axios';
import NetworkGraph from './NetworkGraph'; // Import the NetworkGraph component
import './Chatbot.css'; // Import the stylesheet

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false); // Loading state

  const sendMessage = async () => {
    if (input.trim() === '') return;

    // Add user message to chat
    setMessages([...messages, { sender: 'user', text: input }]);
    setInput(''); // Clear input field

    try {
      setIsLoading(true); // Set loading state

      // Send question to the server
      const response = await axios.get('http://localhost:5000/process?query=' + input);

      // Handle server response
      const { type, data } = response.data;

      if (type === 'text') {
        setMessages((prevMessages) => [...prevMessages, { sender: 'bot', text: data }]);
      } else if (type === 'graph') {
        setMessages((prevMessages) => [...prevMessages, { sender: 'bot', graphData: data }]);
      }
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [...prevMessages, { sender: 'bot', text: 'Sorry, something went wrong.' }]);
    } finally {
      setIsLoading(false); // Clear loading state
    }
  };

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div className="chatbot-container">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className={`chat-message ${message.sender}`}>
            {message.text && <p>{message.text}</p>}
            {message.graphData && <NetworkGraph data={message.graphData} />}
          </div>
        ))}
        {isLoading && <div className="loading-message">Waiting for response...</div>} {/* Loading state */}
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder="Ask a question..."
          disabled={isLoading} // Disable input while loading
        />
        <button onClick={sendMessage} disabled={isLoading}>Send</button> {/* Disable button while loading */}
      </div>
    </div>
  );
};

export default Chatbot;