import React, { Component } from "react";
import '../App.css';

export default class Profile extends Component {
  render() {
    return (
      <div class="successPopup">
        <div class="popup">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="50" viewBox="0 0 50 50"><g transform="translate(-595.805 -678.805)"><circle cx="25" cy="25" r="25" transform="translate(595.805 678.805)" fill="#fff"/><path d="M2348.164,5670.065l5.524,5.523,9.476-9.476" transform="translate(-1735.235 -4967.489)" fill="none" stroke="#4654ea" stroke-width="4"/></g></svg>
          <p>Registration Successful! </p>
          <div class="timeIndicator"></div>
        </div>
        <div class="overlay"></div>
      </div>
    );
  }
}
