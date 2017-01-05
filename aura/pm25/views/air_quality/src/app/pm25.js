import React, {Component} from 'react';
import axios from 'axios';
import PM25Navbar from './pm25navbar';
import PM25Body from './pm25body';

const CITY = ['xian', 'shanghai', 'beijing', 'wuhan'];
const PORT = 8000;
const url = `${window.location.protocol}//${window.location.hostname}:${PORT}`;

export class Pm25Show extends Component {
  constructor(props) {
    super(props);

    const dataInit = {};
    CITY.forEach(city => {
      dataInit[city] = {values: []};
    });

    this.state = {data: dataInit};
  }

  setData() {
    CITY.forEach(city => {
      axios.get(`${url}/api/dataShow?city=${city}&startDate=20160901&endDate=201609011`)
        .then(response => {
          const lineData = response.data.map(element => {
            const pm = Number(`${element.pm_25}`);
            const da = new Date(`${element.local_time}`);

            return {localTime: da, pm25: pm};
          });

          const originalData = this.state.data;
          originalData[city].values = lineData;
          originalData[city].name = city;

          this.setState({data: originalData});
        });
    });
  }

  componentDidMount() {
    this.setData();
  }

  renderPM25Body() {
    const pm25Body = [];
    CITY.forEach(city => {
      console.log(this.state.data);
      pm25Body.push(<PM25Body bodyData={this.state.data[city]}/>);
    });

    return pm25Body;
  }

  render() {
    return (
      <div>
        <PM25Navbar/>
        {this.renderPM25Body()}
      </div>
    );
  }
}
