import React from 'react';
import { Navigation, Home } from 'features/common'
import { UserAdd, UserDetail, UserList, UserLogin, UserModify, UserRemove} from 'features/user'
import { Route, Redirect, Switch } from 'react-router-dom'

export default function App() {
  return (<>
  <Navigation/>
    <Switch>
      <Route exact path='/' component = { Home }/>
      <Redirect from='/home' to = { '/' }/>

      <Route exact path='/add' component= { UserAdd }/>
      <Route exact path='/detail' component= { UserDetail }/>
      <Route exact path='/list' component= { UserList }/>
      <Route exact path='/login' component= { UserLogin }/>
      <Route exact path='/modify' component= { UserModify }/>
      <Route exact path='/remove' component= { UserRemove }/>
    </Switch>
  </>);
}