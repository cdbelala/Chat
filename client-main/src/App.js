import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Profile from './components/Profile';
import HomePage from './pages/HomePage';
import ChatRoom from './components/ChatRoom';
import Login from './components/Login';  // Add import for Login
import './App.css';

function App() {
  return (
    <Router>
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/chat" element={<ChatRoom />} />
            <Route path="/login" element={<Login />} />
            <Route path="/profile" element={<Profile />} />
        </Routes>
    </Router>
  )
}

export default App;
