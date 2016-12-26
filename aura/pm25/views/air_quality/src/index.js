import React from 'react';
import ReactDOM from 'react-dom';
import {Router, Route, browserHistory} from 'react-router';

import {Pm25Show} from './app/pm25';

import './index.scss';

ReactDOM.render(
  <Router history={browserHistory}>
    <Route path="/" component={Pm25Show}/>
  </Router>,
  document.getElementById('root')
);
