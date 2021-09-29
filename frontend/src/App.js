import './App.css';

function App() {
  return (
    <div className="App">
      <h1>Form Iris Setosa</h1>
      <form action="http://nginx/" method="post">
        <label>Sepal length: </label>
        <input name="sepal_length" type="text"></input>
        <br/>
        <label>Sepal width: </label>
        <input name="sepal_width" type="text"></input>
        <br/>
        <label>Petal length: </label>
        <input name="petal_length" type="text"></input>
        <br/>
        <label>Petal width: </label>
        <input name="petal_width" type="text"></input>
        <br/>
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default App;
