import React, {Component} from 'react';
import {Grid, Row, Col} from 'react-bootstrap';

export default class PM25Body extends Component {
  showDataInTable() {
    let rows = [];

    const datas = this.props.bodyData;
    console.log(datas.length);

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

  render() {
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={3}>left</Col>

          <Col xs={12} md={6}>
            <h1>Pm25 show</h1>

            <table>
              <thead>
                <tr>
                  <th>city</th>
                  <th>time</th>
                  <th>pm25</th>
                </tr>
              </thead>

              <tbody>{this.showDataInTable()}</tbody>
            </table>
          </Col>

          <Col xs={12} md={3}>right</Col>
        </Row>
      </Grid>
    );
  }
}

PM25Body.propTypes = {
  bodyData: React.PropTypes.any
};
