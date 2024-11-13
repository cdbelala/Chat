import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
  return (
    <div className="home-page">
      <h1 className="home-title">Welcome to the Chat Room</h1>
      <nav className="home-nav">
    
        <Link to="/profile" className="nav-button">LOGIN</Link>
      </nav>
    </div>
  );
}

export default HomePage;