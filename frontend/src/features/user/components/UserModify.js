import axios from 'axios';
import React, { useState } from 'react';
import { useHistory  } from 'react-router-dom';

export default function UserModify() {
    const history = useHistory()
    const SERVER = 'http://127.0.0.1:8000/api'
    const sessionUser = JSON.parse(localStorage.getItem('sessionUser')); 
    const [modify, setModify] = useState({
        username:sessionUser.username, 
        pwd:sessionUser.pwd, 
        email:sessionUser.email, 
        name:sessionUser.name, 
        address: sessionUser.address,
        birth: sessionUser.birth
    })
    const {username, pwd, email, name, address, birth} = modify
    const handleChange = e => {
        const { value, name } = e.target
        setModify({
            ...modify,
            [name] : value
        })
    }
    const headers = {
      'Content-Type' : 'application/json',
      'Authorization': 'JWT fefege..'
  }
    const UserModify = modifyRequest => 
                axios.put(`${SERVER}/users/modify`, JSON.stringify(modifyRequest),{headers})
    
    const handleSubmit = e => {
        e.preventDefault()
        const modifyRequest = {...modify}
        alert(`회원수정 정보: ${JSON.stringify(modifyRequest)}`)
        UserModify(modifyRequest)
        .then(res =>{
            alert('회원 정보 수정 성공')
            localStorage.setItem('sessionUser', JSON.stringify(res.data))
            history.push("/detail")
        })
        .catch(err =>{
            alert(`회원수정 실패 : ${err}`)
        })

  }

  return (
    <div>
         <h1>회원정보 수정</h1>
    <form onSubmit={handleSubmit} method='PUT'>
        <ul>
            <li>
                <label>
                    <span>아이디 : {sessionUser.username} </span>
                </label>
            </li>
            <li>
                <label>
                    이름 : <input type="text" id="name" name="name" placeholder={sessionUser.name}
                    value={name}
                    onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    이메일 : <input type="email" id="email" name="email" placeholder={sessionUser.email}
                                  value={email}
                                 onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    비밀 번호 : <input type="password" id="pwd" name="pwd" placeholder={sessionUser.pwd} 
                    value={pwd}
                    onChange={handleChange}/>
                </label>
            </li>
            <li>
                <label>
                    주소 : <input type="text" id="address" name="address" placeholder={sessionUser.address}
                    value={address}
                    onChange={handleChange}/>
                </label>
            </li>
            <li>
                <input type="submit" value="수정확인"/>
            </li>

        </ul>
    </form>
    </div>
  );
}