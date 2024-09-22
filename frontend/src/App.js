import React from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import MyCalendar from './components/Calendar';  // Angepasster Importpfad
import Medication from './components/Medication';
import Emergency from './components/Emergency';

function App() {
  return (
    <div className="App">
      <Header />
      <MyCalendar />  // Angepasster Komponentenname
      <Medication />
      <Emergency />
      <Footer />
    </div>
  );
}

export default App;
