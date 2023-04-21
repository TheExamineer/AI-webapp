import React, { useEffect, useState, } from 'react';
import {  Button } from 'react-bootstrap';



export const Table1 = () => {
const [data, setData] = useState([]);

useEffect(() => {
  fetchData();
}, []);

const fetchData = async () => {
  const response = await fetch('http://localhost:5000/get-data');
  const data = await response.json();
  setData(data);
  console.log(data.length);
};


  if (!data) {
    return <div>Loading...</div>;
  }



  const renderTable = () => {
    console.log('rendering table');
    return (
      <table>
        <thead>
          <tr>
            <th>Index</th>
            <th>Image ka Nummber</th>
            <th>Objectivication</th>
            <th>Tasvir</th>
          </tr>
        </thead>
        <tbody>
          {data.map((doc, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{doc.img_id}</td>
              <td>{doc.object}</td>
            <td><img src={`data:image/jpeg;base64,${doc.img}`} alt=""/></td>
  
              
            </tr>
          ))}
        </tbody>
      </table>
    );
  };

  return (
    <div>
      <Button variant="success" onClick={fetchData}>Fetch Data</Button>
      
      {data.length > 0 ? renderTable() : null}
    </div>
  );


}


