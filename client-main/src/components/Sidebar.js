import React from 'react';
import { Link } from 'react-router-dom';
import './Sidebar.css';

function Sidebar({ rooms, joinChatRoom, createRoom }) {
  return (
    <div className="sidebar">
      <h2>Chat Rooms</h2>
      <ul>
        {rooms.map((roomName, index) => (
          <li key={index} onClick={() => joinChatRoom(roomName)}>
            {roomName}
          </li>
        ))}
      </ul>
      <button onClick={createRoom} className="create-room-btn">Create New Room</button>
      <Link to="/" className="return-home">Return to Homepage</Link>
    </div>
  );
}

export default Sidebar;
