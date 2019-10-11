import React, {Component} from "react";
import axios from 'axios';

class Login extends Component {

  state = {
    username: "",
    password: "",
  }

  onSubmit = e => {
    e.preventDefault();
    const form = new FormData();
    const response = axios.post('http://10.25.72.19:8000/api/auth/login/', null, {password: this.password, username: this.username}, {
      headers: { 'Content-Type': 'application/json' },
    });
    console.log(response.data);
  }

  render() {
    return (
        <form id="cuadroLogin" onSubmit={this.onSubmit}>
          <div className="form-group">
          <label for="username" className="float-left">Correo electrónico</label>
          <input type="text" className="form-control" id="username" aria-describedby="username" placeholder="Ingrese su correo electrónico" onChange={e => this.setState({username: e.target.value})} />
          </div>
        <div className="form-group">
          <label for="exampleInputPassword1" className="float-left">Contraseña</label>
          <input type="password" className="form-control" id="passwd" placeholder="Ingrese su contraseña" onChange={e => this.setState({password: e.target.value})} />
        </div>
        <div className="form-group form-check">
          <input type="checkbox" className="form-check-input" id="exampleCheck1" />
          <label className="form-check-label" for="exampleCheck1">Mantener sesión abierta</label>
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
        </form>
    );
  }
}

export default Login;
