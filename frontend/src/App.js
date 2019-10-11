import React from 'react';
import logo from './logo.svg';
import Login from './Login.js';
import './App.css';

function SquareContainer(){
  return (
    <div className="container d-flex min-vh-100 align-items-center">
      <div className="container">
        <Login />
      </div>
    </div>
  );
}

/*function LoginForm(){
  return (
    <div className="container">
      <form id="cuadroLogin">
        <div className="form-group">
        <label for="username" className="float-left">Correo electrónico</label>
        <input type="email" className="form-control" id="username" aria-describedby="username" placeholder="Ingrese su correo electrónico" />
        </div>
      <div className="form-group">
        <label for="exampleInputPassword1" className="float-left">Contraseña</label>
        <input type="password" className="form-control" id="exampleInputPassword1" placeholder="Ingrese su contraseña" />
      </div>
      <div className="form-group form-check">
        <input type="checkbox" className="form-check-input" id="exampleCheck1" />
        <label className="form-check-label" for="exampleCheck1">Mantener sesión abierta</label>
      </div>
      <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
}*/

function App() {
  return (
    <div className="App">
        <SquareContainer />
    </div>
  );
}



export default App;
