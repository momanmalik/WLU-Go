import React from 'react';
import { FaUser } from 'react-icons/fa'
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import myimage from './logo_2.png'

import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Login from "./components/login";
import SignUp from "./components/signup";
import Profile from "./components/profile";
import Search from "./components/search";
import Reviews from "./components/results";
import Details from "./components/user_profile";
import 'bootstrap/dist/css/bootstrap.min.css';
function App() {
  return (<Router>
    <div className="App">
      <nav className="navbar navbar-expand-lg navbar-light fixed-top">
        <div className="container">
          <Link className="navbar-brand" to={"/home"}><img
            src={myimage}
            alt="logo"
          /></Link>
          <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
            <ul className="navbar-nav ml-auto">
            <li className="nav-item">
                <Link className="nav-link" to={"/search"}>New Search</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-in"}>Login</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/sign-up"}>Sign up</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to={"/reviews"}>Reviews</Link>
              </li>
              <li className="nav-item">
            <Link className="nav-link" to={"user_data"}><FaUser/> </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    <div className="auth-wrapper">
        <div className="auth-inner">
          <Switch>
            <Route exact path='/home' component={Login} />
            <Route path='/profile' component={Profile} />
            <Route path='/search' component={Search} />
            <Route path="/sign-in" component={Login} />
            <Route path="/sign-up" component={SignUp} />
            <Route path="/reviews" component={Reviews} />
            <Route path="/user_data" component={Details} />
          </Switch>
        </div>
      </div>   
    </div>
    </Router>
  );
}
export default App;