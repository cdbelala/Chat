import React, { useState } from 'react';

function ChatRoom() {
    const [message, setMessage] = useState('');
    
    const handleSendMessage = () => {
        // Placeholder for sendin a message
        console.log("Message sent:", message);
        setMessage('');
    };

    return (
        <div>
            <h2>Chat Room</h2>
            <div>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Type a message"
                />
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
}

export default ChatRoom;
