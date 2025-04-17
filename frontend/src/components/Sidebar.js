import React from "react";
import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Stock Sentiment</h2>
      <Link to="/">Dashboard</Link>
      <Link to="/analyze">Analyze Headline</Link>
    </div>
  );
};

export default Sidebar;
