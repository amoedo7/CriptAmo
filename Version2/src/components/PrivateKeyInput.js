import React, { useState } from 'react';

const PrivateKeyInput = ({ onSubmit }) => {
  const [key, setKey] = useState('');

  const handleChange = (e) => {
    setKey(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(key);
  };

  return (
    <div className="private-key-input">
      <label className="label">🔑 Ingrese su Clave Privada:</label>
      <input
        type="text"
        value={key}
        onChange={handleChange}
        placeholder="Clave privada de 64 caracteres"
        className="input-field"
      />
      <button onClick={handleSubmit} className="submit-button">Enviar</button>
    </div>
  );
};

export default PrivateKeyInput;
