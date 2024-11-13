import React, { useState, useEffect } from 'react';  // Import React once at the top
import Sidebar from './Sidebar';
import './ChatRoom.css';

function ChatRoom() {
  const [room, setRoom] = useState('General');
  const [rooms] = useState(['General', 'Tech', 'Random']);
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  useEffect(() => {
    setMessages([]); // Clear messages when switching rooms
  }, [room]);

  const sendMessage = () => {
    if (newMessage.trim()) {
      setMessages([...messages, { text: newMessage, user: 'You' }]);
      setNewMessage('');
    }
  };

  return (
    <div className="chatroom">
      <Sidebar rooms={rooms} joinChatRoom={setRoom} />

      <div className="chat-area">
        <h2>{room} Room</h2>

        <div className="chat-log">
          {messages.length === 0 ? (
            <p className="no-messages">No messages yet. Start the conversation!</p>
          ) : (
            messages.map((msg, index) => (
              <div key={index} className="message">
                <strong>{msg.user}:</strong> {msg.text}
              </div>
            ))
          )}
        </div>

        <div className="message-input-container">
          <input
            type="text"
            value={newMessage}
            onChange={(e) => setNewMessage(e.target.value)}
            placeholder="Type your message..."
            className="message-input"
          />
          <button onClick={sendMessage} className="send-button">
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

export default ChatRoom;
