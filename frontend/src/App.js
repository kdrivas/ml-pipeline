import React, { useState } from 'react';
import './App.css';

function App() {  
  const [submit, setSubmit] = useState(false);
  
  const handleSubmit = (event) => {
    setSubmit(true);
  };

  return (
    <div className="App">
      <iframe id="iframe" name="my_iframe" className="frame"></iframe>
      <h1>Form Iris Setosa</h1>
      <form action="http://localhost:8090/scores/send_data_1" method="post" target="my_iframe" onSubmit={handleSubmit}>
        <label>Sepal length: </label>
        <input name="credit_score_1" type="text"></input>
        <br/>
        <label>Sepal width: </label>
        <input name="credit_score_2" type="text"></input>
        <br/>
        <label>Petal length: </label>
        <input name="credit_score_3" type="text"></input>
        <br/>
        <label>Petal width: </label>
        <input name="credit_score_4" type="text"></input>
        <br/>
        <input type="submit" value="Submit"/>
      </form>
      {submit && <div>Data Send</div>}
    </div>
  );
}

export default App;
