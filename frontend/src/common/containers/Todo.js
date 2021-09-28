import { Button, TextField } from "@mui/material";
import React, {useState} from "react";
import styled from 'styled-components'

export default function Todo() {
    const [todo, setTodo] = useState('')
    let val = ''

    const addTodo = e => {
        e.preventDefault()
        val = e.target.value
    }
    const submitTodo = e => {
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value = ''
    }
    const delTodo = e => {
        e.preventDefault()
        setTodo('')
    }

    return (
    <form method="POST" onSubmit={submitTodo}>
        <TodoDiv>
            <input type='text' id='todo-input' onChange={addTodo} />
            <input type='submit' value='Add'/><br/>
            <span>Todo: {todo}</span>
            <input type='button' value='Del' onClick={delTodo}/>
        </TodoDiv>
    </form>
    )
}

const TodoDiv = styled.div` text-align: center; `