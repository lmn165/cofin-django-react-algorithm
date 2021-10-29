import React, { useState, useEffect, useCallback } from 'react';
import { Link, useHistory } from 'react-router-dom';
import axios from 'axios';

export default function UserDetail() {
  const SERVER = 'http://127.0.0.1:8000/api'
  const history = useHistory()  // history 는 이동할 때 사용하는 hook
  const [user, setUser] = useState({
    username: '',
    pwd: '',
    name: '',
    email: '',
    birth: '',
    address: ''
  })
  const {username, pwd, name, email, birth, address} = user
  const fetchOne = () => {
    const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
    alert(`사용자 아이디: ${sessionUser.username}`)
    // alert('pause!')
    axios.get(`${SERVER}/users/detail/${sessionUser.username}`)
    .then(res => {
        alert(`회원정보 조회 성공: ${res.data}`)
        setUser(res.data)
    })
    .catch(err => {
        alert(`조회 실패: ${err}`)
    })
  }
  useEffect(() => {
    fetchOne()
  }, [])

  const logout = e => {
    e.preventDefault()
    localStorage.setItem('sessionUser','')
    history.push('/')
}

  return (
    <div>
        <h1>회원 정보</h1>
        <ul>
            <li>
                <label>
                    <span>아이디: {user.username}</span> 
                </label>
            </li>
            <li>
                <label>
                    <span>이메일: {user.email}</span> 
                </label>
            </li>
            <li>
                <label>
                    <span>비밀번호: ******** </span> 
                </label>
            </li>
            <li>
                <label>
                    <span>이름: {user.name}</span> 
                </label>
            </li>
            <li>
                <input type="button" value="회원정보수정" onClick={()=> history.push('/modify')}/>
            </li>
            <li>
            <input type="button" value="로그아웃" onClick={logout}/>
            </li>
        </ul>
    </div>
  );
}
