import React, { useState, useEffect } from "react";
import axios from "axios";

const Analyze = () => {
  const [headline, setHeadline] = useState("");
  const [result, setResult] = useState(null);
  const [metrics, setMetrics] = useState(null);

  const handleAnalyze = async () => {
    try {
      const res = await axios.post("http://localhost:5000/analyze", { headline });
      setResult(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchMetrics = async () => {
    try {
      const res = await axios.get("http://localhost:5000/metrics");
      setMetrics(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchMetrics();
  }, []);

  return (
    <div>
      <h2>Analyze Headline</h2>
      <input
        type="text"
        placeholder="Enter a stock-related headline..."
        value={headline}
        onChange={(e) => setHeadline(e.target.value)}
        style={{ width: "80%", padding: "10px", marginBottom: "10px" }}
      />
      <br />
      <button onClick={handleAnalyze} style={{ padding: "10px 20px" }}>
        Analyze
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <h3>Sentiment Result:</h3>
          <p><strong>Headline:</strong> {result.headline}</p>
          <p><strong>Sentiment:</strong> {result.sentiment}</p>
        </div>
      )}

      {metrics && (
        <div style={{ marginTop: "30px" }}>
          <h3>Model Metrics</h3>
          <p><strong>Accuracy:</strong> {metrics.accuracy.toFixed(2)}</p>
          <p><strong>F1 Score:</strong> {metrics.f1_score.toFixed(2)}</p>
        </div>
      )}
    </div>
  );
};

export default Analyze;
