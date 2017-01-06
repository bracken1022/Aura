import React, {Component} from 'react';
import {Grid, Row, Col} from 'react-bootstrap';
import {LineChart} from 'react-d3-basic';

export default class PM25Body extends Component {
  render() {
    const margins = {left: 100, right: 100, top: 50, bottom: 50};
    // console.log(this.props.bodyData);
    const chartSeries = [
      {
        field: 'pm25',
        name: `${this.props.bodyData.name}`,
        color: '#FF0000'
      }
    ];
    const x = function (d) {
      return (d.localTime);
    };
    // const propData = [{localTime: new Date(2015, 2, 5), pm25: 100},
    //   {localTime: new Date(2016, 1, 3), pm25: 50},
    //   {localTime: new Date(2016, 3, 3), pm25: 25}];
    const scale = 'time';

    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={12}>
            <LineChart
              margins={margins}
              title={"PM 2.5"}
              data={this.props.bodyData.values}
              width={1000}
              height={300}
              chartSeries={chartSeries}
              x={x}
              xScale={scale}
              />
          </Col>
        </Row>
      </Grid>
    );
  }
}

PM25Body.propTypes = {
  bodyData: React.PropTypes.any
};
