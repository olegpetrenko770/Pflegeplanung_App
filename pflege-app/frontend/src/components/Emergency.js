import React from 'react';
import './Emergency.css'; // Optional: Eigene CSS-Datei für zusätzliche Stile

const Emergency = () => {
  return (
    <div className="emergency-container">
      <h2>Notfallinformationen</h2>
      <p>Im Falle eines Notfalls, bitte sofort die folgenden Schritte befolgen:</p>
      <ol>
        <li>Rufen Sie den Notruf unter <strong>112</strong> an.</li>
        <li>Geben Sie Ihren Namen, Standort und die Art des Notfalls an.</li>
        <li>Bleiben Sie ruhig und folgen Sie den Anweisungen des Notrufpersonals.</li>
      </ol>
      <h3>Wichtige Kontakte</h3>
      <ul>
        <li>Hausarzt: Dr. Müller - Telefon: 01234 567890</li>
        <li>Krankenhaus: St. Marien Hospital - Telefon: 09876 543210</li>
        <li>Apotheke: Stadtapotheke - Telefon: 01122 334455</li>
      </ul>
    </div>
  );
};

export default Emergency;
