import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import './Profile.css';

function Profile() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate=useNavigate();

  const handleSave = async() => {
    if (!username || !password)
    {
      alert('Please enter valid username and password!');
      return;
    }
    try{
      const response = await fetch('/api/profile', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    });
    if (response.ok) {
    alert('Profile created successfully!');
    navigate ('/login');
    }
    else{
      const errorData = await response.json();
      alert(`Error: ${errorData.message}`);

    }
  } catch (error){
    console.error('Error during profile creation', error);
    alert('An error occurred');
  }
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
