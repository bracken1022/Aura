import React, {Component} from 'react';
import axios from 'axios';
import PM25Navbar from './pm25navbar';
import PM25Body from './pm25body';

const dataInit = [];

export class Pm25Show extends Component {
  constructor(props) {
    super(props);

    this.state = {data: dataInit};
  }

  setData() {
    axios.get('http://localhost:8000/api/dataShow?city=xian&startDate=20160901&endDate=201609011')
      .then(response => {
        this.setState({data: response.data});
      });
  }

  componentDidMount() {
    this.setData();
  }

  render() {
    return (
      <div>
        <PM25Navbar/>
        <PM25Body bodyData={this.state.data}/>
      </div>
    );
  }
}
