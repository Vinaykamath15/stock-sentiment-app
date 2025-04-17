import React from 'react';
import { Link } from 'react-router-dom';
import './Dashboard.css';

const stocks = ['Apple', 'Tesla', 'Microsoft', 'Amazon', 'Meta'];

function Dashboard() {
  return (
    <div className="dashboard">
      <h2>Stocks</h2>
      <ul className="stock-list">
        {stocks.map(stock => (
          <li key={stock}>
            <Link to={`/stock/${stock}`}>{stock}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Dashboard;
