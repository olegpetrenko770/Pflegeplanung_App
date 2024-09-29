import React from 'react';
import './App.css';
import About from './components/About';
import Features from './components/Features';
import Contact from './components/Contact';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Willkommen bei der Pflege-App</h1>
        <nav>
          <ul>
            <li><a href="#about">Über uns</a></li>
            <li><a href="#features">Funktionen</a></li>
            <li><a href="#contact">Kontakt</a></li>
          </ul>
        </nav>
      </header>

      <section id="about">
        <About />
      </section>

      <section id="features">
        <Features />
      </section>

      <section id="contact">
        <Contact />
      </section>

      <footer>
        <p>© 2024 Pflege-App. Alle Rechte vorbehalten.</p>
      </footer>
    </div>
  );
}

export default App;
