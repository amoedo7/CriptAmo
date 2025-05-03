import React from 'react';

const GenerateButton = ({ onGenerate }) => {
  return (
    <button onClick={onGenerate} className="generate-button">
      ➔ GENERAR DIRECCIONES
    </button>
  );
};

export default GenerateButton;
