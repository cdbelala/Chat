import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Profile from './components/Profile';
import HomePage from './pages/HomePage';
import ChatRoom from './components/ChatRoom';
import './App.css';

function App() {
  return (
    <Router>
        <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/chat" element={<ChatRoom />} />
            <Route path="/profile" element={<Profile />} />
        </Routes>
    </Router>
  )
}

export default App;
