
import React from 'react'
import { Form, Button } from 'react-bootstrap';
import { useState } from "react";


export const BootstrapDatePickerComponent2 = () => {
  const [selectedDate, setSelectedDate] = useState("");

  const handleDateChange = (event) => {
    setSelectedDate(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Send the selected date to the backend using your preferred method (e.g. fetch, axios, etc.)

    console.log("Selected Date: ", selectedDate);

    fetch("http://127.0.0.1:5000//getting-data", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ date: selectedDate }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Response from backend:", data);
      })
      .catch((error) => {
        console.error("Error sending data to backend:", error);
      });
  };

  return (
    <div>
      <div className="row">
        <div className="col-md-4">
          <Form onSubmit={handleSubmit}>
            <Form.Group controlId="dob">
              <Form.Label>Select Date</Form.Label>
              <Form.Control
                type="date"
                name="dob"
                placeholder="Date of Birth"
                value={selectedDate}
                onChange={handleDateChange}
              />
            </Form.Group>
            <Button type="submit">Submit</Button>
          </Form>
        </div>
      </div>
    </div>
  );
};
