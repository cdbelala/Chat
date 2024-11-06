// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA0bmVcOZHfbqkwFaV-G-8iEkWKL9uDNsk",
  authDomain: "chatapp-c542c.firebaseapp.com",
  projectId: "chatapp-c542c",
  storageBucket: "chatapp-c542c.firebasestorage.app",
  messagingSenderId: "642446661699",
  appId: "1:642446661699:web:295421bc0872f392c79cf6",
  measurementId: "G-467WV9SS0V"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);