import React from 'react';
import './App.css';

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
        <h2>Über uns</h2>
        <p>Unsere App ist eine innovative Pflegeanwendung, die darauf abzielt, die Verwaltung und Organisation von Pflegediensten effizient und benutzerfreundlich zu gestalten. Wir verstehen die Herausforderungen, denen Pflegekräfte und Pflegedienste täglich gegenüberstehen, und haben eine Lösung entwickelt, die den Alltag erleichtert.</p>
        <p>Mit unserer App können Pflegekräfte ihre Aufgaben und Termine einfach verwalten, während Pflegedienste einen umfassenden Überblick über ihre Ressourcen und Einsätze behalten. Unsere benutzerfreundliche Oberfläche und die leistungsstarken Funktionen sorgen dafür, dass die Pflegeprozesse reibungslos und effizient ablaufen.</p>
        <p>Unser Ziel ist es, die Qualität der Pflege zu verbessern und gleichzeitig den administrativen Aufwand zu minimieren. Wir sind stolz darauf, einen Beitrag zur Verbesserung der Pflegebranche zu leisten und die Arbeit der Pflegekräfte zu unterstützen.</p>
        <p><strong>Unsere Mission</strong>: Die Pflege durch innovative Technologie zu revolutionieren und die bestmögliche Unterstützung für Pflegekräfte und Pflegedienste zu bieten.</p>
        <p><strong>Unsere Vision</strong>: Eine Welt, in der Pflegekräfte und Pflegedienste durch modernste Technologie unterstützt werden, um die bestmögliche Pflege zu gewährleisten.</p>
      </section>

      <section id="features">
        <h2>Funktionen</h2>
        <ul>
          <li key="1">Verwaltung von Aufgaben und Terminen</li>
          <li key="2">Übersicht über Ressourcen und Einsätze</li>
          <li key="3">Benutzerfreundliche Oberfläche</li>
          <li key="4">Leistungsstarke Funktionen zur Optimierung der Pflegeprozesse</li>
          <li key="5">Minimierung des administrativen Aufwands</li>
        </ul>
      </section>

      <section id="contact">
        <h2>Kontakt</h2>
        <p>Wenn Sie Fragen haben oder Unterstützung benötigen, können Sie uns gerne kontaktieren:</p>
        <form action="submit_form.php" method="post">
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" name="name" required />
          <label htmlFor="email">E-Mail:</label>
          <input type="email" id="email" name="email" required />
          <label htmlFor="message">Nachricht:</label>
          <textarea id="message" name="message" required></textarea>
          <button type="submit">Absenden</button>
        </form>
      </section>

      <footer>
        <p>© 2024 Pflege-App. Alle Rechte vorbehalten.</p>
      </footer>
    </div>
  );
}

export default App;
