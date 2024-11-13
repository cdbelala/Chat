import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './Profile.css';

function Profile() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSave = () => {
    alert('Profile saved!');
  };

  return (
    <div className="profile-container">
      <h2 className="profile-title">Your Profile</h2>
      <div className="profile-form">
        <label className="profile-label">
          Username:
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            className="profile-input" 
          />
        </label>
        <label className="profile-label">
          Password:
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            className="profile-input" 
          />
        </label>
        <button onClick={handleSave} className="save-button">Create Profile</button>
      </div>
      <Link to="/chat" className="home-button">Login</Link>
    </div>
  );
}

export default Profile;
