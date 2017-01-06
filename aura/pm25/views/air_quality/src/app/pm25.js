import React, {Component} from 'react';
import axios from 'axios';
import PM25Navbar from './pm25navbar';
import PM25Body from './pm25body';

const PORT = 8000;
const url = `${window.location.protocol}//${window.location.hostname}:${PORT}`;

export class Pm25Show extends Component {
  constructor(props) {
    super(props);

    this.state = {cities: ['xian'], data: {xian: {name: 'xian', values: []}}};
  }

  setData() {
    axios.get(`${url}/api/dataShow/cities`)
      .then(response => {
        response.data.cities.forEach(city => {
          console.log(city);

          axios.get(`${url}/api/dataShow?city=${city}&startDate=20160901&endDate=201609011`)
            .then(response => {
              const lineData = response.data.map(element => {
                const pm = Number(`${element.pm_25}`);
                const da = new Date(`${element.local_time}`);

                return {localTime: da, pm25: pm};
              });

              const originalData = this.state.data;
              originalData[city] = {name: city, values: lineData};

              // console.log(originalData);

              this.setState({data: originalData});
            });
        });
        this.setState({cities: response.data.cities});
      });
  }

  componentDidMount() {
    this.setData();
  }

  renderPM25Body() {
    const pm25Body = [];
    // console.log(this.state.cities);
    this.state.cities.forEach(city => {
      console.log(this.state.data);
      if (this.state.data[city] === undefined) {
        return;
      }

      if ('name' in this.state.data[city]) {
        pm25Body.push(<PM25Body bodyData={this.state.data[city]}/>);
      }
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
