import React, { Component } from "react";
import "../card.css"

import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";
import { AwesomeButton } from "react-awesome-button";
import "react-awesome-button/dist/styles.css";

export default class Cards extends Component {
    render(){
    return (
      <div>
        <div className="container">
          <div className="project">
          <div className="circle2"><Progress type="circle"strokeWidth={8}percent={70}/></div>
          <div className="bars1">Birdness<Progress percent={70}/> </div>
          <div className="bars2">Usefulness<Progress percent={60}/> </div>
          <div className="bars3">Enjoyability<Progress percent={50}/> </div>
          <h1><strong>CP 164</strong></h1> 
          <p>Introduction to Data Structures</p>
          <div className="buttons"><AwesomeButton type="primary">Create Your Review</AwesomeButton></div>
        </div>
      </div>

      </div>


    );
  }
 
    
    
    }