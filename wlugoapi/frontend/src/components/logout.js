import React, { Component } from "react";
import Userfront from "@userfront/react";

Userfront.init("8b695vnw");

const LogoutButton = Userfront.build({
  toolId: "mabnnb"
});



export default class Logout extends Component {
  render () {
    return <LogoutButton />
  }
}

