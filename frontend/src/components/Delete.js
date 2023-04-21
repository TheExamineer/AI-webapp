import { useState} from 'react';
import { Button } from 'react-bootstrap';

export const Delete = () => {
  const [message, setMessage] = useState('');

  const handleDeleteAll = async () => {
    try {
      const response = await fetch('http://localhost:5000/delete-all', {
        method: 'DELETE'
      });
      const data = await response.json();
      setMessage(data.message);
    } catch (error) {
      setMessage(error.message);
    }
  };

  return (
    <div>
      <Button variant="danger" onClick={handleDeleteAll}>Empty DB</Button>
      <p>{message}</p>
    </div>
  );
}



