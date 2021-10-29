import React, { useState } from 'react';
import axios from 'axios';
import { useHistory } from 'react-router-dom';

export default function UserLogin() {
  const SERVER = 'http://127.0.0.1:8000/api'
  const [login, setLogin] = useState({})
  const {username, pwd} = login
  const history = useHistory()

  const handleChange = e => {
    const {value, name} = e.target
    setLogin({
      ...login,
      [name] : value
    })
  }
  const headers = {
    'Content-Type': 'application/json',
    'Authorization': 'JWT fefege..'
  }
  const changeNull = ls =>{
    for(const i of ls ){
      document.getElementById(i).value = ''
    }
  }
  const handleClick = e =>{
    e.preventDefault()
    e.stopPropagation()
    const loginRequest = {username, pwd}
    // alert('로그인정보'+JSON.stringify(loginRequest))
    userLogin(loginRequest)
    .then(res => {
      const user = res.data;
      if(user.username != null){
        alert('로그인 성공, '+JSON.stringify(res.data))
        localStorage.setItem('sessionUser', JSON.stringify(res.data))
        history.push("/detail")
      }else{
        alert('아이디, 비번 오류로 로그인 실패')
        changeNull(['username', 'pwd'])
      }
    })
    .catch(err => {
      alert('접속 실패', + err)
      changeNull(['username', 'pwd'])
    })
  }
  const userLogin = loginRequest => axios.post(`${SERVER}/users/login`, JSON.stringify(loginRequest), {headers})
  return (
    <div>
      <h1>유저 로그인</h1>
      <form method="POST">
        <ul>
          <li><label for="id">아이디</label>
          <input type="text" id="username"
              name="username" value={username} onChange={handleChange}/></li>
          <li><label for="pw">비밀번호</label>
          <input type="password" id="pwd" name="pwd" onChange={handleChange}/></li>
          <li><input type="button" title="로그인" value="로그인" onClick={handleClick}/></li>
        </ul>
      </form>
    </div>
  );
}
