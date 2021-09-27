   
import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import { HomePage, Navigation } from 'common/index'
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy} from 'algorithm/index'
import { Linear, Math, NonLinear} from 'datastructure/index'


const App = () => (
<>
  <Navigation/>
  <Switch>
  <Route exact path='/' component = { HomePage }/>
  <Redirect from='/home' to = { '/' }/>

  <Route exact path='/backtracking' component= { BackTracking }/>
  <Route exact path='/bruteforce' component= { BruteForce }/>
  <Route exact path='/divideconquer' component= { DivideConquer }/>
  <Route exact path='/dynamic' component= { DynamicProgramming }/>
  <Route exact path='/greedy' component= { Greedy }/>

  <Route exact path='/linear' component= { Linear }/>
  <Route exact path='/math' component= { Math }/>
  <Route exact path='/nonlinear' component= { NonLinear }/>
  </Switch>
</>
)

export default App;
