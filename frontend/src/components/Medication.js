import React, { useState } from 'react';

const Medication = () => {
  const [medications, setMedications] = useState([]);
  const [newMedication, setNewMedication] = useState({
    name: '',
    dosage: '',
    frequency: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewMedication((prevMedication) => ({
      ...prevMedication,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setMedications((prevMedications) => [...prevMedications, newMedication]);
    setNewMedication({ name: '', dosage: '', frequency: '' });
  };

  return (
    <div className="medication-container">
      <h2>Medikamentenliste</h2>
      <ul>
        {medications.map((medication, index) => (
          <li key={index}>
            <strong>Name:</strong> {medication.name}, <strong>Dosierung:</strong> {medication.dosage}, <strong>Häufigkeit:</strong> {medication.frequency}
          </li>
        ))}
      </ul>
      <h3>Neues Medikament hinzufügen</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={newMedication.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="dosage">Dosierung:</label>
          <input
            type="text"
            id="dosage"
            name="dosage"
            value={newMedication.dosage}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="frequency">Häufigkeit:</label>
          <input
            type="text"
            id="frequency"
            name="frequency"
            value={newMedication.frequency}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Hinzufügen</button>
      </form>
    </div>
  );
};

export default Medication;
