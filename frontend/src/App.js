import React, { useState, useEffect } from 'react';
import axios from 'axios';

export default function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/members")
    .then(response => {
      setData(response.data)
    })
    .catch(error => {
        console.log(error);
    });
  }, []);

  return (
    <div>
      {data.length === 0 ? (
        <p>Loading...</p>
      ) : (
        data.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  );
}
