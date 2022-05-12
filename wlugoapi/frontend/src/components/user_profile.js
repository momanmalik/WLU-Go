import React, { Component } from 'react'
import "../user_profile.css"
import UserService from "../services/auth-service";
 
export default class Details extends Component {
  render() {
    const data =  localStorage.getItem('username')
    const username = data
    const status = 'Student'
    return (
        <div class="profile-container">
            <div class="profile-card">
                <img src="https://www.esa.edu.au/images/default-source/governance/person-placeholder.png?sfvrsn=71c5489_2" alt="image1" class="profile-icon" />
            <div class="profile-name">{username}</div>
        <div class="profile-position">{status}</div>
        <a href="#" class="button">Update User</a>
    </div>
    </div>
    );
  }
}
