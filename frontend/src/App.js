import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, BarChart, Bar, ResponsiveContainer } from 'recharts';

function App() {
  const [revenue, setRevenue] = useState([]);
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    // Backend se data fetch karna
    axios.get('https://mern-fastapi-data-analyst-task-1.onrender.com/api/revenue').then(res => setRevenue(res.data));
    axios.get('https://mern-fastapi-data-analyst-task-1.onrender.com/api/top-customers').then(res => setCustomers(res.data));
  }, []);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>Himanshu's Sales Dashboard</h1>
      <hr />

      <div style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
        {/* Revenue Trend Chart */}
        <div style={{ width: '100%', maxWidth: '600px', background: '#f4f4f4', padding: '15px', borderRadius: '10px' }}>
          <h3>Monthly Revenue Trend</h3>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={revenue}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="order_year_month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="amount" stroke="#8884d8" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Top Customers Table */}
        <div style={{ flex: 1, minWidth: '300px', background: '#f4f4f4', padding: '15px', borderRadius: '10px' }}>
          <h3>Top 10 Customers</h3>
          <table border="1" cellPadding="10" style={{ width: '100%', borderCollapse: 'collapse', background: 'white' }}>
            <thead>
              <tr style={{ background: '#ddd' }}>
                <th>Name</th>
                <th>Region</th>
                <th>Total Spend</th>
              </tr>
            </thead>
            <tbody>
              {customers.map((c, i) => (
                <tr key={i}>
                  <td>{c.name}</td>
                  <td>{c.region}</td>
                  <td>₹{c.amount}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default App;