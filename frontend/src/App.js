import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Expenses from './pages/Expenses';
import Income from './pages/Income';
import Analytics from './pages/Analytics';
import Navbar from './components/Navbar';

const App = () => {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/expenses" component={Expenses} />
        <Route path="/income" component={Income} />
        <Route path="/analytics" component={Analytics} />
      </Switch>
    </Router>
  );
};

export default App;
