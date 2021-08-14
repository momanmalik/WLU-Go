//import React, { Component } from "react";
import "../card.css"
import axios from 'axios'
import { Progress } from 'react-sweet-progress';
import "react-sweet-progress/lib/style.css";
import { AwesomeButton } from "react-awesome-button";
import "react-awesome-button/dist/styles.css";
import { FaBookOpen} from "react-icons/fa";
import Button from 'react-bootstrap/Button';
import React, { useState, Component } from 'react';


const API_URL = 'http://localhost:8000/api/';
export default class Cards extends Component {
  constructor(props){
    super(props)
    this.state = {
      code:this.props.location.state.slice(0,6),
      name : this.props.location.state.slice(7,), 
      data : [],
      ratings : [],
    }
  }

  async getOptions(){
    try {
        const token =  JSON.parse(localStorage.getItem('user')).access
      
        const res = await axios.get(API_URL + 'courses/', { headers: { Authorization: 'Bearer ' + token},
        params : {code:this.props.location.state.slice(0,6)},})
        const data = res.data

        const options = data.map(d => ({
        "description" : d.description,
        "course_id" : d.course_id,
        "department" : d.department
      }))
      
      this.setState({data: options})
      const rating = await axios.get(API_URL + 'ratings/?course_id=' + this.state.data.map(course => course.course_id) , { headers: { Authorization: 'Bearer ' + token},})
      const rating_data = rating.data
      
      const options_rating = rating_data.map(d => ({
      "rating_id" : d.rating_id,
      "user_id" : d.user_id_id,
      "course_id" : d.course_id,
      "birdness" : d.birdness, 
      "enjoyability" : d.enjoyability, 
      "usefulness" : d.usefulness,
      "mean_user_score" : d.mean_user_score,
      "grade" : d.grade,
      }))
   
    this.setState({ratings: options_rating})
    } catch(e) {
      this.props.history.push("/home");
    } 
}

componentDidMount(){
    this.getOptions()
}
    render(){
      console.log(this.state.data)
    return (
      <div>
        <div className="container">
          <div className="project">
          
          <div className="circle2"><Progress type="circle"strokeWidth={8}percent={this.state.ratings.map(course => course.mean_user_score)}/></div>
          
          <div className="bars1">Birdness<Progress percent={this.state.ratings.map(course => course.birdness)}/> </div>
          <div className="bars2">Usefulness<Progress percent={this.state.ratings.map(course => course.usefulness)}/> </div>
          <div className="bars3">Enjoyability<Progress percent={this.state.ratings.map(course => course.enjoyability)}/> </div>
          <h1><strong>{this.state.code}</strong></h1> 
          <p>{this.state.name}&nbsp; <Button variant="outline-primary"> {this.state.data.map(course => <span>{course.department}</span>)}</Button>{' '}</p>
          <div className="buttons"><AwesomeButton type="primary">Create Your Review</AwesomeButton></div>
        </div>
        
        <div className="project">
       
        </div>
      </div>

      </div>


    );
  }
}
