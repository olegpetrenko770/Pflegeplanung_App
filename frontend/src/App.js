import React from 'react';
import './App.css';
import Calendar from './components/Calendar';
import Medication from './components/Medication';
import Emergency from './components/Emergency';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Calendar />
        <Medication />
        <Emergency />
      </main>
      <Footer />
    </div>
  );
}

export default App;
