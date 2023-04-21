import { useState} from 'react';
import { Button } from 'react-bootstrap';

export const Delete = () => {
  const [message, setMessage] = useState('');

  const handleDeleteAll = async () => {
    try {
      const response = await fetch('https://backend-5vhy.onrender.com/delete-all', {
        method: 'DELETE'
      });
      const data = await response.json();
      setMessage(data.message);
    } 
    
    catch (error) {
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



