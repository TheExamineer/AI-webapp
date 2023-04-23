import React, { useEffect, useState, } from 'react';
import {  Button,Table } from 'react-bootstrap';



export const Table1 = () => {
const [data, setData] = useState([]);

useEffect(() => {
  fetchData();
}, []);

const fetchData = async () => {
  const response = await fetch('https://backend-5vhy.onrender.com/get-data');
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
      <Table bordered striped>
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
      </Table>
    );
  };

  return (
    <div>
          <div className="d-flex justify-content-center">
  <Button variant="success" onClick={fetchData}>Fetch Data</Button>
</div>
<div >
  {data.length > 0 ? renderTable() : null}
</div>
    </div>
  );


}

