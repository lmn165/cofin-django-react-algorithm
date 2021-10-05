import React from "react";
import { SignIn } from "common/index"
import { connect } from 'api'

export default function HomePage() {
    const handleClick = e => {
        e.preventDefault()
        alert('Home Click')
        connect()
        .then(res => {alert(`접속 성공 ${res.data.connection}`)})
        .catch(err => {alert(`접속 실패: ${err}`)})
    }
return (<>
    <SignIn/>
    <button onClick={handleClick}>커넥트!</button>
</>)
}