import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import Calendar from './components/Calendar';
import Medication from './components/Medication';
import Emergency from './components/Emergency';

function App() {
  return (
    <div className="App">
      <Header />
      <Calendar />
      <Medication />
      <Emergency />
      <Footer />
    </div>
  );
}

export default App;
