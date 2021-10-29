import axios from 'axios';
import React, { useState } from 'react';
import { useHistory } from 'react-router-dom'

export default function UserAdd() {
    const SERVER = 'http://127.0.0.1:8000/api'
    const history = useHistory()
    const [user, setUser] = useState({
        username: '',
        pwd: '',
        name: '',
        email: '',
        birth: new Date().toLocaleDateString(),
        address: ''
      })
    const {username, pwd, name, email, birth, address} = user
    const handleChange = e => {
        const { value, name } = e.target
        setUser({
            ...user,
            [name]:  value
        })
    }
    const userJoin = body => axios.post(`${SERVER}/users/join`, {headers, body})
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'JWT fefege..'
    }
    const handleSubmit = e => {
        e.preventDefault()
        const joinRequest = {user}
        alert(`회원가입 정보: ${joinRequest}`)
        userJoin(joinRequest)
        .then(res =>{
            alert(`회원가입 성공 ${res}`)
            history.push('/login')
        })
        .catch(err => {
            console.log(`회원가입 실패 : ${err}`)
        });
    }

    return (
        <div>
            <h1>회원 가입을 환영합니다</h1>
            <form onSubmit={handleSubmit} method="POST">
                <ul>
                    <li>
                        <label>
                            아이디: <input type="text" id="username" name="username" value={username} onChange={handleChange}
                            size="10" minlength="4" maxlength="15"/>
                        </label>
                        <small>4~15자리 이내의 영문과 숫자</small>
                    </li>
                    <li>
                        <label>
                            이메일: <input type="email" id="email" name="email" value={email} onChange={handleChange}/>
                        </label>
                    </li>
                    <li>
                        <label>
                            비밀번호: <input type="password" id="pwd" name="pwd" value={pwd} onChange={handleChange}/>
                        </label>
                    </li>
                    <li>
                        <label>
                            이름: <input type="text" id="name" name="name" value={name} onChange={handleChange}/>
                        </label>
                    </li>
                    <li>
                        <label>
                            주소: <input type="text" id="address" name="address" value={address} onChange={handleChange}/>
                            <input type="hidden" id="birth" name="birth" value={birth} onChange={handleChange}/>
                        </label>
                    </li>
                    <li>
                        <input type="submit" value="회원가입"/>
                    </li>
                </ul>
            </form>
        </div>
      );
    }
