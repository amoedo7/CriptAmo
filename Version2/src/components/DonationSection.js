import React from 'react';

const donationAddresses = {
  Bitcoin: "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
   Litecoin: "LRxpA5rr8kAAbtMHg45ruS7929x9gsnEsv",
   Dogecoin: "DBsxS8VfMVpPt5qjEW68BBCyh5KAsCNYec",
   BitcoinCash: "17jrtsZ245v7M5f8Vv6ZdR3NowasZ9hELv",
  Clams: "xF3VnkPVKoQ9PTkzrPjE4bLA33t718KGLG",
  Zcash: "t1QcTuCyA2Qhhwii2SLugmE9J4bmxMxwMZN",
  Dash: "XhRhj8Cv1o8hW2FiMoQnUwjAeHAZfvCAdp",
  Ethereum: "0x548702ecce06cbc6991c86de390bc008459cdf5a",
  BNB: "0x548702ecce06cbc6991c86de390bc008459cdf5a",
};

const DonationSection = () => {
  return (
    <section className="donation-section">
      <h1 className="donation-title"> ¡Apóyame!</h1>
      <pre>
        {Object.entries(donationAddresses).map(([coin, address]) => (
          <div key={coin}>
            <span className="coin-name">{coin}: </span>
            <span className="donation-address">{address}</span>
          </div>
        ))}
      </pre>
    </section>
  );
};

export default DonationSection;
