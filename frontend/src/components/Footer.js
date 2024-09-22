import React from 'react';
import './Footer.css'; // Optional: Eigene CSS-Datei für zusätzliche Stile

const Footer = () => {
  return (
    <footer className="footer">
      <p>© 2024 Pflege App. Alle Rechte vorbehalten.</p>
      <nav>
        <ul>
          <li><a href="/impressum">Impressum</a></li>
          <li><a href="/datenschutz">Datenschutz</a></li>
          <li><a href="/kontakt">Kontakt</a></li>
        </ul>
      </nav>
    </footer>
  );
};

export default Footer;
