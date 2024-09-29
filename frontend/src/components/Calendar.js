import React, { useState } from 'react';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import './Calendar.css'; // Optional: Eigene CSS-Datei für zusätzliche Stile

const MyCalendar = () => {
  const [date, setDate] = useState(new Date());

  const onChange = (newDate) => {
    setDate(newDate);
  };

  return (
    <div className="calendar-container">
      <h2>Kalender</h2>
      <Calendar
        onChange={onChange}
        value={date}
      />
      <div className="selected-date">
        <h3>Ausgewähltes Datum:</h3>
        <p>{date.toDateString()}</p>
      </div>
    </div>
  );
};

export default MyCalendar;
