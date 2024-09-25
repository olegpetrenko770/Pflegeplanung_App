import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="Header">
      <h1>Willkommen bei der Pflege-App</h1>
      <nav>
        <ul>
          <li><a href="#about">Über uns</a></li>
          <li><a href="#features">Funktionen</a></li>
          <li><a href="#contact">Kontakt</a></li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
