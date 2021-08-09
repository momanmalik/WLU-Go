import React, { Component } from 'react'
import Select from 'react-select'
import axios from 'axios'
import AuthService from "../services/auth-service";
import { Redirect } from 'react-router-dom'

import "../index.css"


const API_URL = 'http://localhost:8000/api/';
export default class Search extends Component {

  constructor(props){
    super(props)
    this.state = {
      selectOptions : [],
      id: "",
      name: ''
    }
  }

 async getOptions(){
      try {
        const token =  JSON.parse(localStorage.getItem('user')).access
        
    const res = await axios.get(API_URL + 'courses/', { headers: { Authorization: 'Bearer ' + token}})
    const data = res.data

    const options = data.map(d => ({
      "value" : d.code,
      "label" : d.code + "- " + d.name,
      
    }))

    this.setState({selectOptions: options})

      } catch(e) {
        this.props.history.push("/home");
    }
    
  }

  handleChange(e){
   this.setState({id:e.value, name:e.label})
  }

  componentDidMount(){
      this.getOptions()
  }

  render() {
    console.log(this.state.selectOptions)
    return (
      
      <div class="Search">
          Select a course at Laurier: 
          <div></div>
        <Select options={this.state.selectOptions} onChange={this.handleChange.bind(this)} />
          <p>You have selected <strong>{this.state.name}</strong></p>
      </div>
      
    );
  }
}