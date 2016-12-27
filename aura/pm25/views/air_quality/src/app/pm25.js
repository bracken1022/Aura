import React, {Component} from 'react';
import axios from 'axios';

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

  showDataInTable(datas) {
    let rows = [];

    if (datas.length === 0) {
      rows = [];
      return [];
    }

    for (const data of datas) {
      rows.push(
        <tr>
          <td>{data.city_name}</td>
          <td>{data.local_time}</td>
          <td>{data.pm_25}</td>
        </tr>
      );
    }

    return rows;
  }

  componentDidMount() {
    this.setData();
  }

  render() {
    return (
      <div>
        <h1>Pm25 show</h1>

        <table>
          <thead>
            <tr>
              <th>city</th>
              <th>time</th>
              <th>pm25</th>
            </tr>
          </thead>

          <tbody>{this.showDataInTable(this.state.data)}</tbody>
        </table>

      </div>
    );
  }
}
