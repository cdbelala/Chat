import { Link } from 'react-router-dom';

function HomePage() {
    return (
        <div>
            <h1>Welcome to the Chat Room</h1>
            <nav>
                <Link to="/chat">Enter Chat Room</Link>
                <Link to="/profile">Your Profile</Link>
            </nav>
        </div>
    );
}

export default HomePage;
