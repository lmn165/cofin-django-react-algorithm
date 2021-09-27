import { Button, TextField } from "@mui/material";
import React, {useState} from "react";
import styled from 'styled-components'

export default function Todo() {
    const [todo, setTodo] = useState('')
    let val = ''

    const add = e => {
        e.preventDefault()
        val = e.target.value
    }

    const del = e => {
        e.preventDefault()
        val = ''
        setTodo(val)
    }

    const submitForm = e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = ''
    }

    return (
    <form onSubmit={submitForm} method="POST">
        <TodoDiv>
            <input type='text' id='todo-input' onChange={add} />
            <input type='submit' value='Add'/><br/>
            <span>Todo: {todo}</span>
            <input type='button' onClick={del} value='Del'/>
        </TodoDiv>
    </form>
    )
}

const TodoDiv = styled.div` text-align: center; `