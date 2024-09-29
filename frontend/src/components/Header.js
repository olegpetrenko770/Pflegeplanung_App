import React from 'react';
import './Header.css'; // Optional: Eigene CSS-Datei für zusätzliche Stile

const Header = () => {
  return (
    <header className="header">
      <h1>Pflege App</h1>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/calendar">Kalender</a></li>
          <li><a href="/medication">Medikamente</a></li>
          <li><a href="/emergency">Notfall</a></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
