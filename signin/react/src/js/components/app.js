import React, {Component} from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

import Home from './Home';
import SigninLine from './Signinline';

const App = (props) => {
  return (
    <Router>
      <Switch>
        <Route exact path="/signin/" component={Home} />
        <Route path="/signin/student/" component={SigninLine} />
      </Switch>
    </Router>
  );
}

export default App;