import React, {Component} from 'react';
import {Grid, Row, Col} from 'react-bootstrap';
import {LineChart} from 'react-d3-basic';
import _ from 'lodash';

export default class PM25Body extends Component {
  calculateAveragePm25() {
    const pm25Datas = _.map(this.props.bodyData.values, value => {
      return value.pm25;
    });
    const pm25DataSize = _.size(pm25Datas) === 0 ? 0 : _.size(pm25Datas);

    const div = _.sum(pm25Datas) / pm25DataSize;
    return div.toFixed(0);
  }
  render() {
    const margins = {left: 50, right: 50, top: 50, bottom: 50};
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
    const scale = 'time';

    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={10} md={10}>
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

          <Col xs={2} md={2}>
            <em>average</em>
            <br/>
            <br/>
            <p>{this.calculateAveragePm25()}</p>
          </Col>
        </Row>
      </Grid>
    );
  }
}

PM25Body.propTypes = {
  bodyData: React.PropTypes.any
};
