import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './StockDetails.css';

function StockDetails() {
  const { name } = useParams();
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:5000/stock-news/${name}`)
      .then(res => setData(res.data.results))
      .catch(err => console.error(err));
  }, [name]);

  return (
    <div className="stock-details">
      <h2>{name} Headlines</h2>
      <ul>
        {data.map((item, idx) => (
          <li key={idx}>
            <strong>{item.sentiment.toUpperCase()}:</strong> {item.headline}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default StockDetails;
