import React from 'react';
import logo from './logo.svg';
import Login from './elems/Login.js';
import './App.css';
import './index.css';

function SquareContainer(props){
  return (
    <div className="container vert">
      <div className="row">
        <div className="col-3">
        </div>
        <div className="col-6">
            <div className="bg_login">
                <Login />
            </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <SquareContainer />
  );
}



export default App;
