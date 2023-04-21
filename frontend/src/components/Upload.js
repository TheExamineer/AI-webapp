
import React, { useState } from "react";
import { Form, Button } from 'react-bootstrap';

export const Upload = () => {
    const [file, setFile] = useState();

    

    const handleOnChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleOnSubmit = (e) => {
        const formData = new FormData();
        e.preventDefault();

    
    formData.append('csv', file);

    fetch('https://backend-5vhy.onrender.com/upload-csv', {
      method: 'POST',
      body: formData
    })

    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error))
        
           
    
      
    };

    return (
        <div style={{ textAlign: "center" }}>
            <h1>REACTJS CSV IMPORT EXAMPLE </h1>
            <Form>
                <input
                    type={"file"}
                    id={"csvFileInput"}
                    accept={".csv"}
                    onChange={handleOnChange}
                />

                <Button
                    onClick={(e) => {
                        handleOnSubmit(e);
                    }}
                >
                    IMPORT CSV
                </Button>
            </Form>
        </div>
    );
}