import React, {Component} from "react";
import axios from 'axios';


class Login extends Component {

  state = {
    username: "",
    password: "",
  }

  onSubmit = e => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/auth/login/', {password: this.state.password, username: this.state.username})
      .then((response) => {
        if(response.status === 200){
          var token=response.data.auth_token;
          console.log(token);
        }
      })

  }

  render() {
    return (
      <div className="container">
        <img src={require('../logo.png')} className="imagen"/>
        <form className="bg_login logCon" id="cuadroLogin" onSubmit={this.onSubmit}>
          <div className="form-group">
          <label for="username" className="float-left cream-text">Correo electrónico</label>
          <input type="text" className="form-control" id="username" aria-describedby="username" placeholder="Ingrese su correo electrónico" onChange={e => this.setState({username: e.target.value})} />
          </div>
        <div className="form-group">
          <label for="exampleInputPassword1" className="float-left cream-text">Contraseña</label>
          <input type="password" className="form-control" id="passwd" placeholder="Ingrese su contraseña" onChange={e => this.setState({password: e.target.value})} />
        </div>
        <div className="form-group form-check">
          <input type="checkbox" className="form-check-input" id="exampleCheck1" />
          <label className="form-check-label cream-text" for="exampleCheck1">Mantener sesión abierta</label>
        </div>
        <button type="submit" className="btn btn-primary align-center">Iniciar Sesión</button>
        </form>
      </div>
    );
  }
}

export default Login;
