import React, { useEffect, useState } from 'react';
import { Button, Table } from 'react-bootstrap';
import * as FileSaver from 'file-saver';

export const Table1 = () => {
  const [data, setData] = useState([]);
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const response = await fetch('https://backend-5vhy.onrender.com/get-data');
    const data = await response.json();
    setData(data);
    setStartDate(data.start_date);
    setEndDate(data.end_date);
  };

  const downloadReport = (startDate, endDate) => {
    console.log(startDate)
    console.log(endDate)
    const counts = {};
    data.forEach((doc) => {
      if (
        doc.date >= startDate &&
        doc.date < endDate &&
        doc.object in counts
      ) {
        counts[doc.object] += 1;
      } else if (doc.date >= startDate && doc.date < endDate) {
        counts[doc.object] = 1;
      }
    });

    const rows = [];
    for (const [key, value] of Object.entries(counts)) {
      rows.push([key, value]);
    }
    rows.unshift(['Object Name', 'Count']);
    const csvData = rows.map((row) => row.join(',')).join('\n');
    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8' });
    FileSaver.saveAs(blob, 'report.csv');
  };
  
  const fetchDataAndDownload = async () => {
    await fetchData();
    downloadReport(startDate, endDate);
  }

  if (!data) {
    return <div>Loading...</div>;
  }

  const renderTable = () => {
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
              <td>
                {doc.img && (
                  <img
                    src={`data:image/jpeg;base64,${doc.img}`}
                    alt=""
                  />
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    );
  };

  return (
    <div>
      <div className="d-flex justify-content-center">
        <Button variant="primary" onClick={() => fetchDataAndDownload()}>
          Download Report
        </Button>
      </div>
      <div>
        {startDate && endDate ? (
          <div>
            <p>Start Date: {startDate}</p>
            <p>End Date: {endDate}</p>
          </div>
        ) : null}
        {data.length > 0 ? renderTable() : null}
      </div>
    </div>
  );
};
