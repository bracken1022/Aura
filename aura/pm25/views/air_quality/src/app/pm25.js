import React, {Component} from 'react';
import axios from 'axios';
import PM25Navbar from './pm25navbar';
import PM25Body from './pm25body';

const dataInit = [];

export class Pm25Show extends Component {
  constructor(props) {
    super(props);

    this.state = {data: dataInit, data2: dataInit};
  }

  setData() {
    axios.get('http://localhost:8000/api/dataShow?city=xian&startDate=20160901&endDate=201609011')
      .then(response => {
        const lineData = response.data.map(element => {
          const pm25 = Number(`${element.pm_25}`);
          const da = new Date(`${element.local_time}`);
          const day = Number(da);

          return {x: day, y: pm25};
        });

        this.setState({data: {name: `${response.data[0].city_name}`, values: lineData}});
      });

    axios.get('http://localhost:8000/api/dataShow?city=shanghai&startDate=20160901&endDate=201609011')
      .then(response => {
        const lineData = response.data.map(element => {
          const pm25 = Number(`${element.pm_25}`);
          const da = new Date(`${element.local_time}`);
          const day = Number(da);

          return {x: day, y: pm25};
        });

        this.setState({data2: {name: `${response.data[0].city_name}`, values: lineData}});
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
        <PM25Body bodyData={this.state.data2}/>
      </div>
    );
  }
}
