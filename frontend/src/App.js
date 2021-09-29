import React from 'react'
import { Route, Redirect, Switch } from 'react-router-dom'
import { HomePage, Navigation, Counter, Todo, SignUp } from 'common'
import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy} from 'algorithm'
import { Linear, Math, NonLinear} from 'datastructure'
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import { todoReducer, userReducer } from 'reducers'

const rootReducer = combineReducers({todoReducer, userReducer})
const store = createStore(rootReducer)

const App = () => (
<>
  <Provider store={store}>
    <Navigation/>
    <Switch>
      <Route exact path='/' component = { HomePage }/>
      <Redirect from='/home' to = { '/' }/>

      <Route exact path='/counter' component= { Counter }/>
      <Route exact path='/todo' component= { Todo }/>
      <Route exact path='/signup' component= { SignUp }/>

      <Route exact path='/backtracking' component= { BackTracking }/>
      <Route exact path='/bruteforce' component= { BruteForce }/>
      <Route exact path='/divideconquer' component= { DivideConquer }/>
      <Route exact path='/dynamic' component= { DynamicProgramming }/>
      <Route exact path='/greedy' component= { Greedy }/>

      <Route exact path='/linear' component= { Linear }/>
      <Route exact path='/math' component= { Math }/>
      <Route exact path='/nonlinear' component= { NonLinear }/>
    </Switch>
  </Provider>
</>
)

export default App;
