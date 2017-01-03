import React, {Component} from 'react';
import {Navbar} from 'react-bootstrap';

export default class PM25Navbar extends Component {
  render() {
    return (
      <Navbar>
        <Navbar.Header>
          <Navbar.Brand>
            <a>Aura</a>
          </Navbar.Brand>
        </Navbar.Header>
      </Navbar>
    );
  }
}
