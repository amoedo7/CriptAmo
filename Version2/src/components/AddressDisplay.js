import React from 'react';

const AddressDisplay = ({ addresses }) => {
  return (
    <div className="address-display">
      <h3>Direcciones Generadas:</h3>
      <pre>
        {Object.entries(addresses).map(([name, addr]) => (
          <div key={name}>
            <span className="address-name">{name}: </span>
            <span className="address">{addr}</span>
          </div>
        ))}
      </pre>
    </div>
  );
};

export default AddressDisplay;
