import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import StockDetails from './components/StockDetails';
import Analyze from './components/Analyze';
import Sidebar from './components/Sidebar';

function App() {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/analyze" element={<Analyze />} />
          <Route path="/stock/:name" element={<StockDetails />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

