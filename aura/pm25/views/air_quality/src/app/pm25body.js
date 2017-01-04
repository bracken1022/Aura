import React, {Component} from 'react';
import {Grid, Row, Col} from 'react-bootstrap';
import {LineChart} from 'react-d3';

export default class PM25Body extends Component {
  render() {
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={3}/>

          <Col xs={12} md={6}>

            <LineChart
              data={this.props.bodyData}
              width="100%"
              height={400}
              viewBoxObject={{
                x: 0,
                y: 0,
                width: 500,
                height: 400
              }}
              title={this.props.bodyData.name}
              yAxisLabel="PM25"
              xAxisLabel="Elapsed Time (sec)"
              domain={{x: [10], y: [-10]}}
              />;
          </Col>

          <Col xs={12} md={3}/>
        </Row>
      </Grid>
    );
  }
}

PM25Body.propTypes = {
  bodyData: React.PropTypes.any
};
