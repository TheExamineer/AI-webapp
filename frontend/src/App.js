
import './App.css';import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import { BootstrapDatePickerComponent } from './components/BootstrapDatePickerComponent'
import { BootstrapDatePickerComponent2 } from './components/BootstrapDatePickerComponent2'
import { Upload } from './components/Upload';
import { Table1 } from './components/Table1';  

import {Delete} from './components/Delete';
function App() {
  return (
    <div className="App">  
    <BootstrapDatePickerComponent /> 
    <BootstrapDatePickerComponent2 />  
    <Upload/> 
     <Delete/>
    <Table1/> 

  </div>  
  );
}

export default App;
